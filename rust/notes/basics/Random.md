---
tags: [rust, basics, random, rand]
source: basics/src/random.rs
---

# Random Numbers

Uses the `rand` crate.

```toml
[dependencies]
rand = "0.9"
```

## Basics

```rust
use rand::prelude::*;

let mut rng = rand::rng();  // thread-local RNG (Random Number Generator)

let n: i32  = rng.random();             // random value of any type
let roll    = rng.random_range(1..=6);  // inclusive range [1, 6]
let heads   = rng.random_bool(0.5);     // true with probability p
```

## Common types

```rust
let f: f64 = rng.random();              // [0.0, 1.0)
let i: i32 = rng.random();             // any i32
let b: bool = rng.random();
```

## Ranges

```rust
rng.random_range(0..10)     // [0, 10) exclusive end
rng.random_range(1..=6)     // [1, 6] inclusive end
rng.random_range(0.0..1.0)  // floats too
```

## Shuffling

```rust
let mut v = vec![1, 2, 3, 4, 5];
v.shuffle(&mut rng);
```

## Seeded RNG (Random Number Generator) (reproducible)

```rust
use rand::SeedableRng;
use rand::rngs::StdRng;

let mut rng = StdRng::seed_from_u64(42);
let n: i32 = rng.random();  // same result every run with same seed
```
