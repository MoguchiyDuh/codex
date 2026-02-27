---
tags:
  - rust
  - error-handling
  - crates
  - anyhow
source: error_handling/src/anyhow_example.rs
---

# Anyhow

`anyhow` is an ergonomic error-handling crate for **applications** (not libraries). Its core value: you stop thinking about error types and focus on propagation and context. Internally it uses a trait object, so any `Error`-implementing type can be converted into `anyhow::Error` automatically.

For library crates with structured, typed errors, use [[Thiserror]] instead.

## The Result Type Alias

```rust
use anyhow::Result;

// anyhow::Result<T> = std::result::Result<T, anyhow::Error>
fn might_fail(succeed: bool) -> Result<String> {
    if succeed { return Ok(String::from("success")); }
    return Err(anyhow!("operation failed"));
}
```

One import, one return type, no need to define or thread your own error enum through every function signature.

## anyhow! — Ad-hoc Errors

Creates an `anyhow::Error` from a string or formatted message:

```rust
return Err(anyhow!("version {} is too old, need at least {}", version, required));
```

## bail! — Early Return

`bail!(msg)` is shorthand for `return Err(anyhow!(msg))`:

```rust
fn validate_input(input: &str) -> Result<i32> {
    if input.is_empty() {
        bail!("input cannot be empty");
    }
    let num: i32 = input.parse()?; // automatic conversion from ParseIntError
    if num < 0 {
        bail!("number must be non-negative");
    }
    return Ok(num);
}
```

## ensure! — Assertion with Error

`ensure!(condition, msg)` returns an error if the condition is false — like `assert!` but returns `Err` instead of panicking:

```rust
fn check_range(value: i32, min: i32, max: i32) -> Result<i32> {
    ensure!(value >= min, "value {} is below minimum {}", value, min);
    ensure!(value <= max, "value {} exceeds maximum {}", value, max);
    return Ok(value);
}
```

## Automatic Error Conversion

Any type implementing `std::error::Error` converts into `anyhow::Error` automatically via `?`. No `From` impls needed:

```rust
fn parse_and_compute(input: &str) -> Result<i32> {
    let num: i32 = input.parse()?; // ParseIntError -> anyhow::Error, no From impl required
    return Ok(num * 2);
}
```

## Adding Context

`.context("message")` wraps an error with an additional message. The original error becomes the `source()`:

```rust
fn read_file(path: &str) -> Result<String> {
    let content = std::fs::read_to_string(path)
        .context(format!("failed to read file '{}'", path))?;
    return Ok(content);
}
```

`.with_context(|| ...)` takes a closure — evaluated only when there is an error, so use it when context string construction is non-trivial:

```rust
let data = parse_something()
    .with_context(|| format!("failed to parse data for record {}", id))?;
```

## Chaining Context

Multiple `.context()` calls stack up. The outermost context is displayed first; earlier contexts become `source()` links in the chain:

```rust
fn initialize_system() -> Result<()> {
    let _config = load_config()
        .context("failed to load configuration")
        .context("system initialization failed")?;
    return Ok(());
}

// Output on error:
// "system initialization failed"
//   caused by: "failed to load configuration"
//   caused by: "file corrupted"
```

## Inspecting the Error Chain

`e.chain()` iterates over all errors in the chain — the error itself and each successive `source()`:

```rust
if let Err(e) = get_user_profile(123) {
    for (i, cause) in e.chain().enumerate() {
        println!("  {}: {}", i, cause);
    }
}
```

## Downcasting

`anyhow::Error` supports downcasting back to concrete types, same interface as `Box<dyn Error>`:

```rust
if let Some(custom) = e.downcast_ref::<CustomError>() {
    println!("code: {}", custom.code);
}
```

## anyhow vs thiserror

| | anyhow | thiserror |
|---|---|---|
| Target | Applications | Libraries |
| Error type | Erased (`anyhow::Error`) | Concrete typed enum/struct |
| Caller matching | No exhaustive match | Full pattern matching |
| Context | `.context()` built-in | Manual or none |
| From impls | Not needed | Required (or `#[from]`) |

Use `anyhow` when you're writing `main`, a binary, or CLI logic. Use `thiserror` when you're writing a library whose callers need to handle specific error variants.

## Key Points

- `anyhow::Result<T>` = `Result<T, anyhow::Error>` — a trait object under the hood
- `?` auto-converts any `Error` type; no `From` impls needed
- `bail!` = `return Err(anyhow!(...))`, `ensure!` = conditional bail
- `.context()` / `.with_context()` add layered messages; `.chain()` iterates them
- Downcasting recovers concrete types when needed
- Cross-reference: [[Thiserror]], [[Error Conversion]], [[Propagation]]
