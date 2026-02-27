---
tags:
  - rust
  - oop_concepts
  - traits
source: oop_concepts/src/traits.rs
---

# Traits

Traits define shared behaviour. They are Rust's answer to interfaces/abstract classes — without inheritance.

## Definition and implementation

```rust
trait Greet {
    fn hello(&self) -> String;          // required — must be implemented

    fn goodbye(&self) -> String {       // default — can be overridden
        format!("Goodbye from: {}", self.hello())
    }
}

impl Greet for English {
    fn hello(&self) -> String { String::from("Hello!") }
    // goodbye() uses default
}

impl Greet for Spanish {
    fn hello(&self) -> String { String::from("¡Hola!") }
    fn goodbye(&self) -> String { String::from("¡Adiós!") } // override
}
```

## Static dispatch — `impl Trait`

`impl Trait` in argument position is sugar for a generic bound. The compiler monomorphizes: one copy of the function per concrete type used. Zero runtime overhead.

```rust
fn greet_once(item: &impl Greet) {
    println!("{}", item.hello());
}
// equivalent to:
fn greet_once<T: Greet>(item: &T) { ... }
```

Return-position `impl Trait` (RPIT) hides the concrete type from the caller but commits to one concrete type per call site:

```rust
fn make_greeter() -> impl Greet {
    English  // caller only knows it's a Greet, not English specifically
}
```

## Dynamic dispatch — `dyn Trait`

`&dyn Trait` is a *fat pointer*: two words — a data pointer and a vtable pointer. The vtable holds function pointers to the concrete type's method implementations. Dispatch happens at runtime.

```rust
fn greet_dynamic(item: &dyn Greet) {
    println!("{}", item.hello());
}

fn make_greeter_dynamic(use_english: bool) -> Box<dyn Greet> {
    if use_english { Box::new(English) } else { Box::new(Spanish) }
}
```

Size comparison:
- `&dyn Greet` — 16 bytes (fat pointer, 64-bit)
- `&English` — 8 bytes (thin pointer)

`impl Trait` vs `dyn Trait`:

| | `impl Trait` | `dyn Trait` |
|---|---|---|
| Dispatch | compile-time | runtime (vtable) |
| Cost | zero | vtable indirection |
| Heterogeneous collection | no | yes (`Vec<Box<dyn Trait>>`) |
| Return type hides concrete type | yes (RPIT) | yes |

## Trait objects in heterogeneous collections

```rust
let shapes: Vec<Box<dyn Shape>> = vec![
    Box::new(Circle { radius: 3.0 }),
    Box::new(Rectangle { width: 4.0, height: 5.0 }),
    Box::new(Triangle { a: 3.0, b: 4.0, c: 5.0 }),
];

let total_area: f64 = shapes.iter().map(|s| s.area()).sum();
```

Each element can be a different concrete type — the vtable makes this work.

## Multiple bounds

```rust
fn print_info<T: std::fmt::Display + std::fmt::Debug>(item: T) {
    println!("Display={:<15}  Debug={:?}", format!("{}", item), item);
}
```

`+` combines bounds. Long bounds should use a `where` clause (see [[Generics]]).

## Supertraits

A supertrait constraint means: "to implement `Printable`, you must also implement `Display`."

```rust
trait Printable: std::fmt::Display {
    fn pretty_print(&self) {
        println!("[[ {} ]]", self);  // can call Display methods here
    }
}
```

The compiler enforces the supertrait. Any type implementing `Printable` already has `Display` available.

## Blanket implementations

Implement a trait for all types satisfying some bound:

```rust
impl<T: std::fmt::Display> Printable for T {}
```

Now every type with `Display` gets `Printable` for free. The standard library uses this pattern extensively:
- `impl<T: Iterator> IntoIterator for T`
- `impl<T: Error> From<T> for Box<dyn Error>`

## Associated constants

Traits can define constants that each implementor must provide:

```rust
trait Describable {
    const KIND: &'static str;
    fn describe(&self) -> String;

    // where Self: Sized excludes this method from the vtable
    // — it won't be callable via dyn Describable, but works on concrete types
    fn kind() -> &'static str where Self: Sized {
        Self::KIND
    }
}
```

## Object safety

A trait is *object-safe* if it can be used as `dyn Trait`. Requirements:
- No generic methods.
- No methods that return `Self` (unless guarded with `where Self: Sized`).
- No associated constants (generally).

`Clone` is not object-safe (returns `Self`). `Iterator` is object-safe (`next()` returns `Option<Self::Item>`, not `Self`).

`where Self: Sized` on a method excludes that method from the vtable, which can make an otherwise-unsafe trait object-safe for the remaining methods:

```rust
trait Describable {
    fn kind() -> &'static str where Self: Sized { ... }  // excluded from vtable
    fn describe(&self) -> String;                         // in vtable
}
```

## Cross-references

- [[Generics]] — trait bounds, `where` clauses, associated types.
- [[Std Traits]] — standard traits like `Display`, `Clone`, `From`, `Add`.
- [[Structs]] / [[Enums]] — types that implement traits.
