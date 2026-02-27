---
tags:
  - rust
  - macros
  - advanced
source: macros/src/advanced.rs
---

# Advanced Macros

Builds on the mechanics in [[Declarative Macros]]. Covers patterns used in real-world crate design: internal helpers, bulk code generation, visibility, and an overview of procedural macros.

## Internal Rules (@keyword Convention)

By convention, macro arms prefixed with `@` are internal helpers — not intended to be called directly by users. The compiler does not enforce this; it is a social contract that signals "private implementation detail":

```rust
macro_rules! log {
    (info: $msg:expr)  => { log!(@print "INFO",  $msg) };
    (warn: $msg:expr)  => { log!(@print "WARN",  $msg) };
    (error: $msg:expr) => { log!(@print "ERROR", $msg) };
    // Internal arm — call via the public arms above
    (@print $level:expr, $msg:expr) => {
        println!("[{}] {}", $level, $msg);
    };
}

log!(info: "server started");
log!(warn: "high memory usage");
```

This avoids defining separate helper macros while keeping the public surface clean.

## Generating impl Blocks

Macros can emit full `impl` blocks, removing boilerplate for newtype wrappers:

```rust
macro_rules! impl_display {
    ($type:ty, $fmt:expr) => {
        impl std::fmt::Display for $type {
            fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
                write!(f, $fmt, self.0)
            }
        }
    };
}

struct Meters(f64);
struct Kilograms(f64);
impl_display!(Meters, "{} m");
impl_display!(Kilograms, "{} kg");
```

## Generating Multiple Items

Repetition inside the expansion body lets one macro invocation produce many independent items — structs, impls, trait implementations:

```rust
macro_rules! make_errors {
    ($($name:ident => $msg:literal),+ $(,)?) => {
        $(
            #[derive(Debug)]
            struct $name;

            impl std::fmt::Display for $name {
                fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
                    write!(f, $msg)
                }
            }

            impl std::error::Error for $name {}
        )+
    };
}

make_errors!(
    ParseError   => "parse error",
    NetworkError => "network error",
    TimeoutError => "connection timed out",
);
```

Each `$name` expands to a full struct + two impl blocks.

## Variadic Over Types

The `ty` designator lets macros accept arbitrary types, useful for inspecting type properties:

```rust
macro_rules! print_type_size {
    ($($t:ty),+ $(,)?) => {
        $(
            println!("size_of::<{}>() = {} bytes", stringify!($t), std::mem::size_of::<$t>());
        )+
    };
}

print_type_size!(i8, i16, i32, i64, i128, f32, f64, bool, char, usize);
```

## Trailing Comma Normalization

`$(,)?` at the end of a pattern makes a trailing comma optional, matching both `[1, 2, 3]` and `[1, 2, 3,]`. Worth adding to any public macro:

```rust
macro_rules! flexible_vec {
    ($($elem:expr),* $(,)?) => {
        vec![$($elem),*]
    };
}
```

## cfg-Conditional Macros

`cfg!()` evaluates configuration predicates at compile time and returns a `bool`. Using it inside a macro body lets one macro emit platform-specific values:

```rust
macro_rules! platform_msg {
    () => {
        if cfg!(target_os = "linux") {
            "Linux"
        } else if cfg!(target_os = "windows") {
            "Windows"
        } else {
            "Other OS"
        }
    };
}
```

See also: `compile_error!` in [[Built-in Macros]] for hard build-time failures on unsupported platforms.

## Macro Calling Macro

A macro can invoke another macro in its expansion. Expansion is recursive — the compiler keeps expanding until no macro calls remain:

```rust
macro_rules! add_one {
    ($x:expr) => { $x + 1 };
}

macro_rules! double_then_add_one {
    ($x:expr) => { add_one!($x * 2) };
}

double_then_add_one!(5); // expands to: (5 * 2) + 1 = 11
```

## Macro Export and Visibility

By default a `macro_rules!` macro is only visible within the module it's defined in.

`#[macro_export]` makes it available from the crate root, importable by users of the crate:

```rust
// In a library crate:
#[macro_export]
macro_rules! my_macro { ... }

// In consuming crate:
use my_crate::my_macro;
```

The legacy approach `#[macro_use] extern crate my_crate;` imports all exported macros without naming them — avoid in modern Rust.

## Procedural Macros (Overview)

Procedural macros (proc macros) operate on the token stream directly, parsing and generating Rust syntax programmatically. They run as compiler plugins and require a separate crate with `proc-macro = true` in `[lib]`.

Three kinds:

| Kind | Syntax | Use case |
|---|---|---|
| Derive | `#[derive(Trait)]` | Code generation for structs/enums |
| Attribute | `#[my_attribute]` | Transforms the annotated item |
| Function-like | `my_macro!(...)` | Full token control, arbitrary DSL |

Typical dependencies:

```toml
[lib]
proc-macro = true

[dependencies]
syn   = { version = "2", features = ["full"] }
quote = "1"
proc-macro2 = "1"
```

Real-world examples: `serde` uses derive macros, `tokio::main` is an attribute macro, `sqlx::query!` is a function-like proc macro.

## The ? Operator (Macro Desugaring)

`?` is syntax sugar that desugars to a match expression. Shown here as an example of how language constructs can behave like macros:

```rust
// s.parse()?  expands roughly to:
match s.trim().parse() {
    Ok(v)  => v,
    Err(e) => return Err(e.into()),
}
```

`From::from` (i.e. `.into()`) is called on the error, enabling automatic error type conversion.

## Related Notes

- [[Declarative Macros]]
- [[Built-in Macros]]
