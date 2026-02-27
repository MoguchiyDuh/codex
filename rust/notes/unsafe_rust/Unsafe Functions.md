---
tags:
  - rust
  - unsafe
  - functions
  - memory
source: unsafe_rust/src/unsafe_functions.rs
---

# Unsafe Functions

`unsafe` in Rust has two distinct roles: marking a function as having invariants the compiler cannot verify, and marking a block where the programmer asserts those invariants hold. Both are needed; one does not subsume the other.

## unsafe fn

Marking a function `unsafe fn` is a contract with callers: "you must uphold conditions I cannot express in the type system before calling this."

```rust
unsafe fn add_via_ptrs(a: *const i32, b: *const i32) -> i32 {
    // Rust 2024: unsafe fn body is safe-by-default.
    // Dereferencing still requires an explicit unsafe block inside.
    unsafe { *a + *b }
}

let result: i32 = unsafe { add_via_ptrs(&x, &y) };
```

In Rust 2024 edition, the body of an `unsafe fn` is not implicitly trusted — you still need `unsafe { }` blocks inside for unsafe operations. This makes the unsafe surface area explicit even within an unsafe function.

## Safe Abstraction over Unsafe

The standard pattern: accept `unsafe` internally, expose a safe public interface. Document invariants with `// SAFETY:` comments.

```rust
fn split_at_mid(slice: &[i32], mid: usize) -> (&[i32], &[i32]) {
    assert!(mid <= slice.len());
    let ptr: *const i32 = slice.as_ptr();
    // SAFETY: mid verified <= len, slices are non-overlapping halves of the
    //         same allocation, lifetimes tied to 'slice
    unsafe {
        let left  = std::slice::from_raw_parts(ptr, mid);
        let right = std::slice::from_raw_parts(ptr.add(mid), slice.len() - mid);
        (left, right)
    }
}
```

`assert!` before entering `unsafe` is the most common guard. Callers get a panic instead of UB (Undefined Behavior) on bad input. This is exactly how `slice::split_at` works in the standard library.

## slice::from_raw_parts

Reconstructs a slice from a raw pointer and a length. Caller must guarantee:

- `ptr` is non-null and properly aligned for `T`
- `len` elements starting at `ptr` are initialized
- The memory lives at least as long as the returned slice
- No `&mut` reference to any of those elements exists simultaneously

```rust
let data: Vec<i32> = vec![10, 20, 30, 40, 50];
let reconstructed: &[i32] = unsafe {
    std::slice::from_raw_parts(data.as_ptr(), data.len())
};
```

## std::mem::transmute

Reinterprets the raw bytes of one type as another. The most dangerous unsafe operation in the standard library. The compiler checks that `size_of::<A>() == size_of::<B>()` — nothing else.

```rust
let f: f32 = 1.0_f32;
let bits: u32 = unsafe { std::mem::transmute::<f32, u32>(f) };
// bits == 0x3F800000 (IEEE 754 representation of 1.0)
```

Transmuting to an invalid bit pattern for the target type is immediate UB. Prefer type-safe alternatives:

| Use case | Prefer instead |
|---|---|
| `f32` ↔ `u32` bits | `f32::to_bits()` / `f32::from_bits()` |
| `&[u8]` ↔ `&[u32]` | `bytemuck` crate |
| Any reinterpret | document *why* transmute is required |

## std::mem::forget

Prevents a value's destructor from running. This is safe (no `unsafe` required) because leaking memory is not UB — it's just a resource leak.

```rust
let v: Vec<i32> = vec![1, 2, 3];
std::mem::forget(v); // heap allocation leaked, Drop never called
```

Primary use case: transferring ownership of Rust-allocated memory to C code that will free it.

```rust
let s = String::from("transferred to C");
let ptr: *mut u8 = s.as_ptr() as *mut u8;
std::mem::forget(s); // Rust will not free ptr — C side takes over
```

## ManuallyDrop

A wrapper that suppresses the destructor without consuming the value. Unlike `mem::forget`, you retain access to the inner value and can explicitly drop it when ready.

```rust
use std::mem::ManuallyDrop;

let mut md: ManuallyDrop<String> = ManuallyDrop::new(String::from("manual"));
md.push_str(" drop");
// We own the drop — must call it explicitly
unsafe { ManuallyDrop::drop(&mut md) };
// Accessing *md after this is use-after-free UB
```

`ManuallyDrop` is the building block for custom allocators, arena types, and ownership-transfer patterns.

## union (C-style)

A `union` stores all fields at the same memory address. Reading a field that was not the last one written is UB — there is no tag tracking which variant is active.

```rust
union IntOrFloat {
    i: i32,
    f: f32,
}

let u = IntOrFloat { i: 0x3F800000_i32 }; // IEEE 754 bits for 1.0f
let as_float: f32 = unsafe { u.f }; // 1.0
let as_int:   i32 = unsafe { u.i }; // 0x3F800000
```

Rust enums are tagged unions — prefer them when you need safe sum types. Raw `union` is for [[FFI]] interop or low-level bit manipulation where the layout must match an external format exactly.

## Global Mutable Static

`static mut` variables are global mutable state. Every access requires `unsafe` because concurrent mutation from multiple threads is UB.

```rust
static mut COUNTER: u32 = 0;

unsafe {
    COUNTER += 1;
    // Rust 2024: cannot form &COUNTER (shared ref to mutable static risks UB)
    // Use &raw const / addr_of! to get a raw pointer, then read through it
    let val: u32 = std::ptr::read(&raw const COUNTER);
}
```

For any actual shared mutable global, use `AtomicU32`, `Mutex<T>`, or `OnceLock<T>` instead. `static mut` is essentially reserved for single-threaded embedded targets and FFI symbol exports.

## Unsafe Traits: Send and Sync

`Send` (type can be moved across thread boundaries) and `Sync` (shared `&T` can be sent across threads) are automatically implemented for most types. Raw pointers opt out of both.

```rust
struct MyWrapper(*mut i32);

// SAFETY: we guarantee exclusive access through external synchronization
unsafe impl Send for MyWrapper {}
unsafe impl Sync for MyWrapper {}
```

Implementing these incorrectly enables data races — UB in a multithreaded context. Only `unsafe impl` if you can prove the safety guarantee holds for every possible use.

## Related

- [[Raw Pointers]] — the pointer operations these functions operate on
- [[FFI]] — `extern "C"` and `unsafe` at the language boundary
- [[../basics/Ownership & Borrowing|Ownership & Borrowing]] — what `ManuallyDrop` and `forget` bypass
