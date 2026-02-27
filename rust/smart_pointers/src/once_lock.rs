use shared::print_h3;
use std::sync::{LazyLock, Mutex, OnceLock};

// ------------------- OnceLock<T> -------------------
// Thread-safe cell that can be written exactly once.
// Stable since Rust 1.70. Use for: globals initialized at runtime.

static CONFIG_HOST: OnceLock<String> = OnceLock::new();
static PRIMES: OnceLock<Vec<u32>> = OnceLock::new();

fn get_host() -> &'static str {
    return CONFIG_HOST.get_or_init(|| {
        // Expensive initialization runs at most once
        println!("  [OnceLock] initializing CONFIG_HOST");
        return String::from("localhost:8080");
    });
}

fn get_primes() -> &'static Vec<u32> {
    return PRIMES.get_or_init(|| {
        println!("  [OnceLock] computing primes up to 50");
        let mut sieve: Vec<bool> = vec![true; 51];
        sieve[0] = false;
        sieve[1] = false;
        for i in 2..=7usize {
            if sieve[i] {
                let mut j: usize = i * i;
                while j <= 50 {
                    sieve[j] = false;
                    j += i;
                }
            }
        }
        return (2u32..=50).filter(|&n| sieve[n as usize]).collect();
    });
}

// ------------------- LazyLock<T> -------------------
// Like OnceLock but the initializer is embedded in the type itself.
// Stable since Rust 1.80. Cleaner syntax than OnceLock for most globals.

static REGEX_LIKE: LazyLock<String> = LazyLock::new(|| {
    println!("  [LazyLock] initializing REGEX_LIKE");
    return String::from(r"\d{3}-\d{4}"); // would typically be a compiled regex
});

static GLOBAL_COUNTER: LazyLock<Mutex<u64>> = LazyLock::new(|| {
    println!("  [LazyLock] initializing GLOBAL_COUNTER");
    return Mutex::new(0);
});

// ------------------- OnceLock for non-static scopes -------------------
// OnceLock doesn't require 'static - can be used in structs too

struct Cache {
    inner: OnceLock<Vec<String>>,
}

impl Cache {
    fn new() -> Self {
        return Cache {
            inner: OnceLock::new(),
        };
    }

    fn get_or_load(&self) -> &Vec<String> {
        return self.inner.get_or_init(|| {
            println!("  [Cache] loading items (once)");
            return vec![
                String::from("item_a"),
                String::from("item_b"),
                String::from("item_c"),
            ];
        });
    }
}

pub fn run() {
    print_h3!("OnceLock<T> and LazyLock<T>");

    print_h3!("OnceLock");

    // First call initializes
    let host: &str = get_host();
    println!("CONFIG_HOST = {}", host);

    // Subsequent calls return cached value - init closure NOT called again
    let host2: &str = get_host();
    println!("CONFIG_HOST (cached) = {}", host2);

    println!("--- OnceLock<Vec<u32>> ---");
    let primes: &Vec<u32> = get_primes();
    println!("primes = {:?}", primes);
    let primes2: &Vec<u32> = get_primes(); // no recomputation
    println!(
        "primes (cached, same ptr: {}) = {:?}",
        std::ptr::eq(primes, primes2),
        primes2
    );

    // OnceLock::set() - manual initialization (returns Err if already set)
    static MANUAL: OnceLock<i32> = OnceLock::new();
    let first: Result<(), i32> = MANUAL.set(42);
    let second: Result<(), i32> = MANUAL.set(99); // fails - already set
    println!("MANUAL.set(42) = {:?}", first); // Ok(())
    println!("MANUAL.set(99) = {:?}", second); // Err(99) - value returned back
    println!("MANUAL.get()   = {:?}", MANUAL.get()); // Some(42)

    // OnceLock::get() returns None before initialization
    static UNINIT: OnceLock<String> = OnceLock::new();
    println!("UNINIT.get()   = {:?}", UNINIT.get()); // None

    print_h3!("LazyLock");

    // LazyLock initializes on first access
    println!("REGEX_LIKE = {:?}", *REGEX_LIKE);
    println!("REGEX_LIKE (cached) = {:?}", *REGEX_LIKE); // no re-init

    // LazyLock<Mutex<T>> for a mutable global
    println!("\n--- LazyLock<Mutex<u64>> ---");
    {
        let mut counter = GLOBAL_COUNTER.lock().unwrap();
        *counter += 1;
        println!("GLOBAL_COUNTER after +1 = {}", counter);
    }
    {
        let mut counter = GLOBAL_COUNTER.lock().unwrap();
        *counter += 10;
        println!("GLOBAL_COUNTER after +10 = {}", counter);
    }

    print_h3!("OnceLock in struct (lazy field)");

    let cache: Cache = Cache::new();
    let items: &Vec<String> = cache.get_or_load(); // loads on first call
    println!("items = {:?}", items);
    let items2: &Vec<String> = cache.get_or_load(); // no reload
    println!("items (cached) = {:?}", items2);

    print_h3!("Comparison with older approaches");
    println!("lazy_static! crate    - pre-1.70, external dependency, still works");
    println!("once_cell::sync::Lazy - pre-1.80, external dependency, inspired std");
    println!("std::sync::OnceLock   - stable 1.70+, manual initializer, flexible");
    println!("std::sync::LazyLock   - stable 1.80+, embedded closure, cleaner syntax");
    println!("Prefer LazyLock for new code when the init logic is self-contained");
    println!("Use OnceLock when initialization depends on runtime arguments");
}
