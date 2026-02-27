---
tags:
  - rust
  - io
  - filesystem
source: io_filesystem/src/directories.rs
---

# Directories

Directory operations live in `std::fs`. The API is straightforward but has a few rough edges around iteration (each entry is itself a `Result`) and the distinction between `remove_dir` (only empty) and `remove_dir_all` (recursive).

## Creating

```rust
use std::fs;

fs::create_dir("my_dir")?;              // fails if already exists or parent missing
fs::create_dir_all("a/b/c/d")?;        // creates all intermediate parents, no-op if exists
```

## Checking Existence

```rust
use std::path::Path;

Path::new("my_dir").exists()   // true for any filesystem entry
Path::new("my_dir").is_dir()   // true only for directories
```

## Reading Contents

`fs::read_dir` returns an iterator of `io::Result<DirEntry>`. The outer `?` gets the iterator; each iteration also yields a `Result` that must be handled.

```rust
for entry in fs::read_dir("my_dir")? {
    let entry = entry?;                    // handle per-entry errors
    let path  = entry.path();
    let meta  = entry.metadata()?;

    println!("{} ({})", path.display(), if meta.is_dir() { "dir" } else { "file" });
}
```

Order is not guaranteed — the Operating System (OS) returns entries in filesystem order.

### Filtering by extension

```rust
for entry in fs::read_dir("my_dir")? {
    let entry = entry?;
    if entry.path().extension().and_then(|s| s.to_str()) == Some("txt") {
        println!("{}", entry.path().display());
    }
}
```

## Walking a Tree

The standard library has no `walk_dir`. The idiomatic approach for simple cases is a recursive function; for production use, reach for the `walkdir` crate.

```rust
fn walk(path: &Path, depth: usize) -> io::Result<()> {
    let indent = "  ".repeat(depth);
    if path.is_dir() {
        println!("{}{}/", indent, path.file_name().unwrap().to_string_lossy());
        for entry in fs::read_dir(path)? {
            walk(&entry?.path(), depth + 1)?;
        }
    } else {
        println!("{}{}", indent, path.file_name().unwrap().to_string_lossy());
    }
    Ok(())
}
```

### Collecting all files recursively

```rust
fn collect_files(path: &Path, files: &mut Vec<PathBuf>) -> io::Result<()> {
    if path.is_dir() {
        for entry in fs::read_dir(path)? {
            collect_files(&entry?.path(), files)?;
        }
    } else {
        files.push(path.to_path_buf());
    }
    Ok(())
}
```

## Metadata

```rust
let meta = fs::metadata("my_dir")?;

meta.is_dir()                     // true
meta.is_file()                    // false
meta.permissions().readonly()     // permission check
meta.modified()                   // SystemTime or Err (not all platforms)
```

## Computing Directory Size

There's no built-in `du`. Sum `metadata().len()` recursively:

```rust
fn dir_size(path: &Path) -> io::Result<u64> {
    let mut total = 0u64;
    if path.is_dir() {
        for entry in fs::read_dir(path)? {
            total += dir_size(&entry?.path())?;
        }
    } else {
        total += fs::metadata(path)?.len();
    }
    Ok(total)
}
```

## Removing

```rust
fs::remove_dir("empty_dir")?;          // errors if the directory is not empty
fs::remove_dir_all("dir_with_stuff")?; // recursive — equivalent to rm -rf
```

`remove_dir_all` is not atomic; if it fails partway through, the directory is left in a partial state.

## Checking Empty

```rust
fn is_empty(path: &Path) -> io::Result<bool> {
    Ok(fs::read_dir(path)?.count() == 0)
}
```

Note: `.count()` consumes the iterator and handles all entries internally. Any per-entry error is silently ignored here — for stricter code, iterate manually.

## Related Notes

- [[Paths]] — path construction and decomposition
- [[File IO]] — reading and writing individual files
- [[Advanced]] — timestamps, permissions, atomic operations
