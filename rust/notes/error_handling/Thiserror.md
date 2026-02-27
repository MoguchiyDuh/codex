---
tags:
  - rust
  - error-handling
  - crates
  - thiserror
source: error_handling/src/thiserror_example.rs
---

# Thiserror

`thiserror` is a derive macro crate for defining custom error types in **libraries**. It generates `Display` and `std::error::Error` implementations from attributes, eliminating the boilerplate you'd otherwise write by hand.

For applications where callers don't need to match on specific variants, use [[Anyhow]] instead.

## Basic Derive

`#[derive(Error, Debug)]` enables the `thiserror` machinery. Each variant gets an `#[error("...")]` attribute that becomes its `Display` message.

```rust
use thiserror::Error;

#[derive(Error, Debug)]
enum DataError {
    #[error("data not found")]
    NotFound,

    #[error("invalid data format")]
    InvalidFormat,

    #[error("data too large: {size} bytes (max {max})")]
    TooLarge { size: usize, max: usize },

    #[error("IO error: {0}")]
    Io(String),
}
```

- Named fields in the format string use their field name: `{size}`, `{max}`
- Unnamed (tuple) fields use positional syntax: `{0}`, `{1}`

No manual `impl fmt::Display` needed. The macro generates it at compile time.

## #\[from\] — Automatic From and source()

`#[from]` on a field does two things:

1. Derives `From<FieldType> for YourError`, enabling `?` to convert automatically
2. Sets that field as the `.source()` return for the `Error` trait

```rust
#[derive(Error, Debug)]
enum ParseError {
    #[error("empty input")]
    Empty,

    #[error("invalid number")]
    InvalidNumber(#[from] ParseIntError),
}

fn parse_id(input: &str) -> Result<i32, ParseError> {
    if input.is_empty() { return Err(ParseError::Empty); }
    let id: i32 = input.parse()?; // ParseIntError -> ParseError::InvalidNumber via From
    return Ok(id);
}
```

One `#[from]` annotation replaces both the `From` impl and the `source()` override.

## Multiple #\[from\] Sources

An enum can absorb multiple source error types, each with its own `#[from]`:

```rust
#[derive(Error, Debug)]
enum AppError {
    #[error("configuration error: {0}")]
    Config(String),

    #[error("parse error")]
    Parse(#[from] ParseIntError),

    #[error("data error")]
    Data(#[from] DataError),
}

fn initialize_app(config_valid: bool, data_id: u32) -> Result<(), AppError> {
    if !config_valid { return Err(AppError::Config(String::from("invalid config"))); }
    let _id: i32 = "42".parse()?;       // ParseIntError -> AppError::Parse
    let _data = load_data(data_id)?;     // DataError     -> AppError::Data
    return Ok(());
}
```

## #\[source\] — Manual Source Without From

When you want `.source()` to return a field but don't want a `From` impl generated, use `#[source]` instead of `#[from]`:

```rust
#[derive(Error, Debug)]
enum NetworkError {
    #[error("connection failed: {message}")]
    ConnectionFailed {
        message: String,
        #[source]
        source: std::io::Error, // exposed as .source(), but no From<io::Error> for NetworkError
    },

    #[error("timeout after {duration}ms")]
    Timeout { duration: u64 },
}
```

Use this when you construct the error manually but still want callers to chain-inspect the cause.

## #\[error(transparent)\]

`transparent` delegates both `Display` and `.source()` to the wrapped error. The wrapper type disappears from the user's perspective:

```rust
#[derive(Error, Debug)]
enum WrapperError {
    #[error(transparent)]
    ParseInt(#[from] ParseIntError),

    #[error(transparent)]
    Data(#[from] DataError),
}
```

The caller sees the wrapped error's own message, not a new one. Useful for thin wrapper enums that only exist to unify types.

## thiserror vs Manual Implementation

```rust
// Manual — 10+ lines
#[derive(Debug)]
enum ManualError { Simple }

impl std::fmt::Display for ManualError {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        match self { ManualError::Simple => write!(f, "simple error") }
    }
}
impl std::error::Error for ManualError {}

// thiserror — 4 lines, same result
#[derive(Error, Debug)]
enum AutoError {
    #[error("simple error")]
    Simple,
}
```

The generated code is identical in behavior — `thiserror` is pure compile-time macro expansion with no runtime overhead.

## Real-World Example

```rust
#[derive(Error, Debug)]
enum ApiError {
    #[error("HTTP {status}: {message}")]
    Http { status: u16, message: String },

    #[error("request timeout")]
    Timeout,

    #[error("invalid response format")]
    InvalidResponse(#[from] serde_json::Error),

    #[error("network error")]
    Network(#[from] std::io::Error),
}
```

Callers can match on `ApiError::Http { status, .. }` for status-specific handling — something impossible with `anyhow::Error` without downcasting.

## Key Points

- `#[derive(Error, Debug)]` generates `Display` (from `#[error(...)]`) and `Error` impl
- `#[from]` generates `From<T>` and sets `.source()` — enables `?` conversion
- `#[source]` marks a field as `.source()` without generating `From`
- `#[error(transparent)]` delegates Display + source to the wrapped type
- Zero runtime overhead — all macro expansion happens at compile time
- Cross-reference: [[Anyhow]], [[Error Conversion]], [[Custom Errors]]
