---
tags:
  - rust
  - io
  - process
source: io_filesystem/src/process.rs
---

# Process & Command

`std::process::Command` is a builder for spawning child processes. It maps closely to POSIX `fork`+`exec` but with a safe, cross-platform API.

## Three Execution Modes

| Method | Behaviour | Returns |
|---|---|---|
| `.status()` | Runs to completion, inherits stdio | `ExitStatus` |
| `.output()` | Runs to completion, captures stdout+stderr | `Output` |
| `.spawn()` | Starts the process, returns immediately | `Child` |

## Basic Execution

```rust
use std::process::{Command, ExitStatus};

let status: ExitStatus = Command::new("echo").arg("hello").status()?;
println!("success={}, code={:?}", status.success(), status.code());
```

`status.success()` is true iff exit code is 0. `status.code()` returns `Option<i32>` — `None` if the process was killed by a signal.

## Capturing Output

```rust
use std::process::Output;

let out: Output = Command::new("echo").args(["a", "b"]).output()?;
let text = String::from_utf8_lossy(&out.stdout);
println!("{}", text.trim());
println!("exit: {}", out.status.success());
```

`Output` holds `stdout: Vec<u8>`, `stderr: Vec<u8>`, and `status: ExitStatus`.

## Arguments

```rust
Command::new("ls").args(["-la", "/tmp"]).output()?;

// Equivalent, one at a time
Command::new("ls").arg("-la").arg("/tmp").output()?;
```

Avoid building a single shell string with user input — use `.arg()` per token to prevent shell injection.

## Environment Variables

```rust
// Add or override a single variable
Command::new("sh").arg("-c").arg("echo $KEY")
    .env("KEY", "value")
    .output()?;

// Add multiple at once
Command::new("sh").arg("-c").arg("echo $A $B")
    .envs([("A", "foo"), ("B", "bar")])
    .output()?;

// Start with a clean environment
Command::new("env")
    .env_clear()
    .env("ONLY_THIS", "1")
    .output()?;
```

## Working Directory

```rust
Command::new("pwd").current_dir("/tmp").output()?;
// prints: /tmp
```

## Piping stdin

`Stdio::piped()` creates an Operating System (OS) pipe. Write to the child's stdin before waiting, or you risk deadlock — the child blocks waiting for input while you block waiting for it to exit.

```rust
use std::process::Stdio;
use std::io::Write;

let mut child = Command::new("cat")
    .stdin(Stdio::piped())
    .stdout(Stdio::piped())
    .spawn()?;

child.stdin.as_mut().unwrap().write_all(b"hello\n")?;

// wait_with_output closes stdin (EOF signal) then waits
let out = child.wait_with_output()?;
println!("{}", String::from_utf8_lossy(&out.stdout).trim());
```

## Chaining Processes (Pipeline)

Connect two processes with an OS pipe by converting `ChildStdout` into a `Stdio`:

```rust
let mut first = Command::new("sh")
    .arg("-c").arg("printf 'c\\nb\\na\\n'")
    .stdout(Stdio::piped())
    .spawn()?;

// .take() extracts the ChildStdout from the Option, leaving None
let pipe = Stdio::from(first.stdout.take().unwrap());

let second = Command::new("sort").arg("-r").stdin(pipe).output()?;

first.wait()?;  // reap the first child
println!("{}", String::from_utf8_lossy(&second.stdout).trim());
```

## Suppressing Output

```rust
Command::new("ls").arg("/tmp")
    .stdout(Stdio::null())
    .stderr(Stdio::null())
    .status()?;
```

`Stdio::null()` is the equivalent of redirecting to `/dev/null`.

## Spawn, Poll, Kill

`.spawn()` returns a `Child` handle immediately:

```rust
let mut child = Command::new("sleep").arg("10").spawn()?;

println!("pid={}", child.id());

// Non-blocking check
let done: Option<ExitStatus> = child.try_wait()?;  // None = still running

// Blocking wait
let status = child.wait()?;

// Terminate the process
child.kill()?;
child.wait()?;  // must wait after kill to release OS resources
```

Always call `.wait()` (or `.wait_with_output()`) after `.kill()` — not doing so leaks the zombie process entry until the parent exits.

## Exit Codes

Convention: 0 = success, non-zero = failure. The specific non-zero values are program-defined.

```rust
let status = Command::new("sh").args(["-c", "exit 42"]).status()?;
assert_eq!(status.code(), Some(42));
assert!(!status.success());
```

## Related Notes

- [[Stdio]] — working with stdin/stdout/stderr directly in the current process
- [[Advanced]] — file-level operations that commonly precede process execution
