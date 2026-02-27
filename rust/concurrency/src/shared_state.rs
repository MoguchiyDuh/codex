use shared::{print_h2, print_h3};
use std::sync::atomic::{AtomicBool, AtomicI32, AtomicUsize, Ordering};
use std::sync::{Arc, Mutex, RwLock};
use std::thread;
use std::time::Duration;

pub fn run() {
    print_h2!("Shared State");
    arc_basics();
    arc_mutex();
    arc_rwlock();
    atomics();
    deadlock_example();
}

fn arc_basics() {
    print_h3!("Arc Basics");
    let data: Arc<Vec<i32>> = Arc::new(vec![1, 2, 3, 4, 5]);

    let mut handles: Vec<thread::JoinHandle<()>> = vec![];

    for i in 0..3 {
        let data_clone: Arc<Vec<i32>> = Arc::clone(&data);

        let handle: thread::JoinHandle<()> = thread::spawn(move || {
            let sum: i32 = data_clone.iter().sum();
            println!("  Thread {} sum: {}", i, sum);
        });

        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("  Strong count after threads: {}", Arc::strong_count(&data));
    println!("  Original data still accessible: {:?}", data);
}

fn arc_mutex() {
    print_h3!("Arc<Mutex<T>>");
    let counter: Arc<Mutex<i32>> = Arc::new(Mutex::new(0));
    let mut handles: Vec<thread::JoinHandle<()>> = vec![];

    for i in 0..10 {
        let counter_clone: Arc<Mutex<i32>> = Arc::clone(&counter);

        let handle: thread::JoinHandle<()> = thread::spawn(move || {
            let mut num: std::sync::MutexGuard<i32> = counter_clone.lock().unwrap(); // ERROR: lock can be poisoned if thread panicked
            *num += 1;
            println!("  Thread {} incremented to: {}", i, *num);
            // Lock automatically released when MutexGuard drops
        });

        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    let final_count: i32 = *counter.lock().unwrap();
    println!("  Final count: {}", final_count);

    let data: Arc<Mutex<Vec<i32>>> = Arc::new(Mutex::new(vec![]));
    let mut handles: Vec<thread::JoinHandle<()>> = vec![];

    for i in 0..5 {
        let data_clone: Arc<Mutex<Vec<i32>>> = Arc::clone(&data);

        let handle: thread::JoinHandle<()> = thread::spawn(move || {
            thread::sleep(Duration::from_millis(10));
            let mut vec: std::sync::MutexGuard<Vec<i32>> = data_clone.lock().unwrap();
            vec.push(i);
        });

        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    let final_data: Vec<i32> = data.lock().unwrap().clone();
    println!("  Shared vec: {:?}", final_data);
}

fn arc_rwlock() {
    print_h3!("Arc<RwLock<T>>");
    let data: Arc<RwLock<i32>> = Arc::new(RwLock::new(0));
    let mut handles: Vec<thread::JoinHandle<()>> = vec![];

    for i in 0..5 {
        let data_clone: Arc<RwLock<i32>> = Arc::clone(&data);

        let handle: thread::JoinHandle<()> = thread::spawn(move || {
            thread::sleep(Duration::from_millis(10));
            let mut write_guard: std::sync::RwLockWriteGuard<i32> = data_clone.write().unwrap(); // ERROR: lock can be poisoned
            *write_guard += 1;
            println!("  Writer {} incremented to: {}", i, *write_guard);
            // Write lock released
        });

        handles.push(handle);
    }

    for i in 0..10 {
        let data_clone: Arc<RwLock<i32>> = Arc::clone(&data);

        let handle: thread::JoinHandle<()> = thread::spawn(move || {
            let read_guard: std::sync::RwLockReadGuard<i32> = data_clone.read().unwrap();
            println!("  Reader {} saw: {}", i, *read_guard);
            // Read lock released (multiple readers can hold lock simultaneously)
        });

        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    let final_value: i32 = *data.read().unwrap();
    println!("  Final value: {}", final_value);
}

fn atomics() {
    print_h3!("Atomic Types");

    // Atomics are lock-free shared state; Ordering::SeqCst is the strongest (total order) and
    // safest default — use Relaxed/Acquire/Release only when you understand the memory model
    let counter: Arc<AtomicI32> = Arc::new(AtomicI32::new(0));
    let mut handles: Vec<thread::JoinHandle<()>> = vec![];

    for _ in 0..10 {
        let counter_clone: Arc<AtomicI32> = Arc::clone(&counter);

        let handle: thread::JoinHandle<()> = thread::spawn(move || {
            for _ in 0..100 {
                counter_clone.fetch_add(1, Ordering::SeqCst);
            }
        });

        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    let final_count: i32 = counter.load(Ordering::SeqCst);
    println!("  AtomicI32 final count: {}", final_count);

    let flag: Arc<AtomicBool> = Arc::new(AtomicBool::new(false));
    let flag_clone: Arc<AtomicBool> = Arc::clone(&flag);

    let handle: thread::JoinHandle<()> = thread::spawn(move || {
        thread::sleep(Duration::from_millis(100));
        println!("  Setting flag to true");
        flag_clone.store(true, Ordering::SeqCst);
    });

    while !flag.load(Ordering::SeqCst) {
        println!("  Waiting for flag...");
        thread::sleep(Duration::from_millis(50));
    }

    println!("  Flag is now true!");
    handle.join().unwrap();

    let index: Arc<AtomicUsize> = Arc::new(AtomicUsize::new(0));
    let mut handles: Vec<thread::JoinHandle<usize>> = vec![];

    for _ in 0..5 {
        let index_clone: Arc<AtomicUsize> = Arc::clone(&index);

        let handle: thread::JoinHandle<usize> = thread::spawn(move || {
            // Get unique index for this thread
            let my_index: usize = index_clone.fetch_add(1, Ordering::SeqCst);
            return my_index;
        });

        handles.push(handle);
    }

    let indices: Vec<usize> = handles.into_iter().map(|h| h.join().unwrap()).collect();
    println!("  Thread indices: {:?}", indices);

    let value: AtomicI32 = AtomicI32::new(42);
    // compare_exchange is an atomic CAS (compare-and-swap): sets new only if current == expected
    let result: Result<i32, i32> = value.compare_exchange(
        42,  // expected
        100, // new value
        Ordering::SeqCst, // success ordering
        Ordering::SeqCst, // failure ordering
    );

    match result {
        Ok(prev) => println!(
            "  CAS succeeded, previous: {}, new: {}",
            prev,
            value.load(Ordering::SeqCst)
        ),
        Err(actual) => println!("  CAS failed, actual: {}", actual),
    }
}

fn deadlock_example() {
    print_h3!("Deadlock");
    let resource1: Arc<Mutex<i32>> = Arc::new(Mutex::new(1));
    let resource2: Arc<Mutex<i32>> = Arc::new(Mutex::new(2));

    // BAD: This can deadlock (commented out)
    // Thread 1: lock resource1 -> lock resource2
    // Thread 2: lock resource2 -> lock resource1
    // Both threads waiting for each other = DEADLOCK

    let r1_clone: Arc<Mutex<i32>> = Arc::clone(&resource1);
    let r2_clone: Arc<Mutex<i32>> = Arc::clone(&resource2);

    let handle1: thread::JoinHandle<()> = thread::spawn(move || {
        let lock1: std::sync::MutexGuard<i32> = r1_clone.lock().unwrap();
        thread::sleep(Duration::from_millis(10));
        let lock2: std::sync::MutexGuard<i32> = r2_clone.lock().unwrap();
        println!("  Thread 1: {} + {} = {}", *lock1, *lock2, *lock1 + *lock2);
    });

    let r1_clone: Arc<Mutex<i32>> = Arc::clone(&resource1);
    let r2_clone: Arc<Mutex<i32>> = Arc::clone(&resource2);

    let handle2: thread::JoinHandle<()> = thread::spawn(move || {
        // Same order as thread 1: resource1 first, then resource2
        let lock1: std::sync::MutexGuard<i32> = r1_clone.lock().unwrap();
        thread::sleep(Duration::from_millis(10));
        let lock2: std::sync::MutexGuard<i32> = r2_clone.lock().unwrap();
        println!("  Thread 2: {} * {} = {}", *lock1, *lock2, *lock1 * *lock2);
    });

    handle1.join().unwrap();
    handle2.join().unwrap();

    println!("  No deadlock! Both threads completed");
}
