---
tags: [c, computing]
status: stub
source: compilation.c
---

# Compilation Model

> C source goes through four distinct stages before becoming an executable — each stage has a defined input and output.

## The four stages

### Preprocessing (`gcc -E`)

### Compilation (`gcc -S`)

### Assembly (`gcc -c`)

### Linking

## Object files and symbols

### `.o` files

### Symbol table: `nm`

### Undefined vs defined symbols

## Header files and translation units

### What `#include` actually does

### Why definitions in headers cause multiple-definition errors

### Declaration vs definition

## Static vs dynamic linking

### `.a` archives

### `.so` / `.dylib` shared libraries

### When each is appropriate

## Compiler flags

| Flag                           | Effect                                            |
| ------------------------------ | ------------------------------------------------- |
| `-Wall -Wextra`                | Enable common warnings                            |
| `-g`                           | Embed debug symbols                               |
| `-O0` / `-O2`                  | Optimization level                                |
| `-fsanitize=address,undefined` | Runtime error detection                           |
| `-E` / `-S` / `-c`             | Stop after preprocessing / compilation / assembly |

## Tasks

1. **Inspect preprocessed output** — run `gcc -E src/compilation.c` and find where a `#include <stdio.h>` expands to. Count how many lines it produces.
2. **Multi-file split** — split a program into `main.c`, a `math_utils.c` with helper functions, and a `math_utils.h` header. Compile each to `.o` then link manually.
3. **Symbol table** — compile `src/compilation.c` to an object file and run `nm` on it. Identify one `T` (defined) and one `U` (undefined) symbol.
4. **Linking error** — define the same function in two `.c` files and observe the linker error. Fix it with `static`.

## See also

- [[Preprocessor]]
- [[Tooling]]
