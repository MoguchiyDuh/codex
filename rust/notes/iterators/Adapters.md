---
tags:
  - rust
  - iterators
source: iterators/src/adapters.rs
---

# Iterator Adapters

Adapters transform an iterator into another iterator. They are **lazy** — nothing executes until a consumer (like `collect` or a `for` loop) drives the chain. See [[Basics#Lazy Evaluation]].

## Transformation

### `map`
Applies a closure to each element, yielding the return value:
```rust
let doubled: Vec<i32> = vec![1, 2, 3].iter().map(|x| x * 2).collect();
// [2, 4, 6]
```

### `filter`
Keeps only elements where the closure returns `true`:
```rust
let evens: Vec<i32> = vec![1, 2, 3, 4, 5].iter().copied().filter(|&x| x % 2 == 0).collect();
// [2, 4]
```

### `filter_map`
Combines `filter` + `map`: the closure returns `Option<U>`. `None` drops the element, `Some(v)` passes `v` downstream. Cleaner than `filter` + `map` when parsing or converting:
```rust
let parsed: Vec<i32> = vec!["1", "two", "3"]
    .iter()
    .filter_map(|s| s.parse::<i32>().ok())
    .collect();
// [1, 3]
```

### `flat_map`
Maps each element to an iterator, then flattens one level. Equivalent to `.map(...).flatten()`:
```rust
let chars: Vec<char> = vec!["hello", "world"]
    .iter()
    .flat_map(|s| s.chars())
    .collect();
```

### `flatten`
Flattens one level of nesting. Works on any iterator whose items implement `IntoIterator`:
```rust
let flat: Vec<i32> = vec![vec![1, 2], vec![3, 4]].into_iter().flatten().collect();
```

## Slicing and Skipping

### `take(n)` / `skip(n)`
`take` yields the first `n` elements; `skip` discards the first `n`. Combine for range slicing:
```rust
// Elements at index 1, 2, 3:
let middle: Vec<i32> = numbers.iter().copied().skip(1).take(3).collect();
```

### `take_while` / `skip_while`
Predicate-based variants — stop taking / start yielding once the predicate fails. Unlike `filter`, they are not restartable; once the predicate fails, the rest of the sequence is dropped or passed through unconditionally:
```rust
let leading: Vec<i32> = numbers.iter().copied().take_while(|&x| x < 4).collect();
let trailing: Vec<i32> = numbers.iter().copied().skip_while(|&x| x < 3).collect();
```

### `step_by(n)`
Yields every `n`th element (0th, nth, 2nth, …):
```rust
let every_2nd: Vec<i32> = numbers.iter().copied().step_by(2).collect();
```

## Combining

### `chain`
Concatenates two iterators of the same item type:
```rust
let combined: Vec<i32> = a.iter().chain(b.iter()).chain(c.iter()).copied().collect();
```

### `zip`
Pairs elements from two iterators into tuples. Stops at the shorter iterator:
```rust
let zipped: Vec<(&str, i32)> = names.iter().copied().zip(ages.iter().copied()).collect();
```

### `enumerate`
Wraps each item with its 0-based index:
```rust
let indexed: Vec<(usize, &str)> = fruits.iter().copied().enumerate().collect();
// [(0, "apple"), (1, "banana"), ...]
```

## Inspection and Control

### `peekable`
Wraps the iterator so you can call `.peek()` to view the next item without consuming it. Useful for lookahead parsing:
```rust
let mut p = vec![1, 2, 3].iter().peekable();
while let Some(&val) = p.peek() {
    // decide based on val, then advance
    p.next();
}
```

### `inspect`
Passes elements through unchanged but runs a closure as a side effect — useful for debugging a chain without breaking it:
```rust
let result: Vec<i32> = numbers
    .iter()
    .copied()
    .inspect(|x| println!("before map: {}", x))
    .map(|x| x * 2)
    .inspect(|x| println!("after map: {}", x))
    .collect();
```

### `rev`
Reverses iteration order. Requires the underlying iterator to implement `DoubleEndedIterator` (e.g., slices, ranges). See [[Custom Iterators#DoubleEndedIterator]].

### `cycle`
Repeats the iterator infinitely. Always pair with `take()`:
```rust
let cycled: Vec<i32> = vec![1, 2, 3].into_iter().cycle().take(10).collect();
// [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
```

### `fuse`
Wraps an iterator to guarantee it returns `None` indefinitely after the first `None`. Most std iterators already behave this way, but custom ones may not (see [[Custom Iterators#FusedIterator]]).

## `copied` and `cloned`

`iter()` yields `&T`. These adapters promote references to owned values:

- `copied()` — for `Copy` types; equivalent to `.map(|x| *x)`
- `cloned()` — for `Clone` types; calls `.clone()` on each element

## Chaining Adapters

Adapters compose freely. The compiler monomorphizes the entire chain into a single tight loop — no intermediate allocations:

```rust
let result: Vec<i32> = (1..=20)
    .filter(|x| x % 2 == 0) // evens: 2, 4, 6, ..., 20
    .map(|x| x * 3)          // tripled
    .skip(2)                  // drop first two
    .take(4)                  // keep next four
    .collect();
```

## Related Notes

- [[Basics]] — `iter()` vs `iter_mut()` vs `into_iter()`
- [[Consumers]] — terminating the chain
- [[Advanced]] — `scan`, `map_while`, slice methods like `windows` and `chunks`
- [[Patterns]] — real-world composition recipes
