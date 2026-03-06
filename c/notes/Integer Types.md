---
tags: [c, types, memory]
status: complete
source: src/integers.c, src/main.c
---

# Integer Types

> C integers have platform-dependent sizes, two's complement representation, and implicit promotion rules that silently change behavior at boundaries.

## Type sizes

Plain C types have guaranteed minimums, not fixed sizes:

| Type | Minimum | Typical (64-bit) |
|------|---------|-----------------|
| `char` | 8-bit | 8-bit |
| `short` | 16-bit | 16-bit |
| `int` | 16-bit | 32-bit |
| `long` | 32-bit | 64-bit (Linux/macOS), 32-bit (Windows) |
| `long long` | 64-bit | 64-bit |

`char` signedness is implementation-defined — never assume it's signed or unsigned.

### `<stdint.h>` — fixed-width types

```c
#include <stdint.h>

int8_t   / uint8_t    // 8-bit
int16_t  / uint16_t   // 16-bit
int32_t  / uint32_t   // 32-bit
int64_t  / uint64_t   // 64-bit
intptr_t / uintptr_t  // pointer-sized, platform-dependent
```

Use these whenever size matters — network protocols, file formats, hardware registers, portable APIs.

### `<limits.h>` and `<stdint.h>` constants

```c
INT32_MAX   //  2147483647
INT32_MIN   // -2147483648
UINT32_MAX  //  4294967295
SIZE_MAX    //  2^64-1 on 64-bit
```

### `<inttypes.h>` — printf format macros

```c
#include <inttypes.h>
printf("%" PRIu32 "\n", x);  // correct for uint32_t on all platforms
printf("%" PRId64 "\n", y);  // correct for int64_t
```

`%u` always expects `unsigned int` (32-bit). Using it with `uint64_t` is UB on all platforms.

## Signed vs unsigned

### Two's complement

Negatives stored by inverting all bits and adding 1. `INT8_MIN = -128`, `INT8_MAX = 127` — one extra negative value because the sign bit isn't symmetric.

### Signed overflow — undefined behavior

```c
int32_t x = INT32_MAX;
x++;  // UB — compiler assumes signed overflow never happens
```

The compiler exploits this for optimization — it can eliminate overflow checks:

```c
// with -O2, compiler may prove this is always true and remove the branch
if (x + 1 > x) { ... }
```

In practice on x86 you'll often see wraparound to `INT32_MIN`, but you cannot rely on it.

### Unsigned wraparound — defined behavior

```c
uint8_t x = 255; x++;  // 0   — guaranteed
uint8_t y = 0;   y--;  // 255 — guaranteed, modulo 2^8
```

Unsigned arithmetic is modulo 2^N by definition. Safe to rely on.

### Mixing signed and unsigned

When a signed and unsigned value meet in an expression, **signed converts to unsigned**:

```c
int   a = -1;
unsigned int b = 1;
if (a < b)  // -1 → UINT_MAX, UINT_MAX < 1 is false — counterintuitive
```

Classic bug:

```c
int len = get_len();          // returns -1 on error
if (len < sizeof(buf))        // sizeof is size_t (unsigned)
    // len → SIZE_MAX, check is always false → buffer overflow
```

Compiler catches this with `-Wsign-compare` (included in `-Wall`).

## Integer promotion

Any type smaller than `int` is promoted to `int` before arithmetic:

```c
uint8_t a = 200, b = 100;
uint8_t c = a + b;  // a, b promoted to int → result 300 → truncated to 44
```

**Usual arithmetic conversions** — when two different integer types meet:
1. Both get promoted to at least `int`
2. If same type → done
3. If same signedness → smaller converts to larger
4. If different signedness → signed converts to unsigned

## Safe overflow checks

Must check *before* the operation — checking after triggers the UB you're trying to detect:

```c
// signed addition — check before
int safe_add_i32(int32_t a, int32_t b, int32_t *out) {
    if (a > 0 && b > INT32_MAX - a) return -1;  // positive overflow
    if (a < 0 && b < INT32_MIN - a) return -1;  // negative overflow
    *out = a + b;
    return 0;
}

// unsigned — wraparound check
if (a > UINT32_MAX - b) { /* would wrap */ }
```

## Shift operators

```c
x << n   // multiply by 2^n (left shift)
x >> n   // divide by 2^n — logical (zero-fill) for unsigned, arithmetic (sign-fill) for signed
```

Shifting by ≥ width is UB:
```c
uint32_t x = 1;
x << 32;   // UB — shift amount equals type width
x << 31;   // ok
```

Always use `1u << n` or `(uint32_t)1 << n` for bit manipulation — avoids signed shift UB.

## Bit manipulation patterns

```c
x |=  (1u << n)    // set bit n
x &= ~(1u << n)    // clear bit n
x ^=  (1u << n)    // toggle bit n
(x >> n) & 1       // test bit n
x & (x - 1)        // clear lowest set bit
x & (-x)           // isolate lowest set bit (works due to two's complement)
```

## `-fsanitize=undefined`

Catches UB at runtime during development:

```bash
gcc -fsanitize=undefined,address -g -O1 file.c
```

| Sanitizer | Catches |
|-----------|---------|
| UBSan | signed overflow, shift past width, misaligned access, divide by zero |
| ASan | buffer overflow, use-after-free, heap leaks |

Use both during development. Strip for release builds.

## Exercises

See `EXERCISES.md` — E10.

1. **safe_add_i32** — signed addition without triggering overflow UB. `src/main.c`

## See also

- [[Types & Operators]]
- [[Casting & Type Aliasing]]
- [[../../theory/computing/Data Representation]]
