---
tags: [rust, concurrency, patterns, actor, worker-pool, pipeline, rate-limiting]
source: concurrency/src/patterns.rs
---

# Concurrency Patterns

Higher-level patterns built from [[Tokio Channels]], [[Tokio Runtime]] tasks, and `tokio::sync` primitives.

## Actor Pattern

An actor is a task that owns exclusive state and receives commands through a channel. All other tasks interact with it only via messages — no shared `Mutex` needed.

```rust
enum CounterMessage {
    Increment,
    Decrement,
    GetCount(oneshot::Sender<i32>), // reply channel embedded in message
    Stop,
}

struct Counter { count: i32 }

impl Counter {
    async fn run(mut self, mut rx: mpsc::Receiver<CounterMessage>) {
        while let Some(msg) = rx.recv().await {
            match msg {
                CounterMessage::Increment       => self.count += 1,
                CounterMessage::Decrement       => self.count -= 1,
                CounterMessage::GetCount(reply) => { reply.send(self.count).ok(); }
                CounterMessage::Stop            => break,
            }
        }
    }
}
```

Spawning and using the actor:

```rust
let (tx, rx) = mpsc::channel(32);
tokio::spawn(async move { Counter::new().run(rx).await });

tx.send(CounterMessage::Increment).await.unwrap();

let (reply_tx, reply_rx) = oneshot::channel();
tx.send(CounterMessage::GetCount(reply_tx)).await.unwrap();
let count: i32 = reply_rx.await.unwrap();
```

The actor's state is never shared — only accessed inside the task's `run` loop. This trades `Mutex` contention for message serialization.

## Worker Pool Pattern

A fixed number of worker tasks consume jobs from a shared channel. Useful when you want bounded concurrency over a queue of work.

```rust
let (job_tx, job_rx) = mpsc::channel::<i32>(100);
let job_rx = Arc::new(Mutex::new(job_rx)); // shared among workers

for worker_id in 0..4 {
    let rx = Arc::clone(&job_rx);
    tokio::spawn(async move {
        loop {
            let job = {
                let mut guard = rx.lock().await;
                guard.recv().await
            };
            match job {
                Some(id) => {
                    sleep(Duration::from_millis(100)).await; // do work
                    println!("worker {} done job {}", worker_id, id);
                }
                None => break, // channel closed
            }
        }
    });
}

for id in 0..10 { job_tx.send(id).await.unwrap(); }
drop(job_tx); // signals workers to stop
```

The lock scope must end before the `sleep` — hold the `MutexGuard` only long enough to pull one job, then release it so other workers can proceed.

## Pipeline Pattern

Each stage is an independent task. Stages communicate via channels, forming a chain. Backpressure flows naturally — a slow stage blocks the stage upstream from it.

```rust
// Stage 1: source
let (s1_tx, mut s1_rx) = mpsc::channel::<i32>(10);
tokio::spawn(async move {
    for i in 1..=10 { s1_tx.send(i).await.unwrap(); }
});

// Stage 2: transform
let (s2_tx, mut s2_rx) = mpsc::channel::<i32>(10);
tokio::spawn(async move {
    while let Some(n) = s1_rx.recv().await {
        s2_tx.send(n * n).await.unwrap();
    }
});

// Stage 3: sink
let mut total = 0;
while let Some(n) = s2_rx.recv().await {
    total += n;
}
```

Each stage shuts down automatically when its input channel closes (sender dropped), propagating EOF through the pipeline.

## Rate Limiting

### Semaphore

`tokio::sync::Semaphore` bounds the number of concurrently executing tasks. Each task acquires a permit before running and releases it on drop.

```rust
let semaphore = Arc::new(Semaphore::new(3)); // at most 3 concurrent

for i in 0..10 {
    let sem = Arc::clone(&semaphore);
    tokio::spawn(async move {
        let _permit = sem.acquire().await.unwrap(); // blocks until slot available
        println!("task {} running", i);
        sleep(Duration::from_millis(200)).await;
        // permit released here
    });
}
```

The permit is held as long as `_permit` is in scope. Drop it early (or let the scope end) to free the slot.

### Token Bucket (Manual)

For minimum-interval spacing between operations:

```rust
let last_run = Arc::new(Mutex::new(tokio::time::Instant::now() - Duration::from_secs(1)));
let min_interval = Duration::from_millis(100);

let elapsed = last_run.lock().await.elapsed();
if elapsed < min_interval {
    sleep(min_interval - elapsed).await;
}
*last_run.lock().await = tokio::time::Instant::now();
```

For production rate limiting, prefer a crate like `governor`.

## Pattern Summary

| Pattern | State ownership | Communication | Best for |
|---------|----------------|---------------|----------|
| Actor | Exclusive (one task) | Messages + oneshot replies | Stateful objects, avoiding Mutex |
| Worker Pool | Shared via Arc<Mutex<Rx>> | Job queue channel | Bounded concurrency over a queue |
| Pipeline | Per-stage (none shared) | Chained channels | Stream processing, ETL |
| Semaphore | N/A | Permit acquire/release | Limiting concurrent access to a resource |

## Related

- [[Tokio Channels]] — oneshot, mpsc, broadcast, watch
- [[Tokio Runtime]] — `tokio::spawn`, task lifecycle
- [[Shared State]] — when shared mutable state is unavoidable
