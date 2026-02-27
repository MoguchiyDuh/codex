---
tags: [rust, concurrency, async, tokio, channels]
source: concurrency/src/tokio_channels.rs
---

# Tokio Channels

`tokio::sync` provides async-aware channel types. Unlike `std::sync::mpsc`, sending and receiving are `.await`-able — the task suspends instead of blocking a thread.

## oneshot

A one-shot channel sends exactly one value from one sender to one receiver. The `Sender` is consumed on `send()`.

```rust
let (tx, rx): (oneshot::Sender<i32>, oneshot::Receiver<i32>) = oneshot::channel();

tokio::spawn(async move {
    sleep(Duration::from_millis(100)).await;
    tx.send(42).ok(); // tx consumed here, can't send again
});

match rx.await {
    Ok(value) => println!("{}", value),
    Err(_)    => println!("sender dropped without sending"),
}
```

Common use: request/response — send a `oneshot::Sender` inside a message so the actor can reply (see [[Patterns#Actor Pattern|Actor Pattern]]).

## mpsc (Multiple Producer Single Consumer)

`tokio::sync::mpsc` — Multiple Producer Single Consumer — is the async equivalent of `std::sync::mpsc`. The channel is bounded (capacity set at creation).

```rust
let (tx, mut rx): (mpsc::Sender<i32>, mpsc::Receiver<i32>) = mpsc::channel(5);

for i in 0..3 {
    let tx = tx.clone();
    tokio::spawn(async move {
        tx.send(i * 10).await.unwrap(); // async backpressure if buffer full
    });
}

drop(tx); // drop the original so rx closes when clones are done

while let Some(value) = rx.recv().await {
    println!("{}", value);
}
```

`rx.recv()` returns `None` when all senders are dropped. `tx.send()` is `.await`-able and provides backpressure — it suspends the task (without blocking a thread) until there's buffer space.

For unbounded channels (no backpressure):

```rust
let (tx, mut rx) = mpsc::unbounded_channel::<String>();
tx.send("msg".into()).unwrap(); // never blocks or fails from capacity
```

Prefer bounded channels. Unbounded channels can grow without limit.

## broadcast

`tokio::sync::broadcast` is a Single Producer Multiple Consumer (SPMC) channel where **every active receiver gets every message**. It has a fixed-capacity ring buffer.

```rust
let (tx, _) = broadcast::channel::<String>(16);

let mut rx1 = tx.subscribe();
let mut rx2 = tx.subscribe();

tokio::spawn(async move {
    while let Ok(msg) = rx1.recv().await { println!("rx1: {}", msg); }
});
tokio::spawn(async move {
    while let Ok(msg) = rx2.recv().await { println!("rx2: {}", msg); }
});

tx.send("hello".into()).unwrap(); // both receivers get it
drop(tx); // closes channel
```

If a receiver falls behind and the buffer wraps around, it gets `RecvError::Lagged(n)` — messages were lost. The initial `_rx` returned by `channel()` is typically discarded; new receivers come from `tx.subscribe()`.

## watch

`tokio::sync::watch` holds a **single value**. All receivers always see the latest value — intermediate updates between polls are skipped. No buffer to fill up; the sender never blocks.

```rust
let (tx, rx): (watch::Sender<i32>, watch::Receiver<i32>) = watch::channel(0);

let mut watcher = rx.clone();
tokio::spawn(async move {
    loop {
        if watcher.changed().await.is_err() { break; } // sender dropped
        let val = *watcher.borrow_and_update(); // mark as seen
        println!("changed to: {}", val);
    }
});

tx.send(1).unwrap();
tx.send(2).unwrap(); // watcher may only see 2 if it was slow
```

`borrow_and_update()` marks the current value as seen; `changed()` won't fire again until a new value is sent.

Use `watch` for state broadcasting: config changes, health status, feature flags.

## Channel Comparison

| Channel | Producers | Consumers | Buffering | Use case |
|---------|-----------|-----------|-----------|----------|
| `oneshot` | 1 | 1 | 1 message | Request/response, task result |
| `mpsc` | Many | 1 | N (bounded) or ∞ | Work queues, event streams |
| `broadcast` | 1 | Many | N (ring buffer) | Pub/sub, fan-out |
| `watch` | 1 | Many | Latest value only | State/config broadcast |

## Related

- [[Channels]] — std::sync::mpsc (sync threads)
- [[Tokio Runtime]] — `tokio::spawn`, `join!`, `select!`
- [[Patterns]] — actor, worker pool, pipeline patterns using these channels
