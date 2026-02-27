---
tags: [rust, basics, panic, error-handling]
source: basics/src/panic.rs
---

# Panic

Panics are **unrecoverable** errors — they terminate the thread (and usually the program). Use `Result`/`Option` for recoverable failures instead.

## `panic!`

```rust
panic!("something went wrong");
// Prints message + backtrace, then unwinds or aborts
```

## Common panic triggers

```rust
let arr = [1, 2, 3];
arr[10];                    // PANIC: index out of bounds

None::<i32>.unwrap();       // PANIC: called unwrap on None
Err::<i32, _>("fail").unwrap(); // PANIC: called unwrap on Err

let v: Vec<i32> = vec![];
v[0];                       // PANIC: index out of bounds
```

## `expect` — panics with a message

Better than bare `unwrap` — the message appears in the panic output:

```rust
some_opt.expect("value must exist at this point");
ok_result.expect("DB query should not fail here");
```

## Assertions

```rust
assert!(x == 5);
assert!(x > 0, "x must be positive, got {}", x);   // with format message

assert_eq!(2 + 2, 4);
assert_eq!(result, expected, "wrong result");

assert_ne!(a, b);
```

### Debug-only assertions

Compiled out in release builds (`--release`). Use for expensive invariant checks:

```rust
debug_assert!(x > 0);
debug_assert_eq!(left, right);
debug_assert_ne!(a, b);
```

## Panic behavior

- **default**: stack unwinding — destructors run, memory cleaned up
- **abort mode**: immediate process abort, no cleanup, smaller binary

Configured in `Cargo.toml`:
```toml
[profile.release]
panic = "abort"
```

## `catch_unwind`

Catches unwinding panics at a boundary. Intended for FFI (Foreign Function Interface) and test harnesses, **not** general error handling. Does NOT work with `panic = "abort"`.

```rust
use std::panic;

let result = panic::catch_unwind(|| {
    // code that might panic
    vec![1,2,3][0]
});

match result {
    Ok(val) => println!("ok: {}", val),
    Err(_)  => println!("caught a panic"),
}
```

## `#[should_panic]` in tests

```rust
#[test]
#[should_panic(expected = "divide by zero")]
fn test_divide_by_zero() {
    divide(10, 0);
}
```

## Unwrap alternatives (prefer these)

```rust
opt.unwrap_or(0)                // static default
opt.unwrap_or_else(|| compute())// lazy default
opt.unwrap_or_default()         // type's Default value
result?                         // propagate error with ? operator
```

## Best practices

- Use `Result` for anything that can legitimately fail.
- Use `expect` over `unwrap` — describe the invariant you're asserting.
- Use `assert!` for programmer invariants and tests.
- Use `debug_assert!` for expensive checks that hurt production performance.
- Document if/when a public function may panic.

## See also

- [[Option & Result]] — `?` operator, Result combinators
- [[../error_handling/Index|Error Handling]] — custom error types
