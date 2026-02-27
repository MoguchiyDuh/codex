---
tags: [rust, basics, formatting, macros]
source: basics/src/printing.rs
---

# Printing & Formatting

## Basic macros

```rust
println!("with newline");
print!("no newline");
eprintln!("to stderr");
format!("returns String")   // doesn't print
```

## Format arguments

```rust
println!("{} is {} years old", name, age);          // positional
println!("{0} and {0} again, then {1}", a, b);      // index
println!("{name} is {age}", name = "Bob", age = 25); // named
```

## Display vs Debug

```rust
println!("{}", val);    // Display — user-facing, implement fmt::Display
println!("{:?}", val);  // Debug — developer-facing, derive or implement fmt::Debug
println!("{:#?}", val); // pretty Debug (indented)
```

`Vec`, `HashMap`, etc. implement `Debug` but not `Display`.

## Number formats

```rust
println!("{}", 255);    // 255
println!("{:x}", 255);  // ff
println!("{:X}", 255);  // FF
println!("{:#x}", 255); // 0xff
println!("{:o}", 255);  // 377
println!("{:b}", 255);  // 11111111
println!("{:#b}", 255); // 0b11111111
```

## Float precision

```rust
println!("{:.2}", 3.14159);     // 3.14
println!("{:.5}", 3.14159);     // 3.14159
println!("{:e}", 3.14159);      // 3.14159e0
```

## Width & alignment

```rust
println!("{:10}",   "hi");  // "hi        " (right-padded to 10)
println!("{:<10}",  "hi");  // "hi        " (left-align)
println!("{:>10}",  "hi");  // "        hi" (right-align)
println!("{:^10}",  "hi");  // "    hi    " (center)
println!("{:*^10}", "hi");  // "****hi****" (custom fill char)
```

## Padding numbers

```rust
println!("{:5}",  42);  // "   42"
println!("{:05}", 42);  // "00042"
println!("{:+}",  42);  // "+42" (force sign)
```

## Combining

```rust
println!("{:10.2}", 12.3456);   // "     12.35"
println!("{:08.2}", 12.3456);   // "00012.35"
```

## Dynamic width/precision

```rust
println!("{:width$}",     "hi", width = 10);
println!("{:.precision$}", 3.14, precision = 3);
```

## Escape braces

```rust
println!("literal: {{}}");          // literal: {}
println!("{{{}}}", 42);             // {42}
```

## Pointer

```rust
let x = 42;
println!("{:p}", &x);   // 0x7fff...
```

## Custom Display

```rust
struct Point { x: i32, y: i32 }

impl std::fmt::Display for Point {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        return write!(f, "({}, {})", self.x, self.y);
    }
}

println!("{}", Point { x: 1, y: 2 });  // (1, 2)
```

## `write!` / `writeln!` to buffers

```rust
use std::fmt::Write;
let mut buf = String::new();
write!(&mut buf, "Hello {}", "world").unwrap();
```

## `dbg!` macro

Prints file, line, expression, and value to **stderr**. Returns the value (borrows it):

```rust
let result = dbg!(2 + 3);  // [src/main.rs:5] 2 + 3 = 5
dbg!(&vec);                // borrow to avoid moving
```
