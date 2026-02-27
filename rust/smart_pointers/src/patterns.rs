use shared::{print_h2, print_h3};
use std::cell::RefCell;
use std::rc::Rc;
use std::sync::{Arc, Mutex};

pub fn run() {
    print_h2!("Patterns & Comparison");

    print_h3!("When to use which");
    println!("Box<T>: Heap allocation, single ownership");
    println!("Rc<T>: Multiple ownership, single-threaded");
    println!("Arc<T>: Multiple ownership, multi-threaded");
    println!("RefCell<T>: Interior mutability, single-threaded");
    println!("Mutex<T>: Interior mutability, multi-threaded");
    println!("RwLock<T>: Multiple readers OR single writer");

    print_h3!("Pattern: Rc<RefCell<T>>");
    // Shared mutable state (single-threaded)
    #[derive(Debug)]
    struct SharedCounter {
        value: Rc<RefCell<i32>>,
    }

    impl SharedCounter {
        fn new(initial: i32) -> SharedCounter {
            return SharedCounter {
                value: Rc::new(RefCell::new(initial)),
            };
        }

        fn increment(&self) {
            *self.value.borrow_mut() += 1;
        }

        fn get(&self) -> i32 {
            return *self.value.borrow();
        }
    }

    let counter: SharedCounter = SharedCounter::new(0);
    let counter_clone: SharedCounter = SharedCounter {
        value: Rc::clone(&counter.value),
    };

    counter.increment();
    counter_clone.increment();
    println!("\nRc<RefCell> counter: {}", counter.get());

    print_h3!("Pattern: Arc<Mutex<T>>");
    // Shared mutable state (multi-threaded)
    use std::thread;

    let counter2: Arc<Mutex<i32>> = Arc::new(Mutex::new(0));
    let mut handles: Vec<std::thread::JoinHandle<()>> = vec![];

    for _ in 0..5 {
        let counter_clone: Arc<Mutex<i32>> = Arc::clone(&counter2);
        let handle: std::thread::JoinHandle<()> = thread::spawn(move || {
            *counter_clone.lock().unwrap() += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }
    println!("Arc<Mutex> counter: {}", *counter2.lock().unwrap());

    print_h3!("Pattern: Graph with Rc/Weak");
    // Children hold Rc<Node> (strong, keep nodes alive); parent holds Weak<Node>
    // (non-owning, avoids reference cycles that would leak memory)
    #[derive(Debug)]
    struct Node {
        _id: i32,
        _children: RefCell<Vec<Rc<Node>>>,
        _parent: RefCell<Option<std::rc::Weak<Node>>>,
    }

    println!("\nGraph pattern: Rc for children, Weak for parent");

    print_h3!("Pattern: Observer");
    struct Subject {
        observers: Vec<Rc<RefCell<dyn Observer>>>,
    }

    trait Observer {
        fn update(&mut self, value: i32);
    }

    struct ConcreteObserver {
        id: i32,
        value: i32,
    }

    impl Observer for ConcreteObserver {
        fn update(&mut self, value: i32) {
            self.value = value;
            println!("  Observer {} updated to {}", self.id, self.value);
        }
    }

    impl Subject {
        fn new() -> Subject {
            return Subject { observers: vec![] };
        }

        fn attach(&mut self, observer: Rc<RefCell<dyn Observer>>) {
            self.observers.push(observer);
        }

        fn notify(&self, value: i32) {
            for observer in &self.observers {
                observer.borrow_mut().update(value);
            }
        }
    }

    let mut subject: Subject = Subject::new();
    let obs1: Rc<RefCell<dyn Observer>> =
        Rc::new(RefCell::new(ConcreteObserver { id: 1, value: 0 }));
    let obs2: Rc<RefCell<dyn Observer>> =
        Rc::new(RefCell::new(ConcreteObserver { id: 2, value: 0 }));

    subject.attach(obs1);
    subject.attach(obs2);
    println!("\nObserver pattern:");
    subject.notify(42);

    print_h3!("Pattern: Lazy initialization");
    // Once::call_once guarantees the closure runs exactly once across all threads
    // Prefer LazyLock/OnceLock for new code (stable since 1.70/1.80); Once is lower-level
    use std::sync::Once;
    static INIT: Once = Once::new();
    static mut GLOBAL: i32 = 0;

    INIT.call_once(|| {
        unsafe {
            GLOBAL = 100;
        }
        println!("\nLazy init: GLOBAL initialized to 100");
    });

    let global_val: i32 = unsafe { GLOBAL };
    println!("GLOBAL: {}", global_val);

    print_h3!("Pattern: Cache with Mutex");
    use std::collections::HashMap;

    struct Cache {
        store: Arc<Mutex<HashMap<String, i32>>>,
    }

    impl Cache {
        fn new() -> Cache {
            return Cache {
                store: Arc::new(Mutex::new(HashMap::new())),
            };
        }

        fn get(&self, key: &str) -> Option<i32> {
            return self.store.lock().unwrap().get(key).copied();
        }

        fn set(&self, key: String, value: i32) {
            self.store.lock().unwrap().insert(key, value);
        }
    }

    let cache: Cache = Cache::new();
    cache.set(String::from("answer"), 42);
    println!("\nCache get: {:?}", cache.get("answer"));

    print_h3!("Anti-pattern: Rc cycles");
    // DON'T: Create reference cycles without Weak
    println!("\nAnti-pattern: Rc cycles cause memory leaks");
    println!("Solution: Use Weak for back-references");

    print_h3!("Pattern: Builder with Rc");
    #[derive(Clone)]
    struct Config {
        settings: Rc<HashMap<String, String>>,
    }

    impl Config {
        fn new() -> Config {
            return Config {
                settings: Rc::new(HashMap::new()),
            };
        }

        fn with_setting(mut self, key: &str, value: &str) -> Config {
            let mut new_settings: HashMap<String, String> = (*self.settings).clone();
            new_settings.insert(key.to_string(), value.to_string());
            self.settings = Rc::new(new_settings);
            return self;
        }
    }

    let config: Config = Config::new()
        .with_setting("host", "localhost")
        .with_setting("port", "8080");
    println!("\nBuilder with Rc: {} settings", config.settings.len());

    print_h3!("Pattern: Arc for read-only config");
    struct AppConfig {
        _database_url: String,
        _port: u16,
    }

    let app_config: Arc<AppConfig> = Arc::new(AppConfig {
        _database_url: String::from("postgres://localhost"),
        _port: 5432,
    });

    // Share across threads (read-only)
    let config_clone: Arc<AppConfig> = Arc::clone(&app_config);
    let _handle: std::thread::JoinHandle<()> = thread::spawn(move || {
        // Use config_clone
        drop(config_clone);
    });

    println!("\nArc for read-only config across threads");

    print_h3!("Pattern: Interior mutability for caching");
    struct Expensive {
        cache: RefCell<Option<i32>>,
    }

    impl Expensive {
        fn new() -> Expensive {
            return Expensive {
                cache: RefCell::new(None),
            };
        }

        fn compute(&self) -> i32 {
            if let Some(cached) = *self.cache.borrow() {
                println!("  Using cached value");
                return cached;
            }

            println!("  Computing...");
            let result: i32 = 42; // Expensive computation
            *self.cache.borrow_mut() = Some(result);
            return result;
        }
    }

    let exp: Expensive = Expensive::new();
    println!("\nFirst call:");
    exp.compute();
    println!("Second call:");
    exp.compute();

    print_h3!("Comparison table");
    println!("Box:     Single owner, heap, movable");
    println!("Rc:      Multiple owners, single-thread, immutable");
    println!("Arc:     Multiple owners, multi-thread, immutable");
    println!("RefCell: Single owner, runtime borrow check");
    println!("Mutex:   Single owner, thread-safe, blocking");
    println!("RwLock:  Single owner, multiple readers, blocking");

    println!("\n=== Common Combinations ===");
    println!("Rc<RefCell<T>>:    Shared mutable, single-thread");
    println!("Arc<Mutex<T>>:     Shared mutable, multi-thread");
    println!("Arc<RwLock<T>>:    Shared, read-heavy, multi-thread");
    println!("Box<dyn Trait>:    Dynamic dispatch, heap");
}
