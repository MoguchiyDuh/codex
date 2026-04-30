---
tags:
  - algorithms
  - dp
  - dynamic-programming
status: complete
---

# Dynamic Programming

> Solve a problem by combining solutions to overlapping subproblems, computing each subproblem only once.

## When DP applies

A problem admits a DP solution when it has both:

| Property | Meaning |
|---|---|
| **Optimal substructure** | An optimal solution is built from optimal solutions to smaller subproblems |
| **Overlapping subproblems** | The same subproblem recurs many times in a naive recursion |

Optimal substructure alone gives [[Divide and Conquer]]. Adding overlap is what creates the speedup: store each subproblem's answer, look it up instead of recomputing.

The contrast: greedy algorithms also rely on optimal substructure but make a single locally-optimal choice without exploring alternatives — see [[Greedy Algorithms]].

## Two implementations of the same idea

### Top-down: memoization

Write the natural recursion. Cache results in a table indexed by the subproblem's parameters. On each call, check the cache first.

```pseudo
fib_memo(n, memo):
    if n < 2: return n
    if memo[n] is not set:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]
```

Recursion is preserved; cache turns exponential into linear.

### Bottom-up: tabulation

Order the subproblems so that each is solved after its dependencies. Fill a table iteratively.

```pseudo
fib_tab(n):
    f[0] = 0; f[1] = 1
    for i = 2 to n:
        f[i] = f[i-1] + f[i-2]
    return f[n]
```

Same time complexity, no recursion stack, often better constants.

| | Memoization | Tabulation |
|---|---|---|
| Style | recursive + cache | iterative table fill |
| Stack | $\Theta(\text{recursion depth})$ | $\Theta(1)$ (apart from table) |
| Subproblems computed | only those reachable | all of them |
| Easier to write when | recursion is natural | dependency order is clear |

## The Fibonacci illustration

Naive `fib(n) = fib(n-1) + fib(n-2)` makes two recursive calls per node, building a tree of size $\Theta(\varphi^n)$. The same `fib(k)` is recomputed exponentially many times.

![[dp_memo_vs_tab.png]]

Memoization replaces the binary recursion tree with a path through $n+1$ unique subproblems — $\Theta(n)$ time, $\Theta(n)$ space. Tabulation walks the same $n+1$ values iteratively; with rolling state, $\Theta(1)$ space.

## DP recipe

1. **Define the subproblem.** What does $\text{dp}[i]$ (or $\text{dp}[i][j]$, etc.) represent? Be precise: "the minimum cost to..." — not just a number.
2. **Write the recurrence.** Express $\text{dp}[i]$ in terms of smaller indices, with explicit base cases.
3. **Determine subproblem order.** Make sure dependencies are computed first.
4. **Implement** as memoization or tabulation.
5. **Reconstruct the solution** if you need the actual choice, not just its cost — usually by recording the argmax/argmin alongside the dp value, then back-tracing.

## Classic problems

### Longest common subsequence (LCS)

Given two sequences $X[1..m]$ and $Y[1..n]$, find the longest sequence appearing as a (non-contiguous) subsequence of both.

**Subproblem.** $\text{dp}[i][j]$ = length of LCS of $X[1..i]$ and $Y[1..j]$.

**Recurrence.**

$$
\text{dp}[i][j] =
\begin{cases}
0 & i = 0 \text{ or } j = 0 \\
\text{dp}[i-1][j-1] + 1 & X[i] = Y[j] \\
\max(\text{dp}[i-1][j],\; \text{dp}[i][j-1]) & X[i] \neq Y[j]
\end{cases}
$$

**Complexity.** $\Theta(mn)$ time and space. Used in `diff`, bioinformatics sequence alignment.

![[dp_lcs_table.png]]

### Edit distance (Levenshtein)

Minimum number of insertions, deletions, substitutions to turn $X$ into $Y$.

$$
\text{dp}[i][j] =
\begin{cases}
i & j = 0 \\
j & i = 0 \\
\text{dp}[i-1][j-1] & X[i] = Y[j] \\
1 + \min(\text{dp}[i-1][j],\; \text{dp}[i][j-1],\; \text{dp}[i-1][j-1]) & \text{otherwise}
\end{cases}
$$

$\Theta(mn)$. Used by spell-checkers, fuzzy search, version-control merge.

### 0/1 knapsack

$n$ items, each with weight $w_i$ and value $v_i$, capacity $W$. Maximise total value subject to total weight $\leq W$, each item taken at most once.

**Subproblem.** $\text{dp}[i][w]$ = max value using items $1..i$ with weight budget $w$.

$$
\text{dp}[i][w] =
\begin{cases}
0 & i = 0 \\
\text{dp}[i-1][w] & w_i > w \\
\max(\text{dp}[i-1][w],\; v_i + \text{dp}[i-1][w - w_i]) & \text{otherwise}
\end{cases}
$$

$\Theta(nW)$. **Pseudo-polynomial** — polynomial in the *value* of $W$, not its bit length. NP-hard if encoded compactly.

### Coin change

Minimum number of coins from denominations $\{c_1, \dots, c_k\}$ summing to $V$ (unbounded supply).

$$\text{dp}[v] = 1 + \min_{c_i \leq v} \text{dp}[v - c_i], \quad \text{dp}[0] = 0$$

$\Theta(kV)$. The greedy approach (always take the largest coin that fits) is optimal for the US coin system but not in general — DP is the safe bet.

### Matrix-chain multiplication

Given matrices $A_1, A_2, \dots, A_n$ with dimensions $p_0 \times p_1, p_1 \times p_2, \dots$, choose a parenthesisation minimising scalar multiplications.

**Subproblem.** $\text{dp}[i][j]$ = min cost of multiplying $A_i \cdots A_j$.

$$\text{dp}[i][j] = \min_{i \leq k < j} \left( \text{dp}[i][k] + \text{dp}[k+1][j] + p_{i-1} p_k p_j \right)$$

$\Theta(n^3)$. The pattern — splitting at every possible point $k$ — recurs in CYK parsing, matrix-chain ordering, and many tree-DP problems.

## Time–space tradeoffs

The DP table can sometimes be reduced from 2D to 1D by observing that the recurrence touches only a fixed number of previous rows. LCS for example computes row $i$ from row $i-1$ — keep two rows and toggle. Drops space from $\Theta(mn)$ to $\Theta(\min(m, n))$ at no time cost. Useful when only the optimal *value* is needed, not the path.

## DP vs other paradigms

| Paradigm | Subproblems | Choice |
|---|---|---|
| Divide and conquer | independent | one — combine all results |
| Dynamic programming | overlapping | try all, take the best |
| Greedy | none — committed | one locally-optimal choice |
| Backtracking | combinatorial search tree | try all, prune impossible |

DP can be seen as memoised exhaustive search: enumerate all options at each step, but never re-explore the same subproblem.

## See also

- [[Recursion]]
- [[Divide and Conquer]]
- [[Greedy Algorithms]]
- [[Backtracking]]
- [[Index]]
