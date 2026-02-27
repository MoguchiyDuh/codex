---
tags: [c, computing]
status: complete
source: types.c
---

# Types & Operators

> C's type system is minimal and close to hardware — sizes are implementation-defined, and operators follow strict precedence and promotion rules.

## Primitive types

### Integer types

| Type | Guaranteed minimum size | Typical on 64-bit |
|---|---|---|
| `char` | 1 byte | 1 byte |
| `short` | 2 bytes | 2 bytes |
| `int` | 2 bytes | 4 bytes |
| `long` | 4 bytes | 8 bytes (Linux/macOS), 4 bytes (Windows) |
| `long long` | 8 bytes | 8 bytes |

All integer types have a `signed` and `unsigned` variant. `char` signedness is implementation-defined — use `signed char` or `unsigned char` explicitly when it matters.

### Floating-point types

| Type | Size | Precision |
|---|---|---|
| `float` | 4 bytes | ~7 significant decimal digits |
| `double` | 8 bytes | ~15–16 significant decimal digits |
| `long double` | 10–16 bytes | platform-dependent |

`double` is the default floating-point type in C — undecorated literals like `3.14` are `double`. Use `3.14f` for `float`.

### `void`

Not a type for variables — used as a return type meaning "nothing returned", and as `void *` meaning "pointer to untyped memory". `void *` can be assigned to and from any pointer type without a cast.

### `_Bool` and `<stdbool.h>`

C99 introduced `_Bool` (stores 0 or 1). `<stdbool.h>` defines `bool`, `true`, and `false` as macros over it:

```c
#include <stdbool.h>

bool flag = true;
bool result = (x > 0);   // any non-zero value converts to 1
```

In C, truthiness is numeric: `0` is false, everything else is true. There is no dedicated boolean operator — `&&`, `||`, `!` operate on integers and return `0` or `1`.

## Type sizes and `<stdint.h>`

The C standard guarantees only minimum sizes, not exact ones. `int` being 4 bytes is common but not guaranteed. This matters for portable code, binary formats, and network protocols.

`<stdint.h>` provides exact-width types:

```c
#include <stdint.h>

int8_t   x;   // exactly 8 bits, signed
uint8_t  y;   // exactly 8 bits, unsigned
int32_t  z;   // exactly 32 bits, signed
uint64_t w;   // exactly 64 bits, unsigned
```

`<limits.h>` provides the range constants:

```c
#include <limits.h>

INT_MAX     //  2147483647
INT_MIN     // -2147483648
UINT_MAX    //  4294967295
LLONG_MAX   //  9223372036854775807
```

`<stdint.h>` also provides `INT8_MAX`, `UINT32_MAX`, etc. for the fixed-width types, and `SIZE_MAX` for the maximum value of `size_t`.

## Operators

### Arithmetic

```c
int a = 17, b = 5;

a + b   // 22
a - b   // 12
a * b   // 85
a / b   // 3   — integer division, truncates toward zero
a % b   // 2   — remainder, same sign as dividend
```

Integer division truncates — `17 / 5` is `3`, not `3.4`. For float division, at least one operand must be a `float` or `double`:

```c
(double)a / b    // 3.4
(float)a / b     // 3.4f
```

### Relational

Return `1` (true) or `0` (false) as `int`. Never compare floating-point with `==` — use an epsilon:

```c
a == b    // 0
a != b    // 1
a >  b    // 1
a <  b    // 0

// float comparison
fabs(f1 - f2) < 1e-9   // correct
f1 == f2               // almost always wrong
```

### Logical

Short-circuit: `&&` stops at the first `0`, `||` stops at the first non-zero. The right side is not evaluated if the result is already determined:

```c
int x = 0;
x != 0 && expensive_fn();   // expensive_fn never called
x == 0 || expensive_fn();   // expensive_fn never called
```

### Bitwise

Operate on individual bits of integer types:

```c
unsigned int a = 0b1010;   // 10
unsigned int b = 0b1100;   // 12

a & b    // 0b1000 =  8  — AND: bit set in both
a | b    // 0b1110 = 14  — OR:  bit set in either
a ^ b    // 0b0110 =  6  — XOR: bit set in exactly one
~a       // 0b...10101   — NOT: flip all bits
a << 1   // 0b10100 = 20 — left shift: multiply by 2
a >> 1   // 0b0101  =  5 — right shift: divide by 2
```

Right shift on signed values is arithmetic (sign-extends) on most platforms but is technically implementation-defined. Use unsigned types for bitwise operations.

### Assignment and compound assignment

```c
x = 5;
x += 3;   // x = x + 3
x -= 1;   // x = x - 1
x *= 2;   // x = x * 2
x /= 4;   // x = x / 4
x %= 3;   // x = x % 3
x &= 0xFF;
x |= 0x01;
x ^= 0x10;
x <<= 2;
x >>= 1;
```

All compound assignments evaluate the left side once — important when it has side effects.

### Increment and decrement

```c
x++   // post-increment: use x, then increment
++x   // pre-increment:  increment, then use x
x--   // post-decrement
--x   // pre-decrement
```

In isolation `x++` and `++x` are identical. The difference matters only when the value is used in a larger expression. Avoid both in complex expressions — it invites undefined behavior when the same variable appears twice.

### Ternary

```c
int max = (a > b) ? a : b;
```

Equivalent to an `if-else` that produces a value. Both branches must be the same type (or compatible). Nest sparingly — readability degrades fast.

### Precedence

Higher rows bind tighter. When in doubt, use parentheses.

| Precedence | Operators | Associativity |
|---|---|---|
| 15 | `()` `[]` `->` `.` | left |
| 14 | `!` `~` `++` `--` `+` `-` `*` `&` `sizeof` (unary) | right |
| 13 | `*` `/` `%` | left |
| 12 | `+` `-` | left |
| 11 | `<<` `>>` | left |
| 10 | `<` `<=` `>` `>=` | left |
| 9 | `==` `!=` | left |
| 8 | `&` | left |
| 7 | `^` | left |
| 6 | `\|` | left |
| 5 | `&&` | left |
| 4 | `\|\|` | left |
| 3 | `?:` | right |
| 2 | `=` `+=` `-=` etc. | right |
| 1 | `,` | left |

Common trap: `&` and `|` bind looser than `==`, so `x & 0xFF == 0` parses as `x & (0xFF == 0)` — always `0`. Write `(x & 0xFF) == 0`.

## Implicit conversions and integer promotion

### Integer promotion

Any type narrower than `int` — `char`, `short`, `_Bool` — is promoted to `int` (or `unsigned int` if `int` can't hold the value) before arithmetic. This happens silently:

```c
char a = 200;
char b = 100;
int  c = a + b;   // a and b promote to int before adding — no overflow
```

### Usual arithmetic conversions

When two operands have different types, both are converted to a common type before the operation. Rules in order:
1. If either is `long double` → both become `long double`
2. Else if either is `double` → both become `double`
3. Else if either is `float` → both become `float`
4. Else both are integer — apply promotion, then convert to the wider/unsigned type

### Signed/unsigned mixing

When a signed and unsigned integer are mixed, the signed value converts to unsigned — which silently wraps for negatives:

```c
int           a = -1;
unsigned int  b = 1;

a < b    // false — a converts to UINT_MAX (4294967295), which is > 1
```

This is one of C's most common silent bugs. Enable `-Wsign-compare` to catch it.

## `const` and `volatile`

### `const`

Prevents modification through that name. Does not make the object immutable — a non-const pointer to the same memory can still write it:

```c
const int x = 10;
x = 20;              // compile error

const int *p = &x;
*p = 20;             // compile error

int *q = (int *)&x;
*q = 20;             // compiles, but UB if x is truly const-qualified
```

`const` on a pointer parameter signals to callers that the function won't modify the data:

```c
size_t strlen(const char *s);   // s won't be modified
```

### `volatile`

Tells the compiler the value may change outside its control — do not cache it in a register, re-read from memory on every access. Used for:
- Hardware-mapped registers
- Variables modified by a signal handler
- Variables shared between threads (though `volatile` alone is not sufficient for threading — use atomics)

```c
volatile int flag = 0;   // signal handler sets this
while (!flag) { }        // compiler must re-check flag every iteration
```

## Tasks

1. **Type sizes** — print `sizeof` for every primitive type on your machine. Note which match your expectations. `src/types.c`
2. **Overflow demo** — show that `INT_MAX + 1` is UB for signed but wraps for unsigned. Use `<limits.h>`. Compile with and without `-fsanitize=undefined` and compare. `src/types.c`
3. **Bitwise flags** — define 4 permission flags as `#define` bit masks (`READ`, `WRITE`, `EXEC`, `STICKY`). Write `set_flag`, `clear_flag`, `has_flag` using `&`, `|`, `~`. `src/types.c`
4. **Fixed-width** — rewrite the permission flags using `uint8_t`. Verify `sizeof` is exactly 1. `src/types.c`
5. **Precedence trap** — write `x & 0xFF == 0` and print the result for `x = 0`. Explain why it's always 0. Fix it with parentheses. `src/types.c`

## See also

- [[Integer Types]]
- [[../../theory/computing/Data Representation]]
- [[../../theory/computing/Number Systems]]
