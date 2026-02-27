---
tags: [c, computing]
status: stub
source: preprocessor.c
---

# Preprocessor

> The preprocessor is a text-substitution pass before compilation — it knows nothing about C syntax or types.

## `#define`

### Object-like macros

### Function-like macros — always parenthesize arguments and result

### Macro pitfalls: double evaluation, no type checking

```c
#define MAX(a, b) ((a) > (b) ? (a) : (b))   // double-evaluates a and b
```

## `#include`

### `<header>` vs `"header"` — search path difference

### What include actually does — copy-paste of file contents

### Include guards

```c
#ifndef MY_HEADER_H
#define MY_HEADER_H
// declarations
#endif
```

### `#pragma once` — non-standard but universally supported

## Header file conventions

### What belongs in a header: declarations, type definitions, macros

### What does not belong: definitions, global variable definitions

### Separating interface from implementation

## Conditional compilation

### `#ifdef`, `#ifndef`, `#if`, `#elif`, `#else`, `#endif`

### Platform detection: `__linux__`, `__APPLE__`, `_WIN32`

### Debug builds: `#ifdef DEBUG`

## Predefined macros

| Macro      | Value                      |
| ---------- | -------------------------- |
| `__FILE__` | Current filename as string |
| `__LINE__` | Current line number        |
| `__func__` | Current function name      |
| `__DATE__` | Compilation date           |

## `#error` and `#warning`

## Variadic macros: `__VA_ARGS__`

## Tasks

1. **Safe macros** — write `MIN`, `MAX`, and `CLAMP` macros. Test a case where argument double-evaluation produces wrong results, then fix it with a `static inline` function.
2. **Debug logger** — write a `LOG(fmt, ...)` macro that prints `[file:line] message` using `__FILE__`, `__LINE__`, and `__VA_ARGS__`. Disable it when `NDEBUG` is defined.
3. **Header guard** — create `vec2.h` with a `Vec2` struct and function declarations, guarded with `#ifndef`. Include it twice in the same `.c` file and verify it compiles.
4. **Platform fork** — write a function that returns the OS name as a string, using `#ifdef` to select between `__APPLE__`, `__linux__`, and a fallback.

## See also

- [[Compilation Model]]
- [[Types & Operators]]
