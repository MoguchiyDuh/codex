use shared::{print_h2, print_h3};
use std::sync::{Arc, Mutex, RwLock};
use std::thread;

pub fn run() {
    print_h2!("Mutex<T> & RwLock<T>");

    print_h3!("Mutex<T> basic usage");
    // Mutex provides mutual exclusion (thread-safe interior mutability)
    let m: Mutex<i32> = Mutex::new(5);

    {
        let mut num = m.lock().unwrap();
        *num = 10;
    } // Lock automatically released when guard dropped

    println!("Mutex value: {:?}", m.lock().unwrap());

    print_h3!("Arc<Mutex<T>> pattern");
    // Shared mutable state across threads
    let counter: Arc<Mutex<i32>> = Arc::new(Mutex::new(0));
    let mut handles: Vec<std::thread::JoinHandle<()>> = vec![];

    for i in 0..10 {
        let counter_clone: Arc<Mutex<i32>> = Arc::clone(&counter);
        let handle: std::thread::JoinHandle<()> = thread::spawn(move || {
            let mut num = counter_clone.lock().unwrap();
            *num += 1;
            println!("  Thread {} incremented", i);
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("\nFinal counter: {}", *counter.lock().unwrap());

    print_h3!("try_lock");
    // Non-blocking lock attempt
    let mutex: Mutex<i32> = Mutex::new(42);

    match mutex.try_lock() {
        Ok(guard) => println!("\ntry_lock succeeded: {}", guard),
        Err(_) => println!("try_lock failed (already locked)"),
    }

    let _lock = mutex.lock().unwrap();
    match mutex.try_lock() {
        Ok(guard) => println!("try_lock succeeded: {}", guard),
        Err(_) => println!("try_lock failed (already locked)"),
    }

    print_h3!("into_inner");
    // Extract value (consumes Mutex)
    let mutex2: Mutex<String> = Mutex::new(String::from("data"));
    let value: String = mutex2.into_inner().unwrap();
    println!("\nExtracted: {}", value);

    print_h3!("get_mut");
    // Get mutable reference without locking (single-threaded)
    let mut mutex3: Mutex<i32> = Mutex::new(10);
    let value_mut: &mut i32 = mutex3.get_mut().unwrap();
    *value_mut += 5;
    println!("Modified via get_mut: {}", *mutex3.lock().unwrap());

    print_h3!("RwLock<T> basic usage");
    // Multiple readers OR single writer
    let lock: RwLock<i32> = RwLock::new(5);

    // Multiple readers
    {
        let r1 = lock.read().unwrap();
        let r2 = lock.read().unwrap();
        println!("\nTwo readers: {} {}", r1, r2);
    }

    // Single writer
    {
        let mut w = lock.write().unwrap();
        *w += 1;
    }

    println!("After write: {}", *lock.read().unwrap());

    print_h3!("Arc<RwLock<T>> pattern");
    let data: Arc<RwLock<Vec<i32>>> = Arc::new(RwLock::new(vec![1, 2, 3]));
    let mut handles2: Vec<std::thread::JoinHandle<()>> = vec![];

    // Multiple reader threads
    for i in 0..3 {
        let data_clone: Arc<RwLock<Vec<i32>>> = Arc::clone(&data);
        let handle: std::thread::JoinHandle<()> = thread::spawn(move || {
            let vec = data_clone.read().unwrap();
            println!("  Reader {}: sum = {}", i, vec.iter().sum::<i32>());
        });
        handles2.push(handle);
    }

    // One writer thread
    let data_clone: Arc<RwLock<Vec<i32>>> = Arc::clone(&data);
    let writer: std::thread::JoinHandle<()> = thread::spawn(move || {
        let mut vec = data_clone.write().unwrap();
        vec.push(4);
        println!("  Writer: pushed 4");
    });
    handles2.push(writer);

    for handle in handles2 {
        handle.join().unwrap();
    }

    println!("\nFinal data: {:?}", data.read().unwrap());

    print_h3!("try_read / try_write");
    let rwlock: RwLock<i32> = RwLock::new(10);

    match rwlock.try_read() {
        Ok(guard) => println!("\ntry_read succeeded: {}", guard),
        Err(_) => println!("try_read failed"),
    }

    let _write_guard = rwlock.write().unwrap();
    match rwlock.try_read() {
        Ok(guard) => println!("try_read succeeded: {}", guard),
        Err(_) => println!("try_read failed (write lock held)"),
    }

    print_h3!("Deadlock example (avoided)");
    let mutex_a: Arc<Mutex<i32>> = Arc::new(Mutex::new(1));
    let mutex_b: Arc<Mutex<i32>> = Arc::new(Mutex::new(2));

    // Always acquire locks in same order to avoid deadlock
    let a1: Arc<Mutex<i32>> = Arc::clone(&mutex_a);
    let b1: Arc<Mutex<i32>> = Arc::clone(&mutex_b);
    let t1: std::thread::JoinHandle<()> = thread::spawn(move || {
        let _lock_a = a1.lock().unwrap();
        let _lock_b = b1.lock().unwrap();
        println!("  Thread 1 acquired both locks");
    });

    let a2: Arc<Mutex<i32>> = Arc::clone(&mutex_a);
    let b2: Arc<Mutex<i32>> = Arc::clone(&mutex_b);
    let t2: std::thread::JoinHandle<()> = thread::spawn(move || {
        let _lock_a = a2.lock().unwrap(); // Same order
        let _lock_b = b2.lock().unwrap();
        println!("  Thread 2 acquired both locks");
    });

    t1.join().unwrap();
    t2.join().unwrap();

    print_h3!("Mutex vs RwLock when to use");
    // Mutex: Simple, always safe, use when reads/writes balanced
    // RwLock: Better for read-heavy workloads (more overhead)

    println!("\nMutex size: {} bytes", std::mem::size_of::<Mutex<i32>>());
    println!("RwLock size: {} bytes", std::mem::size_of::<RwLock<i32>>());

    print_h3!("Poison on panic");
    // If a thread panics while holding a Mutex, it's "poisoned" — subsequent lock() returns Err.
    // This prevents other threads from seeing potentially inconsistent state.
    // Recover with .into_inner() on the PoisonError to access the data anyway.
    let mutex_poison: Arc<Mutex<i32>> = Arc::new(Mutex::new(0));
    let mutex_clone: Arc<Mutex<i32>> = Arc::clone(&mutex_poison);

    let handle: std::thread::JoinHandle<()> = thread::spawn(move || {
        let mut _guard = mutex_clone.lock().unwrap();
        panic!("Thread panicked!");
    });

    let _ = handle.join(); // Thread panicked

    match mutex_poison.lock() {
        Ok(_) => println!("\nLock acquired"),
        Err(e) => {
            println!("Mutex poisoned, recovering: {}", *e.into_inner());
        }
    }

    print_h3!("Scoped locking patterns");
    let shared: Arc<Mutex<Vec<i32>>> = Arc::new(Mutex::new(vec![]));

    // Pattern: minimize lock duration
    let shared_clone: Arc<Mutex<Vec<i32>>> = Arc::clone(&shared);
    thread::spawn(move || {
        // Do work without lock
        let new_value: i32 = 42;

        // Acquire lock only when needed
        {
            let mut vec = shared_clone.lock().unwrap();
            vec.push(new_value);
        } // Lock released immediately

        // Continue work without lock
    })
    .join()
    .unwrap();

    println!("\nScoped lock result: {:?}", shared.lock().unwrap());

    print_h3!("Concurrent counter");
    let counter2: Arc<Mutex<u64>> = Arc::new(Mutex::new(0));
    let mut handles3: Vec<std::thread::JoinHandle<()>> = vec![];

    for _ in 0..100 {
        let counter_clone: Arc<Mutex<u64>> = Arc::clone(&counter2);
        let handle: std::thread::JoinHandle<()> = thread::spawn(move || {
            for _ in 0..1000 {
                let mut num = counter_clone.lock().unwrap();
                *num += 1;
            }
        });
        handles3.push(handle);
    }

    for handle in handles3 {
        handle.join().unwrap();
    }

    println!(
        "\nConcurrent counter (100 threads x 1000): {}",
        *counter2.lock().unwrap()
    );
}
