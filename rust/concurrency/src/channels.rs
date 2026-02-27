use shared::{print_h2, print_h3};
use std::sync::mpsc;
use std::thread;
use std::time::Duration;

pub fn run() {
    print_h2!("Channels (mpsc)");
    basic_channel();
    multiple_producers();
    sync_channel();
    channel_dropping();
}

fn basic_channel() {
    print_h3!("Basic Channel (mpsc - Unbounded)");

    let (tx, rx): (mpsc::Sender<i32>, mpsc::Receiver<i32>) = mpsc::channel();

    thread::spawn(move || {
        for i in 1..=5 {
            println!("  Sending: {}", i);
            tx.send(i).unwrap(); // ERROR: send fails if receiver dropped
            thread::sleep(Duration::from_millis(100));
        }
        println!("  Sender done");
    });

    // Iterating rx yields values until all Senders are dropped, then stops (like EOF)
    for received in rx {
        println!("  Received: {}", received);
    }

    println!("  Channel closed (sender dropped)");
}

fn multiple_producers() {
    print_h3!("Multiple Producers, Single Consumer");

    let (tx, rx): (mpsc::Sender<String>, mpsc::Receiver<String>) = mpsc::channel();

    let tx1: mpsc::Sender<String> = tx.clone();
    let tx2: mpsc::Sender<String> = tx.clone();
    let tx3: mpsc::Sender<String> = tx;

    thread::spawn(move || {
        tx1.send("Message from thread 1".to_string()).unwrap();
        thread::sleep(Duration::from_millis(50));
        tx1.send("Another from thread 1".to_string()).unwrap();
    });

    thread::spawn(move || {
        thread::sleep(Duration::from_millis(25));
        tx2.send("Message from thread 2".to_string()).unwrap();
    });

    thread::spawn(move || {
        thread::sleep(Duration::from_millis(75));
        tx3.send("Message from thread 3".to_string()).unwrap();
    });

    for _ in 0..4 {
        let msg: String = rx.recv().unwrap(); // ERROR: recv fails if all senders dropped
        println!("  Received: {}", msg);
    }
}

fn sync_channel() {
    print_h3!("Sync Channel (Bounded Buffer)");

    // sync_channel(N): sender blocks when N items are buffered — useful for backpressure
    let (tx, rx): (mpsc::SyncSender<i32>, mpsc::Receiver<i32>) = mpsc::sync_channel(2);

    let producer: thread::JoinHandle<()> = thread::spawn(move || {
        for i in 1..=5 {
            println!("  Trying to send: {}", i);
            tx.send(i).unwrap(); // BLOCKS if buffer is full
            println!("  Sent: {}", i);
        }
    });

    thread::sleep(Duration::from_millis(200));

    println!("  Consumer starting to receive...");
    for received in rx {
        println!("  Received: {}", received);
        thread::sleep(Duration::from_millis(100));
    }

    producer.join().unwrap();
}

fn channel_dropping() {
    print_h3!("Channel Dropping & Error Handling");

    let (tx, rx): (mpsc::Sender<i32>, mpsc::Receiver<i32>) = mpsc::channel();

    thread::spawn(move || {
        tx.send(42).unwrap();
        // tx dropped here
    });

    thread::sleep(Duration::from_millis(50));

    match rx.recv() {
        Ok(val) => println!("  Received: {}", val),
        Err(_) => println!("  ERROR: Sender disconnected"),
    }

    match rx.recv() {
        Ok(_) => println!("  Received value"),
        Err(_) => println!("  ERROR: Channel closed (expected)"),
    }

    let (tx, rx): (mpsc::Sender<i32>, mpsc::Receiver<i32>) = mpsc::channel();

    tx.send(100).unwrap();

    loop {
        match rx.try_recv() {
            Ok(val) => {
                println!("  try_recv got: {}", val);
                break;
            }
            Err(mpsc::TryRecvError::Empty) => {
                println!("  Channel empty, doing other work...");
                thread::sleep(Duration::from_millis(50));
            }
            Err(mpsc::TryRecvError::Disconnected) => {
                println!("  ERROR: Channel disconnected");
                break;
            }
        }
    }

    let (_tx, rx): (mpsc::Sender<i32>, mpsc::Receiver<i32>) = mpsc::channel();

    match rx.recv_timeout(Duration::from_millis(100)) {
        Ok(val) => println!("  Received: {}", val),
        Err(mpsc::RecvTimeoutError::Timeout) => {
            println!("  Timeout waiting for message (expected)")
        }
        Err(mpsc::RecvTimeoutError::Disconnected) => println!("  ERROR: Disconnected"),
    }
}
