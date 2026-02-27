---
tags:
  - rust
  - smart-pointers
  - interior-mutability
source: smart_pointers/src/refcell.rs
---

# RefCell\<T\> & Cell\<T\>

Both types provide **interior mutability**: the ability to mutate data through a shared (`&`) reference. The borrow rules are still enforced — just at runtime instead of compile time. Neither is `Sync`, so neither is safe to share across threads (use [[Mutex & RwLock]] for that).

## RefCell\<T\>

`RefCell<T>` tracks borrows at runtime with a small integer flag embedded in the type. Violating the rules causes a **panic**, not a compile error.

```rust
let data: RefCell<i32> = RefCell::new(5);

// Immutable borrow
let r = data.borrow();       // returns Ref<i32>
println!("{}", r);

// Mutable borrow (panics if any borrow is active)
*data.borrow_mut() += 10;    // returns RefMut<i32>
```

Rules (same as compile-time, enforced at runtime):
- Any number of `borrow()` at once, OR
- Exactly one `borrow_mut()` — no other borrows while it lives

### try_borrow — non-panicking alternative

```rust
match cell.try_borrow() {
    Ok(val)  => println!("{}", val),
    Err(_)   => println!("already mutably borrowed"),
}
```

Prefer `try_borrow` / `try_borrow_mut` in code where a panic would be unacceptable.

### Rc\<RefCell\<T\>\> — shared mutable state (single-threaded)

The workhorse combination for graph-like structures and observers:

```rust
let shared: Rc<RefCell<Vec<i32>>> = Rc::new(RefCell::new(vec![1, 2, 3]));

let a = Rc::clone(&shared);
let b = Rc::clone(&shared);

a.borrow_mut().push(4);
b.borrow_mut().push(5);

println!("{:?}", shared.borrow()); // [1, 2, 3, 4, 5]
```

### Other useful methods

| Method | Effect |
|---|---|
| `into_inner()` | Consumes `RefCell`, returns inner value |
| `replace(new)` | Swaps in a new value, returns old one |
| `swap(&other)` | Swaps values between two `RefCell`s |

### Graph / back-reference example

```rust
struct Node {
    value: i32,
    neighbors: RefCell<Vec<Rc<Node>>>,
}

node1.neighbors.borrow_mut().push(Rc::clone(&node2));
```

`RefCell` lets you add edges after construction even though `Node` is accessed through `Rc` (which only gives `&Node`).

### Performance

`RefCell<i32>` is larger than `i32` by one integer borrow-flag field. Every `borrow()` / `borrow_mut()` call reads and writes that flag. Overhead is minimal for most uses, but compile-time borrowing is always free.

## Cell\<T\>

`Cell<T>` is a lighter alternative for `Copy` types. It never hands out references to the inner value — it copies in and out:

```rust
let c: Cell<i32> = Cell::new(5);
c.set(10);
println!("{}", c.get()); // 10
```

Mutation through a shared reference:
```rust
fn increment(c: &Cell<i32>) {
    c.set(c.get() + 1);
}
```

`Cell` has **zero overhead** over a plain integer — it is the same size and has no borrow flags.

### Cell extras

```rust
counter.update(|x| x + 1);   // in-place update with closure
let val = cell.take();        // moves out, leaves Default value behind
let old = cell.replace(200);  // swap, returns old
```

`take()` requires `T: Default`.

## Cell vs RefCell — quick comparison

| | `Cell<T>` | `RefCell<T>` |
|---|---|---|
| Works with | `Copy` types | Any `T` |
| Access model | `get()` copies, `set()` copies | `borrow()` / `borrow_mut()` |
| Overhead | Zero | Small integer flag |
| Panics possible | No | Yes (on borrow violation) |

## When to use RefCell

- Implementing the observer pattern (list of subscribers behind `Rc`)
- Graph or tree nodes that need back-edges added after construction
- Memoization / lazy cache fields on a struct that is accessed via `&self`
- Breaking a legitimate borrow-checker limitation when you know the usage is correct

Avoid it when normal `&mut` access or `get_mut` (for `Rc`/`Arc`) is sufficient.

## See also

- [[Rc]] — pairs with `RefCell` for `Rc<RefCell<T>>`
- [[Mutex & RwLock]] — thread-safe interior mutability
- [[Patterns]] — `Rc<RefCell<T>>` pattern, memoization pattern
