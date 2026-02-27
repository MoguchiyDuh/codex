---
tags: [rust, basics, environment, env-vars]
source: basics/src/environment.rs
---

# Environment

## Command-line arguments

```rust
use std::env;

let args: Vec<String> = env::args().collect();
// args[0] = binary path, args[1..] = user args

let first: Option<String> = env::args().nth(1);
let user_args: Vec<String> = env::args().skip(1).collect();
```

`env::args_os()` returns `OsString` — handles non-UTF-8 paths on Windows.

## Reading env vars

```rust
// Returns Err if not set or invalid UTF-8
let val: Result<String, env::VarError> = env::var("HOME");

// Returns Option<OsString> — never fails on encoding
let val: Option<OsString> = env::var_os("HOME");
```

### Common patterns

```rust
// Fallback default
let level = env::var("LOG_LEVEL").unwrap_or_else(|_| "info".to_string());

// Parse typed value with fallback
let port: u16 = env::var("PORT")
    .unwrap_or_else(|_| "8080".to_string())
    .parse()
    .unwrap_or(8080);

// Presence check (bool flag)
let debug: bool = env::var("DEBUG").is_ok();
```

## Setting / removing vars

```rust
// unsafe in Rust 2024 — POSIX doesn't guarantee thread-safety for setenv
unsafe { env::set_var("KEY", "value"); }
unsafe { env::remove_var("KEY"); }
```

Safe to use before spawning any threads.

## Iterating all vars

```rust
for (key, val) in env::vars() {
    println!("{}={}", key, val);
}

// Filter prefix
let cargo_vars: Vec<(String, String)> = env::vars()
    .filter(|(k, _)| k.starts_with("CARGO_PKG"))
    .collect();
```

## Paths

```rust
let cwd: PathBuf = env::current_dir().unwrap();
let exe: PathBuf = env::current_exe().unwrap();
let tmp: PathBuf = env::temp_dir();

// Change working directory (affects entire process)
// env::set_current_dir("/tmp").unwrap();
```

## Config loading pattern

```rust
#[derive(Debug)]
struct AppConfig {
    host: String,
    port: u16,
    debug: bool,
}

impl AppConfig {
    fn from_env() -> Self {
        AppConfig {
            host: env::var("APP_HOST").unwrap_or_else(|_| "127.0.0.1".to_string()),
            port: env::var("APP_PORT").ok().and_then(|s| s.parse().ok()).unwrap_or(3000),
            debug: env::var("APP_DEBUG").map(|v| v == "1" || v == "true").unwrap_or(false),
        }
    }
}
```
