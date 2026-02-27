---
tags: [rust, basics, pattern-matching, match]
source: basics/src/matching.rs
---

# Pattern Matching

## `match`

Exhaustive — every possible case must be handled. Is an expression.

```rust
let result: &str = match number {
    1 => "one",
    2 | 3 => "two or three",        // multiple patterns with |
    4..=9 => "four to nine",        // range pattern (inclusive)
    _ => "other",                   // wildcard catches everything else
};
// ERROR: non-exhaustive match won't compile
```

## Guards

Extra condition after the pattern with `if`:

```rust
match pair {
    (x, y) if x == y    => println!("equal"),
    (x, y) if x + y < 0 => println!("negative sum"),
    _                   => println!("other"),
}
```

## `@` bindings

Binds the matched value to a name while also testing the pattern:

```rust
match val {
    n @ 10..=20 => println!("in range: {}", n),
    n @ 21..=30 => println!("in range: {}", n),
    _           => println!("out of range"),
}
```

## Destructuring in match

### Tuples
```rust
match point {
    (0, 0) => println!("origin"),
    (x, 0) => println!("x-axis at {}", x),
    (0, y) => println!("y-axis at {}", y),
    (x, y) => println!("({}, {})", x, y),
}
```

### Structs
```rust
match p {
    Point { x: 0, y: 0 } => println!("origin"),
    Point { x, y: 0 }    => println!("x-axis at {}", x),
    Point { x, y }        => println!("({}, {})", x, y),
}
```

### Enums
```rust
match msg {
    Message::Quit               => println!("quit"),
    Message::Move { x, y }     => println!("move to ({}, {})", x, y),
    Message::Write(text)        => println!("write: {}", text),
    Message::ChangeColor(r,g,b) => println!("color ({},{},{})", r, g, b),
}
```

## Ignoring values

```rust
match triple {
    (_, _, z) => println!("only z: {}", z),  // _ ignores one field
}

match quad {
    (first, .., last) => println!("{} {}", first, last),  // .. skips any number of fields
}
```

## Slice patterns

Only on `&[T]`, not arrays directly — use `.as_slice()`:

```rust
match arr.as_slice() {
    []              => println!("empty"),
    [single]        => println!("one: {}", single),
    [first, second, ..] => println!("{} {}", first, second),
    [first, .., last]   => println!("first={} last={}", first, last),
}
```

## Reference patterns

```rust
let r: &i32 = &42;
match r {
    &n => println!("{}", n),    // & in pattern peels a reference
}

match &val {
    n => println!("{}", n),     // n is &i32 here
}
```

## `if let` / `while let`

Single-pattern shortcuts — no exhaustiveness check:

```rust
if let Some(n) = opt {
    println!("{}", n);
} else {
    println!("none");
}

while let Some(top) = stack.pop() {
    print!("{} ", top);
}
```

## `let` destructuring

Pattern matching in plain `let`:

```rust
let (a, b, c): (i32, i32, i32) = (1, 2, 3);
let Point { x, y } = p;
```

## Exhaustiveness

The compiler ensures all enum variants are covered. Removing any arm on a non-`_` match of a non-exhaustive type causes a compile error.
