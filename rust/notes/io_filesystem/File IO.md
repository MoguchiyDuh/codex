---
tags:
  - rust
  - io
  - filesystem
source: io_filesystem/src/file_io.rs
---

# File I/O

Core file operations live in `std::fs` (convenience functions) and `std::io` (traits and buffered wrappers). The two layers are distinct: `std::fs::read_to_string` is a one-shot helper; `std::io::Read` is a trait that any type can implement.

## Opening Files

`File::create` truncates or creates. For fine-grained control use `OpenOptions`:

```rust
use std::fs::{File, OpenOptions};

// Create or truncate
let mut file = File::create("out.txt")?;

// Builder pattern — explicit about every flag
let mut file = OpenOptions::new()
    .read(true)
    .write(true)
    .create(true)
    .truncate(false)   // don't wipe existing content
    .open("file.txt")?;

// Append-only
let mut file = OpenOptions::new().append(true).open("log.txt")?;
```

`append(true)` implies `write(true)` and seeks to EOF before every write — it's atomic on POSIX for small writes.

## Reading

### One-shot helpers

```rust
let text: String = std::fs::read_to_string("file.txt")?;  // UTF-8 or error
let bytes: Vec<u8> = std::fs::read("file.txt")?;           // raw bytes, never fails on encoding
```

### `Read` trait methods

Any type that implements `Read` exposes:

| Method | Behaviour |
|---|---|
| `read(&mut buf)` | Fills up to `buf.len()` bytes; returns count actually read |
| `read_exact(&mut buf)` | Errors unless exactly `buf.len()` bytes are read |
| `read_to_end(&mut vec)` | Appends until EOF |
| `read_to_string(&mut s)` | Like `read_to_end` but validates UTF-8 |

```rust
let mut file = File::open("file.txt")?;
let mut buf = [0u8; 10];
let n = file.read(&mut buf)?;        // n ≤ 10
file.read_exact(&mut buf)?;          // exactly 10 or Err
```

### `BufReader` — why it matters

Every `read_line` call on a raw `File` issues a syscall. `BufReader` wraps any `Read` in an 8 KB in-process buffer, batching syscalls.

```rust
use std::io::{BufRead, BufReader};

let reader = BufReader::new(File::open("file.txt")?);

// Iterator over lines (strips newline, propagates errors via Result)
for line in reader.lines() {
    println!("{}", line?);
}

// Manual: read_line appends into a reusable String
let mut reader = BufReader::new(File::open("file.txt")?);
let mut line = String::new();
let bytes = reader.read_line(&mut line)?;
```

`BufReader<File>` implements `BufRead`, which adds `.lines()` and `.read_line()` on top of `Read`.

## Writing

### `Write` trait methods

```rust
file.write(b"Hello")?;          // returns bytes written (may be short)
file.write_all(b"Hello")?;      // retries until all bytes written or error
writeln!(file, "val={}", 42)?;  // format macro, adds newline
write!(file, "no newline")?;
```

### `BufWriter`

Mirrors `BufReader` but for writes — accumulates data in memory and flushes in larger chunks.

```rust
use std::io::BufWriter;

let mut writer = BufWriter::new(File::create("out.txt")?);
for i in 0..1000 {
    writeln!(writer, "line {}", i)?;
}
writer.flush()?;  // must flush manually; drop also flushes but silently swallows errors
```

Always call `.flush()` explicitly if the result matters — the `Drop` impl flushes but ignores errors.

## Seeking

Requires `std::io::Seek` in scope. `SeekFrom` has three variants:

```rust
use std::io::{Seek, SeekFrom};

file.seek(SeekFrom::Start(0))?;      // absolute offset from beginning
file.seek(SeekFrom::Current(5))?;    // +5 from current cursor position
file.seek(SeekFrom::End(-5))?;       // 5 bytes before EOF

let pos: u64 = file.stream_position()?;  // current offset
file.rewind()?;                           // shorthand for SeekFrom::Start(0)
```

Seeking is only valid on types that actually support random access (like `File`). Sockets and pipes do not implement `Seek`.

## Metadata and Handle Cloning

```rust
let metadata = file.metadata()?;
println!("{} bytes, read-only: {}", metadata.len(), metadata.permissions().readonly());

// try_clone shares the OS file descriptor — both handles share the same cursor position
let mut clone = file.try_clone()?;
```

## Error Handling

`io::Error` carries both a human-readable message and a machine-readable `ErrorKind`:

```rust
match File::open("missing.txt") {
    Ok(f)  => { /* use f */ }
    Err(e) => println!("{} ({:?})", e, e.kind()),  // e.g. NotFound
}
```

## Related Notes

- [[Paths]] — constructing and decomposing file paths
- [[Directories]] — listing and walking directory trees
- [[Advanced]] — atomic writes, permissions, hard links, symlinks
