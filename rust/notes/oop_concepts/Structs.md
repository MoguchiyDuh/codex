---
tags:
  - rust
  - oop_concepts
  - structs
source: oop_concepts/src/structs.rs
---

# Structs

The primary way to group related data in Rust. No inheritance — composition and [[Traits]] are the extensibility story.

## Named-field structs

```rust
#[derive(Debug)]
pub struct Person {
    pub name: String,
    pub age: u8,
    pub job: String,
}
```

Fields are private by default. Mark them `pub` individually or keep them private and expose them through methods.

## `impl` blocks

Methods go in `impl` blocks, not inline with the struct definition. You can have multiple `impl` blocks for the same type.

```rust
impl Person {
    pub fn new(name: &str, job: &str) -> Self {
        // Self refers to the implementing type, not the literal name.
        // Substructs reusing this constructor don't need to hardcode Person.
        Self {
            name: name.to_string(),
            age: compute_age(),
            job: job.to_string(),
        }
    }

    pub fn introduce(&self) {
        println!("I'm {}, {} years old, working as a {}", self.name, self.age, self.job);
    }
}
```

`Self` vs the type name: `Self` is a type alias for the implementing type inside `impl`. Prefer it — it's more robust when refactoring.

## Receiver types

| Signature | Meaning |
|---|---|
| `fn foo(&self)` | shared borrow — read-only |
| `fn foo(&mut self)` | exclusive borrow — can mutate |
| `fn foo(self)` | takes ownership — consumes the value |
| `fn foo() -> Self` | associated function (no receiver) — like a static method |

```rust
impl Counter {
    pub fn new() -> Self {          // associated function, no receiver
        Self { count: 0 }
    }
    pub fn increment(&mut self) {   // requires mut binding on the caller's side
        self.count += 1;
    }
    pub fn get(&self) -> i32 {
        self.count
    }
}
```

## Visibility and field access

- Struct itself can be `pub`.
- Fields default to private even if the struct is `pub`.
- The pattern `pub struct Foo { field: T }` (private field + public struct) forces callers to use constructors, giving you control over invariants.

## Tuple structs and unit structs

```rust
struct Meters(f64);         // tuple struct — fields accessed by index: self.0
struct Marker;              // unit struct — zero size, useful as type-level markers (see [[Generics]])
```

## Cross-references

- Methods can return `impl Trait` or `dyn Trait` — see [[Traits]].
- Generic structs: `struct Pair<T>` — see [[Generics]].
- Deriving standard behaviour (`Clone`, `Debug`, `PartialEq`): [[Std Traits]].
