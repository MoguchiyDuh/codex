---
tags:
  - rust
  - iterators
source: iterators/src/patterns.rs
---

# Iterator Patterns

Practical composition recipes. These aren't new APIs — they're combinations of the primitives from [[Adapters]] and [[Consumers]].

## Pipeline Chaining

Build data processing pipelines by composing adapters. The compiler monomorphizes the entire chain into a single loop with no intermediate allocations — this is what "zero-cost abstractions" means in practice:

```rust
let result: Vec<i32> = numbers
    .iter()
    .filter(|&&x| x % 2 == 0) // keep evens
    .map(|&x| x * x)           // square
    .filter(|&x| x > 10)       // keep > 10
    .collect();
```

Iterators vs. a hand-written loop produce equivalent assembly. Prefer the iterator style for readability.

## Grouping

`HashMap::entry` is the idiomatic grouping pattern. There's no `group_by` in std for owned data:

```rust
let mut grouped: HashMap<&str, Vec<i32>> = HashMap::new();
for (key, value) in items {
    grouped.entry(key).or_insert_with(Vec::new).push(value);
}
```

## Windowed / Sliding Aggregation

`slice::windows(n)` yields overlapping sub-slices of length `n`. Useful for moving averages, rolling stats:

```rust
let moving_avg: Vec<f64> = temps
    .windows(3)
    .map(|w| w.iter().sum::<i32>() as f64 / 3.0)
    .collect();
```

## Deduplication of Consecutive Runs

For adjacent duplicates, `peekable` is cleaner than sorting + dedup when order must be preserved:

```rust
let mut deduped: Vec<i32> = Vec::new();
let mut iter = with_dups.iter().peekable();
while let Some(&val) = iter.next() {
    deduped.push(val);
    while iter.peek() == Some(&&val) {
        iter.next(); // skip duplicates
    }
}
```

## Splitting on a Sentinel

`slice::split(predicate)` yields sub-slices between matches. Empty chunks (from consecutive sentinels) can be filtered:

```rust
let chunks: Vec<Vec<i32>> = data
    .split(|&x| x == 0)
    .filter(|c| !c.is_empty())
    .map(|c| c.to_vec())
    .collect();
```

## Running State with `scan`

`scan` is like `fold` but yields each intermediate accumulator as an element. The closure returns `Option` — returning `None` terminates early:

```rust
let balances: Vec<i32> = transactions
    .iter()
    .scan(0, |balance, &amount| {
        *balance += amount;
        Some(*balance)
    })
    .collect();
// [100, 80, 130, 100, 300] for [100, -20, 50, -30, 200]
```

## Two-Pass Pattern

When you need both statistics and a transformation, compute stats first, then map:

```rust
let sum: i32   = values.iter().sum();
let count       = values.len();
let avg: f64   = sum as f64 / count as f64;

let normalized: Vec<f64> = values.iter().map(|&x| x as f64 - avg).collect();
```

## Folding into a Custom Struct

`fold` generalizes beyond numbers — use it to build any accumulator in a single pass:

```rust
let stats = nums.iter().fold(
    Stats { count: 0, sum: 0, min: i32::MAX, max: i32::MIN },
    |mut acc, &x| {
        acc.count += 1;
        acc.sum   += x;
        acc.min    = acc.min.min(x);
        acc.max    = acc.max.max(x);
        acc
    },
);
```

## Early Termination

`find`, `any`, `all` short-circuit — they stop iterating as soon as the answer is known. Prefer them over `filter(...).count() > 0`:

```rust
// Does not iterate all 1_000_000 elements:
let found: Option<i32> = (1..=1_000_000).find(|&x| x * x > 500);
```

## Cartesian Product

Nested `flat_map` produces all combinations. The `move` on the inner closure captures `color` by value since `flat_map` is lazy and the outer reference would outlive the closure:

```rust
let combos: Vec<(&str, &str)> = colors
    .iter()
    .flat_map(|&color| sizes.iter().map(move |&size| (color, size)))
    .collect();
```

## Flattening Nested `Option` / `Result`

`Option<T>` and `Result<T, E>` implement `IntoIterator` (zero or one element), so `flatten()` unwraps one nesting layer at a time:

```rust
// Vec<Option<Vec<i32>>> → Vec<i32>
let flat: Vec<i32> = nested.into_iter().flatten().flatten().collect();
// First flatten: Option<Vec<i32>> → Vec<i32> items
// Second flatten: Vec<i32> → i32 items
```

## Batching for Parallel Work

`slice::chunks(n)` yields non-overlapping sub-slices of at most `n` elements. The last chunk may be smaller:

```rust
let batches: Vec<Vec<i32>> = large
    .chunks(25)
    .map(|chunk| chunk.to_vec())
    .collect();
```

## Interleaving Two Iterators

No standard adapter exists — use a loop with `match` on a tuple of `next()` results:

```rust
let mut interleaved: Vec<i32> = Vec::new();
let mut iter_a = a.iter();
let mut iter_b = b.iter();
loop {
    match (iter_a.next(), iter_b.next()) {
        (Some(&x), Some(&y)) => { interleaved.push(x); interleaved.push(y); }
        (Some(&x), None)     => interleaved.push(x),
        (None, Some(&y))     => interleaved.push(y),
        (None, None)         => break,
    }
}
```

## Related Notes

- [[Adapters]] — `scan`, `flat_map`, `peekable`, `windows`, `chunks`
- [[Consumers]] — `fold`, `find`, `any`, `all`, `collect`
- [[Advanced]] — more slice iterators and `std::iter` constructors
