---
tags: [c, computing]
status: stub
source: integers.c
---

# Integer Types

> C integers have platform-dependent sizes, two's complement representation, and implicit promotion rules that silently change behavior at boundaries.

## Type sizes

### `char` is 1 byte — signed or unsigned, implementation-defined

### `short`, `int`, `long`, `long long` — guaranteed minimums, not fixed

### `<stdint.h>` fixed-width types: `int8_t`, `uint16_t`, `int32_t`, `uint64_t`

### `<limits.h>`: `INT_MAX`, `INT_MIN`, `UINT_MAX`, etc.

## Signed vs unsigned

### Two's complement — how negatives are stored

### Signed overflow is UB — the compiler may assume it never happens

### Unsigned overflow wraps — defined behavior, modular arithmetic

### Mixing signed and unsigned in expressions — conversion rules

## Integer promotion

### Smaller types promote to `int` in expressions

### Usual arithmetic conversions — both operands to the wider type

### Dangerous pattern: `unsigned - unsigned` can wrap to a huge positive

## Shift operators

### Left shift: `x << n` — multiply by 2ⁿ

### Right shift: `x >> n` — arithmetic (signed) vs logical (unsigned)

### Shifting by ≥ width is UB

## Bit manipulation patterns

```c
x |=  (1 << n)    // set bit n
x &= ~(1 << n)    // clear bit n
x ^=  (1 << n)    // toggle bit n
(x >> n) & 1      // test bit n
x & (x - 1)       // clear lowest set bit
x & (-x)          // isolate lowest set bit
```

## Tasks

1. **Overflow trap** — write a function `safe_add(int a, int b, int *out)` that returns 0 on overflow without triggering UB. Use `INT_MAX` from `<limits.h>`.
2. **Unsigned subtraction bug** — write `strlen`-style function using `size_t`. Demonstrate that `len - 1` when `len == 0` wraps to `SIZE_MAX`. Fix it.
3. **Bit flags** — implement a compact permission system: define 8 flags in a `uint8_t`. Set, clear, toggle, and test flags using only bitwise operators.
4. **Popcount** — count the number of set bits in a `uint32_t` without using `__builtin_popcount`. Then compare your result to the builtin.
5. **Endianness** — use a `union { uint32_t u; uint8_t b[4]; }` to determine if your machine is little- or big-endian.

## See also

- [[Types & Operators]]
- [[Casting & Type Aliasing]]
- [[../../theory/computing/Data Representation]]
- [[../../theory/computing/Number Systems]]
