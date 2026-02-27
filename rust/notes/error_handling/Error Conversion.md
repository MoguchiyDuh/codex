---
tags:
  - rust
  - error-handling
  - type-conversion
source: error_handling/src/error_conversion.rs
---

# Error Conversion

When a function calls multiple sub-functions that each return different error types, you need a way to unify them into the function's own error type. Rust does this through `From` implementations and the `?` operator.

## From and the ? Operator

The `?` operator desugars to:

```
expr?  →  match expr {
    Ok(val) => val,
    Err(e)  => return Err(From::from(e)),
}
```

The key part: `From::from(e)`. If the error type in `expr` differs from the function's return error type, Rust calls `From::from` to convert it. So having `impl From<SourceError> for MyError` is what enables `?` to work across mismatched error types.

```rust
impl From<ParseIntError> for AppError {
    fn from(err: ParseIntError) -> AppError {
        return AppError::Parse(err);
    }
}

fn parse_and_double(input: &str) -> Result<i32, AppError> {
    let num: i32 = input.parse()?; // ParseIntError auto-converts to AppError
    return Ok(num * 2);
}
```

No `.map_err()` needed — the conversion is implicit via the `From` impl.

## Multiple From Implementations

A single unified error enum can absorb multiple source error types:

```rust
#[derive(Debug)]
enum UnifiedError {
    Io(IoError),
    Network(NetworkError),
    Parse(ParseIntError),
}

impl From<IoError>       for UnifiedError { fn from(e: IoError)       -> Self { UnifiedError::Io(e) } }
impl From<NetworkError>  for UnifiedError { fn from(e: NetworkError)  -> Self { UnifiedError::Network(e) } }
impl From<ParseIntError> for UnifiedError { fn from(e: ParseIntError) -> Self { UnifiedError::Parse(e) } }

fn combined_operation() -> Result<String, UnifiedError> {
    let _file = read_file()?;   // IoError      -> UnifiedError
    let _data = fetch_data()?;  // NetworkError -> UnifiedError
    let _num: i32 = "abc".parse()?; // ParseIntError -> UnifiedError
    return Ok(String::from("success"));
}
```

The caller only deals with `UnifiedError`, and each variant preserves the original error inside it.

## Manual Conversion with map\_err

When you don't want to define a `From` impl (e.g., converting to `String` for a quick prototype), use `.map_err()` with a closure:

```rust
fn manual_conversion(input: &str) -> Result<i32, String> {
    let num: i32 = input
        .parse()
        .map_err(|e: ParseIntError| format!("Failed to parse: {}", e))?;
    return Ok(num);
}
```

`.map_err(f)` transforms the `Err` value, leaving `Ok` untouched. The `?` then propagates the now-compatible error type.

## Converting to Box\<dyn Error\>

Any type implementing `Error` can be boxed into `Box<dyn Error>`. Rust provides a blanket `From<E: Error> for Box<dyn Error>` impl, so `?` works automatically when the return type is `Box<dyn Error>`:

```rust
fn as_trait_object() -> Result<(), Box<dyn Error>> {
    let err = AppError::Custom(String::from("something went wrong"));
    return Err(Box::new(err));
}
```

Tradeoff: you lose the concrete type at the call site. Recovering it requires downcasting.

## Downcasting

`Box<dyn Error>` and `&dyn Error` support downcasting via `downcast_ref::<T>()`. This uses the vtable's `TypeId` to check if the underlying concrete type matches `T`. It returns `None` if it doesn't — no undefined behavior (UB), no panics.

```rust
if let Some(net_err) = e.downcast_ref::<NetworkError>() {
    println!("Network error code: {}", net_err.code);
}
```

`anyhow::Error` also supports downcasting the same way — see [[Anyhow]].

## Adding Context

Wrapping a result with a string context before returning it upstream:

```rust
fn add_context<E: Error>(result: Result<(), E>, context: &str) -> Result<(), String> {
    result.map_err(|e| format!("{}: {}", context, e))
}
```

This is the manual version of what `anyhow`'s `.context()` does ergonomically — see [[Anyhow]].

## Key Points

- `?` calls `From::from(e)` on the error — implement `From<Source> for Target` to enable it
- Multiple `From` impls on one enum let `?` unify heterogeneous error types cleanly
- `.map_err(|e| ...)` converts without a `From` impl — useful for one-off transformations
- `Box<dyn Error>` accepts any error type via a blanket `From` impl; use `downcast_ref` to recover
- `thiserror`'s `#[from]` generates `From` impls automatically — see [[Thiserror]]
