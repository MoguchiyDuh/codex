---
tags: [rust, basics, strings, str]
source: basics/src/string_example.rs
---

# Strings

## `String` vs `&str`

| | `String` | `&str` |
|---|---|---|
| Ownership | owned, heap-allocated | borrowed slice |
| Mutability | mutable | immutable |
| Size | dynamic | fixed (known at borrow time) |
| Common source | `String::from()`, `format!()` | string literals, slices of `String` |

```rust
let owned: String = String::from("owned");
let literal: &str = "static borrow";
let slice: &str = &owned[0..3];     // borrows from String
```

Functions should take `&str` (not `&String`) — `&String` auto-derefs to `&str` anyway.

## Creation

```rust
let s = String::from("hello");
let s = "hello".to_string();
let s: String = "hello".into();
let s = String::new();                          // empty
let s = String::with_capacity(64);             // pre-allocated, avoids reallocations
```

## Appending

```rust
let mut s = String::from("Hello");
s.push_str(", world");  // appends &str
s.push('!');            // appends char
```

## Concatenation

```rust
// + takes ownership of left side (calls Add::add(self, &str))
let s3 = s1 + &s2;     // s1 moved, s2 borrowed
// s1 is now invalid

// format! borrows both, returns new String
let c = format!("{}{}", a, b);
```

## Slicing

Indices are **byte offsets**, not char indices. Must land on valid UTF-8 boundaries:

```rust
let s = String::from("hello");
let sl: &str = &s[0..2];   // "he"

// PANIC: slicing mid-codepoint
// let emoji = String::from("😀");
// let bad = &emoji[0..1];  // 😀 is 4 bytes, can't slice at 1
```

## Common methods

```rust
s.len()                     // byte count (not char count!)
s.is_empty()
s.contains("world")
s.starts_with("he")
s.ends_with("lo")
s.find("rl")                // Option<usize> — byte offset
s.rfind('o')

s.to_uppercase()
s.to_lowercase()

"  hi  ".trim()             // "hi"
"  hi  ".trim_start()       // "hi  "
"  hi  ".trim_end()         // "  hi"
"xxxhixxx".trim_matches('x')    // "hi"
```

## Splitting

```rust
"a,b,c".split(',').collect::<Vec<_>>()
"one two  three".split_whitespace().collect::<Vec<_>>()
"a\nb\nc".lines().collect::<Vec<_>>()
```

## Replacing

```rust
s.replace("old", "new")            // all occurrences
s.replacen("old", "new", 1)        // first N only
```

## Iterating

```rust
for ch in s.chars()  { }           // Unicode chars
for b  in s.bytes()  { }           // raw bytes
for (byte_offset, ch) in s.char_indices() { }
// byte_offset != char index for multi-byte chars
```

`s.len()` returns byte count. `s.chars().count()` returns char count.

## Mutation

```rust
s.push_str("more");
s.truncate(7);      // keep first 7 bytes
s.clear();
```

## Bytes ↔ String

```rust
let bytes: Vec<u8> = s.clone().into_bytes();
let back: String = String::from_utf8(bytes).unwrap();
let r: &[u8] = s.as_bytes();       // borrows — no allocation
```

## Formatting

```rust
let out = format!("{} is {} years old", name, age);
let debug = format!("{:?}", some_value);
let repeated = "ha".repeat(3);     // "hahaha"
```

## Comparison

```rust
s1 == "literal"     // String == &str works via PartialEq
s1 < s2             // lexicographic
```
