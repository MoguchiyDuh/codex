---
tags: [rust, concurrency, async, tokio]
source: concurrency/src/tokio_runtime.rs
---

# Tokio Runtime

Tokio is the de-facto async executor for Rust. It drives futures to completion, manages a thread pool, and provides async I/O, timers, and synchronization primitives.

## Spawning Tasks

`tokio::spawn` schedules an async block as an independent task on the runtime's thread pool. It returns `JoinHandle<T>`.

```rust
let handle: JoinHandle<i32> = tokio::spawn(async {
    sleep(Duration::from_millis(100)).await;
    return 42;
});

match handle.await {
    Ok(value) => println!("{}", value),
    Err(e)    => println!("task panicked: {}", e),
}
```

Unlike `thread::spawn`, a `JoinHandle<T>` here is itself a future — you `.await` it. If the spawned task panicked, `.await` returns `Err(JoinError)`.

Spawn multiple tasks and collect results:

```rust
let handles: Vec<JoinHandle<i32>> = (0..5)
    .map(|i| tokio::spawn(async move { i * i }))
    .collect();

for (i, handle) in handles.into_iter().enumerate() {
    println!("task {}: {}", i, handle.await.unwrap());
}
```

## spawn_blocking

The async thread pool is for non-blocking work. Never run CPU-heavy loops or blocking syscalls on it — they starve other tasks. Use `spawn_blocking` instead:

```rust
let handle: JoinHandle<u64> = tokio::task::spawn_blocking(|| {
    // runs on a dedicated blocking thread pool, not the async pool
    let mut sum: u64 = 0;
    for i in 0..1_000_000 { sum += i; }
    return sum;
});

// other async work continues here while the blocking task runs
let result: u64 = handle.await.unwrap();
```

`spawn_blocking` dispatches to a separate pool of threads that can safely block. The limit is configured separately from the async worker count.

## join! — Concurrent Execution

`.await`ing futures sequentially means waiting for each before starting the next. `tokio::join!` polls all provided futures concurrently on the **same task** — no new threads or tasks — and returns when all complete.

```rust
let (r1, r2, r3) = tokio::join!(
    async { sleep(Duration::from_millis(100)).await; 1 },
    async { sleep(Duration::from_millis(100)).await; 2 },
    async { sleep(Duration::from_millis(100)).await; 3 },
);
// Total time ≈ 100ms, not 300ms
```

`try_join!` is the fallible version — it cancels all futures and returns the first `Err`:

```rust
let result = tokio::try_join!(may_fail(1), may_fail(2), may_fail(3));
match result {
    Ok((r1, r2, r3)) => { /* all succeeded */ }
    Err(e)           => { /* first failure */ }
}
```

## select! — Racing Futures

`tokio::select!` races multiple futures and takes the first branch whose future completes. The other futures are **dropped** (cancelled) at their next `.await` point.

```rust
tokio::select! {
    result = slow_future() => println!("slow: {}", result),
    result = fast_future() => println!("fast: {}", result), // wins
}
```

Useful for timeouts and interval logic:

```rust
let mut interval = tokio::time::interval(Duration::from_millis(100));

tokio::select! {
    _ = interval.tick()                       => println!("tick"),
    _ = sleep(Duration::from_millis(150))     => println!("sleep won"),
}
```

## Timeouts and Cancellation

`tokio::time::timeout` wraps a future with a deadline:

```rust
match timeout(Duration::from_millis(100), long_operation()).await {
    Ok(result) => println!("{}", result),
    Err(_)     => println!("timed out"),
}
```

Tasks can be cancelled via `JoinHandle::abort()`:

```rust
let handle = tokio::spawn(async {
    sleep(Duration::from_secs(10)).await;
    println!("won't print");
});

sleep(Duration::from_millis(50)).await;
handle.abort();
```

Cancellation is cooperative — the task is dropped at its next `.await` point.

## Error Propagation

`?` works across async function boundaries as normal:

```rust
async fn fetch_data() -> Result<i32, String> {
    sleep(Duration::from_millis(50)).await;
    return Ok(42);
}

async fn process_data() -> Result<String, String> {
    let data = fetch_data().await?; // propagates Err
    return Ok(format!("Processed: {}", data));
}
```

## Key Points

- `tokio::spawn` → new concurrent task, returns `JoinHandle<T>` (a future itself).
- `spawn_blocking` → blocking/CPU work on a separate thread pool.
- `join!` → concurrent execution within one task, waits for all.
- `try_join!` → like `join!` but short-circuits on first error.
- `select!` → race futures, first completion wins, others cancelled.
- `timeout(dur, future)` → wraps any future with a deadline.
- `handle.abort()` → cooperative cancellation at the next `.await`.

## Related

- [[Async Basics]] — how futures and the poll model work
- [[Tokio Channels]] — async channel primitives (mpsc, oneshot, broadcast, watch)
- [[Patterns]] — worker pool and pipeline using tokio tasks
