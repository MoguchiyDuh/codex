---
tags: [rust, basics, option, result, error-handling]
source: basics/src/option_result.rs
---

# Option & Result

## Option\<T\>

Represents a value that may or may not exist. No null pointers in Rust.

```rust
let some: Option<i32> = Some(42);
let none: Option<i32> = None;
```

### Unwrapping

```rust
some.unwrap()               // panics if None
some.unwrap_or(0)           // default if None
some.unwrap_or_else(|| 0)   // lazy default
some.expect("must exist")   // panics with custom message
```

### Transforming

```rust
some.map(|x| x * 2)                    // Some(84) — applies fn inside Some, None passes through
some.and_then(|x| if x > 10 { Some(x) } else { None })  // flatMap — avoids Option<Option<T>>
some.filter(|&x| x > 50)               // None if predicate fails
```

### Fallback

```rust
none.or(Some(999))              // Some(999)
none.or_else(|| Some(888))      // lazy fallback
```

### Option ↔ Result

```rust
some.ok_or("no value")          // Ok(42)
none.ok_or("no value")          // Err("no value")
ok_val.ok()                     // Option — Some(v) or None on Err
err_val.err()                   // Option — Some(e) or None on Ok
```

### Mutation

```rust
let mut opt = Some(5);
let taken = opt.take();         // opt becomes None, taken = Some(5)
let prev  = opt.replace(10);    // opt becomes Some(10), prev = None
```

### Transpose

```rust
let opt_result: Option<Result<i32, &str>> = Some(Ok(42));
let result_opt: Result<Option<i32>, &str> = opt_result.transpose();
// Ok(Some(42))
```

---

## Result\<T, E\>

Represents success (`Ok`) or failure (`Err`). Used for operations that can fail.

```rust
let ok:  Result<i32, &str> = Ok(100);
let err: Result<i32, &str> = Err("failed");
```

### Unwrapping

```rust
ok.unwrap()                 // panics on Err
ok.unwrap_or(0)
ok.unwrap_or_else(|_| 0)
ok.expect("should be Ok")   // panics with message on Err
```

### Transforming

```rust
ok.map(|x| x * 2)                  // Ok(200)
ok.map_err(|e| format!("Err: {}", e))   // transform the error type
ok.and_then(|x| if x > 50 { Ok(x) } else { Err("too small") })
```

### Fallback

```rust
err.or(Ok(999))
err.or_else(|_| Ok(888))
```

### `?` operator

Propagates `Err` early — equivalent to `match result { Ok(v) => v, Err(e) => return Err(e.into()) }`:

```rust
fn calculate() -> Result<f64, String> {
    let x = divide(10.0, 2.0)?;    // returns Err early if divide fails
    let y = divide(x, 5.0)?;
    return Ok(y);
}
```

The error type is converted via `From` if needed.

---

## Common patterns

```rust
// Safe division
fn safe_divide(a: i32, b: i32) -> Option<i32> {
    if b == 0 { return None; }
    return Some(a / b);
}

// Parsing with custom error
fn parse_int(s: &str) -> Result<i32, String> {
    return s.parse::<i32>().map_err(|e| format!("Parse error: {}", e));
}
```

## See also

- [[../error_handling/Index|Error Handling]] — custom error types, anyhow, thiserror
