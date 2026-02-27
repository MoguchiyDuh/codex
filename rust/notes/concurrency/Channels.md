---
tags: [rust, concurrency, channels, mpsc]
source: concurrency/src/channels.rs
---

# Channels

`std::sync::mpsc` — Multiple Producer Single Consumer — provides one-way message passing between threads. A channel has a `Sender<T>` (cloneable) and a single `Receiver<T>`.

## Unbounded Channel

`mpsc::channel()` creates an unbounded channel: senders never block.

```rust
let (tx, rx): (mpsc::Sender<i32>, mpsc::Receiver<i32>) = mpsc::channel();

thread::spawn(move || {
    for i in 1..=5 {
        tx.send(i).unwrap(); // errors if receiver is dropped
    }
});

for value in rx { // iterates until all Senders are dropped
    println!("{}", value);
}
```

Iterating `rx` yields values until every `Sender` clone is dropped — that signals EOF. `recv()` blocks until a message arrives or all senders disconnect.

## Multiple Producers

`Sender<T>` is `Clone`, enabling multiple producers. The receiver side cannot be cloned — there is always exactly one consumer.

```rust
let (tx, rx) = mpsc::channel::<String>();
let tx1 = tx.clone();
let tx2 = tx.clone();
// tx itself is the third producer

thread::spawn(move || tx1.send("from thread 1".into()).unwrap());
thread::spawn(move || tx2.send("from thread 2".into()).unwrap());
thread::spawn(move || tx.send("from thread 3".into()).unwrap());

for _ in 0..3 {
    println!("{}", rx.recv().unwrap());
}
```

Message arrival order across producers is non-deterministic.

## Sync (Bounded) Channel

`mpsc::sync_channel(N)` creates a bounded channel with capacity `N`. The sender blocks when the buffer is full — this provides backpressure.

```rust
let (tx, rx): (mpsc::SyncSender<i32>, mpsc::Receiver<i32>) = mpsc::sync_channel(2);

thread::spawn(move || {
    for i in 1..=5 {
        tx.send(i).unwrap(); // blocks when 2 items are already buffered
    }
});
```

Use bounded channels when you need to slow down producers rather than accumulate unbounded memory.

## Receiving Options

| Method | Behavior |
|--------|----------|
| `rx.recv()` | Blocks until message or all senders dropped |
| `rx.try_recv()` | Non-blocking; returns `TryRecvError::Empty` if no message |
| `rx.recv_timeout(dur)` | Blocks up to `dur`; returns `RecvTimeoutError::Timeout` |

```rust
match rx.try_recv() {
    Ok(val)                          => { /* got value */ }
    Err(mpsc::TryRecvError::Empty)   => { /* no message yet */ }
    Err(mpsc::TryRecvError::Disconnected) => { /* all senders gone */ }
}

match rx.recv_timeout(Duration::from_millis(100)) {
    Ok(val)                                   => { /* got value */ }
    Err(mpsc::RecvTimeoutError::Timeout)      => { /* timed out */ }
    Err(mpsc::RecvTimeoutError::Disconnected) => { /* no senders */ }
}
```

## Channel Lifecycle

- `tx.send()` returns `Err` if the receiver has been dropped.
- `rx.recv()` returns `Err` if all senders have been dropped.
- Drop `tx` (or all clones) to signal the receiver that the stream is finished.

## Key Points

- `mpsc::channel()` — unbounded, sender never blocks.
- `mpsc::sync_channel(N)` — bounded capacity N, sender blocks when full.
- Clone `Sender` for multiple producers; `Receiver` is not `Clone`.
- Iterate `rx` to drain until all senders drop.
- For async channels see [[Tokio Channels]].

## Related

- [[Threads]] — spawning threads that use channels
- [[Tokio Channels]] — async equivalents: oneshot, mpsc, broadcast, watch
- [[Patterns]] — pipeline and worker pool patterns built on channels
