use shared::{print_h2, print_h3};
use std::future::Future;
use std::pin::Pin;
use std::task::{Context, Poll};
use std::time::Duration;

pub async fn run() {
    print_h2!("Async Basics");
    basic_async().await;
    async_blocks().await;
    future_trait_demo().await;
}

async fn basic_async() {
    print_h3!("Basic Async/Await");

    async fn fetch_data() -> String {
        tokio::time::sleep(Duration::from_millis(100)).await;
        return "Data fetched".to_string();
    }

    println!("  Calling async function...");
    let result: String = fetch_data().await;
    println!("  Result: {}", result);

    async fn process_data(data: String) -> String {
        tokio::time::sleep(Duration::from_millis(50)).await;
        return format!("Processed: {}", data);
    }

    let data: String = fetch_data().await;
    let processed: String = process_data(data).await;
    println!("  {}", processed);
}

async fn async_blocks() {
    print_h3!("Async Blocks");

    let future = async {
        tokio::time::sleep(Duration::from_millis(50)).await;
        return 42;
    };

    let result: i32 = future.await;
    println!("  Async block result: {}", result);

    let data: String = "Hello".to_string();

    let future = async move {
        tokio::time::sleep(Duration::from_millis(50)).await;
        return format!("{} from async block", data);
    };

    let message: String = future.await;
    println!("  {}", message);

    let future1 = async {
        tokio::time::sleep(Duration::from_millis(100)).await;
        return 1;
    };

    let future2 = async {
        tokio::time::sleep(Duration::from_millis(100)).await;
        return 2;
    };

    let r1: i32 = future1.await;
    let r2: i32 = future2.await;
    println!("  Sequential: {} + {} = {}", r1, r2, r1 + r2);

    // For concurrent execution, use tokio::join! (see tokio_runtime.rs)
}

struct TimerFuture {
    start: std::time::Instant,
    duration: Duration,
}

impl TimerFuture {
    fn new(duration: Duration) -> Self {
        return Self {
            start: std::time::Instant::now(),
            duration,
        };
    }
}

impl Future for TimerFuture {
    type Output = ();

    // poll() is called by the executor. Pin<&mut Self> prevents the future from being
    // moved in memory (important when the future contains self-referential data across awaits).
    // Context holds a Waker — call waker.wake() to tell the executor to poll again.
    fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output> {
        let elapsed: Duration = self.start.elapsed();

        if elapsed >= self.duration {
            println!("  TimerFuture completed!");
            return Poll::Ready(());
        } else {
            // Clone the Waker before the thread spawn — Waker is cheaply cloneable.
            // The spawned thread will call wake() once the timer expires, causing the
            // executor to re-poll this future.
            let waker = cx.waker().clone();
            let remaining: Duration = self.duration - elapsed;

            std::thread::spawn(move || {
                std::thread::sleep(remaining);
                waker.wake();
            });

            return Poll::Pending;
        }
    }
}

async fn future_trait_demo() {
    print_h3!("Future Trait Implementation");

    println!("  Starting custom timer (200ms)...");
    let timer: TimerFuture = TimerFuture::new(Duration::from_millis(200));
    timer.await;
    println!("  Timer finished!");

    async fn example_pinned() -> i32 {
        tokio::time::sleep(Duration::from_millis(50)).await;
        return 42;
    }

    // Box::pin heap-allocates the future and pins it — required when you need
    // a dyn Future (trait object) or when passing futures across await points.
    let future: Pin<Box<dyn Future<Output = i32>>> = Box::pin(example_pinned());
    let result: i32 = future.await;
    println!("  Box::pin future result: {}", result);

    let future = example_pinned();
    let pinned: Pin<&mut _> = std::pin::pin!(future);
    let result: i32 = pinned.await;
    println!("  pin! macro result: {}", result);
}
