---
tags:
  - rust
  - iterators
source: iterators/src/advanced.rs
---

# Advanced Iterators

## `scan`

Like `fold` but yields each intermediate accumulator value as `Some`. The closure returns `Option` — returning `None` terminates the iterator early, unlike `fold` which always runs to completion:

```rust
let running_sum: Vec<i32> = numbers
    .iter()
    .scan(0, |state, x| {
        *state += x;
        Some(*state)
    })
    .collect();
// [1, 3, 6, 10, 15]
```

See [[Patterns#Running State with scan]] for a practical use case.

## Slice Window / Chunk Iterators

These operate on slices (`&[T]`), not on general `Iterator`. They yield sub-slices, not owned values.

### `windows(n)`
Overlapping windows of exactly `n` elements. Each step advances by one:
```
[1,2,3,4,5].windows(3) → [1,2,3], [2,3,4], [3,4,5]
```

### `chunks(n)`
Non-overlapping. The last chunk may be shorter than `n`:
```
[1,2,3,4,5,6,7].chunks(3) → [1,2,3], [4,5,6], [7]
```

### `chunks_exact(n)`
Like `chunks` but only yields complete chunks. The leftover elements are accessible via `.remainder()`:
```rust
let mut iter = data.chunks_exact(3);
for chunk in iter.by_ref() { /* only full chunks */ }
let rem = iter.remainder(); // [7] in the example above
```

### `rchunks(n)` / `rchunks_exact(n)`
Same as `chunks` / `chunks_exact` but starts chunking from the **end** of the slice.

### `split(predicate)`
Splits on elements matching the predicate. Yields zero-length slices for consecutive matches:
```rust
for part in text.split(|&x| x == 0) { /* ... */ }
```

## `std::iter` Constructors

These create iterators from scratch without a source collection.

### `once(value)`
Single-element iterator. Useful for prepending/appending to a chain:
```rust
let combined: Vec<i32> = std::iter::once(0)
    .chain(numbers.iter().copied())
    .chain(std::iter::once(99))
    .collect();
```

### `repeat(value)`
Infinite iterator cloning the value on each step. Always pair with `take()`:
```rust
let repeated: Vec<i32> = std::iter::repeat(7).take(5).collect();
```

### `repeat_with(closure)`
Like `repeat` but evaluates the closure each time — needed when the value isn't `Clone` or when you need side effects:
```rust
let mut n = 0;
let inc: Vec<i32> = std::iter::repeat_with(|| { n += 1; n }).take(5).collect();
// [1, 2, 3, 4, 5]
```

### `empty()`
An iterator that immediately returns `None`. Useful as a neutral element for `chain` or as a default:
```rust
let e: Vec<i32> = std::iter::empty().collect(); // []
```

### `successors(initial, f)`
Generates a sequence where each element is derived from the previous one. `f` returns `Option` — `None` terminates the sequence. More composable than writing a custom iterator struct for simple recurrences:

```rust
// Fibonacci
let fib: Vec<u32> = std::iter::successors(Some((0u32, 1u32)), |&(a, b)| Some((b, a + b)))
    .map(|(a, _)| a)
    .take(10)
    .collect();

// Powers of 2 (stops at overflow if checked_mul is used)
let powers: Vec<i32> = std::iter::successors(Some(1), |&n| Some(n * 2))
    .take(10)
    .collect();
```

### `from_fn(closure)`
Creates an iterator from a stateful closure. Returns `None` to end iteration. Lightweight alternative to a custom struct when the state can be captured:

```rust
let mut count = 0;
let iter: Vec<i32> = std::iter::from_fn(|| {
    count += 1;
    if count <= 5 { Some(count * 10) } else { None }
}).collect();
// [10, 20, 30, 40, 50]
```

## `map_while`

Maps and takes while the closure returns `Some`. Stops on the first `None` — unlike `filter_map`, which continues past non-matching elements:

```rust
let result: Vec<i32> = (1..10)
    .map_while(|x| if x < 5 { Some(x * 2) } else { None })
    .collect();
// [2, 4, 6, 8]
```

## Peekable Lookahead

`peekable()` wraps an iterator to enable non-consuming peek. Useful for run-length encoding, parsers, and grouping consecutive duplicates:

```rust
let mut p = data.iter().peekable();
while let Some(&val) = p.next() {
    let mut count = 1;
    while p.peek() == Some(&&val) {
        count += 1;
        p.next();
    }
    println!("{} appears {} time(s)", val, count);
}
```

## Flattening `Option` and `Result`

Both `Option<T>` and `Result<T, E>` implement `IntoIterator`, yielding zero or one elements. `flatten()` exploits this to strip the wrapper:

```rust
// Keep only Some values:
let values: Vec<i32> = vec![Some(1), None, Some(2)].into_iter().flatten().collect();

// Keep only Ok values:
let ok: Vec<i32> = vec![Ok(1), Err("e"), Ok(2)].into_iter().flatten().collect();
```

## Manual Intersperse

`intersperse` is in nightly and `itertools`. Manual implementation with `enumerate`:

```rust
let mut result: Vec<&str> = Vec::new();
for (i, word) in words.iter().enumerate() {
    if i > 0 { result.push(" "); }
    result.push(word);
}
```

## Cycle with Take

`cycle()` repeats the underlying iterator indefinitely (requires the iterator to be clonable or re-creatable). Combine with `take()` to bound it:

```rust
let cycled: Vec<i32> = vec![1, 2, 3].into_iter().cycle().take(10).collect();
// [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
```

## Related Notes

- [[Basics]] — `size_hint`, infinite iterators, `repeat`
- [[Adapters]] — `scan`, `peekable`, `cycle`, `map_while`
- [[Custom Iterators]] — when `from_fn`/`successors` aren't enough and you need a struct
- [[Patterns]] — `windows` for moving averages, `chunks` for batching
