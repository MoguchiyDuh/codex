---
tags: [c, ieee754, floats, bits]
source: ieee.c
---

# IEEE 754

IEEE 754 (the international floating-point standard) defines how `float` and `double` are stored in memory.

## Float memory layout (32-bit)

```
bit 31    bits 30-23     bits 22-0
  sign    exponent(8)   mantissa(23)
```

- **Sign** (1 bit): 0 = positive, 1 = negative
- **Exponent** (8 bits): stored biased by 127. Actual exponent = stored − 127.
- **Mantissa** (23 bits): fractional part. Implicit leading 1 (except subnormals).

Value = `(-1)^sign × 1.mantissa × 2^(exponent−127)`

## Extracting raw bits

Access via `char*` (legal — char exemption) or `memcpy` (safest):

```c
void view(float *f) {
    unsigned int bits;
    memcpy(&bits, f, sizeof(float));    // legal reinterpretation

    printf("hex:  0x%X\n", bits);
    printf("bits: ");
    for (int i = 31; i >= 0; i--) {
        printf("%d", (bits >> i) & 1);
        if (i == 31 || i == 23)
            printf(" ");    // split: sign | exponent | mantissa
    }
    printf("\n");
}
```

`(bits >> i) & 1` isolates bit `i` by shifting it to position 0, then masking everything else off.

## Example: `1.0f`

```
0 01111111 00000000000000000000000
```

- Sign = 0 (positive)
- Exponent = 127 → 127 − 127 = 0
- Mantissa = 0 → implicit 1.0
- Value = 1.0 × 2^0 = **1.0** ✓

## Special values

| Value              | Exponent bits | Mantissa bits | Notes         |
| ------------------ | ------------- | ------------- | ------------- |
| `0.0`              | all 0         | all 0         | positive zero |
| `−0.0`             | all 0         | all 0         | sign bit = 1  |
| `+∞`               | all 1         | all 0         | `1.0f / 0.0f` |
| `−∞`               | all 1         | all 0         | sign bit = 1  |
| NaN (Not a Number) | all 1         | non-zero      | `0.0f / 0.0f` |

```c
float inf  = 1.0f / 0.0f;   // +infinity — no trap in C by default
float nan  = 0.0f / 0.0f;   // NaN
float ninf = -1.0f / 0.0f;  // -infinity
```

NaN is the only value where `x != x` is true — use this to check for NaN since there's no `isnan()` in C89 (C99 adds `<math.h>` `isnan()`).

## `double` layout (64-bit)

Same structure, larger fields: 1 sign + 11 exponent + 52 mantissa. Bias = 1023.
