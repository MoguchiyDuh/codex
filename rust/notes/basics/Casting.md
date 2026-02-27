---
tags: [rust, basics, casting, conversion]
source: basics/src/casting.rs
---

# Casting & Conversion

## `as` casting (numeric)

Primitive, lossy, never fails at runtime. Always truncates/reinterprets bits.

```rust
let i: i8 = -1;
let u: u8 = i as u8;       // 255 — bit reinterpret (-1i8 = 0xFF)

let f: f64 = 3.9999;
let t: i32 = f as i32;     // 3 — truncates (not rounds)

let big: u16 = 256;
let small: u8 = big as u8; // 0 — wraps
```

`as` between same-size types reinterprets bits; narrowing truncates/wraps.

## `TryInto` / `TryFrom` (checked)

Returns `Result`, won't silently lose data:

```rust
use std::convert::TryInto;

let big: i32 = 300;
let checked: Result<i8, _> = big.try_into();    // Err — 300 doesn't fit i8
let ok: Result<i8, _> = 100_i32.try_into();     // Ok(100)
```

## `From` / `Into` (infallible widening)

Implementing `From<T>` auto-generates `Into<U>`. These are guaranteed not to lose data.

```rust
let x: u32 = u32::from(42_u8);     // explicit
let y: u64 = 42_u8.into();         // implicit via Into
```

Only defined for lossless conversions (e.g. `u8 → u32`, not `u32 → u8`).

## String parsing

```rust
let n: i32 = "12345".parse().expect("parse i32");
let f: f64 = "3.14".parse().expect("parse f64");

let bad: Result<i32, _> = "abc".parse();    // Err
```

## To string

```rust
let s: String = 42_i32.to_string();
let hex: String = format!("{:#x}", 255);    // "0xff"
```

## Char ↔ integer

```rust
let b: u8  = 'A' as u8;        // 65
let c: char = 65_u8 as char;   // 'A'
let u: u32 = '😀' as u32;      // 128512
```

## Bool → integer

```rust
true  as i32    // 1
false as i32    // 0
```

No reverse: `0 as bool` doesn't compile.

## Bitwise reinterpretation (floats)

```rust
let bits: u32 = 1.5_f32.to_bits();
let back: f32 = f32::from_bits(bits);
```

## Byte arrays ↔ integers

```rust
let arr: [u8; 4] = [1, 2, 3, 4];
let le: u32 = u32::from_le_bytes(arr);
let be: u32 = u32::from_be_bytes(arr);

let back: [u8; 4] = le.to_le_bytes();
```

## String ↔ bytes

```rust
let bytes: &[u8] = "hello".as_bytes();
let s: &str = std::str::from_utf8(bytes).unwrap();         // fails on invalid UTF-8
let lossy = String::from_utf8_lossy(&bytes);               // Cow<str>, replaces invalid bytes with U+FFFD
let s: String = String::from_utf8(bytes.to_vec()).unwrap();
// PANIC: from_utf8 panics if bytes aren't valid UTF-8

let raw: String = unsafe { String::from_utf8_unchecked(bytes.to_vec()) }; // UB (Undefined Behavior) if invalid
```

## FFI (Foreign Function Interface) types

```rust
use std::ffi::{CString, CStr, OsString, OsStr};

// OsString/OsStr — platform-native strings (may not be UTF-8 on Windows)
let os: OsString = OsString::from("path");
let s: Option<&str> = os.to_str();     // None if not valid UTF-8

// CString/CStr — null-terminated, for C FFI (Foreign Function Interface)
let c = CString::new("hello C").unwrap();
let r: &str = c.as_c_str().to_str().unwrap();
```

## Raw pointer casting

```rust
let r: &i32 = &42;
let ptr: *const i32 = r as *const i32;
let back: &i32 = unsafe { &*ptr };
```
