---
tags: [c, computing, types]
status: complete
---

# Integer Promotions

> Two separate rules govern how C silently converts types in expressions — conflating them causes real bugs.

## Integer Promotion (unary)

Before any operation, types *smaller* than `int` are promoted to `int`. Always. This applies to `char`, `short`, `unsigned char`, `unsigned short`.

```c
char a = 200;
char b = 100;
char c = a + b;  // a and b promoted to int, addition done in int, result truncated back to char
```

`int` and larger types are untouched by this rule.

## Usual Arithmetic Conversions (binary)

When two operands of *different* types meet in an expression, the lower-ranked one converts to match the higher. This happens *after* integer promotion.

Rank hierarchy (highest wins):

```
long double
double
float
unsigned long long
long long
unsigned long
long
unsigned int
int
```

Both operands end up the same type before the operation executes.

## The Signed/Unsigned Trap

When `int` meets `unsigned int`, `int` loses — it converts to unsigned.

```c
int a = -1;
unsigned int b = 1;
// a converts to unsigned int → 4294967295 (UINT_MAX)
// a + b = 4294967296 → UB on assignment back to int
if (a > b) { ... }  // false — a is now UINT_MAX
```

This is the most common source of silent bugs from arithmetic conversions. Compiler warns with `-Wall`.

**In practice:** `strlen` returns `size_t` (unsigned). Comparing or assigning to `int` triggers this. Use `size_t` for anything that holds a size or index.

## sizeof

`sizeof` is a compile-time operator, not a function. Returns `size_t` (unsigned).

```c
sizeof(int)       // 4 on most 64-bit systems
sizeof(char)      // always 1, by definition
sizeof arr        // parens optional for expressions, required for types
```

**Array decay trap:** arrays decay to pointers when passed to functions. `sizeof` sees the pointer, not the array.

```c
void foo(int arr[]) {
    sizeof(arr);  // 8 — sizeof a pointer
}

int arr[10];
sizeof(arr);      // 40 — correct, full array
```

Always pass length separately when a function takes an array.

**Prefer element-based sizing:**

```c
// fragile — if type changes, this silently allocates wrong size
malloc(n * sizeof(int));

// correct — sizeof the pointed-to type, stays correct if type changes
malloc(n * sizeof(*ptr));
```

**Array length macro:**

```c
#define ARRLEN(a) (sizeof(a) / sizeof((a)[0]))
```

Only valid when `a` is an actual array in scope, not a pointer.

## See also

- [[Integer Types]]
- [[Casting & Type Aliasing]]
- [[Memory & Pointers]]
