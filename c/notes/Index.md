---
tags: [c]
status: complete
---

# C

> C language notes — mechanics, APIs, and implementation patterns grounded in source files under `src/`.

## Module 1 — Foundations

- [[Compilation Model]] — preprocessor → compiler → assembler → linker, symbols, static vs dynamic linking
- [[Integer Promotions]] — integer promotion, usual arithmetic conversions, signed/unsigned trap, `sizeof`
- [[Types & Operators]] — primitive types, `<stdint.h>`, operators, promotions
-[[Functions]] — call stack, pass-by-pointer, recursion, function pointers

## Module 2 — Memory

- [[Memory & Pointers]] — addresses, `&`/`*`, pointer arithmetic, array decay, `sizeof`
- [[Pointers & const]] — `const T*` vs `T* const`, pointer decay, `void*`, pointer-to-pointer
- [[Heap Memory]] — `malloc`/`calloc`/`realloc`/`free`, corruption types, dynamic array

## Module 3 — Strings and I/O

- [[Strings & size_t]] — `size_t`, `ptrdiff_t`, stack vs heap vs data segment, null terminator traps, exercises
- [[Standard I_O]] — `printf`/`scanf`, file I/O, `argv`

## Module 4 — Structured Data

- [[Structs & Unions]] — padding rules, field-by-field offsets, `packed`, unions, tagged union, designated initializers

## Module 5 — Preprocessor

- [[Preprocessor & Headers]] — macros, `static inline`, header guards, declaration vs definition, linkage, opaque types, Makefile basics
- [[Preprocessor]] — macros, include guards, conditional compilation

## Module 6 — Data Structures

- [[Linked List]] — singly/doubly, push/delete/reverse
- [[Stack & Queue]] — array-backed and linked-list-backed implementations
- [[HashMap]] — hash function, separate chaining, insert/get/delete

## Module 7 — The Type System

- [[Integer Types]] — sizes, signed/unsigned, overflow, bit manipulation
- [[Casting & Type Aliasing]] — value conversion vs reinterpretation, strict aliasing, `memcpy`

## Module 8 — Systems

- [[Processes & Signals]] — `fork`/`exec`/`wait`, file descriptors, signal handlers
- [[Qualifiers & Atomics]] — `volatile`, `restrict`, `_Atomic`, memory orders

## Module 9 — Tooling

- [[Tooling]] — `gcc` flags, Makefiles, `gdb`, sanitizers, Valgrind

## See also

- [[../../theory/os/Stack vs Heap]]
- [[../../theory/data_structures/Index|Data Structures]]
- [[../../theory/computing/Index|Computing]]
