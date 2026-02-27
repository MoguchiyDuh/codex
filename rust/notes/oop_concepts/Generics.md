---
tags:
  - rust
  - oop_concepts
  - generics
source: oop_concepts/src/generics.rs
---

# Generics

Generics let you write code that is parameterized over types. Rust resolves generics at compile time (monomorphization) — no runtime overhead, no boxing, no Garbage Collector (GC) involvement.

## Generic functions

```rust
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut largest = &list[0];
    for item in list.iter() {
        if item > largest { largest = item; }
    }
    largest
}
```

`T: PartialOrd` is a *bound* — the function only works for types that can be compared with `>`. Works for `i32`, `char`, `&str`, or any other `PartialOrd` type without writing separate functions.

## Multiple bounds with `+`

```rust
fn display_and_debug<T: fmt::Display + fmt::Debug + Clone>(val: T) {
    let cloned = val.clone();
    println!("Display={:<15} Debug={:?}", format!("{}", val), cloned);
}
```

Every bound after `+` must hold. The compiler checks this at each call site.

## `where` clauses

When bounds get long or involve associated types, move them to a `where` clause:

```rust
fn complex_bounds<T, U>(t: T, u: U) -> String
where
    T: fmt::Display + Clone,
    U: fmt::Debug + PartialOrd,
{
    format!("t={}, u={:?}", t, u)
}
```

Same semantics as inline bounds, just more readable.

## Generic structs with constrained `impl` blocks

The struct itself is generic over all `T`. Individual `impl` blocks can add constraints — only types satisfying those constraints get those methods:

```rust
#[derive(Debug, Clone)]
struct Pair<T> {
    first: T,
    second: T,
}

// Only Pair<T> where T: Display + PartialOrd gets these methods
impl<T: fmt::Display + PartialOrd> Pair<T> {
    fn new(first: T, second: T) -> Self { Pair { first, second } }

    fn max(&self) -> &T {
        if self.first >= self.second { &self.first } else { &self.second }
    }
}
```

## Multiple type parameters

```rust
#[derive(Debug)]
struct KeyValue<K, V> {
    key: K,
    value: V,
}

impl<K: fmt::Display, V: fmt::Display> KeyValue<K, V> {
    fn show(&self) { println!("{} -> {}", self.key, self.value); }
}
```

Each type parameter is independent. The compiler generates separate monomorphized copies for each `(K, V)` combination used.

## Generic enums

Generic parameters work on [[Enums]] too. The recursive `Tree<T>` requires heap allocation for the recursive variant:

```rust
enum Tree<T> {
    Leaf(T),
    Node(Box<Tree<T>>, Box<Tree<T>>),
}

impl<T: fmt::Display> Tree<T> {
    fn depth(&self) -> usize {
        match self {
            Tree::Leaf(_) => 1,
            Tree::Node(left, right) => 1 + left.depth().max(right.depth()),
        }
    }
}
```

`Box<Tree<T>>` breaks the infinite-size recursion — the size of `Box` is always one pointer width.

## Associated types

Associated types fix the item type per implementation, rather than per call site:

```rust
trait Container {
    type Item;  // implementor decides this, not the caller

    fn get(&self, index: usize) -> Option<&Self::Item>;
    fn len(&self) -> usize;
    fn is_empty(&self) -> bool { self.len() == 0 }
}

impl<T> Container for Stack<T> {
    type Item = T;
    fn get(&self, index: usize) -> Option<&T> { self.items.get(index) }
    fn len(&self) -> usize { self.items.len() }
}
```

Contrast with `trait Container<T>`: that would allow `impl Container<i32>` and `impl Container<String>` on the same struct simultaneously (multiple impls). Associated types allow exactly one impl per struct — the right choice for single-type collections.

Referencing an associated type in a bound:

```rust
fn print_first<C: Container>(c: &C)
where
    C::Item: fmt::Debug,
{
    println!("first = {:?}", c.get(0));
}
```

## Const generics

A compile-time constant can be a type parameter with `const N: usize`:

```rust
struct FixedVec<T, const N: usize> {
    data: [Option<T>; N],
    len: usize,
}

impl<T: Copy + Default + fmt::Debug, const N: usize> FixedVec<T, N> {
    fn capacity() -> usize { N }  // N is known at compile time

    fn push(&mut self, val: T) -> bool {
        if self.len >= N { return false; }
        self.data[self.len] = Some(val);
        self.len += 1;
        true
    }
}

let mut fv: FixedVec<i32, 4> = FixedVec::new();  // capacity baked into the type
```

The standard library uses const generics for `[T; N]`, Single Instruction Multiple Data (SIMD) types, and fixed-size buffers.

## `PhantomData` — zero-cost type markers

`PhantomData<T>` is a zero-size marker that tells the compiler "this struct is logically associated with `T`" without actually storing a `T`. Used to enforce type-level distinctions at compile time:

```rust
use std::marker::PhantomData;

struct Meters;
struct Seconds;

#[derive(Debug, Clone, Copy)]
struct Quantity<T, Unit> {
    value: T,
    _unit: PhantomData<Unit>,  // zero bytes at runtime
}

fn speed(dist: Quantity<f64, Meters>, time: Quantity<f64, Seconds>) -> f64 {
    dist.value / time.value
}

// speed(dist, mass)  // compile error — wrong unit type
```

`size_of::<PhantomData<Meters>>()` is always 0. The type information exists only at compile time.

## Generics combined with lifetimes

Type bounds can include lifetime constraints. `T: 'a` means "T must outlive `'a`" — necessary when storing a reference-to-T behind a reference with lifetime `'a`:

```rust
struct Ref<'a, T: 'a> {
    value: &'a T,
}

impl<'a, T: fmt::Display> Ref<'a, T> {
    fn new(val: &'a T) -> Self { Ref { value: val } }
    fn show(&self) { println!("Ref holds: {}", self.value); }
}
```

Without `T: 'a`, T could contain a reference shorter-lived than `'a`, which would be unsound.

## Cross-references

- [[Traits]] — defining bounds that generics can require.
- [[Std Traits]] — common traits used as bounds (`Clone`, `PartialOrd`, `Display`, `Default`).
- [[Enums]] — generic enums like `Option<T>` and `Result<T, E>`.
