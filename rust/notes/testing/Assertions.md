---
tags: [rust, testing, assertions]
source: testing/src/assertions.rs
---

# Assertions

Assertion macros panic on failure. Outside of tests they work the same way — they're just macros that call `panic!`. Inside `#[test]` functions a panic causes the test to fail with the message.

## Core macros

| Macro | Fails when |
|-------|-----------|
| `assert!(expr)` | `expr` is `false` |
| `assert_eq!(a, b)` | `a != b` |
| `assert_ne!(a, b)` | `a == b` |

`assert_eq!` and `assert_ne!` print both values on failure — significantly easier to debug than a bare `assert!`.

```rust
assert_eq!(2 * 3, 6);
assert_eq!(vec![1, 2, 3], vec![1, 2, 3]);
assert_ne!("foo", "bar");
```

All three accept an optional format message as trailing arguments:

```rust
assert!(x > 0, "expected positive, got {}", x);
assert_eq!(result, expected, "compute() returned wrong value");
```

The message is only formatted if the assertion actually fails.

## Float comparison

IEEE 754 floats cannot represent 0.1, 0.2, or 0.3 exactly — binary floating-point accumulates rounding error. `assert_eq!` on floats is unreliable:

```rust
let a = 0.1 + 0.2;
let b = 0.3;
assert_eq!(a, b); // FAILS — values differ at ~17th decimal place
```

Use an epsilon comparison instead:

```rust
fn approx_eq(a: f64, b: f64, epsilon: f64) -> bool {
    return (a - b).abs() < epsilon;
}

assert!(approx_eq(0.1 + 0.2, 0.3, 1e-10));
```

## Custom assertion macros

For domain-specific checks, declarative macros (`macro_rules!`) keep tests readable without duplicating logic.

### `assert_approx_eq!`

```rust
macro_rules! assert_approx_eq {
    ($left:expr, $right:expr) => {
        assert_approx_eq!($left, $right, 1e-10)
    };
    ($left:expr, $right:expr, $eps:expr) => {{
        let diff = (($left as f64) - ($right as f64)).abs();
        assert!(
            diff < $eps,
            "approx eq failed: |{} - {}| = {} >= {}",
            $left, $right, diff, $eps
        );
    }};
}

assert_approx_eq!(0.1 + 0.2, 0.3);
assert_approx_eq!(std::f64::consts::PI, 3.14159, 1e-4);
```

### `assert_contains!`

```rust
macro_rules! assert_contains {
    ($haystack:expr, $needle:expr) => {
        assert!(
            $haystack.contains($needle),
            "expected {:?} to contain {:?}",
            $haystack, $needle
        );
    };
}

assert_contains!("hello world", "world");
```

### `assert_sorted!`

```rust
macro_rules! assert_sorted {
    ($slice:expr) => {{
        let s = $slice;
        for i in 1..s.len() {
            assert!(s[i - 1] <= s[i], "not sorted at index {}: {} > {}", i, s[i - 1], s[i]);
        }
    }};
}

assert_sorted!(&[1, 2, 3, 4, 5]);
```

## `debug_assert*`

Variants that are compiled out in release builds. Use for expensive invariant checks that you don't want paying a cost in production.

```rust
debug_assert!(1 < 2);
debug_assert_eq!(2 + 2, 4);
debug_assert_ne!(0, 1);
```

Active when `cfg!(debug_assertions)` is true — that's debug builds and `cargo test`. Stripped by `--release`.

## See also

- [[Unit Tests]] — `#[test]`, `#[should_panic]`, Result-returning tests
- [[Organizing Tests]] — test module structure
- [[../basics/Panic|Panic]] — how panic works, `catch_unwind`
