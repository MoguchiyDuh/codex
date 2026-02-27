---
tags:
  - rust
  - smart-pointers
  - concurrency
  - interior-mutability
source: smart_pointers/src/mutex_rwlock.rs
---

# Mutex\<T\> & RwLock\<T\>

Both types provide **thread-safe interior mutability**. They are the concurrent counterparts of [[RefCell]]: instead of runtime borrow-flag checks, they block the calling thread until exclusive access is available.

## Mutex\<T\>

`Mutex<T>` (mutual exclusion) allows either one writer or no access. `lock()` blocks until the lock is acquired and returns a `MutexGuard<T>`. The guard releases the lock when dropped — RAII (Resource Acquisition Is Initialization — tying resource lifetime to object lifetime) at work:

```rust
let m: Mutex<i32> = Mutex::new(5);
{
    let mut num = m.lock().unwrap();
    *num = 10;
} // guard dropped here, lock released
```

### Arc\<Mutex\<T\>\> — shared mutable state across threads

The standard pattern for any shared counter, queue, or state machine:

```rust
let counter: Arc<Mutex<i32>> = Arc::new(Mutex::new(0));

for i in 0..10 {
    let c = Arc::clone(&counter);
    thread::spawn(move || {
        *c.lock().unwrap() += 1;
    });
}
```

### try_lock — non-blocking attempt

```rust
match mutex.try_lock() {
    Ok(guard) => println!("{}", *guard),
    Err(_)    => println!("already locked"),
}
```

Returns immediately with `Err` if the lock is held elsewhere.

### Poison

If a thread panics while holding a `Mutex`, the mutex becomes **poisoned**. All subsequent `lock()` calls return `Err(PoisonError)`. This prevents other threads from observing potentially inconsistent data. To recover:

```rust
match mutex.lock() {
    Ok(guard)  => use_guard(guard),
    Err(e)     => {
        let guard = e.into_inner(); // extract data despite poison
        use_guard(guard);
    }
}
```

### get_mut — lock-free single-owner access

When you hold `&mut Mutex<T>` (sole access guaranteed by the borrow checker), `get_mut()` skips locking entirely:

```rust
let mut m: Mutex<i32> = Mutex::new(10);
*m.get_mut().unwrap() += 5;
```

### Minimize lock duration

Hold locks for the shortest possible time to reduce contention:

```rust
let value = {
    let guard = shared.lock().unwrap();
    *guard // copy out what you need
}; // lock released
do_slow_work(value); // outside the lock
```

## RwLock\<T\>

`RwLock<T>` (read-write lock) distinguishes between readers and writers:
- Multiple readers simultaneously — `read()` returns `RwLockReadGuard<T>`
- Single writer, no concurrent readers — `write()` returns `RwLockWriteGuard<T>`

```rust
let lock: RwLock<i32> = RwLock::new(5);

// Many readers concurrently
let r1 = lock.read().unwrap();
let r2 = lock.read().unwrap();
println!("{} {}", r1, r2);
drop(r1); drop(r2);

// One writer
*lock.write().unwrap() += 1;
```

### Arc\<RwLock\<T\>\>

```rust
let data: Arc<RwLock<Vec<i32>>> = Arc::new(RwLock::new(vec![1, 2, 3]));

// Spin up reader threads
for i in 0..3 {
    let d = Arc::clone(&data);
    thread::spawn(move || {
        println!("Reader {}: {:?}", i, *d.read().unwrap());
    });
}

// One writer
let d = Arc::clone(&data);
thread::spawn(move || d.write().unwrap().push(4));
```

### try_read / try_write

Non-blocking variants, same semantics as `try_lock` on `Mutex`.

## Deadlock avoidance

If two threads each hold one lock and try to acquire the other, both block forever. The fix: always acquire locks **in the same order**:

```rust
// Both threads: acquire mutex_a THEN mutex_b — never reversed
let _a = mutex_a.lock().unwrap();
let _b = mutex_b.lock().unwrap();
```

## Mutex vs RwLock

| | `Mutex<T>` | `RwLock<T>` |
|---|---|---|
| Concurrent reads | No | Yes |
| Write access | Exclusive | Exclusive |
| Overhead | Lower | Higher |
| Risk of writer starvation | No | Possible (platform-dependent) |
| Best for | Balanced read/write or write-heavy | Read-heavy workloads |

In practice, use `Mutex` unless profiling shows lock contention on reads, then consider `RwLock`.

## Common combinations

```rust
Arc<Mutex<T>>         // shared mutable state, general case
Arc<RwLock<T>>        // shared state, read-heavy
Arc<Mutex<HashMap>>   // thread-safe cache
```

## See also

- [[Arc]] — required to share `Mutex`/`RwLock` across threads
- [[RefCell]] — single-threaded interior mutability (no locking)
- [[Patterns]] — `Arc<Mutex<T>>` cache pattern, scoped locking
