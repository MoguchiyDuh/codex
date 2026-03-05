---
tags: [c, memory, types, computing]
status: complete
---

# Structs & Unions

> The compiler silently inserts padding into structs — field order determines wasted space.

## Alignment Rules

Every type has an alignment requirement — its address must be a multiple of its size.

| Type | Size | Alignment |
|------|------|-----------|
| `char` | 1 | 1 |
| `short` | 2 | 2 |
| `int` | 4 | 4 |
| `double` | 8 | 8 |
| pointer | 8 | 8 |

## Struct Layout — Field by Field

Before placing each field, round the current offset **up** to the nearest multiple of that
field's alignment. After all fields, round total size up to the struct's alignment
(= largest member's alignment).

```c
struct S {
    char a;   // offset 0,  size 1
    char b;   // offset 1,  size 1  (alignment 1 — no padding)
    int c;    // offset 4,  size 4  (alignment 4 — 2 bytes padding after b)
    char d;   // offset 8,  size 1
              // trailing: 3 bytes padding (struct alignment = 4)
};
// sizeof == 12
```

```
[a][b][pad pad][c c c c][d][pad pad pad]
 0  1   2   3   4 5 6 7  8   9  10  11
```

**Field order controls wasted space — largest to smallest minimizes padding:**

```c
struct Bad  { char a; int b; char c; };  // sizeof 12
struct Good { int b; char a; char c; };  // sizeof 8
```

## offsetof

Returns byte offset of a field within a struct. Lives in `<stddef.h>`.

```c
offsetof(struct S, a)  // 0
offsetof(struct S, c)  // 4
offsetof(struct S, d)  // 8
```

Use for debugging layout, serialization, and binary protocol implementation.

## __attribute__((packed))

Removes all padding. GCC/Clang extension.

```c
struct __attribute__((packed)) Packet {
    uint8_t  type;      // offset 0
    uint16_t length;    // offset 1
    uint32_t sequence;  // offset 3
};
// sizeof == 7 — exact wire format
```

**Use for:** network packets, binary file formats, hardware registers.
**Cost:** unaligned reads — slower on x86, potential crash on strict-alignment architectures.
On Apple M1, hardware handles unaligned access silently but with a performance penalty.
Use `-fsanitize=address` to catch misuse in testing.

Always use fixed-width types (`uint8_t`, `uint16_t`, `uint32_t`) in packed structs —
`char`/`short`/`int` sizes are platform-defined.

## Unions

All fields share the same memory. `sizeof` = size of largest member.

```c
union U {
    int   i;
    float f;
    char  bytes[4];
};
// sizeof == 4 — all fields overlap at offset 0
```

Writing one field and reading another reinterprets the raw bytes. Only the last-written
field has defined value — reading others is implementation-defined.

**Tagged union — variant type:**

```c
typedef enum { TYPE_INT, TYPE_FLOAT, TYPE_STR } Tag;

typedef struct {
    Tag tag;
    union {
        int    i;
        float  f;
        char  *s;
    } value;
} Variant;

Variant v = { .tag = TYPE_INT, .value.i = 42 };
```

The tag tells you which field is active. This is what Rust enums are under the hood.

**Endianness detection:**

```c
union {
    uint32_t word;
    uint8_t  bytes[4];
} u;
u.word = 0x01020304;
// little-endian: bytes[0] == 0x04 (least significant byte first)
// big-endian:    bytes[0] == 0x01
```

## Designated Initializers

Initialize specific fields by name — rest are zeroed. Order doesn't matter.

```c
struct Point { int x; int y; int z; };
struct Point p = { .z = 5, .x = 1 };  // y == 0
```

Prefer over positional initialization — survives field reordering, intent is explicit.

## Exercises

See `EXERCISES.md` — E6, E7.

1. **Layout inspector** — define structs with mixed field types, print `sizeof` and `offsetof` each field, reorder to minimize size. `src/structs.c`
2. **Tagged union** — implement a `Value` type holding `int`, `double`, or `char *` with a `value_print` function. `src/tagged_union.c`

## See also

- [[Integer Promotions]]
- [[Pointers & const]]
- [[Memory & Pointers]]
