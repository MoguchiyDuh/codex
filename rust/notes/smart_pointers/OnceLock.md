---
tags:
  - rust
  - smart-pointers
  - lazy-init
  - concurrency
source: smart_pointers/src/once_lock.rs
---

# OnceLock\<T\> & LazyLock\<T\>

Both types live in `std::sync` and solve the same problem: **initializing a value exactly once**, safely, across threads. No external crates required for new code (Rust 1.70+).

## OnceLock\<T\> (stable 1.70)

A thread-safe cell that can be written exactly once. Reading before initialization returns `None`; subsequent writes after the first are rejected.

### Static globals initialized at runtime

```rust
static CONFIG_HOST: OnceLock<String> = OnceLock::new();

fn get_host() -> &'static str {
    CONFIG_HOST.get_or_init(|| {
        println!("initializing once");
        String::from("localhost:8080")
    })
}

let h1 = get_host(); // closure runs
let h2 = get_host(); // closure skipped — cached
```

`get_or_init` is guaranteed to call the closure at most once, even under concurrent access.

### Manual initialization with set()

```rust
static MANUAL: OnceLock<i32> = OnceLock::new();

let _ = MANUAL.set(42);  // Ok(())
let _ = MANUAL.set(99);  // Err(99) — already set, value returned back
println!("{:?}", MANUAL.get()); // Some(42)
```

`get()` returns `None` before any initialization, `Some(&T)` after.

### OnceLock in structs — lazy fields

`OnceLock` does not require `'static`. It can be an ordinary struct field for per-instance lazy initialization:

```rust
struct Cache {
    inner: OnceLock<Vec<String>>,
}

impl Cache {
    fn get_or_load(&self) -> &Vec<String> {
        self.inner.get_or_init(|| {
            println!("loading once");
            vec![String::from("item_a"), String::from("item_b")]
        })
    }
}

let cache = Cache { inner: OnceLock::new() };
cache.get_or_load(); // loads
cache.get_or_load(); // cached, same pointer
```

## LazyLock\<T\> (stable 1.80)

Like `OnceLock`, but the initializer closure is **embedded in the type**. Cleaner syntax for the common case where the init logic is self-contained:

```rust
static REGEX_LIKE: LazyLock<String> = LazyLock::new(|| {
    println!("initializing");
    String::from(r"\d{3}-\d{4}")
});

println!("{}", *REGEX_LIKE); // init runs here, once
println!("{}", *REGEX_LIKE); // cached
```

### LazyLock\<Mutex\<T\>\> — mutable global

```rust
static COUNTER: LazyLock<Mutex<u64>> = LazyLock::new(|| Mutex::new(0));

*COUNTER.lock().unwrap() += 1;
```

## OnceLock vs LazyLock — which to pick

| | `OnceLock<T>` | `LazyLock<T>` |
|---|---|---|
| Stable since | 1.70 | 1.80 |
| Initializer location | Passed to `get_or_init()` at call site | Stored in the type at declaration |
| Init depends on runtime args | Yes — pass different closures | No — closure is fixed |
| Use in structs (non-static) | Yes | No (`'static` only) |
| Syntax for globals | More verbose | Cleaner |

**Rule of thumb**: prefer `LazyLock` for new global constants; use `OnceLock` when initialization depends on runtime data (CLI args, environment variables) or when you need a lazy struct field.

## Historical context

Before 1.70/1.80, the ecosystem used:
- `lazy_static!` macro — external crate, still widely seen in older code
- `once_cell::sync::Lazy` / `once_cell::sync::OnceCell` — external crate that inspired the std types

Prefer the `std` types for new code.

## See also

- [[Mutex & RwLock]] — for `LazyLock<Mutex<T>>` globals
- [[Patterns]] — `Once::call_once` lower-level primitive
