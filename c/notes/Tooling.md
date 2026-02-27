---
tags: [c, computing]
status: stub
---

# Tooling

> The C development toolchain — compiler flags, build automation, debugger, and sanitizers.

## `gcc` / `clang` flags

| Flag                   | Purpose                                             |
| ---------------------- | --------------------------------------------------- |
| `-Wall -Wextra`        | Enable most useful warnings                         |
| `-Werror`              | Treat warnings as errors                            |
| `-g`                   | Embed debug info (required for `gdb`)               |
| `-O0`                  | No optimization — predictable debugger behavior     |
| `-O2` / `-O3`          | Optimize for release                                |
| `-fsanitize=address`   | AddressSanitizer — detects memory errors at runtime |
| `-fsanitize=undefined` | UBSan — catches undefined behavior                  |
| `-fsanitize=leak`      | Leak sanitizer                                      |
| `-std=c11`             | Target C11 standard                                 |

Never ship with `-fsanitize` — it slows down and changes binary behavior.

## `make` and Makefiles

### Rules: target, prerequisites, recipe

### Automatic variables: `$@` (target), `$<` (first prereq), `$^` (all prereqs)

### Pattern rules: `%.o: %.c`

### Phony targets: `.PHONY: all clean`

### Variables: `CC`, `CFLAGS`, `LDFLAGS`

## `gdb` basics

### Compile with `-g` first

### Core commands

| Command                      | Effect                            |
| ---------------------------- | --------------------------------- |
| `run` / `r`                  | Start the program                 |
| `break main` / `b file.c:42` | Set breakpoint                    |
| `next` / `n`                 | Step over                         |
| `step` / `s`                 | Step into                         |
| `continue` / `c`             | Run until next breakpoint         |
| `print expr` / `p`           | Evaluate and print expression     |
| `x/4xb addr`                 | Examine 4 bytes at address in hex |
| `backtrace` / `bt`           | Print call stack                  |
| `watch var`                  | Break when variable changes       |
| `quit` / `q`                 | Exit                              |

## Valgrind

### `valgrind --leak-check=full ./program` — leak detection

### When to use Valgrind vs `-fsanitize=leak`

## Static analysis

### `clang-tidy` — style and correctness checks

### `cppcheck` — undefined behavior and logic checks

## Tasks

1. **Makefile** — write a Makefile for a project with `main.c`, `linked_list.c`, and `linked_list.h`. Targets: `all`, `clean`, and individual `.o` files. Use pattern rules and `CFLAGS`.
2. **gdb session** — introduce a deliberate null pointer dereference. Run under `gdb`, get a backtrace, and find the exact line.
3. **Sanitizer catch** — write a program with a use-after-free bug. Compile with `-fsanitize=address` and read the full error output. Identify and fix the bug.
4. **Valgrind** — run the linked list implementation from [[Linked List]] under `valgrind --leak-check=full`. Fix any reported leaks.

## See also

- [[Compilation Model]]
- [[../../theory/architecture/CPU Architecture]]
