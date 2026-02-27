---
tags:
  - rust
  - iterators
source: iterators/src/basics.rs
---

# Iterator Basics

## The Three Iteration Methods

Every collection in Rust exposes three flavors of iteration, each with different ownership semantics:

| Method | Yields | Ownership |
|---|---|---|
| `iter()` | `&T` | Borrows — original still usable |
| `iter_mut()` | `&mut T` | Mutably borrows — can modify in place |
| `into_iter()` | `T` | Moves — original is consumed |

```rust
let v = vec![1, 2, 3];

// Borrows: v is still valid after
for x in v.iter() { /* &i32 */ }

// Mutates in place
let mut v2 = vec![1, 2, 3];
for x in v2.iter_mut() { *x *= 2; }

// Consumes: v3 is moved, unusable after
let v3 = vec![10, 20, 30];
for x in v3.into_iter() { /* i32 */ }
```

## The `Iterator` Trait

All iterators implement the `Iterator` trait. The only required method is `next()`:

```rust
pub trait Iterator {
    type Item;
    fn next(&mut self) -> Option<Self::Item>;
}
```

`next()` returns `Some(item)` while elements remain, then `None` when exhausted.

## For Loop Desugaring

A `for` loop is syntactic sugar over `IntoIterator` + `next()`:

```rust
// These are equivalent:
for x in &arr { /* ... */ }

let mut iter = arr.iter();
while let Some(x) = iter.next() { /* ... */ }
```

`for x in &arr` calls `arr.iter()`. `for x in arr` calls `arr.into_iter()`.

## Lazy Evaluation

Iterators are lazy — no work happens until a consumer is called:

```rust
let v = vec![1, 2, 3, 4, 5];

// This does nothing — the closure never runs:
let lazy = v.iter().map(|x| x * 2);

// This triggers evaluation:
let result: Vec<i32> = v.iter().map(|x| x * 2).collect();
```

## `copied()` and `cloned()`

`iter()` yields references. Use adapters to get owned values:

```rust
let v = vec![1, 2, 3];

// Copy types (i32, bool, etc.): use copied()
let doubled: Vec<i32> = v.iter().copied().map(|x| x * 2).collect();

// Non-Copy types: use cloned()
let strings = vec![String::from("a"), String::from("b")];
let cloned: Vec<String> = strings.iter().cloned().collect();
// strings is still valid
```

## `size_hint()`

Returns `(lower_bound, Option<upper_bound>)` — an estimate of remaining elements. Used by the allocator to pre-size `Vec` in `collect()`. Not guaranteed to be exact unless `ExactSizeIterator` is implemented (see [[Custom Iterators]]).

## Infinite Iterators

Some iterators never return `None`. Always pair with `take()` or similar to bound them:

```rust
let first_5: Vec<i32> = std::iter::repeat(42).take(5).collect();

// Open range is also infinite:
let first_10: Vec<i32> = (1..).take(10).collect();
```

## Iterable Types

Beyond `Vec`, most standard collections implement `IntoIterator`:

- `[T; N]` / `&[T]` slices — `iter()` / `into_iter()`
- `String` — `s.chars()`, `s.bytes()`, `s.lines()`
- `HashMap<K, V>` — yields `(&K, &V)` on `iter()`
- `HashSet<T>` — yields `&T` on `iter()`
- Ranges `(1..=10)` — implement `Iterator` directly

## Related Notes

- [[Adapters]] — transforming iterators lazily
- [[Consumers]] — triggering evaluation
- [[Custom Iterators]] — implementing `Iterator` yourself
