---
tags:
  - rust
  - macros
  - stdlib
source: macros/src/built_in.rs
---

# Built-in Macros

Standard library and compiler-provided macros. These are always in scope — no import needed.

## Formatting

| Macro | Target | Newline |
|---|---|---|
| `print!` | stdout | No |
| `println!` | stdout | Yes |
| `eprint!` / `eprintln!` | stderr | No / Yes |
| `format!` | Returns `String` | — |

```rust
let s: String = format!("value: {}", 42);
eprintln!("debug: something went wrong");
```

## Assertions

`assert!`, `assert_eq!`, `assert_ne!` — panic immediately on failure. All accept an optional format string for a custom message:

```rust
assert!(1 + 1 == 2);
assert_eq!(2 + 2, 4);
assert_ne!(2 + 2, 5);
assert!(condition, "failed because: {}", reason);
```

`debug_assert*` variants are identical but compiled out in `--release` builds — zero cost in production:

```rust
debug_assert!(1 < 2);
debug_assert_eq!(3 * 3, 9);
debug_assert_ne!(0, 1);
```

## dbg!

Prints `[file:line] expr = value` to stderr and returns the value unchanged. Useful for inline inspection without restructuring code:

```rust
let x: i32 = 5;
let y: i32 = dbg!(x * 2) + 1; // stderr: [src/main.rs:2] x * 2 = 10
                               // y = 11

let v: Vec<i32> = dbg!(vec![1, 2, 3]); // also works on owned values
```

## Placeholder Panics

Used to mark code that isn't finished yet or that should never be reached:

```rust
fn in_progress() -> i32 {
    todo!("implement this later")        // panics: "not yet implemented: ..."
}

fn not_supported() -> i32 {
    unimplemented!("this variant is not supported") // panics: "not implemented: ..."
}

let _parity = match n % 2 {
    0 => "even",
    1 => "odd",
    _ => unreachable!("modulo 2 is always 0 or 1"), // signals impossible branch
};
```

`unreachable!` is also an optimization hint — the compiler may use it to eliminate dead code.

## matches!

Expands to a `match` expression returning `bool`. Supports guards and `|` patterns:

```rust
let val: Option<i32> = Some(42);
let is_positive: bool = matches!(val, Some(x) if x > 0); // true

let color: &str = "red";
let is_warm: bool = matches!(color, "red" | "orange" | "yellow"); // true
```

Cleaner than writing a full `match` or `if let` just to get a boolean.

## write! and writeln!

Write formatted output into any type implementing a `Write` trait. Two distinct traits exist:

- `std::fmt::Write` — for in-memory targets like `String`
- `std::io::Write` — for byte stream targets like `Vec<u8>` or files

Both must be imported. If both are needed, alias them to avoid the name collision:

```rust
use std::fmt::Write as FmtWrite;
use std::io::Write as IoWrite;

let mut buf = String::new();
write!(buf, "hello ").unwrap();
writeln!(buf, "world {}", 42).unwrap();

let mut bytes: Vec<u8> = Vec::new();
write!(bytes, "binary data: {}", 255).unwrap();
```

## Compile-Time Environment

### env! and option_env!

Read environment variables at compile time, not runtime:

```rust
let pkg: &str = env!("CARGO_PKG_NAME");    // panics at build if var is missing
let ver: &str = env!("CARGO_PKG_VERSION");

let maybe: Option<&str> = option_env!("OPTIONAL_VAR"); // None if missing, no panic
```

Useful for embedding crate metadata or secrets that must exist at build time.

### file!, line!, column!, module_path!

Emit the source location as string/integer literals, resolved at compile time:

```rust
println!("file!()        = {}", file!());        // "src/built_in.rs"
println!("line!()        = {}", line!());        // line number
println!("column!()      = {}", column!());      // column number
println!("module_path!() = {}", module_path!()); // "macros::built_in"
```

## concat! and stringify!

- `concat!` — joins string literal arguments into a single `&'static str` at compile time
- `stringify!` — converts its token stream argument to a `&'static str` without evaluating it

```rust
let s: &str = concat!("Hello", ", ", "world", "!"); // "Hello, world!"
let t: &str = stringify!(1 + 2 * 3);                // "1 + 2 * 3" (not "7")
```

See [[Declarative Macros]] for `stringify!` usage inside macro definitions.

## cfg!

Evaluates a configuration predicate at compile time and returns a `bool`. Unlike `#[cfg(...)]` which conditionally compiles entire items, `cfg!()` works inside expressions:

```rust
let is_debug: bool = cfg!(debug_assertions);
let is_unix:  bool = cfg!(target_family = "unix");
let is_64bit: bool = cfg!(target_pointer_width = "64");
```

## vec!

Two forms: list initialization and repeat initialization:

```rust
let v1: Vec<i32> = vec![1, 2, 3];
let v2: Vec<i32> = vec![0; 10]; // ten zeros
```

`vec![val; n]` calls `Clone` on `val` — the element type must implement `Clone`.

## include Family

Embed external files at compile time, relative to the current source file:

| Macro | Result type | Use |
|---|---|---|
| `include!("file.rs")` | (source code) | Embed `.rs` as source |
| `include_str!("file.txt")` | `&'static str` | Embed text content |
| `include_bytes!("file.bin")` | `&'static [u8]` | Embed binary content |

All paths are resolved at compile time. Missing files are build errors.

## compile_error!

Emits a hard compiler error with a custom message. Primarily used inside `#[cfg(...)]` guards to give useful errors on unsupported platforms:

```rust
#[cfg(not(any(target_os = "linux", target_os = "macos")))]
compile_error!("Only Linux and macOS are supported");
```

## Related Notes

- [[Declarative Macros]]
- [[Advanced Macros]]
