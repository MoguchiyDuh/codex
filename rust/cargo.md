# Cargo Commands Reference

## Primary Build & Run

- `cargo build` (alias: `b`): Compile the current package.
- `cargo build --release`: Build optimized artifacts.
- `cargo run` (alias: `r`): Build and execute a binary.
- `cargo run --bin <name>`: Run a specific binary.
- `cargo check` (alias: `c`): Analyze the code for errors without compiling into a binary (much faster than build).
- `cargo clean`: Remove the `target/` directory.

## Testing & Benchmarking

- `cargo test` (alias: `t`): Run unit and integration tests.
- `cargo test <name>`: Run tests matching a specific name.
- `cargo bench`: Run benchmarks.

## Package & Project Management

- `cargo new <path>`: Create a new cargo project.
- `cargo init`: Initialize a cargo project in the current directory.
- `cargo add <crate>`: Add a dependency to `Cargo.toml`.
- `cargo remove <crate>` (alias: `rm`): Remove a dependency.
- `cargo update`: Update dependencies in `Cargo.lock`.
- `cargo tree`: Display a tree visualization of the dependency graph.
- `cargo metadata`: Output resolved dependencies in JSON (for tools).
- `cargo vendor`: Download all dependencies locally.

## Documentation

- `cargo doc` (alias: `d`): Build documentation for the project and dependencies.
- `cargo doc --open`: Build and open documentation in a browser.

## Code Quality & Formatting

- `cargo fmt`: Format all files according to `rustfmt`.
- `cargo clippy`: Run the Rust linter for common mistakes and improvements.
- `cargo fix`: Automatically apply fixes provided by the compiler or clippy.

## Debugging & Tooling

- `cargo rustc`: Compile with custom flags passed directly to `rustc`.
- `cargo rustdoc`: Generate docs with custom flags passed directly to `rustdoc`.
- `cargo config`: Inspect or modify cargo configuration.
- `cargo locate-project`: Show the path to the root `Cargo.toml`.
- `cargo pkgid`: Print the package ID.
- `cargo read-manifest`: (Deprecated) Print a JSON representation of a `Cargo.toml` manifest.
- `cargo verify-project`: (Deprecated) Check correctness of crate manifest.

## Registry & Publishing

- `cargo login <token>`: Log into a registry (e.g., crates.io).
- `cargo logout`: Remove the registry API token.
- `cargo publish`: Upload the package to the registry.
- `cargo search <query>`: Search for crates on crates.io.
- `cargo yank`: Remove a version from the registry index.
- `cargo owner`: Manage crate ownership on the registry.
- `cargo package`: Create a distributable `.crate` file.

## Binary Installation

- `cargo install <crate>`: Download and install a crate as a system binary.
- `cargo uninstall <crate>`: Remove an installed binary.

## Other Commands

- `cargo help <command>`: Show detailed help for a specific command.
- `cargo version`: Show cargo version.
- `cargo miri`: (Plugin) Run the Miri interpreter for checking undefined behavior.
- `cargo report`: Display various reports (e.g., future-incompat).
- `cargo fetch`: Pre-fetch dependency assets.
- `cargo generate-lockfile`: Create/update `Cargo.lock`.
- `cargo info`: Display information about a package.

## Common Flags

- `-p <package>` / `--package <package>`: Specify a package in a workspace.
- `--all`: Run command for all packages in a workspace.
- `--workspace`: Same as `--all`.
- `--bin <name>`: Target a specific binary.
- `--example <name>`: Target a specific example.
- `--lib`: Target the library.
- `--release`: Use release profile (optimized).
- `--target <triple>`: Cross-compile for a specific architecture.
- `--features <features>`: Space/comma separated list of features to enable.
- `--all-features`: Enable all features.
- `--no-default-features`: Disable default features.
- `--verbose` / `-v`: Show extra output.
- `--quiet` / `-q`: Show less output.
- `--color <auto|always|never>`: Configure terminal colors.

# Cargo Deep Dive: Configuration & Optimization

## 1. `Cargo.toml` Structure

The manifest file follows the TOML format and is divided into several key sections.

### `[package]`

Metadata about your crate.

```toml
[package]
name = "my_project"
version = "0.1.0"
edition = "2024" # Rust edition, 2024 is the latest
authors = ["User <email@example.com>"]
description = "A brief description"
license = "MIT"
default-run = "my_bin" # Default binary for 'cargo run'
```

### `[dependencies]`

Libraries your project needs.

```toml
[dependencies]
serde = { version = "1.0", features = ["derive"] } # Version + Features
tokio = "1.0"                                     # Simple version
# Local path dependency
shared = { path = "../shared" }
# Git dependency
regex = { git = "https://github.com/rust-lang/regex" }
```

### `[features]`

Conditional compilation flags.

```toml
[features]
default = ["logging"]
logging = ["dep:log"] # Optional dependency
advanced = []
```

### `[workspace]`

Used in multi-crate projects (like this repo).

```toml
[workspace]
members = ["basics", "collections"]
resolver = "2" # Modern dependency resolution
```

---

## 2. `.cargo/config.toml` (Project Config)

Stored in `.cargo/config.toml`, this file configures the build environment.

### Build Settings

```toml
[build]
jobs = 8                # Parallel build jobs
target = "x86_64-unknown-linux-gnu" # Default target (Linux GNU)
rustflags = ["-C", "target-cpu=native"] # Optimization flags
```

### Aliases

```toml
[alias]
r = "run"
c = "check"
t = "test"
b = "build"
rb = "run --release"
```

---

## 3. Build Profiles & Optimization

Rust provides deep control over how binaries are optimized in `[profile.X]` sections.

### Optimization Flags

```toml
[profile.release]
opt-level = 3          # 0 (none) to 3 (max), 's' (size), 'z' (min size)
lto = true             # Link Time Optimization (huge binary size/perf impact)
codegen-units = 1      # Reduce parallel units for better optimization
panic = "abort"        # Reduce binary size by removing unwinding code
strip = true           # Remove debug symbols automatically
```

### Dev vs Release

- **`[profile.dev]`**: Optimized for compile speed (debug info, no optimizations).
- **`[profile.release]`**: Optimized for runtime performance (no debug info, max optimizations).

---

## 4. Size vs Performance

| Goal             | Settings                                             | Result                               |
| :--------------- | :--------------------------------------------------- | :----------------------------------- |
| **Max Speed**    | `opt-level = 3`, `lto = "fat"`, `codegen-units = 1`  | Fastest execution, slow compile.     |
| **Min Size**     | `opt-level = "z"`, `panic = "abort"`, `strip = true` | Tiniest binary, useful for embedded. |
| **Fast Compile** | `opt-level = 0`, `codegen-units = 256`               | Best for development iteration.      |

---

## 5. Environment Variables

Cargo also reads environment variables which override file configs:

- `CARGO_BUILD_JOBS`
- `RUSTFLAGS`
- `CARGO_TARGET_DIR`
