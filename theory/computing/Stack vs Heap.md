---
tags: [c, stack, heap, memory]
---

# Stack vs Heap

Two separate memory regions. Different lifetimes, different allocation mechanisms, different failure modes.

## Side-by-side

| | Stack | Heap |
|---|---|---|
| **Allocation** | Automatic (entering a scope) | Manual (`malloc`/`calloc`) |
| **Deallocation** | Automatic (leaving scope) | Manual (`free`) |
| **Speed** | O(1), just moves stack pointer | Slower — allocator bookkeeping |
| **Size** | ~8MB on Linux (fixed) | Limited by available RAM |
| **Lifetime** | Tied to the enclosing function | Until `free()` |
| **Failure** | Stack overflow (segfault) | `malloc` returns NULL |
| **Fragmentation** | None | Yes — holes accumulate over time |

## The stack

Each function call creates a **stack frame** pushed onto a LIFO (Last In First Out) stack. The frame holds:

- Local variables
- Function arguments (ABI-dependent)
- Return address
- Saved registers

Frame is pushed on call, popped on `return`. No allocator, no bookkeeping — just a single stack pointer register moving up and down.

```c
void foo(void) {
    int x = 42;     // lives in foo's frame
    int arr[256];   // 1KB on the stack — fine
}                   // frame popped here, x and arr gone
```

### Stack grows downward on x86-64

```
high address  ┌──────────────┐
              │   main()     │  ← bottom frame (oldest)
              ├──────────────┤
              │   foo()      │  ← called from main
              ├──────────────┤
              │   bar()      │  ← called from foo (newest)
low address   └──────────────┘
              ↑ grows this way
```

Earlier frames have higher addresses. `&local_in_main > &local_in_bar`.

### Dangling pointer (returning a stack address)

```c
int *bad(void) {
    int x = 42;
    return &x;      // UB — frame is gone after return
}

int *p = bad();
printf("%d\n", *p); // may print 42, garbage, or crash — undefined behavior
```

The memory `p` points to gets overwritten by the next function call.

## The heap

A large pool of memory managed by the allocator (`malloc`/`free`). You ask for a block, use it as long as you need, then return it.

```c
int *p = malloc(256 * sizeof(int));  // 1KB on the heap — survives after this function returns
if (p == NULL) { /* handle */ }

// ... use p across multiple function calls ...

free(p);
p = NULL;
```

Heap memory has no automatic lifetime — it lives until you explicitly `free` it or the process exits.

### When to use the heap

- Data that outlives the function that created it
- Size not known at compile time
- Large allocations (anything approaching stack limits)
- Dynamic data structures (linked lists, trees, hash tables, growing arrays)

## The four heap bugs

| Bug | What happens |
|---|---|
| **Memory leak** | `malloc` without `free` — memory never returned |
| **Use-after-free** | Accessing memory after `free` — silent corruption or crash |
| **Double-free** | Calling `free` twice on the same pointer — heap corruption |
| **Buffer overflow** | Writing past the allocated size — corrupts adjacent allocations |

Detect all of these with `-fsanitize=address`:

```sh
gcc -fsanitize=address -g file.c -o file && ./file
```

## Stack overflow

Stack has a fixed size (~8MB on Linux, check with `ulimit -s`). Exceed it and you get a segfault with no useful message:

```c
void infinite(void) { infinite(); }  // blows the stack

void big_local(void) {
    int arr[2000000];  // 8MB on the stack — likely overflows
}
```

Move large arrays to the heap. Use `-fsanitize=address` to catch stack buffer overflows.

## Rule of thumb

Use the stack for small, short-lived data. Use the heap for everything else.
