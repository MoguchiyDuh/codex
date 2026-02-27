---
tags: [rust, testing, organization]
source: testing/src/organizing.rs
---

# Organizing Tests

## Where tests live

| Location | Purpose |
|----------|---------|
| `src/*.rs` inside `#[cfg(test)]` | Unit tests — same file as the code |
| `tests/` | Integration tests — separate binary, only public interface |
| `benches/` | Benchmarks (typically with the `criterion` crate) |
| `examples/` | Runnable examples via `cargo run --example` |

Unit tests in `#[cfg(test)]` can access private items via `use super::*`. Integration tests in `tests/` cannot — they test the crate from the outside.

## Test helper functions

Rust has no built-in `before_each`. Use plain functions instead:

```rust
#[cfg(test)]
mod tests {
    use super::*;

    fn make_account() -> BankAccount {
        return BankAccount::new("Test User", 500.0);
    }

    #[test]
    fn test_new_account_balance() {
        let acc = make_account();
        assert_eq!(acc.balance(), 500.0);
        assert_eq!(acc.owner(), "Test User");
    }

    #[test]
    fn test_deposit_increases_balance() {
        let mut acc = make_account();
        assert_eq!(acc.deposit(100.0), Ok(600.0));
        assert_eq!(acc.balance(), 600.0);
    }
}
```

Each test gets a fresh instance — no shared mutable state between tests. This is by design: tests run in parallel by default (each in its own thread), so shared mutable state requires synchronization or `--test-threads=1`.

## Nested test modules

You can nest modules inside `#[cfg(test)]` to group tests by feature or behavior. The nested modules inherit the `#[cfg(test)]` gate from the parent.

```rust
#[cfg(test)]
mod tests {
    use super::*;

    mod deposit_tests {
        use super::*;

        #[test]
        fn test_large_deposit() {
            let mut acc = make_account();
            acc.deposit(1_000_000.0).unwrap();
            assert_eq!(acc.balance(), 1_000_500.0);
        }

        #[test]
        fn test_fractional_deposit() {
            let mut acc = make_account();
            acc.deposit(0.01).unwrap();
            assert!((acc.balance() - 500.01).abs() < 1e-9);
        }
    }

    mod withdraw_tests {
        use super::*;

        #[test]
        fn test_withdraw_to_zero() {
            let mut acc = make_account();
            acc.withdraw(500.0).unwrap();
            assert_eq!(acc.balance(), 0.0);
        }
    }
}
```

The full test name becomes `tests::deposit_tests::test_large_deposit` — useful for filtering with `cargo test deposit_tests`.

## Testing error paths

Always verify both the happy path and failure cases. For `Result`-returning methods, check the error message contains the expected substring rather than matching the exact string:

```rust
#[test]
fn test_withdraw_insufficient_funds() {
    let mut acc = make_account();
    let result = acc.withdraw(9999.0);
    assert!(result.is_err());
    let err = result.unwrap_err();
    assert!(err.contains("insufficient funds"), "got: {}", err);
}

#[test]
fn test_withdraw_exact_balance() {
    let mut acc = make_account();
    assert_eq!(acc.withdraw(500.0), Ok(0.0));
}
```

## `cargo test` reference

```
cargo test                        # all tests in the workspace
cargo test -p testing             # tests in one package
cargo test test_deposit           # filter by name substring
cargo test -- --nocapture        # show println! output
cargo test -- --test-threads=1   # serial — needed for shared resources
cargo test -- --include-ignored  # run #[ignore] tests too
```

The filter (`cargo test <pattern>`) matches against the full test path including module names, so `cargo test deposit_tests` runs everything in `deposit_tests`.

## TDD flow

TDD (Test Driven Development) means writing the test before the implementation. In Rust the workflow is:

1. Write the `#[test]` — it won't compile yet if types don't exist
2. Write the minimal implementation to make it compile and pass
3. Refactor, keeping tests green

CI (Continuous Integration) pipelines typically run `cargo test --all` to catch regressions on every push.

## See also

- [[Unit Tests]] — `#[test]`, `#[should_panic]`, `#[ignore]`
- [[Assertions]] — assert macros, float comparison, custom macros
