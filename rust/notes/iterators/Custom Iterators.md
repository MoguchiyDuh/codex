---
tags:
  - rust
  - iterators
source: iterators/src/custom_iterators.rs
---

# Custom Iterators

## Implementing `Iterator`

The minimum requirement is the `Item` associated type and `next()`. Once those are implemented, every method in the `Iterator` trait (map, filter, collect, sum, …) is available for free via default implementations.

```rust
struct Counter {
    current: u32,
    max: u32,
}

impl Counter {
    fn new(max: u32) -> Counter {
        Counter { current: 0, max }
    }
}

impl Iterator for Counter {
    type Item = u32; // associated type — only one impl per struct

    fn next(&mut self) -> Option<Self::Item> {
        if self.current < self.max {
            self.current += 1;
            return Some(self.current);
        }
        return None;
    }
}

let sum: u32 = Counter::new(10).sum(); // 55
```

`type Item` is an associated type rather than a generic parameter so there is exactly one `Item` type per struct — you can't accidentally implement `Iterator<Item = i32>` and `Iterator<Item = u64>` for the same type.

## Infinite Iterators

Return `Some` unconditionally. Always pair with `take()` when consuming:

```rust
struct Fibonacci { a: u64, b: u64 }

impl Iterator for Fibonacci {
    type Item = u64;

    fn next(&mut self) -> Option<Self::Item> {
        let current = self.a;
        self.a = self.b;
        self.b = current + self.b;
        return Some(current); // never None
    }
}

let fib: Vec<u64> = Fibonacci::new().take(10).collect();
```

## Overflow-Safe Termination

Use `checked_mul` (or similar) with `?` to naturally end the iterator on overflow instead of panicking:

```rust
impl Iterator for PowersOfTwo {
    type Item = u64;

    fn next(&mut self) -> Option<Self::Item> {
        let result = self.current;
        self.current = self.current.checked_mul(2)?; // None on overflow → iterator ends
        return Some(result);
    }
}
```

## Iterator Wrappers

A generic struct wrapping another iterator lets you build custom adapters that compose with the rest of the ecosystem:

```rust
struct SkipOdd<I> {
    iter: I,
}

impl<I> Iterator for SkipOdd<I>
where
    I: Iterator<Item = i32>,
{
    type Item = i32;

    fn next(&mut self) -> Option<Self::Item> {
        loop {
            match self.iter.next() {
                Some(n) if n % 2 == 0 => return Some(n),
                Some(_) => continue,
                None => return None,
            }
        }
    }
}
```

## `DoubleEndedIterator`

Allows iteration from both ends simultaneously by implementing `next_back()`. Enables `.rev()` and bidirectional consumption:

```rust
impl DoubleEndedIterator for Range {
    fn next_back(&mut self) -> Option<Self::Item> {
        if self.start < self.end {
            self.end -= 1;
            return Some(self.end);
        }
        return None;
    }
}

let mut r = Range::new(1, 6);
r.next();      // Some(1) — from front
r.next_back(); // Some(5) — from back
r.next();      // Some(2)
r.next_back(); // Some(4)

let rev: Vec<i32> = Range::new(1, 6).rev().collect(); // [5, 4, 3, 2, 1]
```

The front and back cursors must not cross — when `start >= end`, both `next()` and `next_back()` return `None`.

## `ExactSizeIterator`

Signals that the iterator knows its exact remaining length. Requires `size_hint()` to return `(n, Some(n))` — this is checked in debug builds. Implementing `len()` is optional but conventional:

```rust
impl Iterator for ExactCounter {
    fn size_hint(&self) -> (usize, Option<usize>) {
        let remaining = self.max - self.count;
        (remaining, Some(remaining))
    }
    // ...
}

impl ExactSizeIterator for ExactCounter {
    fn len(&self) -> usize {
        self.max - self.count
    }
}

let mut ec = ExactCounter::new(5);
println!("{}", ec.len()); // 5
ec.next();
println!("{}", ec.len()); // 4
```

`collect()` uses `size_hint` to pre-allocate the destination `Vec`, avoiding reallocations.

## `FusedIterator`

A marker trait that promises the iterator will keep returning `None` after the first `None`. Without it, calling `next()` after exhaustion is technically unspecified behavior for custom types. The implementation is empty — it just opts in to the contract:

```rust
impl std::iter::FusedIterator for FusedCounter {}
```

The `done` flag in the struct is a common implementation pattern to make the contract actually hold.

## Returning Iterators from Functions

Use `impl Iterator<Item = T>` to hide the concrete type:

```rust
fn make_counter(max: u32) -> impl Iterator<Item = u32> {
    (1..=max).into_iter()
}
```

This works when there's a single concrete type behind the scenes. If you need to return one of several iterator types, you need `Box<dyn Iterator<Item = T>>`.

## Trait Hierarchy Summary

```
Iterator
└── FusedIterator       (marker: None stays None)
└── ExactSizeIterator   (knows len())
└── DoubleEndedIterator (next_back())
```

Implementing the supertrait does not grant the subtrait — each must be `impl`d explicitly.

## Related Notes

- [[Basics]] — the `Iterator` trait and `next()`
- [[Adapters]] — `fuse`, `rev`, `peekable`
- [[Advanced]] — `std::iter::from_fn` and `successors` as lightweight alternatives to custom structs
