---
tags:
  - rust
  - iterators
source: iterators/src/consumers.rs
---

# Iterator Consumers

Consumers **drive evaluation** of the lazy iterator chain and produce a final result. After a consumer runs, the iterator is exhausted and cannot be reused.

## `collect`

Materializes the iterator into any type that implements `FromIterator`. The target type must be annotated (turbofish or binding type):

```rust
let v: Vec<i32>     = iter.collect();
let s: String       = chars.collect();
let set: HashSet<i32> = iter.collect();
let map: HashMap<&str, i32> = pairs.into_iter().collect();
```

**Collecting into `Result`:** If items are `Result<T, E>`, collecting into `Result<Vec<T>, E>` short-circuits on the first `Err` — it does not accumulate all errors:
```rust
let parsed: Result<Vec<i32>, _> = vec!["1", "2", "3"]
    .iter()
    .map(|s| s.parse::<i32>())
    .collect();
// Ok([1, 2, 3]) — all succeeded
```

## Aggregation

### `count`
Consumes the iterator and returns the number of elements.

### `sum` / `product`
Folds with addition or multiplication. The item type must implement `Sum` / `Product`:
```rust
let total: i32 = numbers.iter().sum();
let sum_sq: i32 = numbers.iter().map(|x| x * x).sum();
```

### `min` / `max`
Return `Option<&T>` (or `Option<T>` for owned iterators). Use `min_by_key` / `max_by_key` for custom ordering:
```rust
let longest = strings.iter().max_by_key(|s| s.len());
```

## Search

### `find`
Returns `Option<&T>` — the first element satisfying the predicate. Short-circuits on match:
```rust
let found: Option<&i32> = numbers.iter().find(|&&x| x > 3);
```

### `position`
Like `find` but returns `Option<usize>` — the 0-based index of the first match.

### `any` / `all`
Short-circuiting boolean tests over the whole sequence:
```rust
let has_even = numbers.iter().any(|&x| x % 2 == 0);  // stops at first even
let all_pos  = numbers.iter().all(|&x| x > 0);        // stops at first non-positive
```

## Folding

### `fold`
The general accumulator. Takes an initial value and a closure `(acc, item) -> acc`. Runs to completion — no short-circuit:
```rust
let sum = numbers.iter().fold(0, |acc, x| acc + x);
let s   = vec!["a", "b", "c"].iter().fold(String::new(), |acc, s| acc + s);
```

### `reduce`
Like `fold` but uses the first element as the initial accumulator (so the closure receives `T`, not `&T`). Returns `None` on an empty iterator:
```rust
let sum: Option<i32> = numbers.iter().copied().reduce(|acc, x| acc + x);
```

### `try_fold`
A `fold` that can short-circuit. The closure returns `Result<B, E>` or `Option<B>`; the first `Err`/`None` stops iteration and is returned:
```rust
let result: Result<i32, String> = numbers.iter().try_fold(0, |acc, &x| {
    if x > 10 { return Err("too large".into()); }
    Ok(acc + x)
});
```

## Side Effects

### `for_each`
Runs a closure for each element. Equivalent to a `for` loop but fits into a method chain:
```rust
numbers.iter().for_each(|x| println!("{}", x));
```

### `try_for_each`
Like `for_each` but the closure returns `Result`/`Option`. Stops and returns on the first error.

## Positional Access

### `nth(n)`
Returns the `n`th element (0-indexed) and **consumes all elements up to and including it**. Subsequent calls to the iterator continue from `n+1`:
```rust
let mut iter = numbers.iter();
let _third = iter.nth(2);       // consumed 0, 1, 2
let fourth = iter.next();       // returns element at index 3
```

### `last`
Consumes the entire iterator and returns the final element as `Option`.

## Splitting

### `partition`
Splits into two `Vec`s based on a predicate — first collects truthy, then falsy:
```rust
let (evens, odds): (Vec<i32>, Vec<i32>) =
    numbers.iter().copied().partition(|&x| x % 2 == 0);
```

### `unzip`
Splits an iterator of `(A, B)` tuples into two separate collections:
```rust
let (firsts, seconds): (Vec<i32>, Vec<i32>) = pairs.into_iter().unzip();
```

## Short-Circuiting Summary

| Consumer | Short-circuits? |
|---|---|
| `find`, `position` | Yes — on first match |
| `any` | Yes — on first `true` |
| `all` | Yes — on first `false` |
| `try_fold`, `try_for_each` | Yes — on first `Err`/`None` |
| `collect`, `fold`, `sum`, `product` | No |

Short-circuit consumers avoid iterating the entire sequence, which matters for large or infinite sources.

## Related Notes

- [[Basics]] — lazy evaluation; why consumers are needed
- [[Adapters]] — building the chain that consumers drive
- [[Patterns]] — fold for custom accumulators, collect into `Result`
