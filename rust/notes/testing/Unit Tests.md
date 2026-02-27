---
tags: [rust, testing, unit-tests]
source: testing/src/unit_tests.rs
---

# Unit Tests

Unit tests verify individual functions or modules in isolation. In Rust they live alongside the source they test, gated by `#[cfg(test)]` so they're compiled only when running `cargo test` — no test code bleeds into release binaries.

## Basic structure

```rust
#[cfg(test)]
mod tests {
    use super::*; // access private items in the parent module

    #[test]
    fn test_add_basic() {
        assert_eq!(add(2, 3), 5);
    }
}
```

`use super::*` is intentional — unit tests are allowed to access private functions. That's the point.

## Testing `Option` and `Result`

```rust
#[test]
fn test_divide_normal() {
    assert_eq!(divide(10.0, 2.0), Some(5.0));
}

#[test]
fn test_divide_by_zero() {
    assert_eq!(divide(10.0, 0.0), None);
}

#[test]
fn test_parse_positive_valid() {
    assert_eq!(parse_positive("42"), Ok(42));
    assert_eq!(parse_positive("  7  "), Ok(7)); // trims whitespace
}

#[test]
fn test_parse_positive_negative_number() {
    let result = parse_positive("-1");
    assert!(result.is_err());
    assert!(result.unwrap_err().contains("negative"));
}
```

For error cases, prefer `is_err()` + inspecting the message over matching the exact `Err(...)` value — it's more resilient to message wording changes.

## `#[should_panic]`

A test marked `#[should_panic]` passes only if the body panics. Optionally add `expected` to assert the panic message contains a substring.

```rust
#[test]
#[should_panic(expected = "index out of bounds")]
fn test_panic_message() {
    let v: Vec<i32> = vec![];
    let _ = v[0];
}
```

Without `expected`, any panic satisfies the test. With it, the panic message must contain the given string — a mismatch still fails the test.

See [[../basics/Panic|Panic]] for how panics work at runtime.

## `#[ignore]`

Skips a test by default. Useful for slow, flaky, or environment-dependent tests.

```rust
#[test]
#[ignore = "slow test - run explicitly with --include-ignored"]
fn test_slow_operation() {
    std::thread::sleep(std::time::Duration::from_millis(100));
    assert_eq!(1 + 1, 2);
}
```

Run ignored tests explicitly:
```
cargo test -- --include-ignored
```

## Tests returning `Result`

Tests can return `Result<(), E>`. An `Err` return fails the test with the error's `Display` message. This lets you use `?` instead of `.unwrap()`, which gives cleaner failures.

```rust
#[test]
fn test_with_result_return() -> Result<(), Box<dyn std::error::Error>> {
    let n = parse_positive("10")?;
    assert_eq!(n, 10);
    return Ok(());
}
```

## Running tests

```
cargo test -p testing                    # run all tests in the package
cargo test -p testing unit_tests         # filter by name substring
cargo test -- --nocapture               # show println! output
cargo test -- --include-ignored         # include #[ignore] tests
cargo test -- --test-threads=1          # serial execution
```

## See also

- [[Assertions]] — assert macros in detail
- [[Organizing Tests]] — test module structure, helper patterns, nested modules
