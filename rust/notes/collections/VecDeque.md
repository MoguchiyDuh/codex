---
tags: [rust, collections, vecdeque, deque]
source: collections/src/deques.rs
---

# VecDeque\<T\>

`VecDeque<T>` is a double-ended queue (deque) backed by a ring buffer. It supports O(1) push and pop at both ends, making it efficient for First In First Out (FIFO) queues and Last In First Out (LIFO) stacks without the O(n) cost that `Vec` incurs for front operations. Random access by index is O(1).

## Creation

```rust
use std::collections::VecDeque;

let dq: VecDeque<i32> = VecDeque::new();
let dq = VecDeque::from([1, 2, 3, 4, 5]);
let dq: VecDeque<i32> = VecDeque::from(vec![1, 2, 3]);
let dq: VecDeque<i32> = VecDeque::with_capacity(10);
```

## Push and Pop at Both Ends

```rust
dq.push_front(10);  // O(1) — add to front
dq.push_back(10);   // O(1) — add to back

let front: Option<i32> = dq.pop_front(); // O(1) — remove from front
let back:  Option<i32> = dq.pop_back();  // O(1) — remove from back
```

This is the main advantage over [[Vec]], where `push_front`/`pop_front` would be O(n).

## Accessing Elements

```rust
let f: Option<&i32> = dq.front();     // peek front without removing
let b: Option<&i32> = dq.back();      // peek back without removing

let x: i32 = dq[2];                   // panics if out of bounds
let x: Option<&i32> = dq.get(2);     // safe
let x: Option<&i32> = dq.get(100);   // None

// mutable access
if let Some(v) = dq.front_mut() { *v *= 10; }
if let Some(v) = dq.back_mut()  { *v *= 10; }
if let Some(v) = dq.get_mut(2)  { *v = 999; }
```

## Arbitrary Insert and Remove

Both are O(n) due to element shifting — prefer front/back operations where possible.

```rust
dq.insert(2, 3);          // insert value 3 at index 2
let removed = dq.remove(2); // returns Option<T> (None if out of bounds, no panic)
```

## Rotating

`rotate_left(n)` moves the first `n` elements to the back. `rotate_right(n)` is the reverse.

```rust
let mut dq = VecDeque::from([1, 2, 3, 4, 5]);
dq.rotate_left(2);   // [3, 4, 5, 1, 2]
dq.rotate_right(1);  // [2, 3, 4, 5, 1]
```

## Contiguous Memory and Slices

Because `VecDeque` is a ring buffer, its elements may wrap around internally and not be contiguous. This matters when APIs require `&[T]`.

```rust
// as_slices returns up to two slices covering all elements
let (s1, s2): (&[i32], &[i32]) = dq.as_slices();

// make_contiguous forces all elements into one slice and returns it
let slice: &[i32] = dq.make_contiguous();
// now you can call sort_unstable_by, pass to C functions, etc.
```

## Searching

```rust
dq.contains(&30);          // O(n) linear scan
dq.binary_search(&3);      // requires sorted; returns Result<usize, usize>
```

## Bulk Operations

```rust
dq.resize(6, 0);           // grow or shrink, filling with 0
dq.truncate(3);            // keep first 3
dq.clear();

dq.extend([4, 5, 6]);     // add multiple to back
dq.append(&mut other);    // drain other into dq (other becomes empty)
dq.retain(|&x| x % 2 == 0); // in-place filter

let tail = dq.split_off(3); // dq keeps [0..3), tail gets [3..)
dq.swap(0, 4);              // swap by index
```

## Common Patterns

```rust
// FIFO queue
let mut queue: VecDeque<&str> = VecDeque::new();
queue.push_back("first");
queue.push_back("second");
while let Some(item) = queue.pop_front() { /* process */ }

// LIFO stack (equivalent to Vec; VecDeque works but Vec is simpler)
let mut stack: VecDeque<i32> = VecDeque::new();
stack.push_back(1);
stack.push_back(2);
while let Some(item) = stack.pop_back() { /* process */ }

// rotating buffer
let mut buf = VecDeque::from([1, 2, 3, 4, 5]);
buf.rotate_left(1);
```

## Capacity

```rust
dq.reserve(20);       // room for 20 MORE elements
dq.shrink_to_fit();
dq.len();
dq.is_empty();
```

## Vec vs VecDeque

| Operation | [[Vec]] | VecDeque |
|-----------|---------|----------|
| push/pop back | O(1) amortized | O(1) amortized |
| push/pop front | O(n) | O(1) amortized |
| Index access | O(1) | O(1) |
| Contiguous memory | always | only after `make_contiguous` |

## See Also

- [[Vec]] — simpler, always contiguous, no efficient front ops
- [[BinaryHeap]] — when you need priority ordering, not FIFO/LIFO
