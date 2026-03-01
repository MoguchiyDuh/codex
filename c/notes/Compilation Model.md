---
tags: [c, computing, tooling]
status: complete
source: src/compilation_model/
---

# Compilation Model

> C compilation is four distinct stages — each transforms source into a lower-level representation.

## Pipeline Overview

```
source.c  →  [preprocessor]  →  source.i
source.i  →  [compiler]      →  source.s
source.s  →  [assembler]     →  source.o
source.o  →  [linker]        →  executable
```

## Stage 1 — Preprocessor

Pure text substitution. Knows nothing about C syntax.

- `#include` → paste file contents literally at that position
- `#define` → text replacement throughout the file
- `#ifdef` / `#endif` → conditionally include or exclude text
- Strips comments
- Output: `.i` file (expanded C source)

```bash
gcc -E main.c -o main.i   # stop after preprocessing, inspect the output
```

## Stage 2 — Compiler

Translates C to assembly. Type checking, warnings, and optimization happen here.

- Input: `.i`
- Output: `.s` (assembly)

```bash
gcc -S main.c             # produces main.s
```

Syntax errors, type mismatches, and undeclared identifiers are caught here. Each `.c` file is compiled independently — the compiler has no knowledge of other files.

## Stage 3 — Assembler

Translates assembly to machine code. No optimization.

- Input: `.s`
- Output: `.o` — object file (machine code + unresolved symbol references)

```bash
gcc -c main.c             # produces main.o
```

## Stage 4 — Linker

Combines object files into a final executable. Resolves symbol references.

- Input: one or more `.o` files + libraries
- Output: executable binary

```bash
gcc main.o util.o -o program
```

## Object Files and Symbols

When your `.c` file calls `malloc`, the compiler emits an unresolved reference to the symbol `malloc`. The linker finds where `malloc` lives (in libc) and wires the call to it.

Two distinct errors — different stages:

| Error | Stage | Cause |
|-------|-------|-------|
| `undeclared function 'foo'` | Compiler | Called with no declaration in scope |
| `undefined reference to 'foo'` | Linker | Declared but never implemented or not linked |

Inspect symbols in an object file with `nm`:

```bash
nm main.o
# T = defined in this file
# U = undefined (to be resolved by linker)
```

## Static vs Dynamic Linking

| | Static (`.a`) | Dynamic (`.so` / `.dylib`) |
|---|---|---|
| Library code | copied into your binary | loaded at runtime |
| Binary size | larger | smaller |
| Deployment | self-contained | depends on system libraries |
| Bug fixes | must recompile | library update affects all users |

```bash
gcc main.c -o program          # dynamic by default
gcc main.c -static -o program  # static
otool -L ./program             # show dynamic dependencies (macOS)
```

## Multi-file Compilation

```bash
gcc -c hashmap.c -o hashmap.o   # compile each file separately
gcc -c main.c    -o main.o
gcc hashmap.o main.o -o program # link together
```

Or in one step (still goes through all 4 stages internally):

```bash
gcc hashmap.c main.c -o program
```

## Compiler Flags

| Flag | Effect |
|------|--------|
| `-Wall -Wextra` | Enable common warnings |
| `-g` | Embed debug symbols |
| `-O0` / `-O2` | Optimization level |
| `-fsanitize=address,undefined` | Runtime error detection |
| `-E` / `-S` / `-c` | Stop after preprocessing / compilation / assembly |

## Source Files

| File | Description |
|------|-------------|
| `src/compilation_model/main.c` | entry point, calls math_utils |
| `src/compilation_model/math_utils.c` | function definitions |
| `src/compilation_model/math_utils.h` | declarations — what a header looks like |
| `src/compilation_model/build_stages.sh` | runs each stage explicitly, produces `.i` `.s` `.o` |
| `src/compilation_model/main.i` | preprocessed output — inspect to see `#include` expansion |
| `src/compilation_model/main.s` | assembly output |
| `src/compilation_model/main.o` | object file — run `nm main.o` to inspect symbols |

## See also

- [[Preprocessor]]
- [[Tooling]]
