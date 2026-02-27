---
tags:
  - rust
  - oop_concepts
  - enums
source: oop_concepts/src/enums.rs
---

# Enums

Rust enums are Algebraic Data Types (ADTs) — specifically *sum types*. Each variant is one of a fixed set of possibilities, and variants can carry different data. They are exhaustively matched by the compiler.

## Variants with data

```rust
#[derive(Debug)]
pub enum WebEvent {
    PageLoad,                    // unit variant — no data
    KeyPress(char),              // tuple variant — one unnamed field
    Click { x: i64, y: i64 },   // struct variant — named fields
}
```

Each variant can carry a completely different payload. The enum's size is `max(variant sizes) + discriminant`.

## Methods on enums

`impl` blocks work on enums exactly like on [[Structs]]. `match` is the idiomatic way to branch on variants:

```rust
impl TrafficLight {
    pub fn duration(&self) -> u8 {
        match self {
            TrafficLight::Red    => 30,
            TrafficLight::Yellow => 5,
            TrafficLight::Green  => 25,
        }
    }
}
```

The compiler enforces exhaustiveness — every variant must be handled (or use `_` wildcard).

## Pattern matching

```rust
let event = WebEvent::Click { x: 10, y: 20 };
match event {
    WebEvent::PageLoad           => println!("loaded"),
    WebEvent::KeyPress(c)        => println!("key: {}", c),
    WebEvent::Click { x, y }     => println!("click at ({}, {})", x, y),
}
```

Destructuring works for all variant forms. Named-field variants use `{ field }` syntax.

## Standard library enums

The two most important enums in std:

```rust
enum Option<T> {
    Some(T),
    None,
}

enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

Both are generic. `Option` replaces null. `Result` is the error-handling primitive. Neither requires an import — they're in the prelude.

## Enums vs structs

Use an enum when a value can be one of several distinct shapes. Use a [[Structs|struct]] when a value always has all fields present. The two compose: enum variants can contain structs, structs can contain enums.

## Cross-references

- Generic enums (`enum Tree<T>`): [[Generics]].
- `#[derive(Debug)]` on enums: [[Std Traits]].
- Trait impls on enums work identically to structs: [[Traits]].
