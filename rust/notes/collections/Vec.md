---
tags: [rust, collections, vec]
source: collections/src/vectors.rs
---

# Vec\<T\>

`Vec<T>` is Rust's growable heap-allocated array. It owns its data, stores elements contiguously, and manages length/capacity separately. The allocator doubles capacity on growth (amortized O(1) push).

## Creation

```rust
let v: Vec<i32> = Vec::new();
let v = vec![1, 2, 3];                  // macro shorthand
let v = Vec::with_capacity(10);         // pre-allocate; avoids reallocations
let v: Vec<i32> = (0..5).collect();     // from any iterator
let v = vec![0; 5];                     // [0, 0, 0, 0, 0] — repeat a value
```

`with_capacity` is the main performance lever: if you know the upper bound of elements, use it to avoid repeated reallocations.

## Adding and Removing

| Operation | Cost | Notes |
|-----------|------|-------|
| `push(x)` | O(1) amortized | appends to end |
| `insert(i, x)` | O(n) | shifts elements right |
| `pop()` | O(1) | returns `Option<T>` |
| `remove(i)` | O(n) | shifts elements left |
| `swap_remove(i)` | O(1) | swaps target with last, breaks order |

```rust
let mut v = vec![1, 2, 3, 4, 5];
v.push(10);
v.insert(1, 99);   // [1, 99, 2, 3, 4, 5, 10]
let _ = v.pop();   // removes 10
let _ = v.remove(1);     // O(n) — use swap_remove when order doesn't matter
let _ = v.swap_remove(0); // O(1)
```

## Accessing Elements

Direct indexing panics on out-of-bounds. Prefer `get` when the index might be invalid.

```rust
let v = vec![10, 20, 30, 40];
let x = v[0];                    // panics if out of bounds
let x = v.get(1);                // Option<&i32> — safe
let x = v.get(100);              // None, no panic
let first = v.first();           // Option<&i32>
let last  = v.last();            // Option<&i32>
```

## Capacity Management

```rust
let mut v: Vec<i32> = Vec::with_capacity(10);
v.push(1);
println!("{} / {}", v.len(), v.capacity()); // 1 / 10

v.reserve(20);       // ensure capacity for 20 MORE elements
v.shrink_to_fit();   // release excess memory
```

## Bulk Modifications

```rust
v.resize(5, 0);          // grow or shrink; fills new slots with 0
v.extend([4, 5, 6]);     // append from iterator
v.append(&mut other);    // drain other into v (other becomes empty)
v.truncate(3);           // keep first 3, drop rest (no realloc)
v.clear();               // same as truncate(0)
```

## Iteration

```rust
// Immutable — borrows v
for val in &v { println!("{}", val); }

// Mutable — borrows v mutably
for val in &mut v { *val *= 2; }

// Consuming — moves v
for val in v { /* v is gone after */ }

// Indexed
for (i, val) in v.iter().enumerate() { }
```

## Searching and Sorting

```rust
v.contains(&3);                          // O(n) linear scan
v.iter().position(|&x| x == 3);         // Option<usize>

// binary_search requires sorted input
// Ok(idx) = found, Err(idx) = insertion point
v.binary_search(&3);

v.sort();                                // stable, ascending
v.sort_by(|a, b| b.cmp(a));            // descending
v.sort_by_key(|x| x.abs());            // sort by derived key
```

## Deduplication and Filtering

```rust
// dedup only removes consecutive duplicates — sort first for a full dedup
v.sort();
v.dedup();

// retain keeps elements matching the predicate, in-place
v.retain(|&x| x % 2 == 0);

// filter produces a new Vec, original intact
let evens: Vec<i32> = v.iter().filter(|&&x| x % 2 == 0).copied().collect();
```

## Splitting and Windowing

```rust
let tail = v.split_off(3);          // v keeps [0..3), tail gets [3..)
let chunks: Vec<&[i32]> = v.chunks(2).collect();    // non-overlapping
let windows: Vec<&[i32]> = v.windows(3).collect();  // overlapping
```

## Common Patterns

```rust
// collect from iterator chain
let evens: Vec<i32> = (0..10).filter(|x| x % 2 == 0).collect();

// flatten nested vecs
let flat: Vec<i32> = vec![vec![1,2], vec![3,4]].into_iter().flatten().collect();

// remove a specific value
v.retain(|&x| x != 3);

// deep copy
let clone = v.clone();
```

## Panics

- `v[i]` — index out of bounds
- `v.insert(i, x)` — index > len
- `v.remove(i)` — index out of bounds

Use the `get`/`get_mut` variants to avoid panics in untrusted contexts.

## See Also

- [[VecDeque]] — O(1) push/pop at both ends
- [[BinaryHeap]] — always-max (or always-min) priority access
