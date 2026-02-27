---
tags:
  - rust
  - smart-pointers
  - reference-counting
source: smart_pointers/src/rc_pointer.rs
---

# Rc\<T\> & Weak\<T\>

`Rc<T>` (Reference Counting — tracking how many owners a value has) enables **multiple ownership** of a single heap allocation in a **single-threaded** context. The allocation is freed when the strong count drops to zero. For the thread-safe equivalent, see [[Arc]].

## Basic usage

```rust
use std::rc::Rc;

let data: Rc<String> = Rc::new(String::from("shared"));
let ref1 = Rc::clone(&data); // cheap: just increments the counter
let ref2 = Rc::clone(&data);

println!("{}", Rc::strong_count(&data)); // 3
```

`Rc::clone` does **not** deep-copy the data. It copies only the pointer and bumps the count.

## Immutability

`Rc<T>` only hands out shared (`&T`) references. You cannot get `&mut T` through `Rc` when more than one owner exists. For mutation, combine with [[RefCell]]: `Rc<RefCell<T>>`.

## Weak\<T\> — non-owning references

`Weak<T>` holds a reference that does **not** increment the strong count. The allocation is freed when strong count hits 0, regardless of how many weak refs remain. A `Weak` must be upgraded to an `Rc` before use:

```rust
let strong: Rc<i32> = Rc::new(42);
let weak: Weak<i32> = Rc::downgrade(&strong);

match weak.upgrade() {
    Some(rc) => println!("{}", rc),
    None => println!("dropped"),
}

drop(strong);
weak.upgrade(); // None — allocation is gone
```

## Preventing reference cycles

A cycle of `Rc` pointers keeps all nodes alive forever — a memory leak. The pattern is: **children hold `Rc` (strong), parent holds `Weak`**:

```rust
struct TreeNode {
    value: i32,
    parent: Option<Weak<TreeNode>>,   // non-owning
    children: Vec<Rc<TreeNode>>,      // owning
}
```

## try_unwrap — reclaim the value

If exactly one strong reference exists, `try_unwrap` consumes the `Rc` and returns the inner value:

```rust
let single: Rc<String> = Rc::new(String::from("unique"));
match Rc::try_unwrap(single) {
    Ok(value) => println!("{}", value),
    Err(rc)   => println!("{} refs remain", Rc::strong_count(&rc)),
}
```

## get_mut — mutation without RefCell

When `strong_count == 1`, `Rc::get_mut` gives a `&mut T` with no runtime borrow-check overhead:

```rust
let mut solo: Rc<String> = Rc::new(String::from("mutable"));
if let Some(s) = Rc::get_mut(&mut solo) {
    s.push_str(" modified");
}
```

Returns `None` as soon as a second clone exists.

## ptr_eq — identity check

```rust
let rc1 = Rc::new(10);
let rc2 = Rc::clone(&rc1);
let rc3 = Rc::new(10);

Rc::ptr_eq(&rc1, &rc2); // true  — same allocation
Rc::ptr_eq(&rc1, &rc3); // false — different allocations, same value
```

## Performance

| Operation | Cost |
|---|---|
| `Rc::clone` | One integer increment |
| `Drop` | One integer decrement (+ free if 0) |
| Memory per `Rc<T>` | One pointer (8 bytes on 64-bit) |
| Extra heap overhead | Two counters (strong + weak) |

`Rc<i32>` is the same size as `&i32` (one pointer), but the pointed-to allocation also carries the two reference counts.

## Rc is not Send

`Rc` deliberately does not implement `Send` or `Sync`. The compiler will reject any attempt to move an `Rc` into a thread. Use [[Arc]] for cross-thread sharing.

## See also

- [[Arc]] — thread-safe counterpart
- [[RefCell]] — interior mutability to pair with `Rc`
- [[Patterns]] — `Rc<RefCell<T>>` pattern, graph pattern
