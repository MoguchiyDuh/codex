---
tags: [rust, concurrency, shared-state, mutex, rwlock, atomics, arc]
source: concurrency/src/shared_state.rs
---

# Shared State

When threads need to read or mutate the same data, Rust forces you to pick an explicit synchronization strategy. The three main tools are `Arc` (read-only sharing), `Mutex`/`RwLock` (guarded mutation), and atomics (lock-free primitives).

## Arc — Shared Ownership

`Arc<T>` (Atomic Reference Counted) allows multiple threads to own the same immutable value. See [[../smart_pointers/Arc|Arc]] for the full ownership model.

```rust
let data: Arc<Vec<i32>> = Arc::new(vec![1, 2, 3]);

for i in 0..3 {
    let clone = Arc::clone(&data);
    thread::spawn(move || {
        println!("thread {}: sum = {}", i, clone.iter().sum::<i32>());
    });
}
```

`Arc::clone` increments the reference count atomically. The underlying data is dropped when the count hits zero.

## Arc\<Mutex\<T\>>

`Mutex<T>` wraps data with a mutual exclusion lock. Only one thread holds the lock at a time. Combine with `Arc` to share across threads.

```rust
let counter: Arc<Mutex<i32>> = Arc::new(Mutex::new(0));

let handles: Vec<_> = (0..10).map(|_| {
    let c = Arc::clone(&counter);
    thread::spawn(move || {
        let mut num = c.lock().unwrap(); // blocks until lock acquired
        *num += 1;
        // MutexGuard drops here, lock released
    })
}).collect();

for h in handles { h.join().unwrap(); }
println!("{}", *counter.lock().unwrap()); // 10
```

`lock()` returns `Result<MutexGuard<T>, PoisonError>`. A mutex becomes *poisoned* if a thread panics while holding the lock. Most code just `unwrap()` — if a thread panicked in a critical section, the program state is likely corrupt anyway.

Lock scope matters. Drop the guard before any `.await` or long work:

```rust
{
    let mut guard = mutex.lock().unwrap();
    *guard += 1;
} // guard dropped, lock released before sleep
thread::sleep(Duration::from_millis(100));
```

## Arc\<RwLock\<T\>>

`RwLock<T>` allows **multiple concurrent readers** or **one exclusive writer** — never both simultaneously. Better than `Mutex` when reads heavily outnumber writes.

```rust
let data: Arc<RwLock<i32>> = Arc::new(RwLock::new(0));

// Writer
let w = Arc::clone(&data);
thread::spawn(move || {
    let mut guard = w.write().unwrap(); // exclusive
    *guard += 1;
});

// Reader (multiple can hold simultaneously)
let r = Arc::clone(&data);
thread::spawn(move || {
    let guard = r.read().unwrap();
    println!("{}", *guard);
});
```

Like `Mutex`, `RwLock` can be poisoned. On Linux, `RwLock` can starve writers if readers keep arriving — not guaranteed fair.

## Atomics

Atomics are lock-free shared integers/booleans. No mutex overhead, but limited to simple operations. Always pair with an explicit `Ordering`.

```rust
let counter: Arc<AtomicI32> = Arc::new(AtomicI32::new(0));

let handles: Vec<_> = (0..10).map(|_| {
    let c = Arc::clone(&counter);
    thread::spawn(move || {
        for _ in 0..100 {
            c.fetch_add(1, Ordering::SeqCst);
        }
    })
}).collect();
```

### Memory Ordering

| Ordering | Meaning |
|----------|---------|
| `SeqCst` | Total sequential order across all threads — safest default |
| `Acquire` | Loads: see all writes before the matching `Release` |
| `Release` | Stores: publish all preceding writes |
| `Relaxed` | No ordering guarantees — only atomicity |

Use `SeqCst` unless you understand the memory model. `Relaxed` is for counters where you only care about the final value, not ordering relative to other operations.

### Common Operations

```rust
let flag = Arc::new(AtomicBool::new(false));

// spinwait on flag
while !flag.load(Ordering::SeqCst) {
    thread::sleep(Duration::from_millis(50));
}

// compare-and-swap (CAS): sets new only if current == expected
let result = value.compare_exchange(
    42,   // expected
    100,  // new
    Ordering::SeqCst,
    Ordering::SeqCst,
);
// Ok(prev) on success, Err(actual) on failure
```

## Deadlocks

A deadlock occurs when two threads each hold a lock the other needs. The fix is **consistent lock ordering** — always acquire locks in the same order across all threads.

```rust
// DEADLOCK: thread A locks r1 then r2, thread B locks r2 then r1
// FIX: both threads lock r1 first, then r2
let _lock1 = resource1.lock().unwrap();
let _lock2 = resource2.lock().unwrap();
```

Other strategies: use `try_lock` with backoff, or eliminate shared state via [[Channels]] or the [[Patterns#Actor Pattern|actor pattern]].

## Choosing the Right Primitive

| Scenario | Tool |
|----------|------|
| Read-only data across threads | `Arc<T>` |
| Single writer or infrequent writes | `Arc<Mutex<T>>` |
| Many readers, few writers | `Arc<RwLock<T>>` |
| Simple counters/flags | `Arc<AtomicI32>` / `Arc<AtomicBool>` |
| Async context | `tokio::sync::Mutex` (see [[Tokio Runtime]]) |

## Related

- [[Threads]] — spawning the threads that share this state
- [[Patterns]] — actor pattern as an alternative to shared state
