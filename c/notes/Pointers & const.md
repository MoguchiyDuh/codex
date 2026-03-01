---
tags: [c, memory, types]
status: complete
---

# Pointers & const

> `const` is a contract with the compiler — it enforces intent, not just style.

## const with Pointers

Three distinct meanings depending on where `const` appears:

```c
const char *p        // pointer to const data — can't modify *p, can change p
char * const p       // const pointer — can modify *p, can't change p
const char * const p // neither — fully immutable
```

Read right-to-left: `const char *p` → "p is a pointer to char that is const."

```c
const char *p = "hello";
p[0] = 'H';    // error — can't modify data
p = "world";   // fine — can move pointer

char buf[] = "hello";
char * const q = buf;
q[0] = 'H';    // fine — can modify data
q = other;     // error — can't move pointer
```

## const in Function Signatures

`const` on a parameter tells the caller "I won't modify your data." Required whenever a function only reads its input.

```c
// wrong — caller can't safely pass a string literal or const char*
int my_strlen(char *s);

// correct
int my_strlen(const char *s);
```

`const` propagates outward, never inward — you can always add `const`, never silently remove it:

```c
const char *src = "hello";
char *dst = src;        // warning: discards const qualifier
const char *dst = src;  // fine
```

For struct pointer params: add `const` when the function doesn't modify the struct:

```c
char *hm_get(const HashMap *hm, const char *key);
//           ^^^^^ doesn't modify the map
```

## Pointer Decay

Arrays are not pointers. But an array decays to a pointer to its first element in most contexts.

```c
int arr[5] = {1, 2, 3, 4, 5};
int *p = arr;       // decays to &arr[0]
```

**What's lost:** size information.

```c
int arr[5];
sizeof(arr);        // 20 — compiler knows full array
int *p = arr;
sizeof(p);          // 8 — just a pointer

void foo(int arr[]) {    // identical to: void foo(int *arr)
    sizeof(arr);         // 8 — decayed, size gone
}
```

`int arr[]` as a function parameter is syntactic sugar for `int *arr`. Always pass length separately.

Decay and const:

```c
const int arr[] = {1, 2, 3};
int *p = arr;         // warning — drops const
const int *p = arr;   // correct
```

Array of pointers decays the same way:

```c
char *names[] = {"alice", "bob"};
// decays to char** when passed to a function
```

## void *

Generic pointer — points to memory of unknown type. No arithmetic, no dereferencing without a cast.

```c
void *p = malloc(10);   // malloc returns void*
int *ip = p;            // implicit cast — fine in C, not C++
```

`const void *` follows normal rules — can't modify data through it:

```c
void *memcpy(void *dst, const void *src, size_t n);
```

GCC allows arithmetic on `void *` as an extension (treats it as `char *`), but it's non-standard — don't rely on it.

## Pointer-to-Pointer

When a function needs to modify a pointer itself, pass its address:

```c
// wrong — p is a local copy, malloc result lost, memory leaked
void alloc(int *p) {
    p = malloc(sizeof(int));
}

// correct
void alloc(int **p) {
    *p = malloc(sizeof(int));
}

int *x = NULL;
alloc(&x);   // x now points to allocated memory
```

Pattern in linked list — modifying head from inside a function:

```c
void push(Node **head, int val) {
    Node *n = malloc(sizeof(Node));
    n->val = val;
    n->next = *head;
    *head = n;
}

Node *head = NULL;
push(&head, 42);
```

Equivalent to Rust's `&mut T` — you're borrowing the pointer itself mutably.

## See also

- [[Memory & Pointers]]
- [[Integer Promotions]]
- [[Heap Memory]]
