---
tags: [rust, basics, lifetimes, borrowing]
source: basics/src/lifetimes.rs
---

# Lifetimes

Lifetimes are compile-time annotations that tell the borrow checker how long references are valid. They prevent dangling references — no runtime cost.

## Why lifetimes exist

When a function takes multiple references and returns one, the compiler needs to know which input the output reference borrows from:

```rust
// 'a means: return value lives at least as long as the shorter of x and y
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { return x; }
    return y;
}
```

Without `'a`, the compiler can't verify the returned reference won't outlive its source.

## Multiple lifetime parameters

When inputs don't need to outlive each other, use separate lifetimes:

```rust
fn starts_with<'a, 'b>(text: &'a str, prefix: &'b str) -> bool {
    return text.starts_with(prefix);
}
```

## Lifetimes in structs

A struct holding a reference must annotate that it can't outlive the referenced data:

```rust
struct Excerpt<'a> {
    part: &'a str,      // Excerpt cannot outlive the &str it holds
}

impl<'a> Excerpt<'a> {
    fn announce(&self, msg: &str) -> i32 {  // elided: &self lifetime
        println!("{}", msg);
        return self.part.len() as i32;
    }
}
```

## Lifetime elision

The compiler infers lifetimes in common patterns so you don't have to write them:

1. Each input reference gets its own lifetime.
2. If there's exactly one input reference, its lifetime is assigned to all output references.
3. If one input is `&self` or `&mut self`, its lifetime is assigned to all output references.

```rust
// Written:   fn first_word(s: &str) -> &str
// Expanded:  fn first_word<'a>(s: &'a str) -> &'a str
fn first_word(s: &str) -> &str {
    return s.split_whitespace().next().unwrap_or("");
}
```

## `'static` lifetime

Reference valid for the entire program duration. String literals are `'static`:

```rust
let s: &'static str = "I live in the binary";

// Box::leak intentionally leaks heap memory to get &'static str at runtime
let leaked: &'static str = Box::leak(Box::new(String::from("runtime static")));
```

## Generic lifetimes with traits

```rust
fn longest_with_ann<'a, T: std::fmt::Display>(x: &'a str, y: &'a str, ann: T) -> &'a str {
    println!("{}", ann);
    if x.len() > y.len() { return x; }
    return y;
}
```

## Lifetime subtyping

The borrow checker verifies that referenced data outlives all borrows of it:

```rust
let outer = String::from("outer");
{
    let inner = String::from("inner");
    let longer = longest(&outer, &inner);
    println!("{}", longer);     // OK: inner still alive here
}                               // inner dropped, but longer's scope ended too
```

## Common compile errors

```rust
// ERROR: returning reference to local variable
// fn dangle() -> &str {
//     let s = String::from("hello");
//     &s          // s dropped at end of fn
// }

// ERROR: borrowed value does not live long enough
// let r: &str;
// {
//     let s = String::from("temp");
//     r = &s;     // s dropped before r is used
// }
// println!("{}", r);
```

## See also

- [[Ownership & Borrowing]] — the underlying ownership model
- [[../smart_pointers/Index|Smart Pointers]] — Rc/Arc for when lifetimes are too restrictive
