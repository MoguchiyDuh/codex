use shared::{print_h2, print_h3};
use std::sync::Arc;
use std::time::Duration;
use tokio::sync::{Mutex, Semaphore, mpsc};
use tokio::time::sleep;

pub async fn run() {
    print_h2!("Concurrency Patterns");
    actor_pattern().await;
    worker_pool_pattern().await;
    pipeline_pattern().await;
    rate_limiting().await;
}

struct Counter {
    count: i32,
}

enum CounterMessage {
    Increment,
    Decrement,
    GetCount(tokio::sync::oneshot::Sender<i32>),
    Stop,
}

impl Counter {
    fn new() -> Self {
        return Self { count: 0 };
    }

    fn handle_message(&mut self, msg: CounterMessage) -> bool {
        match msg {
            CounterMessage::Increment => {
                self.count += 1;
                println!("  Counter incremented to: {}", self.count);
                return true;
            }
            CounterMessage::Decrement => {
                self.count -= 1;
                println!("  Counter decremented to: {}", self.count);
                return true;
            }
            CounterMessage::GetCount(sender) => {
                sender.send(self.count).ok();
                return true;
            }
            CounterMessage::Stop => {
                println!("  Counter actor stopping");
                return false;
            }
        }
    }

    async fn run(mut self, mut rx: mpsc::Receiver<CounterMessage>) {
        while let Some(msg) = rx.recv().await {
            let should_continue: bool = self.handle_message(msg);
            if !should_continue {
                break;
            }
        }
    }
}

async fn actor_pattern() {
    print_h3!("Actor Pattern");

    // Actor pattern: one task owns exclusive state, all others interact via message passing.
    // Eliminates shared mutable state — no Mutex needed since only the actor task touches Counter.
    let (tx, rx): (mpsc::Sender<CounterMessage>, mpsc::Receiver<CounterMessage>) =
        mpsc::channel(32);

    let counter: Counter = Counter::new();

    // Spawn actor
    tokio::spawn(async move {
        counter.run(rx).await;
    });

    // Send messages to actor
    tx.send(CounterMessage::Increment).await.unwrap();
    tx.send(CounterMessage::Increment).await.unwrap();
    tx.send(CounterMessage::Decrement).await.unwrap();

    sleep(Duration::from_millis(50)).await;

    // Query actor state
    let (response_tx, response_rx) = tokio::sync::oneshot::channel();
    tx.send(CounterMessage::GetCount(response_tx))
        .await
        .unwrap();

    let count: i32 = response_rx.await.unwrap();
    println!("  Final count: {}", count);

    tx.send(CounterMessage::Stop).await.unwrap();
}

async fn worker_pool_pattern() {
    print_h3!("Worker Pool Pattern");
    let (job_tx, job_rx): (mpsc::Sender<i32>, mpsc::Receiver<i32>) = mpsc::channel(100);
    let job_rx: Arc<Mutex<mpsc::Receiver<i32>>> = Arc::new(Mutex::new(job_rx));

    let num_workers: usize = 4;
    let mut handles: Vec<tokio::task::JoinHandle<()>> = vec![];

    // Spawn worker pool
    for worker_id in 0..num_workers {
        let job_rx_clone: Arc<Mutex<mpsc::Receiver<i32>>> = Arc::clone(&job_rx);

        let handle = tokio::spawn(async move {
            loop {
                let job: Option<i32> = {
                    let mut rx: tokio::sync::MutexGuard<mpsc::Receiver<i32>> =
                        job_rx_clone.lock().await;
                    rx.recv().await
                };

                match job {
                    Some(job_id) => {
                        println!("  Worker {} processing job {}", worker_id, job_id);
                        sleep(Duration::from_millis(100)).await;
                        println!("  Worker {} finished job {}", worker_id, job_id);
                    }
                    None => {
                        println!("  Worker {} shutting down", worker_id);
                        break;
                    }
                }
            }
        });

        handles.push(handle);
    }

    // Submit jobs
    for job_id in 0..10 {
        job_tx.send(job_id).await.unwrap();
    }

    drop(job_tx); // Signal no more jobs

    // Wait for all workers to finish
    for handle in handles {
        handle.await.unwrap();
    }

    println!("  All workers finished");
}

async fn pipeline_pattern() {
    print_h3!("Pipeline Pattern");
    // Stage 1: Generate numbers
    let (stage1_tx, mut stage1_rx): (mpsc::Sender<i32>, mpsc::Receiver<i32>) = mpsc::channel(10);

    tokio::spawn(async move {
        for i in 1..=10 {
            println!("  Stage 1: Generating {}", i);
            stage1_tx.send(i).await.unwrap();
            sleep(Duration::from_millis(50)).await;
        }
    });

    // Stage 2: Square numbers
    let (stage2_tx, mut stage2_rx): (mpsc::Sender<i32>, mpsc::Receiver<i32>) = mpsc::channel(10);

    tokio::spawn(async move {
        while let Some(num) = stage1_rx.recv().await {
            let squared: i32 = num * num;
            println!("  Stage 2: Squared {} -> {}", num, squared);
            stage2_tx.send(squared).await.unwrap();
        }
    });

    // Stage 3: Sum running total
    let mut total: i32 = 0;

    while let Some(squared) = stage2_rx.recv().await {
        total += squared;
        println!("  Stage 3: Running total = {}", total);
    }

    println!("  Pipeline final total: {}", total);
}

async fn rate_limiting() {
    print_h3!("Rate Limiting");
    // Semaphore: a bounded pool of permits — acquire() blocks until a permit is available,
    // then the permit is returned (dropped) when _guard goes out of scope
    let semaphore: Arc<Semaphore> = Arc::new(Semaphore::new(3)); // Max 3 concurrent
    let mut handles: Vec<tokio::task::JoinHandle<()>> = vec![];

    for i in 0..10 {
        let permit: Arc<Semaphore> = Arc::clone(&semaphore);

        let handle = tokio::spawn(async move {
            let _guard: tokio::sync::SemaphorePermit = permit.acquire().await.unwrap(); // Wait for permit
            println!("  Task {} acquired permit, running...", i);
            sleep(Duration::from_millis(200)).await;
            println!("  Task {} done, releasing permit", i);
            // Permit released when _guard drops
        });

        handles.push(handle);
    }

    for handle in handles {
        handle.await.unwrap();
    }

    println!("  All rate-limited tasks finished");

    // Token bucket style rate limiting
    let rate_limiter: Arc<Mutex<tokio::time::Instant>> = Arc::new(Mutex::new(
        tokio::time::Instant::now() - Duration::from_secs(1),
    ));
    let min_interval: Duration = Duration::from_millis(100);

    println!("  Token bucket rate limiting:");

    for i in 0..5 {
        let rate_limiter_clone: Arc<Mutex<tokio::time::Instant>> = Arc::clone(&rate_limiter);

        let last_run: tokio::time::Instant = *rate_limiter_clone.lock().await;
        let elapsed: Duration = last_run.elapsed();

        if elapsed < min_interval {
            let wait_time: Duration = min_interval - elapsed;
            println!("  Request {} waiting {:?}...", i, wait_time);
            sleep(wait_time).await;
        }

        println!("  Request {} executing", i);
        *rate_limiter_clone.lock().await = tokio::time::Instant::now();

        sleep(Duration::from_millis(50)).await;
    }

    println!("  Rate limiting demo complete");
}
