---
tags: [c, os]
status: complete
source: functions.c
---

# Functions

> Functions in C are a calling convention over the stack — understanding them means understanding frame layout, parameter passing, and why returning a local address is always wrong.

## Declaration and definition

### Prototype vs definition

A prototype declares the function signature to the compiler before the definition appears. Without it, the compiler assumes `int` return and unspecified args (K&R legacy — avoid).

```c
int apply(char sym, int a, int b);   // prototype — tells the compiler the signature

int apply(char sym, int a, int b) {  // definition — the actual body
    // ...
}
```

### `static` functions — file scope only

`static` on a function restricts its linkage to the current translation unit. Use it to hide implementation details and avoid name collisions across files.

```c
static int helper(int x) { return x * 2; }  // invisible outside this .c file
```

### `(void)` vs `()` in prototypes

`int f(void)` means "takes no arguments". `int f()` means "takes unspecified arguments" (K&R legacy — the compiler won't check calls). Always use `(void)` for zero-argument functions in C.

## The call stack

### Stack frame layout

Each function call pushes a frame: return address, saved caller registers, local variables, parameters. On ARM64 (Apple Silicon) the stack grows downward — lower addresses are deeper frames.

### Dangling pointer — never return address of a local

```c
int *bad(void) {
    int x = 42;
    return &x;   // UB: x lives in this frame, frame is gone on return
}
```

The pointer is valid inside the function. The moment the function returns, the frame is reclaimed — the pointer now points to garbage that will be overwritten by the next call. Run with `-fsanitize=address` to catch it immediately.

## Parameter passing

### Pass-by-value — always a copy

C passes everything by value. The function receives a copy — modifying the parameter never affects the caller's variable.

### Output pointers

To return multiple values or write back to the caller, pass pointers and write through them:

```c
int divmod(int a, int b, int *quot, int *rem) {
    if (b == 0) return -1;
    if (quot != NULL) *quot = a / b;
    if (rem  != NULL) *rem  = a % b;
    return 0;
}
```

Return value is used as a status code. NULL-guarding the output pointers makes individual outputs optional.

### Arrays decay to pointers

When an array is passed to a function, it decays to a pointer to its first element — size information is lost. Always pass the length separately.

## Function pointers

### Syntax

```c
typedef int (*BinOp)(int, int);   // pointer to a function taking two ints, returning int
```

Without `typedef`:

```c
int (*fn)(int, int) = add;   // fn holds the address of add
fn(3, 4);                    // calls add(3, 4)
```

Function names decay to pointers — no `&` needed on assignment. Both `fn = add` and `fn = &add` compile, but `add` is idiomatic.

### Callbacks

Pass behavior into a function as a parameter. The receiver doesn't know or care which function it gets — it just calls it.

```c
typedef void (*Callback)(int);

void map(int *arr, size_t n, Callback cb) {
    if (!arr || !n || !cb) return;
    for (size_t i = 0; i < n; i++)
        arr[i] = cb(arr[i]);
}
```

Stdlib canonical example — `qsort`:

```c
int cmp_int(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);   // branchless, overflow-safe
}

qsort(arr, n, sizeof(int), cmp_int);
```

The comparator takes `const void *` because `qsort` is type-agnostic. You cast inside. Return negative/zero/positive — not a bool. Never use `return x - y` — signed overflow is UB.

### Dispatch table

Store function pointers in a struct keyed by a selector. No `if`/`switch` at the call site.

```c
typedef struct { char sym; BinOp fn; } Op;

static const Op ops[] = {{'+', add}, {'-', sub}, {'*', mul}, {'/', div_safe}};
#define OPS_LEN (sizeof(ops) / sizeof(ops[0]))

double calculate(char sym, double a, double b) {
    for (size_t i = 0; i < OPS_LEN; i++)
        if (ops[i].sym == sym) return ops[i].fn(a, b);
    return 0.0;   // unknown symbol
}
```

`static const` at file scope — lives in read-only data, no runtime allocation.

**ASCII indexing alternative:** `table[(int)sym]` gives O(1) dispatch but requires a 128-entry array, mostly NULL. Needs a NULL guard before calling. Worth it only for dense tables (e.g. VM opcode dispatch with 100+ ops).

## `static` locals

### Initialized once, persist across calls

```c
int next_id(void) {
    static int counter = 0;   // initialized once at program start
    return ++counter;
}
```

The initializer runs once. Subsequent calls skip it and see the accumulated state. No global variable needed — scope is still limited to the function.

## Variadic functions

### `<stdarg.h>` machinery

```c
#include <stdarg.h>

int sum_n(int count, ...) {
    int total = 0;
    va_list args;
    va_start(args, count);          // initialize after the last named param
    for (int i = 0; i < count; ++i)
        total += va_arg(args, int); // extract next arg as int
    va_end(args);                   // mandatory cleanup
    return total;
}
```

The caller must supply the count — the function has no way to know how many variadic args were passed. This is why `printf` uses a format string to count them. Passing the wrong type to `va_arg` is UB.

## See also

- [[../../theory/os/Stack vs Heap]]
- [[Memory & Pointers]]
