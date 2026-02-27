---
tags:
  - rust
  - io
  - filesystem
source: io_filesystem/src/paths.rs
---

# Paths

Rust's path types mirror the `str`/`String` split: `Path` is a borrowed, unsized slice; `PathBuf` is the owned, heap-allocated version.

```
Path   : &str   (borrowed, unsized — always used behind a reference)
PathBuf: String (owned, growable)
```

## Creating Paths

```rust
use std::path::{Path, PathBuf};

let borrowed: &Path = Path::new("/usr/local/bin");
let owned: PathBuf = PathBuf::from("/usr/local/bin");
```

`Path::new` is free — it just reinterprets a `&str` (or `&OsStr`) as a `&Path`. No allocation.

## Building Paths

```rust
// push mutates in place
let mut base = PathBuf::from("/home/user");
base.push("documents");
base.push("file.txt");   // /home/user/documents/file.txt

// join returns a new PathBuf (chainable, non-mutating)
let full = Path::new("/home/user").join("documents").join("file.txt");
```

Pushing an absolute path replaces everything before it — same behaviour as Python's `os.path.join`.

### Collecting from parts

`PathBuf` implements `FromIterator`, so you can build from a slice:

```rust
let parts = vec!["home", "user", "documents", "file.txt"];
let path: PathBuf = parts.iter().collect();  // joined with OS separator
```

## Decomposing Paths

```rust
let path = Path::new("/home/user/documents/file.txt");

path.parent()      // Some("/home/user/documents")
path.file_name()   // Some("file.txt")      — OsStr
path.file_stem()   // Some("file")          — OsStr, no extension
path.extension()   // Some("txt")           — OsStr
```

All return `Option` because not every path has each component (e.g. `/` has no parent).

### Changing components in place

```rust
let mut p = PathBuf::from("document.txt");
p.set_extension("md");              // document.md
p.set_file_name("readme.md");      // readme.md (replaces entire filename)
p.pop();                            // removes last component
```

## Iterating Structure

### Components

```rust
use std::path::Component;

for component in Path::new("/home/user/file.txt").components() {
    match component {
        Component::RootDir      => println!("Root"),
        Component::Normal(name) => println!("{}", name.to_string_lossy()),
        _                       => {}
    }
}
```

### Ancestors

```rust
for ancestor in Path::new("/home/user/file.txt").ancestors() {
    println!("{}", ancestor.display());
}
// /home/user/file.txt
// /home/user
// /home
// /
```

## Querying the Filesystem

These methods hit the OS (filesystem calls):

```rust
let p = Path::new(".");
p.exists()       // true if path resolves to anything
p.is_file()      // true if regular file
p.is_dir()       // true if directory
p.is_absolute()  // purely lexical, no syscall
p.is_relative()  // purely lexical, no syscall
```

### Canonicalize

Resolves symlinks and `..` components into an absolute path. Fails if the path does not exist.

```rust
let canonical: PathBuf = Path::new(".").canonicalize()?;
```

## String Conversion

Paths are not guaranteed to be valid UTF-8 on Linux — filenames are arbitrary byte sequences.

| Method | Returns | Behaviour on non-UTF-8 |
|---|---|---|
| `.to_str()` | `Option<&str>` | `None` if not valid UTF-8 |
| `.to_string_lossy()` | `Cow<str>` | Borrows if valid UTF-8; allocates with U+FFFD replacements otherwise |
| `.display()` | `Display` impl | Use only for human output, not round-tripping |

```rust
let s: Cow<str> = path.to_string_lossy();  // always succeeds
if let Some(s) = path.to_str() { /* guaranteed valid UTF-8 */ }
```

## Prefix / Suffix Checks

```rust
path.starts_with("/home")        // component-aware prefix check
path.ends_with("file.txt")       // component-aware suffix check
path.strip_prefix("/home/user")  // returns relative path or Err
```

These are component-aware, not raw string comparisons — `/home/user2` does not start with `/home/user`.

## Path Comparison

`Path` implements `PartialEq` with byte-level comparison (case-sensitive on Linux, case-insensitive on Windows via the OS layer):

```rust
Path::new("/a/b") == Path::new("/a/b")  // true
```

## Converting Between `Path` and `PathBuf`

```rust
let borrowed: &Path = Path::new("file.txt");
let owned: PathBuf  = borrowed.to_path_buf();  // clones
let back: &Path     = owned.as_path();         // borrow, zero-cost
```

## Platform Separator

```rust
std::path::MAIN_SEPARATOR  // '/' on Unix, '\\' on Windows
```

Avoid hardcoding `/` in path construction — use `push`/`join` instead.

## Related Notes

- [[File IO]] — opening and reading files using paths
- [[Directories]] — listing directory contents
