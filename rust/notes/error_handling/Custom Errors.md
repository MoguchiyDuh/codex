---
tags:
  - rust
  - error-handling
  - custom-types
source: error_handling/src/custom_errors.rs
---

# Custom Errors

The idiomatic way to define errors is an enum (for categorically distinct failure modes) or a struct (for a single failure type with rich context). Both need `Debug + Display`, and optionally `std::error::Error` to be usable anywhere in the ecosystem.

## Error Enum

An enum variant per failure mode allows exhaustive pattern matching and lets callers handle each case differently.

```rust
use std::fmt;

#[derive(Debug)]
enum ParseError {
    EmptyInput,
    InvalidFormat,
    NumberTooLarge,
    NumberTooSmall,
}

impl fmt::Display for ParseError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            ParseError::EmptyInput     => write!(f, "Input cannot be empty"),
            ParseError::InvalidFormat  => write!(f, "Invalid format provided"),
            ParseError::NumberTooLarge => write!(f, "Number exceeds maximum value"),
            ParseError::NumberTooSmall => write!(f, "Number is below minimum value"),
        }
    }
}
```

`Display` is the user-facing message. `Debug` (derived) is for `{:?}` — useful in logs and during development.

## Pattern Matching on Error Variants

Because the error is a known enum, callers can match on individual variants and respond appropriately, rather than treating all errors the same:

```rust
match parse_number("150") {
    Ok(n) => println!("Success: {}", n),
    Err(ParseError::EmptyInput)     => println!("Please provide input"),
    Err(ParseError::InvalidFormat)  => println!("Use numeric format"),
    Err(ParseError::NumberTooLarge) => println!("Number must be <= 100"),
    Err(ParseError::NumberTooSmall) => println!("Number must be >= 0"),
}
```

This is the primary advantage of typed errors over `Box<dyn Error>` or `String`. See [[Error Trait]] for the tradeoff discussion.

## Struct Errors with Context

Use a struct when there is one failure mode but you want to attach metadata:

```rust
#[derive(Debug)]
struct ValidationError {
    field: String,
    message: String,
}

impl fmt::Display for ValidationError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Validation error in '{}': {}", self.field, self.message)
    }
}
```

This is cleaner than stuffing context into a `String` variant. The `Display` impl can format the fields directly.

Another example — carrying the offending value and valid bounds:

```rust
#[derive(Debug)]
struct RangeError {
    value: i32,
    min: i32,
    max: i32,
}

impl fmt::Display for RangeError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Value {} is out of range [{}, {}]", self.value, self.min, self.max)
    }
}
```

## Multiple Domain Errors

Define separate error types per domain (files, database, network) and keep them independent. Functions return the specific type for their domain:

```rust
fn open_file(path: &str) -> Result<String, FileError> { ... }
fn query_database(query: &str) -> Result<Vec<String>, DatabaseError> { ... }
```

When you need a function that calls both, you have two options:

1. **Unified enum** — wrap both into a top-level error enum (see [[Error Conversion]])
2. **`Box<dyn Error>`** — erase types, lose exhaustive matching

## When to Use thiserror

Writing `impl fmt::Display` and `impl Error` manually is boilerplate. The `thiserror` crate derives both from a single `#[error("...")]` attribute. Use it for any non-trivial error type — see [[Thiserror]].

## Key Points

- Enum errors: one variant per failure mode, enables exhaustive matching
- Struct errors: single failure with rich context fields
- `Display` = user message, `Debug` = developer/log format
- Domain-specific error types compose via conversion — see [[Error Conversion]]
- `thiserror` eliminates the `Display` + `Error` boilerplate — see [[Thiserror]]
