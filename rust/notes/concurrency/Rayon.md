---
tags: [rust, concurrency, rayon, parallelism]
source: concurrency/src/rayon_parallel.rs
---

# Rayon

Rayon is a data-parallelism library. It lets you convert sequential iterator chains to parallel ones by swapping `.iter()` for `.par_iter()`. It uses a work-stealing thread pool sized to the number of logical CPU cores by default.

Rayon is for CPU-bound data processing. For async I/O concurrency use [[Tokio Runtime]] instead.

## Basic Parallel Iteration

Add `use rayon::prelude::*` and replace the iterator method:

```rust
use rayon::prelude::*;

let mut data = vec![1, 2, 3, 4, 5, 6, 7, 8];

// parallel mutable
data.par_iter_mut().for_each(|x| *x *= 2);

// parallel map + collect
let squared: Vec<i32> = data.par_iter().map(|x| x * x).collect();

// parallel filter
let evens: Vec<i32> = data.par_iter().filter(|&&x| x % 2 == 0).copied().collect();

// parallel filter_map
let big: Vec<i32> = data.par_iter()
    .filter_map(|&x| if x > 5 { Some(x * 2) } else { None })
    .collect();
```

For owned iteration: `vec.into_par_iter()`. For ranges: `(0..100).into_par_iter()`.

## Parallel Reductions

### fold + reduce

Rayon's parallel `fold` splits the data into per-thread local accumulators (identity factory `|| 0`), then `reduce` combines the partial results — a two-phase reduction:

```rust
let sum: i32 = data.par_iter()
    .fold(|| 0, |acc, &x| acc + x) // per-thread partial sums
    .reduce(|| 0, |a, b| a + b);   // combine partials
```

### reduce

For commutative, associative operations:

```rust
let product: i32 = (1..=10).into_par_iter().reduce(|| 1, |a, b| a * b);
```

### Convenience Methods

```rust
let sum: i32    = data.par_iter().sum();
let all_pos     = data.par_iter().all(|&x| x > 0);
let any_big     = data.par_iter().any(|&x| x > 50);
let found       = data.par_iter().find_any(|&&x| x > 50); // non-deterministic
```

`find_any` returns whichever match any thread finds first — the result is non-deterministic across runs.

## Parallel Chunks

```rust
let chunk_sums: Vec<i32> = data.par_chunks(10)
    .map(|chunk| chunk.iter().sum())
    .collect();
```

`par_chunks` divides the slice into chunks of at most N elements and processes each chunk in parallel.

## Partition

```rust
let (evens, odds): (Vec<i32>, Vec<i32>) = data.into_par_iter().partition(|x| x % 2 == 0);
```

## Custom Thread Pool

The global pool uses all CPU cores. Override with `ThreadPoolBuilder`:

```rust
let pool = rayon::ThreadPoolBuilder::new()
    .num_threads(4)
    .thread_name(|i| format!("worker-{}", i))
    .build()
    .unwrap();

pool.install(|| {
    let sum: i32 = data.par_iter().sum();
    println!("{}", sum);
});
```

`pool.install(|| ...)` runs the closure in the context of that pool. Work inside uses the pool's threads, not the global pool.

Check the current pool size:

```rust
println!("{}", rayon::current_num_threads());
```

## When Rayon Helps (and Doesn't)

Parallelism has overhead: work distribution, cache misses, thread synchronization. For small datasets the overhead dominates:

```rust
// 10_000_000 elements: parallel is meaningfully faster
let sum: u64 = large_data.par_iter().sum();

// 100 elements: parallel is often slower
let sum: i32 = small_data.par_iter().sum(); // overhead > benefit
```

Rule of thumb: benchmark first. Rayon pays off when per-element work is non-trivial or data is large (typically 10k+ elements for cheap ops).

## Key Points

- Drop-in: swap `.iter()` for `.par_iter()`, `.iter_mut()` for `.par_iter_mut()`, `.into_iter()` for `.into_par_iter()`.
- Default pool = logical CPU cores; override with `ThreadPoolBuilder`.
- `fold` + `reduce` for two-phase parallel reductions.
- `find_any` is non-deterministic.
- Small workloads: parallel overhead exceeds benefit — measure before committing.
- Not for async I/O; use [[Tokio Runtime]] for that.

## Related

- [[Threads]] — OS threads via `std::thread`
- [[Patterns]] — worker pool pattern as an alternative for task-based parallelism
