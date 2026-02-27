---
tags: [c, memory, pointers]
source: ptr_ref.c
---

# Memory & Pointers

## Variables as named memory regions

Every variable is a named region of memory with an address. The address is fixed for the variable's lifetime (stack variables move only if the frame moves, which it doesn't mid-execution).

```c
int a = 1;
printf("%d (%p)\n", a, &a);  // value and address
```

## `&` and `*`

- `&x` — address-of: produces a pointer to `x`
- `*p` — dereference: reads/writes the value at the address `p` holds

```c
int a = 1, b = 2;

void swap(int *a, int *b) {
    int temp = *b;
    *b = *a;
    *a = temp;
}

swap(&a, &b);   // pass addresses, not values
```

Without `&`, C passes by value — the function gets a copy and the original is unchanged.

## Pointer arithmetic

Arithmetic on a pointer steps by the size of the pointed-to type, not by bytes:

```c
int arr[] = {1, 2, 3, 4, 5};
int *p = arr;       // arr decays to &arr[0]

p + 1               // points to arr[1] (+4 bytes on 32/64-bit int)
*(p + 2)            // same as arr[2]
```

`arr[i]` is exactly `*(arr + i)` — indexing is pointer arithmetic + dereference.

## `sizeof` and `size_t`

`sizeof` returns the size in bytes as a `size_t` (unsigned, pointer-sized). Print with `%zu`.

```c
printf("%zu\n", sizeof(int));       // 4
printf("%zu\n", sizeof(arr[0]));    // 4

int length = sizeof(arr) / sizeof(arr[0]);  // element count
```

### `sizeof` on a pointer always returns 8 (on 64-bit)

When an array decays to a pointer (passed to a function), `sizeof` gives the pointer size, not the array size:

```c
int sum(int *arr, int len) {
    // sizeof(arr) == 8 here — arr is a pointer, not an array
    // must pass len explicitly
}
```

This is why C functions that take arrays always need a separate length parameter.

## Passing arrays to functions

Arrays decay to a pointer to their first element. The function receives `int *`, not `int[]`:

```c
int arr[] = {1, 2, 3, 4, 5};
int res = sum(arr, 5);      // arr decays to &arr[0]
```
