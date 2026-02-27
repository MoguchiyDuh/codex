---
tags: [rust, basics, functions, closures]
source: basics/src/functions.rs
---

# Functions

## Basics

```rust
fn add(a: i32, b: i32) -> i32 {
    return a + b;
}

fn swap(a: i32, b: i32) -> (i32, i32) {
    return (b, a);     // multiple return via tuple
}
```

All parameters and return types must be explicitly annotated. No implicit returns (we use `return`).

## Optional parameters

Rust has no default arguments. Use `Option<T>`:

```rust
fn greet(title: Option<&str>, name: &str) -> String {
    if let Some(t) = title {
        return format!("{} {}", t, name);
    }
    return name.to_string();
}
```

## Variadic-like: slices

```rust
fn sum_all(nums: &[i32]) -> i32 {
    let mut total = 0;
    for &n in nums { total += n; }
    return total;
}

sum_all(&[1, 2, 3, 4, 5]);
```

## `const fn`

Evaluated at compile time when used in a `const` context. Result is baked into the binary.

```rust
const fn factorial(n: u32) -> u32 {
    if n == 0 { return 1; }
    return n * factorial(n - 1);
}

const FACTORIAL_5: u32 = factorial(5);  // zero runtime cost
```

## Methods and associated functions

```rust
struct Rectangle { width: u32, height: u32 }

impl Rectangle {
    fn new(w: u32, h: u32) -> Self { Self { width: w, height: h } }  // associated fn (no self)
    fn square(s: u32) -> Self { Self::new(s, s) }

    fn area(&self) -> u32 { self.width * self.height }                // immutable method
    fn scale(&mut self, factor: u32) { self.width *= factor; }        // mutable method
}
```

Associated functions (no `self`) are called with `::`. Methods are called with `.`.

## Generic functions

```rust
fn max_generic<T: PartialOrd>(a: T, b: T) -> T {
    if a > b { return a; }
    return b;
}

fn print_debug<T: std::fmt::Debug>(value: T) {
    println!("{:?}", value);
}
```

## Higher-order functions

### Function pointers

`fn(i32, i32) -> i32` — plain address, no captured state, always `Copy`.

```rust
fn operation(a: i32, b: i32, op: fn(i32, i32) -> i32) -> i32 {
    return op(a, b);
}
operation(10, 5, add);
```

### Closure bounds

```rust
fn apply<F: Fn(i32) -> i32>(f: F, value: i32) -> i32 {
    return f(value);
}
apply(|x| x * 2, 10);
```

## Closures

```rust
let add_five = |x: i32| -> i32 { return x + 5; };
```

### Capture modes

| Trait | Captures | Call count |
|-------|----------|------------|
| `Fn` | `&T` (immutable borrow) | any number |
| `FnMut` | `&mut T` (mutable borrow) | any number |
| `FnOnce` | `T` (moves value in) | once |

Every `Fn` is also `FnMut` and `FnOnce` (subtrait hierarchy).

```rust
// FnMut — borrows mutably
let mut counter = 0;
let mut inc = || { counter += 1; counter };
inc(); inc();

// FnOnce — moves value in, consumed on call
let text = String::from("consumed");
let consume = move || println!("{}", text);
consume();  // text dropped here
```

`move` keyword forces capture by move even if the closure would otherwise borrow.

## Diverging functions (`!`)

The never type `!` coerces to any type, so it can appear in any branch position:

```rust
fn panic_example() -> ! {
    panic!("never returns");
}

let result: i32 = if condition { panic_example() } else { 42 };
```
