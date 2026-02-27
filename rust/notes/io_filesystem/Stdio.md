---
tags:
  - rust
  - io
  - stdio
source: io_filesystem/src/stdio.rs
---

# Standard I/O

`std::io` exposes three standard streams as functions returning handles: `io::stdin()`, `io::stdout()`, `io::stderr()`. All three implement the `Read`/`Write` traits and are internally mutex-guarded for thread safety.

## stdout

```rust
use std::io::{self, Write};

// Low-level: write bytes directly
let mut out = io::stdout();
out.write_all(b"hello\n")?;
out.flush()?;

// Macro layer (most common)
print!("no newline");
println!("with newline");
```

stdout is **line-buffered** when connected to a terminal, **block-buffered** when redirected to a pipe or file. This means `print!` with no newline may not appear immediately — call `io::stdout().flush()?` after it.

```rust
print!("Enter value: ");
io::stdout().flush()?;  // show prompt before blocking on input
```

## stderr

stderr is **unbuffered** — writes appear immediately regardless of redirection.

```rust
let mut err = io::stderr();
err.write_all(b"error\n")?;

// Macros
eprint!("no newline to stderr");
eprintln!("with newline to stderr");
```

Use stderr for diagnostics, errors, and progress output that should not be captured by `> file`.

## stdin

stdin reads block until input is available. `read_line` appends a newline-terminated line into a `String`:

```rust
let mut input = String::new();
io::stdin().read_line(&mut input)?;
let trimmed = input.trim();  // strips the trailing '\n'
```

### Parsing input

```rust
let mut input = String::new();
io::stdin().read_line(&mut input)?;

let n: i32 = input.trim().parse()
    .map_err(|e| io::Error::new(io::ErrorKind::InvalidInput, e))?;
```

### Locked handle

`.lock()` acquires the mutex for the duration of the guard, avoiding repeated locking overhead when reading many lines:

```rust
let stdin = io::stdin();
let handle = stdin.lock();  // StdinLock<'_>

for line in handle.lines() {
    println!("{}", line?);
}
```

`StdinLock` implements `BufRead`, giving access to `.lines()` and `.read_line()`.

### Reading until EOF

```rust
let mut all = String::new();
io::stdin().read_to_string(&mut all)?;  // blocks until Ctrl+D (Unix) / Ctrl+Z (Windows)
```

## Formatting Output

`println!` and `write!` use the same format syntax:

```rust
let v = 42i32;
println!("{}", v);    // decimal
println!("{:x}", v);  // hex
println!("{:b}", v);  // binary
println!("{:05}", v); // zero-padded to width 5
```

## Terminal Detection

`IsTerminal::is_terminal()` detects whether a stream is connected to a real terminal versus being piped or redirected. Useful for deciding whether to emit ANSI color codes:

```rust
use std::io::IsTerminal;

if io::stdout().is_terminal() {
    print!("\x1b[32mgreen text\x1b[0m");
} else {
    print!("plain text");
}
```

## File Descriptors and Redirection

| Shell syntax | Effect |
|---|---|
| `prog > out.txt` | stdout (fd 1) to file |
| `prog 2> err.txt` | stderr (fd 2) to file |
| `prog < in.txt` | stdin (fd 0) from file |
| `prog \| other` | stdout piped to next program's stdin |

Rust code does not need to do anything special for these to work — the OS handles fd redirection before the process starts.

## Reading Space-Separated Values

Common competitive-programming pattern:

```rust
let mut line = String::new();
io::stdin().read_line(&mut line)?;
let nums: Vec<i32> = line.split_whitespace()
    .filter_map(|s| s.parse().ok())
    .collect();
```

## Related Notes

- [[File IO]] — the same `Read`/`Write` traits applied to files
- [[Process]] — spawning child processes and piping their stdio
