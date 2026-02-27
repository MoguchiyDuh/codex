---
tags:
  - rust
  - io
  - filesystem
source: io_filesystem/src/advanced.rs
---

# Advanced Filesystem Operations

Operations beyond basic read/write: copying, renaming, links, permissions, timestamps, atomic writes, and syncing.

## Copy and Rename

```rust
use std::fs;

fs::copy("src.txt", "dst.txt")?;       // copies content and permissions; returns bytes copied
fs::rename("old.txt", "new.txt")?;     // atomic on POSIX if same filesystem; replaces dst if it exists
```

`fs::rename` across filesystems falls back to a non-atomic copy+delete on some platforms. For cross-filesystem moves, copy then delete manually.

## Hard Links

A hard link is a second directory entry pointing to the same inode. Both names are equal — neither is "the original."

```rust
fs::hard_link("original.txt", "hardlink.txt")?;
```

- Deleting one name does not affect the other.
- Hard links cannot span filesystems.
- Hard links to directories are typically forbidden (prevents cycles in directory trees).

## Symbolic Links

A symlink is a file whose content is a path. Reading through a symlink transparently follows it.

```rust
#[cfg(unix)]
{
    use std::os::unix::fs;

    fs::symlink("target.txt", "link.txt")?;

    let is_sym = std::fs::symlink_metadata("link.txt")?.is_symlink();
    // symlink_metadata does NOT follow the link — use it to inspect the link itself
    // regular metadata() follows the link

    let target = std::fs::read_link("link.txt")?;
    println!("points to: {}", target.display());
}
```

`symlink_metadata` vs `metadata`: the former inspects the link entry itself; the latter follows it.

## File Permissions

### Cross-platform (coarse)

```rust
let meta = fs::metadata("file.txt")?;
let mut perms = meta.permissions();

println!("{}", perms.readonly());

perms.set_readonly(true);
fs::set_permissions("file.txt", perms)?;
```

### Unix-specific (fine-grained)

```rust
#[cfg(unix)]
{
    use std::os::unix::fs::PermissionsExt;
    use std::fs::Permissions;

    let mode = fs::metadata("file.txt")?.permissions().mode();
    println!("{:o}", mode);  // e.g. 100644

    // Set exact mode bits
    let perms = Permissions::from_mode(0o644);  // rw-r--r--
    fs::set_permissions("file.txt", perms)?;
}
```

Common mode values: `0o644` (rw-r--r--), `0o755` (rwxr-xr-x), `0o600` (rw-------).

## Temporary Files

Use `std::env::temp_dir()` to locate the system temp directory (respects `$TMPDIR`/`%TEMP%`):

```rust
let tmp = std::env::temp_dir().join("my_app_tmp.txt");
fs::write(&tmp, b"data")?;
fs::remove_file(&tmp)?;
```

For automatic cleanup on drop, use the `tempfile` crate instead.

## File Timestamps

```rust
let meta = fs::metadata("file.txt")?;

meta.created()?    // creation time — not available on all Unix filesystems
meta.modified()?   // last content modification
meta.accessed()?   // last read access — often disabled on Linux (relatime mount)
```

All return `SystemTime`. Convert to a human-readable form with `chrono` or `time` crates.

## Atomic Writes

The standard safe-write pattern: write to a temp file, sync it, then rename into place. On POSIX filesystems, `rename` is atomic — readers see either the old file or the complete new file, never a partial write.

```rust
let final_path = "config.json";
let tmp_path   = "config.json.tmp";

let mut tmp = File::create(tmp_path)?;
tmp.write_all(b"{}")?;
tmp.sync_all()?;           // flush kernel buffers to physical disk

fs::rename(tmp_path, final_path)?;  // atomic swap
```

This pattern is used by editors, package managers, and databases to prevent corruption on crash.

## Syncing to Disk

Normally, writes go to the kernel page cache and are flushed asynchronously. Two methods force synchronous flushing:

| Method | Syncs |
|---|---|
| `file.sync_all()` | file data + metadata (size, timestamps, etc.) |
| `file.sync_data()` | file data only — faster when metadata changes are irrelevant |

```rust
let mut file = File::create("important.txt")?;
file.write_all(b"critical data")?;
file.sync_all()?;  // safe to power off after this
```

## File Locking

The standard library has no file locking API. On Unix, use the `fs2` or `file-lock` crates which wrap `flock`/`fcntl`. Advisory locks only — the Operating System (OS) does not enforce them against processes that don't opt in.

## Disk Space

Not available in `std`. Use the `fs2` or `sysinfo` crates for available/total disk space queries.

## Related Notes

- [[File IO]] — basic file reading, writing, and seeking
- [[Directories]] — directory creation and removal
- [[Paths]] — path construction used throughout these operations
