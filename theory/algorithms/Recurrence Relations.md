---
tags:
  - algorithms
  - recurrence
  - master-theorem
status: complete
---

# Recurrence Relations

> An equation that defines a function in terms of its value on smaller inputs. The natural way to express the running time of a divide-and-conquer algorithm.

## Form

A recurrence for an algorithm's running time looks like:

$$T(n) = a \cdot T(n/b) + f(n)$$

where the algorithm splits the problem into $a$ subproblems of size $n/b$ and does $f(n)$ work outside the recursive calls. Examples:

| Algorithm                 | Recurrence                           |
| ------------------------- | ------------------------------------ |
| Binary search             | $T(n) = T(n/2) + \Theta(1)$          |
| Merge sort                | $T(n) = 2T(n/2) + \Theta(n)$         |
| Karatsuba multiplication  | $T(n) = 3T(n/2) + \Theta(n)$         |
| Strassen matrix multiply  | $T(n) = 7T(n/2) + \Theta(n^2)$       |
| Naive recursive Fibonacci | $T(n) = T(n-1) + T(n-2) + \Theta(1)$ |

Solving a recurrence means finding a closed-form $\Theta$ bound on $T(n)$.

## Three solving methods

### Substitution method

Guess the bound, then prove it by induction. Useful when the recurrence's shape suggests a particular answer.

For $T(n) = 2T(n/2) + n$, guess $T(n) \leq c n \log n$ and verify:

$$T(n) \leq 2 \cdot c (n/2) \log(n/2) + n = cn(\log n - 1) + n = cn \log n - cn + n \leq cn \log n$$

provided $c \geq 1$. Base case checked separately. Conclusion: $T(n) \in O(n \log n)$.

### Recursion-tree method

Draw the recursion as a tree, label each node with the work done at that level, sum across levels.

For $T(n) = 2T(n/2) + n$:

| Level      | Subproblem size | # nodes | Work / node | Level total |
| ---------- | --------------- | ------- | ----------- | ----------- |
| 0          | $n$             | $1$     | $n$         | $n$         |
| 1          | $n/2$           | $2$     | $n/2$       | $n$         |
| 2          | $n/4$           | $4$     | $n/4$       | $n$         |
| $\vdots$   |                 |         |             |             |
| $\log_2 n$ | $1$             | $n$     | $1$         | $n$         |

Every level does $\Theta(n)$ work, tree height is $\log_2 n$, total $\Theta(n \log n)$. The recursion tree is the visual intuition behind the master theorem.

![[recursion_tree_merge_sort.png]]

### Master theorem

A formula that solves $T(n) = a T(n/b) + f(n)$ for $a \geq 1, b > 1$, and reasonable $f$, by comparing $f(n)$ to the _watershed_ function $n^{\log_b a}$.

| Case | Condition                                                                                             | Solution                                     |
| ---- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| 1    | $f(n) \in O(n^{\log_b a - \varepsilon})$ for some $\varepsilon > 0$                                   | $T(n) \in \Theta(n^{\log_b a})$              |
| 2    | $f(n) \in \Theta(n^{\log_b a} \log^k n),\; k \geq 0$                                                  | $T(n) \in \Theta(n^{\log_b a} \log^{k+1} n)$ |
| 3    | $f(n) \in \Omega(n^{\log_b a + \varepsilon})$ and regularity: $a f(n/b) \leq c f(n)$ for some $c < 1$ | $T(n) \in \Theta(f(n))$                      |

The intuition: which dominates — the leaves of the recursion tree (Case 1), uniform work across levels (Case 2), or the root (Case 3)?

### Worked applications

| Recurrence             | $a$ | $b$ | $\log_b a$               | $f(n)$ | Case      | Result                 |
| ---------------------- | --- | --- | ------------------------ | ------ | --------- | ---------------------- |
| $T(n) = 2T(n/2) + n$   | 2   | 2   | 1                        | $n$    | 2 ($k=0$) | $\Theta(n \log n)$     |
| $T(n) = 4T(n/2) + n$   | 4   | 2   | 2                        | $n$    | 1         | $\Theta(n^2)$          |
| $T(n) = T(n/2) + 1$    | 1   | 2   | 0                        | $1$    | 2         | $\Theta(\log n)$       |
| $T(n) = 3T(n/2) + n$   | 3   | 2   | $\log_2 3 \approx 1.585$ | $n$    | 1         | $\Theta(n^{\log_2 3})$ |
| $T(n) = 2T(n/2) + n^2$ | 2   | 2   | 1                        | $n^2$  | 3         | $\Theta(n^2)$          |

Karatsuba's $\Theta(n^{1.585})$ is famously below the school-method's $\Theta(n^2)$ — the master theorem makes that quantitative.

## When the master theorem doesn't apply

Recurrences outside the standard form need other tools:

- $T(n) = T(n-1) + n$ — subtractive, not divisive. Solve by unrolling: $T(n) = \sum_{k=1}^{n} k = \Theta(n^2)$.
- $T(n) = T(n-1) + T(n-2) + 1$ (Fibonacci-like) — solved via the characteristic equation $x^2 = x + 1$, giving $T(n) = \Theta(\varphi^n)$.
- Non-uniform splits, e.g. $T(n) = T(n/3) + T(2n/3) + n$ — recursion tree shows leaves at varying depths but all levels still do $\Theta(n)$, total $\Theta(n \log n)$.
- An extended **Akra-Bazzi method** generalises the master theorem to most of these cases.

## See also

- [[Complexity]]
- [[Divide and Conquer]]
- [[Merge Sort]]
- [[Quick Sort]]
- [[Index]]
