---
tags: [rust, concurrency, async, futures]
source: concurrency/src/async_basics.rs
---

# Async Basics

Async Rust is cooperative concurrency on a single thread (or small thread pool). Instead of blocking and suspending a whole OS thread, async functions return a `Future` that can be paused at `.await` points and resumed by an executor.

An `async fn` compiles to a state machine implementing `Future`. Calling it does nothing — you must `.await` it (or hand it to an executor via `tokio::spawn`).

## async fn and .await

```rust
async fn fetch_data() -> String {
    tokio::time::sleep(Duration::from_millis(100)).await;
    return "Data fetched".to_string();
}

// Inside another async fn:
let data: String = fetch_data().await;
```

`.await` suspends the current task until the future completes. The executor is free to run other tasks in the meantime — no thread is blocked.

Sequential chaining:

```rust
let data      = fetch_data().await;
let processed = process_data(data).await;
```

This is sequential — `process_data` doesn't start until `fetch_data` finishes. For concurrent execution use `tokio::join!` (see [[Tokio Runtime]]).

## Async Blocks

An `async { ... }` block is an inline future. Use `async move` to capture by value.

```rust
let future = async {
    tokio::time::sleep(Duration::from_millis(50)).await;
    42
};
let result: i32 = future.await;

// move captures ownership
let data = "Hello".to_string();
let future = async move {
    format!("{} world", data) // data moved in
};
```

## The Future Trait

At the bottom of async Rust is the `Future` trait:

```rust
pub trait Future {
    type Output;
    fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output>;
}
```

The executor calls `poll()` repeatedly. The future returns either `Poll::Ready(value)` or `Poll::Pending`. When returning `Pending`, the future **must** arrange for the executor to be notified via `cx.waker().wake()` — otherwise the future will never be polled again.

Example custom future:

```rust
impl Future for TimerFuture {
    type Output = ();

    fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output> {
        if self.start.elapsed() >= self.duration {
            return Poll::Ready(());
        }

        let waker = cx.waker().clone();
        let remaining = self.duration - self.start.elapsed();
        std::thread::spawn(move || {
            std::thread::sleep(remaining);
            waker.wake(); // tell the executor to poll again
        });

        return Poll::Pending;
    }
}
```

In practice you never implement `Future` manually — just write `async fn`.

## Pin

`Pin<&mut Self>` in `poll`'s signature prevents the future from being moved in memory. This matters because async state machines can hold self-referential pointers across `.await` points — moving them would invalidate those pointers.

For most usage you interact with `Pin` in two situations:

```rust
// Heap-allocate and pin — needed for dyn Future trait objects
let future: Pin<Box<dyn Future<Output = i32>>> = Box::pin(some_async_fn());

// Stack-pin with the pin! macro
let future = some_async_fn();
let pinned: Pin<&mut _> = std::pin::pin!(future);
let result = pinned.await;
```

## Key Points

- `async fn` returns a `Future` — calling it is lazy, nothing runs until `.await`.
- `.await` suspends the current task cooperatively, not the thread.
- Sequential `.await` chains run one after the other; use `tokio::join!` for concurrency.
- The `Future` trait's `poll()` is called by the executor; the waker signals when to re-poll.
- `Pin` ensures futures are not moved in memory across suspension points.

## Related

- [[Tokio Runtime]] — the executor: `tokio::spawn`, `join!`, `select!`, timeouts
- [[Tokio Channels]] — async channel primitives
