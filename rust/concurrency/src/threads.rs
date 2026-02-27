use shared::{print_h2, print_h3};
use std::thread;
use std::time::Duration;

pub fn run() {
    print_h2!("Threads (std::thread)");
    basic_spawn();
    join_handles();
    thread_builder();
    scoped_threads();
    move_closures();
}

fn basic_spawn() {
    print_h3!("Basic Thread Spawning");
    let handle: thread::JoinHandle<()> = thread::spawn(|| {
        for i in 1..=5 {
            println!("  Spawned thread: {}", i);
            thread::sleep(Duration::from_millis(50));
        }
    });

    for i in 1..=3 {
        println!("  Main thread: {}", i);
        thread::sleep(Duration::from_millis(50));
    }

    handle.join().unwrap();
    println!("  Spawned thread finished");
}

fn join_handles() {
    print_h3!("Join Handles & Return Values");
    let handle: thread::JoinHandle<i32> = thread::spawn(|| {
        println!("  Computing in thread...");
        thread::sleep(Duration::from_millis(100));
        return 42;
    });

    println!("  Waiting for result...");
    let result: Result<i32, Box<dyn std::any::Any + Send>> = handle.join();

    match result {
        Ok(value) => println!("  Thread returned: {}", value),
        Err(_) => println!("  Thread panicked!"), // ERROR: thread panic
    }

    let handles: Vec<thread::JoinHandle<i32>> = (0..5)
        .map(|i| {
            thread::spawn(move || {
                thread::sleep(Duration::from_millis(10));
                return i * i;
            })
        })
        .collect();

    let results: Vec<i32> = handles.into_iter().map(|h| h.join().unwrap()).collect();

    println!("  Results from 5 threads: {:?}", results);
}

fn thread_builder() {
    print_h3!("Thread Builder");

    let handle: thread::JoinHandle<()> = thread::Builder::new()
        .name("worker-1".to_string())
        .spawn(|| {
            let thread_name: String = thread::current().name().unwrap_or("unnamed").to_string();
            println!("  Thread name: {}", thread_name);
        })
        .unwrap(); // ERROR: spawn can fail if OS can't create thread

    handle.join().unwrap();

    let handle: thread::JoinHandle<()> = thread::Builder::new()
        .name("big-stack".to_string())
        .stack_size(4 * 1024 * 1024) // 4 MB stack
        .spawn(|| {
            println!("  Thread with custom stack size");
        })
        .unwrap();

    handle.join().unwrap();
}

fn scoped_threads() {
    print_h3!("Scoped Threads");
    let mut data: Vec<i32> = vec![1, 2, 3, 4, 5];

    // thread::scope guarantees all scoped threads join before the closure returns,
    // so they can safely borrow locals without 'static requirement
    thread::scope(|scope| {
        // Spawn thread that borrows data immutably
        let handle1: thread::ScopedJoinHandle<()> = scope.spawn(|| {
            println!("  Thread 1 reading: {:?}", data);
        });

        // Spawn another thread that borrows data immutably
        let handle2: thread::ScopedJoinHandle<()> = scope.spawn(|| {
            let sum: i32 = data.iter().sum();
            println!("  Thread 2 sum: {}", sum);
        });

        handle1.join().unwrap();
        handle2.join().unwrap();
    }); // All scoped threads are guaranteed to finish here

    data.push(6);
    println!("  After scope, data: {:?}", data);

    thread::scope(|scope| {
        let mid: usize = data.len() / 2;
        let (left, right) = data.split_at_mut(mid);

        scope.spawn(move || {
            for val in left {
                *val *= 2;
            }
        });

        scope.spawn(move || {
            for val in right {
                *val *= 3;
            }
        });
    });

    println!("  After parallel mutation: {:?}", data);
}

fn move_closures() {
    print_h3!("Move Closures");
    let data: Vec<i32> = vec![1, 2, 3, 4, 5];

    // move closures transfer ownership of captured variables into the new thread,
    // satisfying the 'static bound that thread::spawn requires
    let handle: thread::JoinHandle<i32> = thread::spawn(move || {
        let sum: i32 = data.iter().sum();
        return sum;
    });

    // data is no longer accessible here (moved into thread)
    // println!("{:?}", data); // ERROR: value moved

    let result: i32 = handle.join().unwrap();
    println!("  Sum from moved data: {}", result);

    let original: String = "Hello".to_string();

    let handles: Vec<thread::JoinHandle<String>> = (0..3)
        .map(|i| {
            let data: String = original.clone();
            thread::spawn(move || {
                return format!("{} from thread {}", data, i);
            })
        })
        .collect();

    let messages: Vec<String> = handles.into_iter().map(|h| h.join().unwrap()).collect();

    println!("  Messages: {:?}", messages);
}
