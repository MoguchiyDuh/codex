---
tags:
  - rust
  - smart-pointers
  - patterns
source: smart_pointers/src/patterns.rs
---

# Smart Pointer Patterns

Practical combinations and when to reach for each.

## Quick selection guide

| Need | Use |
|---|---|
| Heap allocation, single owner | `Box<T>` |
| Dynamic dispatch | `Box<dyn Trait>` |
| Multiple owners, single thread | `Rc<T>` |
| Multiple owners, multiple threads | `Arc<T>` |
| Shared mutation, single thread | `Rc<RefCell<T>>` |
| Shared mutation, multiple threads | `Arc<Mutex<T>>` |
| Read-heavy shared state, threads | `Arc<RwLock<T>>` |
| Non-owning reference, cycle breaking | `Weak<T>` |

---

## Rc\<RefCell\<T\>\> — shared mutable state (single-threaded)

Combine [[Rc]] (multiple owners) with [[RefCell]] (interior mutability). The canonical single-threaded pattern for objects that need to be mutated from multiple places:

```rust
struct SharedCounter {
    value: Rc<RefCell<i32>>,
}

impl SharedCounter {
    fn new(n: i32) -> Self { Self { value: Rc::new(RefCell::new(n)) } }
    fn increment(&self) { *self.value.borrow_mut() += 1; }
    fn get(&self) -> i32 { *self.value.borrow() }
}

let a = SharedCounter::new(0);
let b = SharedCounter { value: Rc::clone(&a.value) };

a.increment();
b.increment();
println!("{}", a.get()); // 2
```

---

## Arc\<Mutex\<T\>\> — shared mutable state (multi-threaded)

Replace `Rc` with [[Arc]] and `RefCell` with [[Mutex & RwLock|Mutex]] for cross-thread safety:

```rust
let counter: Arc<Mutex<i32>> = Arc::new(Mutex::new(0));

for _ in 0..5 {
    let c = Arc::clone(&counter);
    thread::spawn(move || *c.lock().unwrap() += 1);
}
```

---

## Arc\<RwLock\<T\>\> — read-heavy shared state

When reads vastly outnumber writes:

```rust
// Declared in patterns.rs comparison table — see also mutex_rwlock.rs
Arc<RwLock<T>>  // multiple concurrent readers, exclusive writer
```

---

## Graph — Rc for children, Weak for parent

Children hold `Rc<Node>` (strong, keep nodes alive); the parent field holds `Weak<Node>` (non-owning) to avoid reference cycles that would leak memory:

```rust
struct Node {
    _id: i32,
    _children: RefCell<Vec<Rc<Node>>>,
    _parent: RefCell<Option<Weak<Node>>>, // Weak breaks the cycle
}
```

Without `Weak`, a parent and child pointing to each other would form a cycle: strong count never reaches 0, allocation never freed.

---

## Observer pattern — Rc\<RefCell\<dyn Trait\>\>

A subject holds a list of observers as trait objects. `Rc<RefCell<dyn Observer>>` gives shared ownership and the ability to mutate observer state through `&self` on the subject:

```rust
struct Subject {
    observers: Vec<Rc<RefCell<dyn Observer>>>,
}

impl Subject {
    fn notify(&self, value: i32) {
        for obs in &self.observers {
            obs.borrow_mut().update(value);
        }
    }
}
```

---

## Interior mutability for memoization

`RefCell<Option<T>>` as a cache field lets a method with `&self` compute-and-store on first call:

```rust
struct Expensive {
    cache: RefCell<Option<i32>>,
}

impl Expensive {
    fn compute(&self) -> i32 {
        if let Some(v) = *self.cache.borrow() {
            return v;
        }
        let result = 42; // expensive
        *self.cache.borrow_mut() = Some(result);
        result
    }
}
```

---

## Thread-safe cache — Arc\<Mutex\<HashMap\>\>

```rust
struct Cache {
    store: Arc<Mutex<HashMap<String, i32>>>,
}

impl Cache {
    fn get(&self, key: &str) -> Option<i32> {
        self.store.lock().unwrap().get(key).copied()
    }
    fn set(&self, key: String, value: i32) {
        self.store.lock().unwrap().insert(key, value);
    }
}
```

`Cache` is cheaply cloneable (`Arc::clone`) and sharable across threads.

---

## Read-only config shared across threads

When configuration is immutable after startup, `Arc<T>` alone is sufficient — no lock needed:

```rust
let config: Arc<AppConfig> = Arc::new(AppConfig { port: 5432, .. });

let cfg = Arc::clone(&config);
thread::spawn(move || use_config(&cfg));
```

---

## Lazy initialization — Once (low level)

`std::sync::Once` guarantees a closure runs exactly once across all threads. Prefer [[OnceLock]] / `LazyLock` for new code; `Once` is lower-level and requires `unsafe` when writing to a static:

```rust
static INIT: Once = Once::new();
static mut GLOBAL: i32 = 0;

INIT.call_once(|| unsafe { GLOBAL = 100; });
```

---

## Anti-pattern — Rc cycles

```rust
// DON'T: two nodes pointing to each other with Rc — both leak
node_a.next = Some(Rc::clone(&node_b));
node_b.prev = Some(Rc::clone(&node_a)); // cycle!

// DO: use Weak for the back-reference
node_b.prev = Some(Rc::downgrade(&node_a));
```

---

## Common combinations at a glance

| Combination | Use case |
|---|---|
| `Rc<RefCell<T>>` | Shared mutable, single thread |
| `Arc<Mutex<T>>` | Shared mutable, multi thread |
| `Arc<RwLock<T>>` | Shared, read-heavy, multi thread |
| `Box<dyn Trait>` | Dynamic dispatch, heap |
| `Rc<RefCell<Vec<Rc<Node>>>>` | Graph / tree, single thread |
| `Arc<Mutex<HashMap<K,V>>>` | Thread-safe cache |

## See also

- [[Box]], [[Rc]], [[Arc]], [[RefCell]], [[Mutex & RwLock]], [[OnceLock]], [[Cow]]
