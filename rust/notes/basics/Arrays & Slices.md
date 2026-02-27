---
tags: [rust, basics, arrays, slices]
source: basics/src/array_example.rs
---

# Arrays & Slices

## Arrays

Fixed-size, stack-allocated, homogeneous. Size is part of the type: `[T; N]`.

```rust
let arr: [i32; 5] = [1, 2, 3, 4, 5];
let zeros: [i32; 3] = [0; 3];                          // repeat syntax
let init: [i32; 4] = std::array::from_fn(|i| (i*2) as i32);  // closure init
```

Arrays of `Copy` types implement `Copy`.

## Indexing

```rust
arr[0]              // direct — PANIC if out of bounds
arr.get(2)          // Option<&i32> — safe
arr.get(99)         // None
```

## Properties

```rust
arr.len()
arr.is_empty()
arr.first()         // Option<&T>
arr.last()          // Option<&T>
arr.contains(&8)
```

## Slices (`&[T]`)

A fat pointer (ptr + len) borrowing a contiguous sequence. Works with arrays, Vec, etc.

```rust
let slice: &[i32] = &arr[1..4];        // [arr[1], arr[2], arr[3]]
let (left, right) = arr.split_at(3);   // (&[i32], &[i32])
```

## Iteration

```rust
for item in arr.iter()      { }     // borrows
for item in arr.iter_mut()  { *item *= 2; }     // mutable borrow
for (idx, val) in arr.iter().enumerate() { }

for window in arr.windows(3) { }    // overlapping slices of size n
for chunk  in arr.chunks(2)  { }    // non-overlapping chunks of size n
```

## Mutation

```rust
arr.reverse()
arr.rotate_left(2)      // [1,2,3,4,5] → [3,4,5,1,2]
arr.fill(7)             // overwrite all with 7
arr.swap(0, 2)          // swap elements at indices

let mut dst = [0; 3];
dst.copy_from_slice(&src);  // src and dst must have the same length
```

## Sorting & searching

```rust
arr.sort()                  // stable sort (allocates temp buffer)
arr.sort_unstable()         // unstable but faster

// binary_search requires sorted array
match arr.binary_search(&8) {
    Ok(idx)  => println!("found at {}", idx),
    Err(idx) => println!("would insert at {}", idx),
}
```

## Conversion

```rust
let v: Vec<i32> = arr.to_vec();
let s: &[i32]   = arr.as_slice();
```

## Note on moving

`for item in arr` moves the array (for non-Copy types). Use `.iter()` to borrow instead:

```rust
for item in arr         { }  // arr moved, can't use after
for item in arr.iter()  { }  // arr borrowed, still usable after
```
