---
tags:
  - rust
  - error-handling
  - propagation
source: error_handling/src/propagation.rs
---

# Propagation

Error propagation is how you pass a failure up the call stack without handling it at the current level. Rust provides the `?` operator as the primary tool; the alternative is manual `match` with explicit `return Err(e)`.

## ? vs Manual Match

Both are equivalent. `?` is syntactic sugar:

```rust
// Manual
fn calculate_manual() -> Result<f64, String> {
    let result1 = match divide(10.0, 2.0) {
        Ok(val) => val,
        Err(e)  => return Err(e),
    };
    let result2 = match divide(result1, 5.0) {
        Ok(val) => val,
        Err(e)  => return Err(e),
    };
    return Ok(result2);
}

// With ?
fn calculate_auto() -> Result<f64, String> {
    let result1 = divide(10.0, 2.0)?;
    let result2 = divide(result1, 5.0)?;
    return Ok(result2);
}
```

`?` desugars to the manual form — plus an implicit `From::from` call on the error type if conversion is needed. See [[Error Conversion]] for that detail.

## Chaining Operations

`?` linearizes what would otherwise be nested match expressions:

```rust
fn process_input(input: &str) -> Result<i32, String> {
    let num       = parse_number(input)?;
    let validated = validate_positive(num)?;
    let result    = double(validated)?;
    return Ok(result);
}
```

Each step can fail independently. The first `Err` short-circuits the function and returns immediately.

## ? with Option

`?` works on `Option` in functions that return `Option`. It returns `None` on a `None` value:

```rust
fn get_uppercase(s: &str) -> Option<char> {
    let c = get_first_char(s)?; // returns None if string is empty
    return Some(c.to_ascii_uppercase());
}
```

You cannot use `?` on `Option` in a function returning `Result` without converting first (e.g., `.ok_or_else(...)`).

## Early Return Without ?

For multiple independent guard conditions, explicit `return Err(...)` reads cleanly and avoids unnecessary nesting:

```rust
fn check_multiple_conditions(val: i32) -> Result<i32, String> {
    if val < 0   { return Err(String::from("negative")); }
    if val > 100 { return Err(String::from("too large")); }
    if val % 2 != 0 { return Err(String::from("not even")); }
    return Ok(val);
}
```

## Same-Type Error Propagation

When all steps in a pipeline return the same error type, `?` propagates without any conversion:

```rust
#[derive(Debug)]
enum Error {
    Parse(String),
    Validation(String),
    Compute(String),
}

fn pipeline(input: &str) -> Result<i32, Error> {
    let num      = parse(input)?;    // Result<i32, Error>
    let validated = validate(num)?;  // Result<i32, Error>
    let result   = compute(validated)?; // Result<i32, Error>
    return Ok(result);
}
```

For different error types, you need `From` impls — see [[Error Conversion]].

## ? in Closures

`?` inside a closure returns from the closure, not the outer function. To propagate errors through an iterator, collect into `Result<Vec<T>, E>`:

```rust
fn process_list(items: Vec<&str>) -> Result<Vec<i32>, String> {
    let results: Result<Vec<i32>, String> = items
        .into_iter()
        .map(|item| {
            let num: i32 = item.parse().map_err(|_| String::from("parse failed"))?;
            return Ok(num * 2);
        })
        .collect(); // short-circuits on first Err

    return results;
}
```

This works because `Result<Vec<T>, E>` implements `FromIterator`. The collection stops at the first `Err` and returns it. All items must succeed for an `Ok(Vec<T>)`.

## Converting Option to Result

To use `?` on an `Option` inside a `Result`-returning function:

```rust
fn extract() -> Result<i32, String> {
    let opt: Option<i32> = get_value()?;          // propagates Result
    return opt.ok_or_else(|| String::from("value missing")); // Option -> Result
}
```

`.ok_or(err)` and `.ok_or_else(|| err)` convert `None` to `Err`. Use `ok_or_else` when the error value is expensive to construct (lazy evaluation).

## Key Points

- `?` = `match` + `return Err(From::from(e))` — short-circuits on any `Err`
- Works on both `Result` and `Option`, but the function return type must match
- `?` in a closure returns from the closure only; collect into `Result<Vec<_>>` to propagate through iterators
- For cross-type propagation, `From` impls are required — see [[Error Conversion]]
- Adding context to propagated errors: see [[Anyhow]]
