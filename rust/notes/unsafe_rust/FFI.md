---
tags:
  - rust
  - unsafe
  - ffi
  - c-interop
source: unsafe_rust/src/ffi_basics.rs
---

# FFI (Foreign Function Interface)

FFI (Foreign Function Interface) is the mechanism for calling functions written in another language (typically C) from Rust, and vice versa. Every call across the boundary is `unsafe` because Rust cannot verify the other side's memory safety guarantees.

## extern Blocks

Declare C functions with an `extern "C"` block. `"C"` specifies the ABI (Application Binary Interface) — the calling convention, register usage, and stack layout that both sides must agree on.

```rust
use std::ffi::{c_char, c_int};

unsafe extern "C" {
    fn strlen(s: *const c_char) -> usize;
    fn abs(x: c_int) -> c_int;
}

let pos: c_int = unsafe { abs(-42) };
```

The `unsafe extern "C"` syntax (Rust 2024) makes the unsafety explicit at the block level. Each call still requires its own `unsafe { }` at the call site.

## C-compatible Primitive Types

Use `std::ffi::c_*` types rather than Rust primitives when crossing the boundary. C's `int` is not guaranteed to be 32 bits on all platforms.

| Rust type | C equivalent | Typical size |
|---|---|---|
| `c_char` | `char` | 1 byte |
| `c_int` | `int` | 4 bytes |
| `c_double` | `double` | 8 bytes |
| `c_longlong` | `long long` | 8 bytes |
| `usize` | `size_t` | pointer-width |
| `isize` | `ptrdiff_t` | pointer-width |

## repr(C) Structs

By default, Rust may reorder fields and add padding to optimize layout. `#[repr(C)]` (representation attribute C) forces the struct to use C's sequential layout with C alignment rules — required for any struct passed by value across FFI.

```rust
// Must match: typedef struct { double x; double y; } CPoint; in C
#[repr(C)]
#[derive(Debug, Clone, Copy)]
struct CPoint {
    x: c_double,
    y: c_double,
}

let p = CPoint { x: 3.0, y: 4.0 };
let mag: c_double = unsafe { c_point_magnitude(p) };
```

`Clone + Copy` are needed because C receives the struct by value — Rust must be able to bitwise-copy it to the call stack.

## repr(C) Enums

Similarly, enums need `#[repr(C)]` to have a predictable integer layout when used in FFI:

```rust
#[repr(C)]
enum Status {
    Ok      = 0,
    Error   = 1,
    Timeout = 2,
}
```

Without `#[repr(C)]`, Rust may choose any integer width and representation it likes.

## Strings: CString and CStr

C strings are null-terminated byte sequences. Rust's `String`/`&str` are not null-terminated and may contain interior nulls. Always convert explicitly.

**`CString`** — owned, heap-allocated, null-terminated. Use to pass strings to C.

```rust
let c_string: CString = CString::new("hello from Rust").expect("interior null");
let len: usize = unsafe { strlen(c_string.as_ptr()) };
```

`CString::new` fails with `Err(NulError)` if the input contains `\0` — this protects against C interpreting the string as shorter than intended.

**`CStr`** — borrowed reference to a null-terminated sequence. Use to read strings returned from C.

```rust
let cstr: &CStr = unsafe { CStr::from_bytes_with_nul_unchecked(b"static\0") };
let rust_str: &str = cstr.to_str().unwrap(); // validates UTF-8
```

**Ownership transfer with `into_raw` / `from_raw`:**

```rust
let raw: *mut c_char = CString::new("transfer to C").unwrap().into_raw();
// C now owns the allocation — Rust will not free it
// ...
// When C is done, reclaim ownership to drop properly:
let reclaimed: CString = unsafe { CString::from_raw(raw) };
```

If you use `mem::forget` instead of `into_raw`, you cannot reclaim ownership. `into_raw` is the correct pattern. See [[Unsafe Functions#std::mem::forget]].

## Exporting Rust Functions to C

Two attributes together make a Rust function callable from C:

- `#[unsafe(no_mangle)]` — keeps the symbol name as-is in the binary (disables Rust name mangling)
- `extern "C"` — uses the C calling convention

```rust
#[unsafe(no_mangle)]
pub extern "C" fn rust_add(a: c_int, b: c_int) -> c_int {
    return a + b;
}
```

C side declares: `extern int rust_add(int a, int b);` and calls it directly.

## Callbacks: Passing Rust Function Pointers to C

C can call back into Rust via function pointers, provided the Rust function uses `extern "C"` calling convention.

```rust
extern "C" fn double_it(x: c_int) -> c_int { return x * 2; }
extern "C" fn negate(x: c_int)    -> c_int { return -x; }

// c_apply(value, fn): defined in C, calls fn(value)
let doubled: c_int = unsafe { c_apply(21, double_it) };
let negated: c_int = unsafe { c_apply(99, negate) };
```

Rust closures cannot cross the FFI boundary — they have hidden captured state. Only bare `extern "C" fn` pointers work.

## Passing Buffers (Rust allocates, C writes)

The canonical pattern: Rust allocates the buffer and owns the memory, C writes into it.

```rust
let mut buf: Vec<u8> = vec![0u8; 32];
let written: c_int = unsafe {
    c_repeat_char(b'*' as c_char, 8, buf.as_mut_ptr() as *mut c_char, 32)
};
// SAFETY: C null-terminated within buf_len, buf is still live
let result: &CStr = unsafe { CStr::from_ptr(buf.as_ptr() as *const c_char) };
```

Always pass the buffer length. Never trust C to stay in bounds — the length cap is your only defense against buffer overflows.

## Round Trip: Rust → C → Rust

C code can call exported Rust functions, creating a full round trip:

```rust
// C: int call_rust_add(int a, int b) { return rust_add(a, b); }
let via_c: c_int = unsafe { call_rust_add(15, 27) }; // Rust → C → rust_add

// C: int sum_then_square(int a, int b) { return rust_square(rust_add(a, b)); }
let sq: c_int = unsafe { sum_then_square(3, 4) }; // chains rust_add + rust_square
```

This is the standard pattern for incrementally integrating Rust into C codebases.

## Safe Wrapper Pattern

Expose a safe public function, keep `unsafe` internal:

```rust
fn safe_factorial(n: u32) -> i64 {
    unsafe { c_factorial(n as c_int) }
}
```

The caller never touches `unsafe`. Invariants (e.g., non-negative input) are enforced by the type (`u32`) rather than documentation.

## Linking

Three ways to link C code:

```rust
// In build.rs:
println!("cargo:rustc-link-lib=m");          // dynamic: links libm.so
println!("cargo:rustc-link-lib=static=m");   // static: links libm.a

// Or on the extern block:
#[link(name = "m")]
unsafe extern "C" { ... }

// Or compile C source directly (cc crate in build.rs):
cc::Build::new().file("c_src/math_utils.c").compile("mathutils");
```

The `cc` crate is the standard choice when you own the C source files.

## Related

- [[Raw Pointers]] — the pointer types used at FFI boundaries
- [[Unsafe Functions]] — `transmute`, `ManuallyDrop`, `union` for C-interop patterns
