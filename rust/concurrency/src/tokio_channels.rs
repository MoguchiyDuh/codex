use shared::{print_h2, print_h3};
use std::time::Duration;
use tokio::sync::{broadcast, mpsc, oneshot, watch};
use tokio::time::sleep;

pub async fn run() {
    print_h2!("Tokio Channels");
    oneshot_channel().await;
    mpsc_channel().await;
    broadcast_channel().await;
    watch_channel().await;
}

async fn oneshot_channel() {
    print_h3!("Oneshot Channel");
    let (tx, rx): (oneshot::Sender<i32>, oneshot::Receiver<i32>) = oneshot::channel();

    tokio::spawn(async move {
        sleep(Duration::from_millis(100)).await;
        println!("  Sending value...");
        let result: Result<(), i32> = tx.send(42);
        if result.is_err() {
            println!("  ERROR: Receiver dropped"); // ERROR: receiver dropped before send
        }
    });

    match rx.await {
        Ok(value) => println!("  Received: {}", value),
        Err(_) => println!("  ERROR: Sender dropped without sending"), // ERROR: sender dropped
    }

    let (tx, rx): (oneshot::Sender<String>, oneshot::Receiver<String>) = oneshot::channel();

    tokio::spawn(async move {
        sleep(Duration::from_millis(50)).await;
        tx.send("Hello".to_string()).ok();
        // Can't send again - tx is consumed
    });

    let msg: String = rx.await.unwrap();
    println!("  Message: {}", msg);
}

async fn mpsc_channel() {
    print_h3!("MPSC Channel");

    let (tx, mut rx): (mpsc::Sender<i32>, mpsc::Receiver<i32>) = mpsc::channel(5);

    for i in 0..3 {
        let tx_clone: mpsc::Sender<i32> = tx.clone();

        tokio::spawn(async move {
            for j in 0..3 {
                let value: i32 = i * 10 + j;
                println!("  Producer {} sending: {}", i, value);

                let result: Result<(), mpsc::error::SendError<i32>> = tx_clone.send(value).await;
                if result.is_err() {
                    println!("  ERROR: Receiver closed"); // ERROR: receiver dropped
                    return;
                }

                sleep(Duration::from_millis(50)).await;
            }
        });
    }

    drop(tx);

    while let Some(value) = rx.recv().await {
        println!("  Consumer received: {}", value);
    }

    println!("  All producers finished");

    let (tx, mut rx): (
        mpsc::UnboundedSender<String>,
        mpsc::UnboundedReceiver<String>,
    ) = mpsc::unbounded_channel();

    tokio::spawn(async move {
        for i in 0..5 {
            tx.send(format!("Message {}", i)).unwrap();
        }
    });

    while let Some(msg) = rx.recv().await {
        println!("  Unbounded received: {}", msg);
    }
}

async fn broadcast_channel() {
    print_h3!("Broadcast Channel");
    // broadcast::channel(capacity) creates a SPMC channel where every receiver gets every message.
    // The initial receiver (_rx) is discarded — use tx.subscribe() to create new receivers.
    // If a receiver falls behind (lagged), it gets a RecvError::Lagged — messages are dropped.
    let (tx, _rx): (broadcast::Sender<String>, broadcast::Receiver<String>) =
        broadcast::channel(16);

    let mut rx1: broadcast::Receiver<String> = tx.subscribe();
    let mut rx2: broadcast::Receiver<String> = tx.subscribe();
    let mut rx3: broadcast::Receiver<String> = tx.subscribe();

    let handle1 = tokio::spawn(async move {
        while let Ok(msg) = rx1.recv().await {
            println!("  Subscriber 1 received: {}", msg);
        }
    });

    let handle2 = tokio::spawn(async move {
        while let Ok(msg) = rx2.recv().await {
            println!("  Subscriber 2 received: {}", msg);
        }
    });

    let handle3 = tokio::spawn(async move {
        while let Ok(msg) = rx3.recv().await {
            println!("  Subscriber 3 received: {}", msg);
        }
    });

    sleep(Duration::from_millis(50)).await;

    for i in 0..3 {
        let msg: String = format!("Broadcast {}", i);
        println!("  Broadcasting: {}", msg);

        let result: Result<usize, broadcast::error::SendError<String>> = tx.send(msg);
        match result {
            Ok(count) => println!("  Sent to {} receivers", count),
            Err(_) => println!("  ERROR: No active receivers"), // ERROR: all receivers dropped
        }

        sleep(Duration::from_millis(50)).await;
    }

    drop(tx); // Close channel

    handle1.await.unwrap();
    handle2.await.unwrap();
    handle3.await.unwrap();
}

async fn watch_channel() {
    print_h3!("Watch Channel");

    // watch channel holds a single value. Receivers always see the LATEST value — intermediate
    // updates between polls are lost. Useful for state broadcasting (config, health, settings).
    // Unlike broadcast, watch never fills up and never blocks the sender.
    let (tx, rx): (watch::Sender<i32>, watch::Receiver<i32>) = watch::channel(0);

    let mut rx1: watch::Receiver<i32> = rx.clone();
    let mut rx2: watch::Receiver<i32> = rx.clone();

    let handle1 = tokio::spawn(async move {
        loop {
            let result: Result<(), watch::error::RecvError> = rx1.changed().await;
            if result.is_err() {
                println!("  Watcher 1: sender dropped");
                break;
            }

            // borrow_and_update() gets a reference to the current value AND marks it as seen.
        // After this call, changed() won't fire again unless a new value is sent.
        let value: i32 = *rx1.borrow_and_update();
            println!("  Watcher 1 saw change: {}", value);
        }
    });

    let handle2 = tokio::spawn(async move {
        loop {
            let result: Result<(), watch::error::RecvError> = rx2.changed().await;
            if result.is_err() {
                println!("  Watcher 2: sender dropped");
                break;
            }

            let value: i32 = *rx2.borrow_and_update();
            println!("  Watcher 2 saw change: {}", value);
        }
    });

    sleep(Duration::from_millis(50)).await;

    for i in 1..=5 {
        println!("  Updating state to: {}", i);
        tx.send(i).unwrap();
        sleep(Duration::from_millis(100)).await;
    }

    let current: i32 = *rx.borrow();
    println!("  Current value: {}", current);

    drop(tx); // Close channel

    handle1.await.unwrap();
    handle2.await.unwrap();
}
