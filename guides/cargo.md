# Cargo & Rustup Ultimate Cheat Sheet (GNU Focus)

## 1. Installation & Toolchain (rustup)

### Installation

```bash
# Universal (Linux/macOS)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Windows
choco install rustup.install
choco install mingw        # Required for GNU toolchain
```

### Toolchain Management

```bash
rustup update             # Update Rust and rustup
rustup target add x86_64-unknown-linux-gnu          # Add cross-compile target
rustup component add rust-analyzer ruff             # Add components

# On Windows
rustup toolchain install stable-x86_64-pc-windows-gnu # Install GNU toolchain
rustup default stable-x86_64-pc-windows-gnu         # Set GNU as default
```

---

## 2. Project Lifecycle

### Basics

```bash
cargo new <name>          # Create new binary project
cargo new --lib <name>    # Create new library project
cargo init                # Initialize repo in current dir
```

### Development Loop

```bash
cargo check               # Fast compile check (no binary)
cargo build               # Build debug binary (target/debug/)
cargo build --release     # Build optimized binary (target/release/)
cargo run                 # Build and run
cargo test                # Run all tests
cargo bench               # Run benchmarks (requires nightly/custom)
cargo clean               # Wipe the target directory
```

---

## 3. Dependency Management

### Commands

```bash
cargo add <pkg>           # Add dependency to Cargo.toml
cargo add <pkg> --dev     # Add dev-dependency
cargo add <pkg> -F <feat> # Add with specific features
cargo rm <pkg>            # Remove dependency
cargo update              # Update dependencies in Cargo.lock
cargo tree                # Show dependency graph (check duplicates)
cargo vendor              # Download all dependencies locally
```

### Feature Flags (Cargo.toml)

```toml
[dependencies]
tokio = { version = "1.0", features = ["full"] }
serde = { version = "1.0", optional = true }

[features]
default = ["tokio"]
extra = ["serde"]
```

---

## 4. GNU Target & Cross-Compilation

### Cross-Build (Windows to GNU)

```bash
cargo build --target x86_64-pc-windows-gnu
```

### Static vs Dynamic Linking

To force static linking for MingW (GNU Windows):

```toml
# .cargo/config.toml
[target.x86_64-pc-windows-gnu]
rustflags = ["-C", "link-args=-static"]
```

### Cross-Compile for Linux (from Windows)

```bash
# Requires a cross-linker (e.g., zig or a dedicated GCC)
cargo build --target x86_64-unknown-linux-gnu
```

---

## 5. Advanced Workspaces

### Root `Cargo.toml`

```toml
[workspace]
members = [
    "crates/*",
    "apps/*",
]
resolver = "2" # Specifies how Cargo resolves dependencies

# Resolver Versions:
# - "1" (Default): Unifies features across all workspace members.
# - "2" (Rust 1.51+): Keeps features separate for different build targets
#   (e.g., dev-deps don't affect build-deps). Recommended for modern projects.

[workspace.dependencies]
serde = "1.0" # Define once, inherit in members
```

### Member `Cargo.toml`

```toml
[package]
name = "my-member"
# ...
[dependencies]
serde = { workspace = true } # Inherit from root
```

---

## 6. Optimization & Profiles

### Release Power Settings

```toml
# Cargo.toml
[profile.release]
opt-level = 3          # Max optimization (0-3)
lto = true             # Link Time Optimization (Fat)
codegen-units = 1      # More optimization, slower build
panic = "abort"        # Reduce size by removing stack unwinding
strip = true           # Automatically strip symbols (Rust 1.59+)
```

### Optimize for Size

```toml
[profile.release]
opt-level = "z"        # Optimize for size (z or s)
```

---

## 7. Ecosystem Power Tools

```bash
cargo install cargo-watch   # Watch and run (e.g., cargo watch -x check)
cargo install cargo-expand  # View result of macro expansion
cargo install cargo-audit   # Scan for security vulnerabilities
cargo install cargo-nextest # Modern, faster test runner
cargo install cargo-edit    # Provides cargo add/rm (older Rust versions)
```

---

## 8. Glossary & Abbreviations

| Term          | Full Name              | Description                                                              |
| :------------ | :--------------------- | :----------------------------------------------------------------------- |
| **GNU**       | GNU's Not Unix         | Refers to the MinGW-w64 toolchain on Windows.                            |
| **LTO**       | Link Time Optimization | Deep optimization across crate boundaries at link time.                  |
| **Target**    | -                      | The system architecture/OS the code is being built for.                  |
| **Crate**     | -                      | A Rust package (unit of compilation).                                    |
| **Workspace** | -                      | A set of packages that share a single `Cargo.lock` and output directory. |
| **Codegen**   | Code Generation        | The process of turning Rust into machine code (divided into units).      |
| **MSVCRT**    | MS Visual C++ Runtime  | Standard Windows C runtime.                                              |
| **UCRT**      | Universal C Runtime    | Modern Windows C runtime (preferred for newer apps).                     |
