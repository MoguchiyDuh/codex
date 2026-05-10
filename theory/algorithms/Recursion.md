---
tags:
  - algorithms
  - recursion
status: complete
---

# Recursion

> A function that solves a problem by calling itself on a smaller instance, terminating at a base case.

## Anatomy

Every recursive function has two parts:

| Part           | Purpose                                                                  |
| -------------- | ------------------------------------------------------------------------ |
| Base case      | A non-recursive answer for the smallest input — terminates the recursion |
| Recursive case | Reduces the problem to a smaller instance and combines the result        |

A function missing the base case (or one whose recursive calls never approach it) does not terminate — it overflows the call stack.

```pseudo
factorial(n):
    if n ≤ 1:                # base case
        return 1
    return n * factorial(n - 1)   # recursive case
```

## Call stack and space cost

Each recursive call pushes a stack frame holding parameters, locals, and the return address. The **maximum recursion depth** equals the maximum number of frames live simultaneously.

Recursion depth $d$ contributes $\Theta(d)$ to space complexity. For `factorial(n)` that's $\Theta(n)$. For balanced recursion such as merge sort, the depth is $\Theta(\log n)$.

Stack size is bounded — a few MB on most systems, translating to roughly $10^4$–$10^5$ frames. Naive recursion on inputs of $10^6$ overflows; either rewrite iteratively or convert to tail recursion (where supported).

## Tail recursion

A call is **tail-recursive** when it is the last action of the function — its return value is returned unchanged.

```pseudo
factorial_tail(n, acc):
    if n ≤ 1:
        return acc
    return factorial_tail(n - 1, n * acc)   # tail call
```

A compiler that performs **tail-call optimisation (TCO)** rewrites the call as a jump, reusing the current frame. Stack usage drops to $\Theta(1)$. Languages with guaranteed TCO: Scheme, Standard ML, OCaml. Languages without it (Python, Java) treat tail calls like any other call — TCO is an optimisation, not a semantic guarantee.

The non-tail `factorial` above multiplies _after_ the recursive call returns, so it is not tail-recursive. The tail form accumulates the running product as a parameter.

## Recursive thinking

A recursive solution leans on three ingredients:

1. **Reduction.** Express the problem on input of size $n$ in terms of one or more instances of size $< n$.
2. **Trust the recursion.** Assume the recursive call works correctly on the smaller instance. Don't trace its execution mentally; verify only the reduction step.
3. **Terminate.** Ensure every recursive path reaches a base case in finite steps.

This is induction in disguise: base case $\equiv$ induction base, recursive step $\equiv$ inductive step.

## Tree recursion

When a function calls itself more than once, the call structure forms a tree, not a chain. Naive Fibonacci is the canonical example:

```pseudo
fib(n):
    if n < 2: return n
    return fib(n - 1) + fib(n - 2)
```

The recurrence is $T(n) = T(n-1) + T(n-2) + \Theta(1)$, with $T(n) = \Theta(\varphi^n)$ where $\varphi \approx 1.618$. Exponential — because the same subproblem is recomputed many times. The fix is **memoization** (top-down) or **tabulation** (bottom-up), turning $\Theta(\varphi^n)$ into $\Theta(n)$. Treated in [[Dynamic Programming]].

## Direct vs indirect recursion

| Form              | Pattern                         |
| ----------------- | ------------------------------- |
| Direct            | $f$ calls $f$                   |
| Indirect (mutual) | $f$ calls $g$ and $g$ calls $f$ |

Mutual recursion appears in parsers (expression / term / factor) and tree traversals over alternating node types.

## Converting recursion to iteration

Any recursion can be converted to iteration by maintaining an explicit stack — what the runtime does for you implicitly. Worth doing when:

- input is large enough to risk stack overflow,
- TCO is unavailable and the recursion is tail,
- iteration is simply clearer (linear recursion over a sequence is often a `for` loop).

DFS on a graph is the textbook example: recursive form is two lines but blows the stack on a million-node graph; iterative form uses an explicit `stack` and survives.

## When recursion is the right tool

Best suited to problems with a recursive **structure**: trees, divide-and-conquer, backtracking search, grammars. Forcing recursion onto inherently iterative problems (linear scans, accumulations) trades clarity for stack frames.

## See also

- [[Recurrence Relations]]
- [[Divide and Conquer]]
- [[Dynamic Programming]]
- [[Backtracking]]
- [[Index]]
