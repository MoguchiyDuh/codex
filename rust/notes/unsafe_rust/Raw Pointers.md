---
tags:
  - rust
  - unsafe
  - pointers
source: unsafe_rust/src/raw_pointers.rs
---

# Raw Pointers

Raw pointers are Rust's escape hatch from the borrow checker. Unlike references, they carry no lifetime, no aliasing guarantee, and no automatic validity check. Two types exist: `*const T` (immutable) and `*mut T` (mutable).

**Creating** raw pointers is safe — you can cast any reference or arbitrary integer to one. **Dereferencing** is not; that requires an `unsafe` block.

## Creation

```rust
let x: i32 = 42;
let ptr_const: *const i32 = &x as *const i32;

let mut y: i32 = 100;
let ptr_mut: *mut i32 = &mut y as *mut i32;

// Syntactically valid, but dereferencing this is UB (Undefined Behavior)
let _dangling: *const i32 = 0x12345 as *const i32;
```

Casting an arbitrary integer to a pointer is legal. Dereferencing it is UB — likely a segfault, but UB means the compiler can do anything.

## Dereferencing

```rust
let val: i32 = unsafe { *ptr_const };

unsafe {
    *ptr_mut = 200;
}
```

Every dereference must be inside an `unsafe` block. You are asserting to the compiler that the pointer is valid, aligned, and points to initialized memory of the correct type.

## Pointer Arithmetic

```rust
let arr: [i32; 5] = [10, 20, 30, 40, 50];
let base: *const i32 = arr.as_ptr();

unsafe {
    for i in 0..5usize {
        let elem = base.add(i);   // advances by i * size_of::<i32>() bytes
        println!("{}", *elem);
    }
    let third = base.offset(2);  // signed equivalent of add
}
```

- `.add(n)` — unsigned offset, equivalent to `ptr + n` in C
- `.offset(n)` — signed offset, allows negative steps
- Going out of the allocation boundary is **immediate UB** regardless of whether you dereference

## Null Pointers

```rust
let null_ptr: *const i32 = std::ptr::null();
let null_mut: *mut i32   = std::ptr::null_mut();

null_ptr.is_null(); // true — safe to call, does not dereference
```

Dereferencing a null pointer is UB. Always check `is_null()` when receiving pointers from external sources (e.g., [[FFI]]).

## ptr::read and ptr::write

These are explicit alternatives to `*ptr` dereference syntax, useful when you need fine-grained control over Copy semantics and drop behavior.

```rust
let src: i32 = 999;
let copied: i32 = unsafe { std::ptr::read(&src as *const i32) };

let mut dst: i32 = 0;
// Writes without reading or dropping the existing value at dst
unsafe { std::ptr::write(&mut dst as *mut i32, 777) };
```

`ptr::write` is critical when the destination contains uninitialized memory — calling `*dst = value` would attempt to drop the old value first, which is UB on uninitialized data.

## Bulk Copy: copy_nonoverlapping and copy

```rust
let src_arr: [i32; 3] = [1, 2, 3];
let mut dst_arr: [i32; 3] = [0; 3];

unsafe {
    // Equivalent to C's memcpy — src and dst MUST NOT overlap
    std::ptr::copy_nonoverlapping(src_arr.as_ptr(), dst_arr.as_mut_ptr(), 3);
}

unsafe {
    // Equivalent to C's memmove — handles overlapping regions safely
    std::ptr::copy(dst_arr.as_ptr(), dst_arr.as_mut_ptr().add(0), 2);
}
```

## Thin vs Fat Pointers

Not all raw pointers are the same size.

| Pointer type | Size | Metadata |
|---|---|---|
| `*const i32` | 8 bytes | none (thin) |
| `*const str` | 16 bytes | + length |
| `*const dyn Debug` | 16 bytes | + vtable pointer |

Fat pointers carry metadata alongside the address. This matters when casting between pointer types across an [[FFI]] boundary — always use thin pointers there.

## Aliased Mutable Pointers (UB)

```rust
// DO NOT DO THIS
let mut z = 5;
let p1 = &mut z as *mut i32;
let p2 = &mut z as *mut i32;
unsafe { *p1 = 10; *p2 = 20; } // UB — data race on a single-threaded stack value
```

Two `*mut` pointers to the same location that are both written through is UB. The compiler assumes no such aliasing exists when optimizing. This is the core invariant that `&mut T` enforces at the type level — raw pointers give it up entirely.

## Checklist Before Dereferencing

- Pointer is non-null
- Pointer is properly aligned for `T`
- Memory it points to is initialized
- No other `&mut T` reference to the same location exists
- Pointer does not outlive the allocation it points into

## Related

- [[Unsafe Functions]] — `slice::from_raw_parts`, `transmute`, and other unsafe stdlib ops
- [[FFI]] — passing raw pointers across the C boundary
- [[../basics/Ownership & Borrowing|Ownership & Borrowing]] — what raw pointers opt out of
