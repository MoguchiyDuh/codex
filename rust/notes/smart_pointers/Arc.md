---
tags:
  - rust
  - smart-pointers
  - reference-counting
  - concurrency
source: smart_pointers/src/arc_pointer.rs
---

# Arc\<T\> & Weak\<T\>

`Arc<T>` (Atomically Reference Counted) is the thread-safe version of [[Rc]]. It uses atomic operations on its reference count, making it safe to clone and drop from multiple threads simultaneously. The API mirrors `Rc` almost exactly.

## Basic usage

```rust
use std::sync::Arc;

let data: Arc<String> = Arc::new(String::from("shared across threads"));
let clone = Arc::clone(&data); // atomic increment
```

## Sharing across threads

The canonical pattern: clone the `Arc` before spawning, move the clone into the thread:

```rust
let data: Arc<Vec<i32>> = Arc::new(vec![1, 2, 3, 4, 5]);

for i in 0..3 {
    let d = Arc::clone(&data);
    thread::spawn(move || {
        println!("Thread {}: sum = {}", i, d.iter().sum::<i32>());
    });
}
```

Each thread gets its own `Arc` (a pointer + atomic counter bump). The underlying data is shared — zero copies.

## Immutability

Like `Rc`, `Arc<T>` only provides `&T`. For mutable shared state across threads, combine with [[Mutex & RwLock]]: `Arc<Mutex<T>>`.

## Weak\<T\>

`std::sync::Weak<T>` works identically to `std::rc::Weak<T>` — non-owning, must upgrade to access:

```rust
let strong: Arc<i32> = Arc::new(42);
let weak: Weak<i32> = Arc::downgrade(&strong);

// Upgrade works from any thread
let handle = thread::spawn(move || match weak.upgrade() {
    Some(arc) => println!("{}", arc),
    None      => println!("dropped"),
});
```

Useful for the same cycle-breaking pattern as with `Rc` — e.g. a cache that holds `Weak` references so entries can be evicted when all other owners drop.

## try_unwrap / get_mut

Same semantics as `Rc`:

- `Arc::try_unwrap(arc)` — succeeds only if `strong_count == 1`, returns `Ok(T)`
- `Arc::get_mut(&mut arc)` — returns `Option<&mut T>`, succeeds only if `strong_count == 1`

```rust
let mut unique: Arc<String> = Arc::new(String::from("solo"));
if let Some(s) = Arc::get_mut(&mut unique) {
    s.push_str(" modified");
}
```

## ptr_eq

```rust
let a1 = Arc::new(10);
let a2 = Arc::clone(&a1);
let a3 = Arc::new(10);

Arc::ptr_eq(&a1, &a2); // true
Arc::ptr_eq(&a1, &a3); // false
```

## Arc vs Rc — when to pick which

| | `Rc<T>` | `Arc<T>` |
|---|---|---|
| Thread-safe | No | Yes |
| Counter operations | Plain integer | Atomic |
| Relative cost | Faster | ~10–50 ns overhead per clone/drop |
| `Send` + `Sync` | No | Yes (when `T: Send + Sync`) |

Prefer `Rc` within a single thread; reach for `Arc` only when you need to share across threads. Both have the same pointer size (8 bytes on 64-bit).

## Common patterns

```rust
// Read-only config shared across workers
let config: Arc<Config> = Arc::new(Config { ... });
for _ in 0..N {
    let cfg = Arc::clone(&config);
    thread::spawn(move || use_config(&cfg));
}

// Mutable shared state — needs Mutex
let counter: Arc<Mutex<i32>> = Arc::new(Mutex::new(0));
```

See [[Patterns]] for full worked examples.

## See also

- [[Rc]] — single-threaded counterpart (cheaper)
- [[Mutex & RwLock]] — required for mutation through `Arc`
- [[Patterns]] — `Arc<Mutex<T>>`, `Arc<RwLock<T>>`, read-only config
