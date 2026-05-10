---
tags:
  - algorithms
  - divide-and-conquer
  - paradigm
status: complete
---

# Divide and Conquer

> A design paradigm: split a problem into smaller independent subproblems of the same kind, solve each recursively, and combine their results.

## Three steps

1. **Divide** the input into smaller instances of the same problem.
2. **Conquer** each subproblem recursively. If small enough, solve directly (base case).
3. **Combine** the subproblem solutions into a solution for the original input.

The recurrence on running time is $T(n) = a T(n/b) + f(n)$ — $a$ subproblems each of size $n/b$, plus $f(n)$ work to divide and combine. Solving it (substitution, recursion-tree, or master theorem) is the analysis half of the paradigm. Detailed in [[Recurrence Relations]].

## Canonical examples

| Algorithm                    | Divide                         | Conquer                         | Combine                      | Time                   |
| ---------------------------- | ------------------------------ | ------------------------------- | ---------------------------- | ---------------------- |
| [[Merge Sort]]               | split array in half            | sort each half                  | merge                        | $\Theta(n \log n)$     |
| [[Quick Sort]]               | partition around pivot         | sort each side                  | nothing                      | $\Theta(n \log n)$ avg |
| [[Searching\|Binary search]] | split sorted array in half     | search one side                 | nothing                      | $\Theta(\log n)$       |
| [[Selection\|Quickselect]]   | partition                      | recurse one side                | nothing                      | $\Theta(n)$ avg        |
| Karatsuba multiplication     | split numbers into halves      | three half-size multiplications | shift-and-add                | $\Theta(n^{\log_2 3})$ |
| Strassen matrix multiply     | split into $2 \times 2$ blocks | seven block multiplications     | block additions              | $\Theta(n^{\log_2 7})$ |
| Closest pair of points       | split by $x$-median            | recurse each side               | merge across the split strip | $\Theta(n \log n)$     |
| FFT                          | split by even/odd indices      | recurse                         | butterfly combine            | $\Theta(n \log n)$     |

A common pattern: the _combine_ step is the algorithmic insight. Merge sort's merge is linear; that's why splitting wins. Strassen's seven multiplications instead of eight is the reason it beats $\Theta(n^3)$.

## When divide and conquer pays off

The paradigm beats the naive iterative approach when:

- **Subproblems are independent.** Solving one doesn't depend on another's result. (Otherwise consider [[Dynamic Programming]] for overlapping subproblems.)
- **Combining is cheaper than the saved work.** If combining costs $\Theta(n^2)$ for an $n$-sized split, you've gained nothing.
- **The split is balanced.** Unbalanced splits degrade to $\Theta(n^2)$ — see quicksort's worst case.

When subproblems overlap, divide and conquer recomputes them. The cure is memoisation: stash each subproblem's answer the first time you compute it. That's the bridge to dynamic programming.

## Master theorem at a glance

For $T(n) = a T(n/b) + f(n)$:

| Compare $f(n)$ to $n^{\log_b a}$         | Solution                                                  |
| ---------------------------------------- | --------------------------------------------------------- |
| $f$ is polynomially smaller              | $\Theta(n^{\log_b a})$ — leaves dominate                  |
| $f$ matches up to log factors            | $\Theta(n^{\log_b a} \log^{k+1} n)$ — every level equally |
| $f$ is polynomially larger (and regular) | $\Theta(f(n))$ — root dominates                           |

Worked applications and the precise statement are in [[Recurrence Relations]].

![[master_theorem_cases.png]]

## Karatsuba multiplication

Multiply two $n$-digit numbers. Schoolbook multiplication is $\Theta(n^2)$. Karatsuba (1960) was the first sub-quadratic algorithm.

Split each number into halves: $X = X_1 \cdot 10^{n/2} + X_0$, similarly $Y$. Naive expansion needs four products $X_1 Y_1, X_1 Y_0, X_0 Y_1, X_0 Y_0$. Karatsuba uses an algebraic identity to compute the middle term from one extra multiplication:

$$X_1 Y_0 + X_0 Y_1 = (X_1 + X_0)(Y_1 + Y_0) - X_1 Y_1 - X_0 Y_0$$

So three multiplications suffice. Recurrence $T(n) = 3 T(n/2) + \Theta(n)$, by master theorem Case 1, $T(n) = \Theta(n^{\log_2 3}) \approx \Theta(n^{1.585})$.

The successor of Karatsuba is Schönhage-Strassen ($\Theta(n \log n \log \log n)$ via FFT). Recently surpassed by Harvey-Hoeven ($\Theta(n \log n)$).

## Strassen matrix multiplication

Two $n \times n$ matrices. School method: $\Theta(n^3)$. Strassen splits into $2 \times 2$ blocks; the naive eight block products would give $T(n) = 8 T(n/2) + \Theta(n^2) = \Theta(n^3)$. Strassen replaces them with seven cleverly combined products:

$$T(n) = 7 T(n/2) + \Theta(n^2) \implies T(n) = \Theta(n^{\log_2 7}) \approx \Theta(n^{2.807})$$

Practical only for very large dense matrices because the constant factor is high and numerical stability degrades. State-of-the-art is around $\Theta(n^{2.37})$ but with constants too large for any real implementation.

## Closest pair of points

Given $n$ points in the plane, find the two closest. Brute force is $\Theta(n^2)$. Divide-and-conquer in $\Theta(n \log n)$:

1. Sort points by $x$.
2. Recurse on left and right halves; let $\delta$ be the smaller of the two minimum distances.
3. Combine: any cross-half pair closer than $\delta$ lies within a vertical strip of width $2\delta$ around the median $x$. Sort the strip by $y$; for each point, only the next 7 in $y$-order can possibly be within $\delta$. Linear scan finds any improvement.

Combine step is $\Theta(n)$, recurrence $T(n) = 2 T(n/2) + \Theta(n) = \Theta(n \log n)$. The $\delta$-strip / 7-neighbours geometry is the elegant combine step.

## Limits of divide and conquer

| Problem type                          | Better paradigm         |
| ------------------------------------- | ----------------------- |
| Overlapping subproblems               | [[Dynamic Programming]] |
| Local greedy choice suffices          | [[Greedy Algorithms]]   |
| Search with constraints / pruning     | [[Backtracking]]        |
| Subproblems with mutable shared state | iterative / amortized   |

## See also

- [[Recurrence Relations]]
- [[Merge Sort]]
- [[Quick Sort]]
- [[Searching]]
- [[Selection]]
- [[Dynamic Programming]]
- [[Index]]
