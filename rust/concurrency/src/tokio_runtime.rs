use shared::{print_h2, print_h3};
use std::time::Duration;
use tokio::task::JoinHandle;
use tokio::time::{sleep, timeout};

pub async fn run() {
    print_h2!("Tokio Runtime");
    spawn_tasks().await;
    spawn_blocking_demo().await;
    join_select_macros().await;
    error_handling().await;
}

async fn spawn_tasks() {
    print_h3!("Spawning Tasks");

    let handle: JoinHandle<i32> = tokio::spawn(async {
        sleep(Duration::from_millis(100)).await;
        return 42;
    });

    let result: Result<i32, tokio::task::JoinError> = handle.await;
    match result {
        Ok(value) => println!("  Task returned: {}", value),
        Err(e) => println!("  ERROR: Task panicked: {}", e), // ERROR: task panic
    }

    let mut handles: Vec<JoinHandle<i32>> = vec![];

    for i in 0..5 {
        let handle: JoinHandle<i32> = tokio::spawn(async move {
            sleep(Duration::from_millis(50)).await;
            return i * i;
        });
        handles.push(handle);
    }

    for (i, handle) in handles.into_iter().enumerate() {
        let result: i32 = handle.await.unwrap();
        println!("  Task {} result: {}", i, result);
    }
}

async fn spawn_blocking_demo() {
    print_h3!("spawn_blocking");

    // spawn_blocking runs a closure on a dedicated blocking thread pool (not the async thread pool).
    // This prevents CPU-bound or blocking syscall work from starving other async tasks.
    // The async runtime's worker threads should never block; use spawn_blocking for that.
    let handle: JoinHandle<u64> = tokio::task::spawn_blocking(|| {
        println!("  Running expensive computation...");
        let mut sum: u64 = 0;
        for i in 0..1_000_000 {
            sum += i;
        }
        return sum;
    });

    sleep(Duration::from_millis(50)).await;
    println!("  Doing async work while blocking task runs...");

    let result: u64 = handle.await.unwrap();
    println!("  Blocking task result: {}", result);

    let async_handle: JoinHandle<String> = tokio::spawn(async {
        sleep(Duration::from_millis(100)).await;
        return "Async task".to_string();
    });

    let blocking_handle: JoinHandle<String> = tokio::task::spawn_blocking(|| {
        std::thread::sleep(Duration::from_millis(100));
        return "Blocking task".to_string();
    });

    let async_result: String = async_handle.await.unwrap();
    let blocking_result: String = blocking_handle.await.unwrap();

    println!("  Results: {} | {}", async_result, blocking_result);
}

async fn join_select_macros() {
    print_h3!("join! and select!");

    println!("  Using join! to run concurrently:");

    let future1 = async {
        sleep(Duration::from_millis(100)).await;
        return 1;
    };

    let future2 = async {
        sleep(Duration::from_millis(100)).await;
        return 2;
    };

    let future3 = async {
        sleep(Duration::from_millis(100)).await;
        return 3;
    };

    // join! polls all futures concurrently on the same task — no new threads or tasks.
    // All three futures progress interleaved; total time ≈ max(individual times), not sum.
    let (r1, r2, r3) = tokio::join!(future1, future2, future3);
    println!("  join! results: {} {} {}", r1, r2, r3);

    async fn may_fail(id: i32) -> Result<i32, String> {
        sleep(Duration::from_millis(50)).await;
        if id == 2 {
            return Err(format!("Task {} failed", id));
        }
        return Ok(id);
    }

    let result = tokio::try_join!(may_fail(1), may_fail(2), may_fail(3));

    match result {
        Ok((r1, r2, r3)) => println!("  try_join! success: {} {} {}", r1, r2, r3),
        Err(e) => println!("  try_join! failed (expected): {}", e),
    }

    println!("  Using select! to race futures:");

    // select! races futures — the first one to complete "wins" and the others are dropped.
    // Dropped futures are cancelled at their next .await point (cooperative cancellation).
    tokio::select! {
        result = async {
            sleep(Duration::from_millis(200)).await;
            "slow"
        } => println!("  select! chose: {}", result),
        result = async {
            sleep(Duration::from_millis(50)).await;
            "fast"
        } => println!("  select! chose: {}", result),
    }

    let mut interval = tokio::time::interval(Duration::from_millis(100));

    for _ in 0..3 {
        tokio::select! {
            _ = interval.tick() => println!("  Interval ticked"),
            _ = sleep(Duration::from_millis(150)) => println!("  Sleep finished first"),
        }
    }
}

async fn error_handling() {
    print_h3!("Error Handling & Timeouts");

    async fn long_operation() -> String {
        sleep(Duration::from_secs(2)).await;
        return "Done".to_string();
    }

    match timeout(Duration::from_millis(100), long_operation()).await {
        Ok(result) => println!("  Operation completed: {}", result),
        Err(_) => println!("  Operation timed out (expected)"),
    }

    let handle: JoinHandle<()> = tokio::spawn(async {
        sleep(Duration::from_secs(10)).await;
        println!("  This won't print - task was cancelled");
    });

    sleep(Duration::from_millis(50)).await;
    handle.abort(); // Cancel the task
    println!("  Task cancelled");

    async fn fetch_data() -> Result<i32, String> {
        sleep(Duration::from_millis(50)).await;
        return Ok(42);
    }

    async fn process_data() -> Result<String, String> {
        let data: i32 = fetch_data().await?;
        sleep(Duration::from_millis(50)).await;
        return Ok(format!("Processed: {}", data));
    }

    match process_data().await {
        Ok(result) => println!("  Result: {}", result),
        Err(e) => println!("  ERROR: {}", e),
    }
}
