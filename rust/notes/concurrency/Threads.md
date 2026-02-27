---
tags: [rust, concurrency, threads]
source: concurrency/src/threads.rs
---

# Threads

Rust's `std::thread` gives you OS threads. Each thread runs independently and the scheduler decides execution order — never assume interleaving order.

## Spawning

`thread::spawn` takes a closure and returns a `JoinHandle<T>` where `T` is the closure's return type. The closure must be `'static` (no borrowed references to locals) and `Send`.

```rust
let handle: thread::JoinHandle<i32> = thread::spawn(|| {
    return 42;
});

let result: Result<i32, Box<dyn std::any::Any + Send>> = handle.join();
```

`handle.join()` blocks until the thread finishes. If the thread panicked, `join()` returns `Err`. Dropping a handle without joining detaches the thread — it keeps running but you lose the ability to wait on it.

Spawning multiple threads and collecting results:

```rust
let handles: Vec<thread::JoinHandle<i32>> = (0..5)
    .map(|i| thread::spawn(move || i * i))
    .collect();

let results: Vec<i32> = handles.into_iter().map(|h| h.join().unwrap()).collect();
```

## Thread Builder

`thread::Builder` lets you configure a thread before spawning. `spawn` on `Builder` returns `io::Result<JoinHandle<T>>` — it can fail if the OS refuses to create the thread.

```rust
let handle = thread::Builder::new()
    .name("worker-1".to_string())
    .stack_size(4 * 1024 * 1024) // 4 MB
    .spawn(|| {
        println!("{}", thread::current().name().unwrap_or("unnamed"));
    })
    .unwrap();
```

The default stack size is platform-dependent (usually 2–8 MB). Increase it if you have deep recursion.

## Move Closures

`thread::spawn` requires `'static` captures, so you cannot borrow locals into a thread. Use `move` to transfer ownership:

```rust
let data: Vec<i32> = vec![1, 2, 3];

let handle = thread::spawn(move || {
    data.iter().sum::<i32>() // data moved in
});
// data is inaccessible here
```

To share data across multiple threads, clone before moving:

```rust
let original = "Hello".to_string();
let handles: Vec<_> = (0..3).map(|i| {
    let copy = original.clone();
    thread::spawn(move || format!("{} from thread {}", copy, i))
}).collect();
```

## Scoped Threads

`thread::scope` lifts the `'static` requirement. The scope guarantees all spawned threads finish before the closure returns, so they can safely borrow locals.

```rust
let data = vec![1, 2, 3, 4, 5];

thread::scope(|scope| {
    scope.spawn(|| println!("{:?}", data));        // immutable borrow OK
    scope.spawn(|| println!("sum: {}", data.iter().sum::<i32>()));
}); // both threads joined here, data borrow ends

// data still accessible
```

Scoped threads also allow mutable borrows of disjoint slices:

```rust
thread::scope(|scope| {
    let (left, right) = data.split_at_mut(mid);
    scope.spawn(move || { for v in left  { *v *= 2; } });
    scope.spawn(move || { for v in right { *v *= 3; } });
});
```

## Key Points

- `JoinHandle::join()` → `Ok(T)` on success, `Err(...)` if the thread panicked.
- `thread::spawn` requires the closure to be `'static + Send`.
- Use `move` closures to transfer ownership into threads.
- Use `thread::scope` when you need to borrow locals — threads are bounded to the scope's lifetime.
- Use `thread::Builder` to set name or stack size.

## Related

- [[Shared State]] — sharing data between threads with `Arc`, `Mutex`, atomics
- [[Channels]] — communicating between threads via MPSC (Multiple Producer Single Consumer) channels
