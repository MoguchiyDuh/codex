---
tags: [c, computing]
status: stub
source: structs.c
---

# Structs

> Structs are contiguous blocks of named fields in memory — the compiler controls layout, including padding for alignment.

## Definition and initialization

### `struct` keyword and `typedef`

### Designated initializers

### Zero initialization

## Memory layout

### Fields at offsets — `offsetof` from `<stddef.h>`

### Padding for alignment

### `__attribute__((packed))` — remove padding, costs performance

### `sizeof` a struct is not the sum of field sizes

## Pointers to structs

### Arrow operator `->` vs dot `.`

### Passing structs by pointer vs by value

### Returning structs by value — when it's fine

## Nested structs and self-referential structs

### Embedding a struct inside another

### Forward declaration for linked structures

## Unions

### All members share the same memory

### Size is the largest member

### Type-punning via union (C99+)

## Bit fields

### Packing integers into fewer bits

### Limitations — no address-of, order is implementation-defined

## Tasks

1. **Layout inspection** — define a struct with `char`, `int`, `char`, `double` in that order. Print `sizeof` and `offsetof` each field. Reorder fields to minimize size.
2. **Linked struct** — define a `Node` struct with an `int` value and a `Node *next` pointer. Write a function that builds a chain of 5 nodes and prints them.
3. **Pass by pointer** — define a `Vec2` struct. Write `vec2_add(Vec2 *a, Vec2 *b, Vec2 *out)` that writes the result through the output pointer.
4. **Union demo** — use a `union { float f; uint32_t u; }` to print the raw bits of `3.14f`. Compare to `memcpy` approach from [[Casting & Type Aliasing]].
5. **Packed struct** — mark a struct with `__attribute__((packed))`. Measure and compare `sizeof` before and after.

## See also

- [[Memory & Pointers]]
- [[Casting & Type Aliasing]]
- [[../../theory/computing/Data Representation]]
- [[../../theory/architecture/Memory Hierarchy]]
