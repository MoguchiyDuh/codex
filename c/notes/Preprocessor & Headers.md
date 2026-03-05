---
tags: [c, computing, tooling]
status: complete
---

# Preprocessor & Headers

> The preprocessor runs before the compiler — pure text substitution with no knowledge of C types or syntax.

## Macros

**Object-like — constants:**

```c
#define MAX_SIZE 1024
```

No type, no scope, no symbol in the binary. Prefer `const` or `enum` for typed constants:

```c
const int MAX_SIZE = 1024;   // typed, scoped, debuggable
enum { MAX_SIZE = 1024 };    // common for integer constants
```

**Function-like — always wrap in parens:**

```c
#define SQUARE(x) ((x) * (x))   // correct
#define SQUARE(x) x * x         // wrong — SQUARE(2+3) → 2+3*2+3 = 11
```

Still broken for side effects — `SQUARE(i++)` evaluates `i++` twice (UB). Use `static inline` instead:

```c
static inline int square(int x) { return x * x; }
```

Type-checked, no double-evaluation, inlined by the compiler.

**Legitimate macro uses — things functions can't do:**

```c
#define ARRLEN(a)  (sizeof(a) / sizeof((a)[0]))
#define UNUSED(x)  ((void)(x))
```

## Conditional Compilation

```c
#ifdef DEBUG
    printf("debug: x = %d\n", x);
#endif

#ifdef __APPLE__
    // macOS-specific
#elif defined(__linux__)
    // Linux-specific
#endif
```

Pass `-DDEBUG` to `gcc` to define `DEBUG` at compile time.

## Declaration vs Definition

```c
// declaration — tells the compiler "this exists somewhere"
int add(int a, int b);
extern int counter;

// definition — creates the thing, allocates storage
int add(int a, int b) { return a + b; }
int counter = 0;
```

A declaration can appear many times. A definition must appear **exactly once** (One Definition Rule). Multiple definitions = linker error.

## Headers

`#include` pastes file contents literally. Nothing more.

```c
#include <stdio.h>    // system include path
#include "myfile.h"   // current directory first
```

**Rule: headers contain declarations only. Definitions go in `.c` files.**

| Belongs in header | Does not belong |
|-------------------|-----------------|
| Function declarations | Function definitions |
| `extern` variable declarations | Variable definitions (`int x = 0;`) |
| `typedef`, `struct`, `enum` definitions | — |
| `#define` macros | — |
| `static inline` functions | Regular `static` functions |

## Header Guards

Prevent double inclusion when headers include other headers:

```c
// math_utils.h
#ifndef MATH_UTILS_H
#define MATH_UTILS_H

int add(int a, int b);
extern int call_count;

#endif
```

Or use `#pragma once` — not standard but supported everywhere, less boilerplate.

## Linkage

**External linkage (default):** functions and globals visible to the entire program.

**`static` at file scope — internal linkage:** symbol hidden from other translation units.

```c
static int helper(int x) { ... }  // private to this .c file
static int state = 0;             // private to this .c file
```

Use `static` for any implementation detail not part of the public API.

**`extern`:** declare a variable that's defined in another translation unit.

```c
// counter.h
extern int counter;   // declaration

// counter.c
int counter = 0;      // one definition
```

## Opaque Types

Hide struct internals from callers — only expose a pointer to an incomplete type:

```c
// vec.h
#pragma once
typedef struct Vec Vec;   // incomplete — callers can't access fields

Vec  *vec_new(void);
void  vec_push(Vec *v, int val);
void  vec_free(Vec *v);

// vec.c
struct Vec {              // full definition here only
    int   *data;
    size_t len;
    size_t cap;
};
```

Callers use `Vec *` but can never access `.data`, `.len`, `.cap` directly. Encapsulation in C.

## static Locals

`static` on a local variable: function scope, but initialized once and retains value between calls.

```c
int next_id(void) {
    static int counter = 0;   // initialized once at program start
    return ++counter;         // persists across calls: 1, 2, 3, ...
}
```

Different from `static` at file scope — same keyword, two distinct meanings based on context.

## Multi-file Compilation

```makefile
CC     = gcc
CFLAGS = -Wall -Wextra -fsanitize=address,undefined

program: main.o vec.o
	$(CC) $(CFLAGS) $^ -o $@

%.o: %.c vec.h
	$(CC) $(CFLAGS) -c $<

clean:
	rm -f *.o program
```

`make` rebuilds only object files whose source or headers changed — edit `vec.c`, only `vec.o` recompiles.

## Exercises

See `EXERCISES.md` — E1, E2, E8, E9, E10, E11.

1. **Split vec** — split `src/vec.c` into `vec.h` + `vec.c` + `vec_main.c` with opaque type and Makefile. `src/vec/`
2. **Split hashmap** — same for `src/hashmap.c`. `src/hashmap/`
3. **Safe macros** — implement `MIN`, `MAX`, `CLAMP`, `SWAP` macros. Show where naive versions break. `src/macros.c`
4. **static local ID generator** — `gen_id(const char *prefix)` with auto-incrementing counter. `src/macros.c`
5. **extern global** — `src/config.c` + `src/config.h` with shared `log_level`. `src/config.c`
6. **static collision** — demonstrate linker error from two files defining `helper`, fix with `static`.

## See also

- [[Compilation Model]]
- [[Tooling]]
