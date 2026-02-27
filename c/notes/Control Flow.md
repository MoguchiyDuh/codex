---
tags: [c, computing]
status: stub
source: control.c
---

# Control Flow

> C's control structures map directly to branch and jump instructions — no hidden overhead.

## `if` / `else if` / `else`

### Truthiness in C — zero is false, everything else is true

### Dangling `else`

## `switch`

### Fall-through behavior

### `break` and `default`

### When to prefer `switch` over `if-else` chains

## `for`

### Anatomy: init, condition, post

### `for` with pointer iteration

## `while` and `do-while`

### When `do-while` is the right choice

## `break`, `continue`, `goto`

### `goto` — only legitimate uses (error cleanup pattern)

## Tasks

1. **FizzBuzz** — classic. Then rewrite it using a lookup table instead of branching.
2. **Binary search** — implement iteratively with a `while` loop. Verify it handles empty arrays and single-element arrays.
3. **State machine** — implement a simple lexer that classifies characters as letters, digits, or whitespace using `switch`. Count tokens in a string.
4. **Goto cleanup** — write a function that opens two files and allocates memory. Use `goto` for the error path to ensure cleanup. Compare to the nested-if equivalent.

## See also

- [[Functions]]
- [[../../theory/algorithms/Searching]]
- [[../../theory/algorithms/Complexity]]
