---
tags:
  - rust
  - macros
  - declarative
source: macros/src/declarative.rs
---

# Declarative Macros

Declarative macros (also called "macros by example") are defined with `macro_rules!`. They match against the structure of input tokens and expand to replacement code at compile time — no runtime cost. They are Rust's primary Domain Specific Language (DSL) tool for code generation without procedural complexity.

## Basic Syntax

```rust
macro_rules! say_hello {
    () => {
        println!("Hello from a macro!");
    };
}
```

Invocation style is flexible — `!()`, `![]`, and `!{}` are all valid:

```rust
say_hello!();
say_hello![];
say_hello! {};
```

## Patterns and Designators

Each arm is `(pattern) => { expansion };`. The pattern uses **designators** to capture parts of the input:

| Designator | Matches |
|---|---|
| `expr` | Any expression |
| `ident` | Identifier (variable or function name) |
| `ty` | Type |
| `stmt` | Statement |
| `pat` | Pattern |
| `path` | Module path (e.g. `std::collections::HashMap`) |
| `block` | A `{ ... }` block |
| `item` | Item: `fn`, `struct`, `enum`, etc. |
| `tt` | Token Tree (TT) — catch-all for any single token or grouped tokens |
| `literal` | A literal value |
| `vis` | Visibility qualifier (`pub`, etc.) |

### Multiple patterns

Arms are tried top to bottom; the first match wins:

```rust
macro_rules! describe {
    () => { println!("No arguments given."); };
    ($val:expr) => { println!("Got: {:?}", $val); };
    ($val:expr, $label:expr) => { println!("{}: {:?}", $label, $val); };
}
```

### Generating code from an ident

```rust
macro_rules! create_fn {
    ($fn_name:ident) => {
        fn $fn_name() {
            println!("Function '{}' was generated.", stringify!($fn_name));
        }
    };
}

create_fn!(generated_function); // defines fn generated_function() { ... }
```

## Repetition

Repetition syntax mirrors regex quantifiers, applied to `$(...)`:

| Syntax | Meaning |
|---|---|
| `$(...)*` | Zero or more |
| `$(...)+` | One or more |
| `$(...)?` | Zero or one |

A separator token placed between `$(...)` and the quantifier is inserted between expansions: `$($x:expr),*` separates by commas.

`$(,)?` at the end allows an optional trailing comma.

The outer `{{ }}` creates a block expression, enabling `let` bindings inside while returning a value as the block's final expression:

```rust
macro_rules! my_vec {
    ($($elem:expr),* $(,)?) => {{
        let mut v: Vec<_> = Vec::new();
        $(v.push($elem);)*
        v
    }};
}

let v: Vec<i32> = my_vec![1, 2, 3, 4, 5];
let empty: Vec<i32> = my_vec![];
```

### Struct generation with multiple field captures

```rust
macro_rules! make_struct {
    ($name:ident { $($field:ident : $ty:ty),* $(,)? }) => {
        struct $name {
            $($field: $ty,)*
        }
    };
}

make_struct!(Point { x: f64, y: f64 });
```

## Recursive Macros

A macro can call itself. The base case ends recursion; each recursive step processes part of the input:

```rust
macro_rules! count_items {
    () => { 0usize };
    ($head:expr $(, $tail:expr)*) => {
        1usize + count_items!($($tail),*)
    };
}

let count: usize = count_items!(10, 20, 30, 40); // 4
```

## TT Muncher Pattern

A Token Tree (TT) muncher processes tokens one at a time via recursion. It's used when simple repetition can't express the logic — e.g., when each token needs different handling:

```rust
macro_rules! print_all {
    () => {};  // base case
    ($first:expr $(, $rest:expr)*) => {
        println!("{:?}", $first);
        print_all!($($rest),*);  // recurse with remainder
    };
}

print_all!(1, "hello", 3.14, true);
```

## Macro Hygiene

Variables introduced inside a macro expansion are scoped to that expansion — they do not leak into the caller's scope. This prevents accidental name collisions:

```rust
macro_rules! hygienic {
    ($val:expr) => {{
        let inner: i32 = $val * 2; // 'inner' is invisible outside
        inner
    }};
}

let doubled: i32 = hygienic!(10); // OK: 20
// println!("{}", inner);          // ERROR: 'inner' not in scope
```

## stringify! and concat!

`stringify!` turns its token stream argument into a `&str` literal at compile time, without evaluating it. `concat!` joins string literals at compile time:

```rust
let tokens: &str = stringify!(x + y * z); // "x + y * z"

macro_rules! make_greeting {
    ($name:ident) => {
        concat!("Hello, ", stringify!($name), "!")
    };
}

let greeting: &str = make_greeting!(World); // "Hello, World!"
```

## Related Notes

- [[Advanced Macros]]
- [[Built-in Macros]]
