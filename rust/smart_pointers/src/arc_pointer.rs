use shared::{print_h2, print_h3};
use std::sync::{Arc, Weak};
use std::thread;

pub fn run() {
    print_h2!("Arc<T> & Weak<T>");

    print_h3!("Basic Arc usage");
    // Arc is thread-safe version of Rc (atomic operations)
    let data: Arc<String> = Arc::new(String::from("shared across threads"));
    println!("Created Arc, strong count: {}", Arc::strong_count(&data));

    print_h3!("Sharing across threads");
    let data2: Arc<Vec<i32>> = Arc::new(vec![1, 2, 3, 4, 5]);
    let mut handles: Vec<std::thread::JoinHandle<()>> = vec![];

    for i in 0..3 {
        let data_clone: Arc<Vec<i32>> = Arc::clone(&data2);
        let handle: std::thread::JoinHandle<()> = thread::spawn(move || {
            println!("  Thread {}: sum = {}", i, data_clone.iter().sum::<i32>());
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Main thread still has data: {:?}", data2);

    print_h3!("Arc with Weak");
    let strong: Arc<i32> = Arc::new(42);
    let weak: Weak<i32> = Arc::downgrade(&strong);

    println!(
        "\nStrong count: {}, Weak count: {}",
        Arc::strong_count(&strong),
        Arc::weak_count(&strong)
    );

    let _weak_clone: Weak<i32> = weak.clone();
    println!("After weak clone, weak count: {}", Arc::weak_count(&strong));

    print_h3!("Upgrade in thread");
    let strong2: Arc<String> = Arc::new(String::from("data"));
    let weak2: Weak<String> = Arc::downgrade(&strong2);

    let handle: std::thread::JoinHandle<()> = thread::spawn(move || match weak2.upgrade() {
        Some(arc) => println!("  Thread upgraded: {}", arc),
        None => println!("  Thread: data was dropped"),
    });

    handle.join().unwrap();
    println!("Main still has: {}", strong2);

    print_h3!("Arc immutability");
    let numbers: Arc<Vec<i32>> = Arc::new(vec![1, 2, 3]);
    // ERROR: Can't mutate through Arc
    // numbers.push(4); // Would fail

    // Multiple threads can read
    let mut handles2: Vec<std::thread::JoinHandle<()>> = vec![];
    for i in 0..3 {
        let nums: Arc<Vec<i32>> = Arc::clone(&numbers);
        let handle: std::thread::JoinHandle<()> = thread::spawn(move || {
            println!("  Thread {}: {:?}", i, nums);
        });
        handles2.push(handle);
    }

    for handle in handles2 {
        handle.join().unwrap();
    }

    print_h3!("try_unwrap");
    // try_unwrap succeeds only when strong_count == 1 (sole owner), returning the inner T
    let unique: Arc<i32> = Arc::new(100);
    match Arc::try_unwrap(unique) {
        Ok(value) => println!("\nUnwrapped: {}", value),
        Err(arc) => println!("Still has {} refs", Arc::strong_count(&arc)),
    }

    print_h3!("get_mut");
    let mut unique2: Arc<String> = Arc::new(String::from("unique"));
    if let Some(value) = Arc::get_mut(&mut unique2) {
        value.push_str(" modified");
        println!("\nModified: {}", value);
    }

    print_h3!("Arc::ptr_eq");
    let arc1: Arc<i32> = Arc::new(10);
    let arc2: Arc<i32> = Arc::clone(&arc1);
    let arc3: Arc<i32> = Arc::new(10);

    println!("\narc1 == arc2 (ptr): {}", Arc::ptr_eq(&arc1, &arc2));
    println!("arc1 == arc3 (ptr): {}", Arc::ptr_eq(&arc1, &arc3));

    // ------------------- Multiple threads modifying counter -------------------
    // Arc alone doesn't allow mutation - need Arc<Mutex<T>>
    // See mutex_rwlock.rs for mutable shared state

    print_h3!("Performance: Arc vs Rc");
    // Arc uses atomic operations (slower but thread-safe)
    // Rc uses normal operations (faster but not thread-safe)
    println!("\nArc size: {} bytes", std::mem::size_of::<Arc<i32>>());
    println!("Rc size: {} bytes", std::mem::size_of::<std::rc::Rc<i32>>());

    print_h3!("Common pattern: Arc<T>");
    #[derive(Debug)]
    struct Config {
        setting1: String,
        setting2: i32,
    }

    let config: Arc<Config> = Arc::new(Config {
        setting1: String::from("value"),
        setting2: 42,
    });

    let mut handles3: Vec<std::thread::JoinHandle<()>> = vec![];
    for i in 0..3 {
        let cfg: Arc<Config> = Arc::clone(&config);
        let handle: std::thread::JoinHandle<()> = thread::spawn(move || {
            println!("  Thread {} config: {:?}", i, cfg);
        });
        handles3.push(handle);
    }

    for handle in handles3 {
        handle.join().unwrap();
    }

    print_h3!("Weak for cache eviction");
    struct Cache {
        _data: Arc<Vec<u8>>,
        _weak_ref: Weak<Vec<u8>>,
    }

    let data: Arc<Vec<u8>> = Arc::new(vec![1, 2, 3]);
    let weak_ref: Weak<Vec<u8>> = Arc::downgrade(&data);

    let _cache: Cache = Cache {
        _data: data,
        _weak_ref: weak_ref,
    };

    println!("\nCache pattern with Weak references");

    print_h3!("Arc with large data");
    let large: Arc<Vec<i32>> = Arc::new((0..1_000_000).collect());
    let clone1: Arc<Vec<i32>> = Arc::clone(&large); // Cheap, just increments counter
    let clone2: Arc<Vec<i32>> = Arc::clone(&large);

    println!(
        "\nSharing 1M elements across {} references",
        Arc::strong_count(&large)
    );

    drop(clone1);
    drop(clone2);
    println!("After drops: {} refs remain", Arc::strong_count(&large));
}
