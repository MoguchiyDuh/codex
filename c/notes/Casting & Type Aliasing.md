---
tags: [c, computing]
status: complete
source: ieee.c
---

# Casting & Type Aliasing

> C casts reinterpret or convert bits with no runtime checks — wrong casts are silently undefined behavior.

## Value conversion vs reinterpretation

| Cast | What happens |
|---|---|
| `(float)i` where `i` is `int` | Value conversion — CPU converts 42 → 42.0f |
| `*(int *)&f` where `f` is `float` | Reinterpretation — reads the raw bits as `int` |

The second form looks like it works but violates strict aliasing.

## Strict aliasing rule

The compiler assumes pointers of different types never point to the same memory. Accessing the same memory through two incompatible pointer types is UB — the optimizer may cache the original value in a register and ignore writes through the aliased pointer:

```c
float f = 1.0f;
int *p = (int *)&f;
*p = 0x3F800000;   // UB — compiler may not observe this write
```

## `char *` exception

`char *` and `unsigned char *` are exempt — they can legally alias any type. Used for byte-level inspection:

```c
float f = 3.14f;
unsigned char *b = (unsigned char *)&f;
for (int i = 0; i < 4; i++)
    printf("%02x ", b[i]);   // legal — prints raw bytes
```

## `memcpy` — safe reinterpretation

The standard-compliant way to inspect a type's raw bits. The compiler recognizes it and emits a register move for small sizes — no actual copy at runtime:

```c
float f = 3.14f;
unsigned int bits;
memcpy(&bits, &f, sizeof(float));   // well-defined
printf("0x%X\n", bits);
```

## Union type-punning (C only)

In C99+, reading a union member other than the one last written is defined behavior. This does not apply in C++:

```c
union { float f; unsigned int u; } pun;
pun.f = 1.0f;
printf("0x%X\n", pun.u);   // defined in C, UB in C++
```

## Summary

| Method | Legal | Notes |
|---|---|---|
| `*(int *)&f` | No | Strict aliasing UB |
| `char *` access | Yes | Exempted by the standard |
| `memcpy` | Yes | Optimized away for small sizes |
| `union` | Yes (C only) | UB in C++ |

## Tasks

1. **Raw float bits** — use `memcpy` to print the raw hex bits of `1.0f`, `0.5f`, `-1.0f`, and `0.0f`. Decode each field (sign, exponent, mantissa) manually. `src/ieee.c`
2. **Aliasing violation** — write the `*(int *)&f` cast, compile with `-O2`, and observe that the optimizer may discard the write. Fix it with `memcpy`. `src/ieee.c`
3. **Union punning** — implement the same raw-bits inspection using a `union`. Verify results match `memcpy`. `src/ieee.c`
4. **Byte-level inspection** — use `unsigned char *` to print all 4 bytes of a `float` in order. Note the endianness. `src/ieee.c`

## See also

- [[../../theory/computing/IEEE 754]]
- [[../../theory/computing/Data Representation]]
- [[Memory & Pointers]]
