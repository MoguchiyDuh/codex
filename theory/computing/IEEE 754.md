---
tags: [theory, computing, ieee754, floats]
status: complete
---

# IEEE 754

> The international standard for binary floating-point arithmetic — how `float` and `double` are stored in memory.

## 32-bit layout (single precision)

```
bit 31   bits 30–23   bits 22–0
 sign    exponent(8)  mantissa(23)
```

- **Sign** (1 bit): 0 = positive, 1 = negative
- **Exponent** (8 bits): stored with a bias of 127. Actual exponent = stored − 127.
- **Mantissa** (23 bits): fractional part after the implicit leading 1.

Value = `(-1)^sign × 1.mantissa × 2^(exponent − 127)`

## 64-bit layout (double precision)

Same structure, larger fields: 1 sign + 11 exponent + 52 mantissa. Bias = 1023.

## Example: decoding `1.0`

```
0 01111111 00000000000000000000000
```

- Sign = 0 → positive
- Exponent = 127 − 127 = 0
- Mantissa = 0 → implicit 1.0
- Value = 1.0 × 2⁰ = **1.0**

## Known bit patterns

| Value | Hex | Explanation |
|---|---|---|
| `1.0` | `0x3F800000` | exp=127, mantissa=0 |
| `-1.0` | `0xBF800000` | same, sign bit set |
| `0.5` | `0x3F000000` | exp=126 (127−1) |
| `2.0` | `0x40000000` | exp=128 (127+1) |
| `0.0` | `0x00000000` | all bits zero |

## Special values

| Value | Exponent bits | Mantissa bits |
|---|---|---|
| `+0` / `−0` | all 0 | all 0 |
| `+∞` / `−∞` | all 1 | all 0 |
| NaN | all 1 | non-zero |

NaN is the only value where `x != x` is true — the standard IEEE 754 NaN check.

Subnormals: exponent all 0, mantissa non-zero — represent values smaller than the minimum normalized float. No implicit leading 1.

## Precision limits and gotchas

Not all decimals have exact binary representations:

```
0.1 + 0.2 = 0.30000000000000004
```

Single precision gives ~7 significant decimal digits. Double gives ~15–16.

Never compare floats with `==` — use an epsilon: `fabs(a - b) < 1e-9`.

## Reinterpreting bits safely

The only legal way to inspect the raw bits of a float is via `memcpy` — direct pointer casting is undefined behavior (strict aliasing):

```c
float f = 1.0f;
unsigned int bits;
memcpy(&bits, &f, sizeof(float));   // well-defined
```

## See also

- [[Data Representation]]
- [[Number Systems]]
- [[Bitwise Operations]]
