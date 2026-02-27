---
tags: [rust, basics, types]
source: basics/src/data_types.rs
---

# Data Types

## Integers

| Signed | Unsigned | Size |
|--------|----------|------|
| `i8` | `u8` | 8-bit |
| `i16` | `u16` | 16-bit |
| `i32` | `u32` | 32-bit (default) |
| `i64` | `u64` | 64-bit |
| `i128` | `u128` | 128-bit |
| `isize` | `usize` | pointer-sized (platform-dependent) |

`usize` is used for indexing and collection sizes. `isize`/`usize` are 64-bit on 64-bit platforms.

## Floats

`f32` and `f64` (default). Both implement `PartialEq` but NOT `Eq` because `NaN != NaN` — a rule from IEEE 754 (the international floating-point standard).

```rust
let nan: f64 = f64::NAN;
nan.is_nan()        // true — never use == to check NaN
f64::INFINITY
f64::NEG_INFINITY
```

## Bool

1 byte. `true` / `false`. No implicit int conversion.

## Char

4 bytes — Unicode scalar value (U+0000..=U+10FFFF). **Not** a UTF-8 (Unicode Transformation Format 8-bit) byte.

```rust
let emoji: char = '😀';   // 4 bytes, valid char
```

## Tuples

Fixed-size, heterogeneous. Access via `.0`, `.1`, etc., or destructure.

```rust
let t: (i32, f64, bool) = (42, 3.14, true);
let (a, b, c) = t;
let unit: () = ();      // unit type — zero-sized, used as "nothing" return value
```

## Arrays

Fixed size, same type. Stack-allocated.

```rust
let arr: [i32; 5] = [1, 2, 3, 4, 5];
let zeros: [i32; 3] = [0; 3];      // repeat syntax
```

## Numeric literals

```rust
let decimal  = 98_222;      // _ separators for readability
let hex      = 0xff;
let octal    = 0o77;
let binary   = 0b1111_0000;
let byte: u8 = b'A';        // ASCII (American Standard Code for Information Interchange) byte literal
```

## Overflow handling

Debug mode panics on overflow; release mode wraps. Use explicit methods instead:

```rust
255_u8.wrapping_add(1)      // 0   — wraps
255_u8.checked_add(1)       // None
255_u8.saturating_add(1)    // 255 — clamps at MAX
255_u8.overflowing_add(1)   // (0, true)
```

## Type aliases

```rust
type Kilometers = i32;
let d: Kilometers = 100;    // same as i32 at runtime, just a label
```

## Sizes

```rust
std::mem::size_of::<i32>()      // 4
std::mem::size_of::<char>()     // 4
std::mem::size_of::<&str>()     // 16 (fat pointer: ptr + len)
```
