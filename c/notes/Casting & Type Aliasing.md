---
tags: [c, casting, aliasing, undefined-behavior]
source: ieee.c
---

# Casting & Type Aliasing

## C casts — "trust me" to the compiler

C casts are an unconditional instruction to reinterpret bits as a different type. No runtime checks, no conversion logic unless the types warrant it (e.g. int→float). Wrong casts are silently UB (Undefined Behavior).

```c
float f = 3.14f;
int *p = (int *)&f;     // cast: "treat this float's address as int*"
int bits = *p;          // reads the raw IEEE 754 bits — UB via strict aliasing
```

## Strict aliasing rule

The compiler assumes that pointers of different types don't point to the same memory. Accessing the same memory through two incompatible pointer types is UB — the compiler is allowed to reorder or eliminate such accesses.

```c
float f = 1.0f;
int *p = (int *)&f;
*p = 0x3F800000;        // UB — strict aliasing violation
```

The optimizer may cache `f` in a register and never see the write through `p`.

## `char*` is the legal exception

`char*` (and `unsigned char*`) can alias any type — this is explicitly carved out by the C standard. The compiler cannot assume they don't overlap with other types.

```c
float f = 1.0f;
char *bytes = (char *)&f;   // legal — char* can alias anything
for (int i = 0; i < 4; i++)
    printf("%02x ", (unsigned char)bytes[i]);
```

## `memcpy` — the safe reinterpretation method

`memcpy` bypasses strict aliasing by working at the byte level. It's the standard-compliant way to reinterpret the bits of one type as another:

```c
#include <string.h>

float f = 3.14f;
unsigned int bits;
memcpy(&bits, &f, sizeof(float));   // legal — copies bytes, no aliasing
printf("0x%X\n", bits);
```

The compiler recognizes `memcpy` and typically optimizes it to a register move — no actual memory copy at runtime for small sizes.

## Summary

| Method                       | Legal            | Notes                                     |
| ---------------------------- | ---------------- | ----------------------------------------- |
| `(int *)&f` then dereference | ✗                | Strict aliasing UB                        |
| `char *` access              | ✓                | `char*` exemption                         |
| `memcpy`                     | ✓                | Standard-compliant, optimized away        |
| `union`                      | ✓ in C, ✗ in C++ | Type-punning via union is defined in C99+ |
