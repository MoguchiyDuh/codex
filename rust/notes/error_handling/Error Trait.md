---
tags:
  - rust
  - error-handling
  - traits
source: error_handling/src/error_trait.rs
---

# Error Trait

`std::error::Error` is the standard trait for error types. Implementing it makes a type compatible with the broader Rust ecosystem — error-handling crates, `Box<dyn Error>` return types, and generic bounds all depend on it.

## Supertraits

`Error` requires both `Debug` and `Display`:

- `Display` — the user-facing message (`{}`)
- `Debug` — the developer-facing representation (`{:?}`)

You must implement both before the compiler will accept `impl Error for YourType`.

```rust
use std::fmt;
use std::error::Error;

#[derive(Debug)]
enum AppError {
    IoError(String),
    ParseError(String),
}

impl fmt::Display for AppError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            AppError::IoError(msg)   => write!(f, "IO error: {}", msg),
            AppError::ParseError(msg) => write!(f, "Parse error: {}", msg),
        }
    }
}

impl Error for AppError {}
```

## source() and the Error Chain

`source()` returns the lower-level error that caused this one — the previous link in an error chain. The return type is `Option<&(dyn Error + 'static)>`. The `'static` bound means the returned reference must not contain non-static lifetimes, which ensures the error can be stored, passed across threads, and safely downcasted.

```rust
impl Error for HighLevelError {
    fn source(&self) -> Option<&(dyn Error + 'static)> {
        Some(&self.source) // exposes the wrapped LowLevelError
    }
}
```

When `source()` returns `None`, the type is declaring it has no underlying cause.

## Walking the Chain

```rust
fn print_error_chain(err: &dyn Error) {
    println!("Error: {}", err);
    let mut current = err.source();
    while let Some(source) = current {
        println!("  Caused by: {}", source);
        current = source.source();
    }
}
```

Iterate with `.source()` until you hit `None`. This is the manual equivalent of what `anyhow`'s `.chain()` does automatically — see [[Anyhow]].

## Box\<dyn Error\>

When a function can return different error types, use `Box<dyn Error>` as the return type. Any type implementing `Error` can be boxed and returned without knowing the concrete type at compile time.

```rust
fn might_fail(succeed: bool) -> Result<String, Box<dyn Error>> {
    if succeed {
        return Ok(String::from("success"));
    }
    return Err(Box::new(AppError::IoError(String::from("disk full"))));
}
```

The downside: you lose static type information. The caller can only recover the concrete type via downcasting. For typed errors, prefer a concrete enum or [[Thiserror]].

## Generic Bounds on Error

```rust
fn handle_any_error<E: Error>(result: Result<(), E>) {
    match result {
        Ok(_)  => println!("succeeded"),
        Err(e) => println!("failed: {}", e),
    }
}
```

`E: Error` is the static-dispatch alternative to `Box<dyn Error>`. Zero overhead, but the caller's error type must be known at the call site.

## description() — Deprecated

`Error` used to have a `description()` method returning `&str`. It was deprecated in Rust 1.27 — `Display` covers the same ground more flexibly. Compiler will warn on use.

## Key Points

- `Error` requires `Debug + Display` as supertraits — implement both first
- `source()` exposes the underlying cause; return `None` if there is none
- `Box<dyn Error>` erases error types at the cost of downcasting to recover them
- `'static` on the `source()` bound enables safe storage and downcasting
- For cross-references: [[Custom Errors]], [[Error Conversion]], [[Propagation]]
