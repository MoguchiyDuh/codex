---
tags: [c, os]
status: complete
source: ptr_ref.c
---

# Memory & Pointers

> C's direct access to memory — every variable has an address, and pointers are variables that hold one.

## Addresses and pointer types

Every variable occupies memory with a fixed address for its lifetime. `&x` produces that address; `*p` dereferences it.

```c
int a = 42;
int *p = &a;   // p holds the address of a
*p = 99;       // writes through the pointer — a is now 99
```

A pointer type encodes both the address and the type stored there. `int *` and `float *` may hold the same numeric address but dereference differently.

## Pass-by-pointer

C is pass-by-value. To mutate a caller's variable, pass its address:

```c
void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

swap(&x, &y);
```

Without `&`, the function receives a copy — the original is unchanged.

## Pointer arithmetic

Arithmetic steps by the size of the pointed-to type, not by bytes:

```c
int arr[] = {10, 20, 30};
int *p = arr;    // arr decays to &arr[0]

*(p + 1)         // arr[1] — steps sizeof(int) bytes forward
arr[i]           // identical to *(arr + i)
```

`p[i]` and `*(p + i)` compile to the same instruction.

## Array decay

Arrays are not pointers, but decay to a pointer to their first element when passed to a function:

```c
void sum(int *arr, int len) { ... }

int nums[] = {1, 2, 3};
sum(nums, 3);   // nums decays to &nums[0]
```

Array size is lost at decay — always pass length separately.

## `sizeof` and `size_t`

`sizeof` returns the size in bytes as `size_t` (unsigned, pointer-sized). Print with `%zu`.

```c
sizeof(int)                          // 4
sizeof(arr)                          // total bytes — only valid in the same scope
sizeof(arr) / sizeof(arr[0])         // element count
```

Inside a function receiving `int *arr`, `sizeof(arr)` returns 8 (pointer size), not the array size.

## Tasks

1. **swap** — implement `swap(int *a, int *b)` using only pointer parameters, no return value. `src/ptr_ref.c`
2. **array sum** — write `sum(int *arr, int len)`. Inside the function, print `sizeof(arr)` and explain the result. `src/ptr_ref.c`
3. **pointer walk** — iterate over an array using only pointer arithmetic — no index variable, no `[]`. `src/ptr_ref.c`
4. **sizeof table** — print `sizeof` for `int`, `int *`, `int **`, `char`, `double`, and a struct of your choice. `src/ptr_ref.c`
5. **string length via pointer** — implement `strlen` using only pointer arithmetic, no index. `src/ptr_ref.c`

## See also

- [[../../theory/os/Stack vs Heap]]
- [[../../theory/architecture/Memory Hierarchy]]
- [[Heap Memory]]
