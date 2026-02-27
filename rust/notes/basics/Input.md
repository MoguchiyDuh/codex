---
tags: [rust, basics, io, stdin]
source: basics/src/input.rs
---

# Standard Input

## Reading a line

```rust
use std::io;

let mut input = String::new();
io::stdin().read_line(&mut input).unwrap();
let trimmed = input.trim();     // removes trailing \n / \r\n
```

`read_line` appends to the buffer — always start with a fresh `String::new()`.

## Parsing

```rust
let n: i32 = input.trim().parse().expect("expected integer");
let f: f64 = input.trim().parse().unwrap_or(0.0);

// Handle error explicitly
match input.trim().parse::<i32>() {
    Ok(n)  => println!("got {}", n),
    Err(e) => println!("bad input: {}", e),
}
```

## Multiple values on one line

```rust
let parts: Vec<&str> = line.trim().split_whitespace().collect();
let numbers: Vec<i32> = parts.iter().filter_map(|s| s.parse().ok()).collect();

// Destructure fixed count
let (a, b, c): (i32, i32, i32) = (
    parts.get(0).and_then(|s| s.parse().ok()).unwrap_or(0),
    parts.get(1).and_then(|s| s.parse().ok()).unwrap_or(0),
    parts.get(2).and_then(|s| s.parse().ok()).unwrap_or(0),
);
```

## Multiple lines (BufReader)

```rust
use std::io::{BufRead, BufReader};

let reader = BufReader::new(io::stdin());
for line in reader.lines() {
    let line = line.unwrap();
    // process line
}
```

`BufReader` is more efficient than calling `read_line` in a loop — it batches syscalls.

## Read all stdin to string

```rust
use std::io::Read;
let mut buffer = String::new();
io::stdin().read_to_string(&mut buffer).unwrap();
```

## stdout / stderr

```rust
use std::io::Write;

print!("no newline");
io::stdout().flush().unwrap();  // flush needed after print! before reading input

eprintln!("stderr message");

let mut stdout = io::stdout();
write!(stdout, "write macro").unwrap();
writeln!(stdout, "writeln macro").unwrap();
```

## Command-line arguments

```rust
let args: Vec<String> = std::env::args().collect();
// args[0] = program path
// args[1..] = user-provided args

let first_arg = std::env::args().nth(1);  // Option<String>
```

For complex arg parsing, see the `clap` example in `argparse.rs`.

## Input validation pattern

```rust
fn validate_positive(input: &str) -> Result<i32, String> {
    let n: i32 = input.trim().parse().map_err(|_| "not a number".to_string())?;
    if n <= 0 {
        return Err("must be positive".to_string());
    }
    return Ok(n);
}
```

## Key-value parsing

```rust
for part in "name:John age:30".split_whitespace() {
    let kv: Vec<&str> = part.split(':').collect();
    if kv.len() == 2 {
        println!("{}={}", kv[0], kv[1]);
    }
}
```
