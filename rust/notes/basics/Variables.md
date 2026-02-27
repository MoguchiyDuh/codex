---
tags: [rust, basics, variables]
source: basics/src/variables.rs
---

# Variables

## Bindings

`let` is immutable by default. `let mut` allows reassignment (same type only).

```rust
let x: i32 = 5;
// x = 6;          // ERROR: cannot assign twice to immutable variable

let mut y: i32 = 10;
y = 20;             // OK
```

## Shadowing

`let` with the same name creates a **new** binding — can even change the type:

```rust
let spaces: &str = "   ";
let spaces: usize = spaces.len();   // different type, same name — new binding

// let mut count = "123";
// count = count.len();             // ERROR: can't change type with mut
```

Shadowing in inner scopes only applies inside that scope:

```rust
let z: i32 = 5;
let z: i32 = z + 1;    // 6
{
    let z: i32 = z * 2; // 12 — only here
}
println!("{}", z);      // still 6
```

## const and static

```rust
const MAX: u32 = 100_000;      // inlined at every use, SCREAMING_SNAKE_CASE, must have type
static GLOBAL: i32 = 42;       // single memory address, lives for entire program ('static)
// static mut DANGER: i32 = 0; // requires unsafe to access — UB (Undefined Behavior) if multi-threaded
```

`const` vs `static`: const is inlined (like a `#define`), static has one memory location.

## Destructuring

```rust
let (a, b, c): (i32, f64, char) = (500, 6.4, 'A');
let (first, _, third): (i32, f64, char) = tuple;    // _ ignores a field

let [x1, x2, x3]: [i32; 3] = [1, 2, 3];

struct Point { x: i32, y: i32 }
let Point { x: px, y: py } = p;
let Point { x, y } = p;        // shorthand when names match
```

## Patterns in let

```rust
if let Some(value) = opt {      // pattern match in conditional
    println!("{}", value);
}

let r: &i32 = &50;
let &deref_val = r;             // & in pattern position peels one reference layer
```

## Misc

```rust
let _unused: i32 = 42;     // _ prefix suppresses unused variable warning
```

Type inference defaults: integer literals → `i32`, float literals → `f64`.
