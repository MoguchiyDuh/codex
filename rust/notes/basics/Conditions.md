---
tags: [rust, basics, control-flow]
source: basics/src/conditions.rs
---

# Conditionals

## if / else if / else

Standard. No parentheses around condition.

```rust
if x > 5 {
    println!("big");
} else if x == 5 {
    println!("five");
} else {
    println!("small");
}
```

## if as expression

All branches must return the same type:

```rust
let n: i32 = if condition { 5 } else { 6 };

let category: &str = if age < 18 { "minor" }
                     else if age < 65 { "adult" }
                     else { "senior" };
```

## Logical operators

`&&`, `||`, `!`. Both `&&` and `||` short-circuit — the right side is not evaluated if the result is already determined by the left side.

```rust
false && expensive_check()  // expensive_check NOT called
true  || expensive_check()  // expensive_check NOT called
```

## if let

Combines pattern matching with a conditional. Use when you care about one variant:

```rust
if let Some(v) = some_val {
    println!("{}", v);
} else {
    println!("None");
}

if let (1, y) = tuple {
    println!("first is 1, second is {}", y);
}
```

## while let

Loop that continues as long as the pattern matches:

```rust
let mut stack = vec![1, 2, 3];
while let Some(top) = stack.pop() {
    println!("{}", top);
}
```

## See also

- [[Pattern Matching]] — `match` for exhaustive pattern dispatch
