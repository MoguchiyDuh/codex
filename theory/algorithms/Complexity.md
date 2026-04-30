---
tags:
  - algorithms
  - complexity
  - big-o
status: complete
---

# Complexity

> Asymptotic notation classifies how an algorithm's running time grows with input size, abstracting away constants and lower-order terms.

## Why asymptotics

A program's wall-clock time depends on hardware, compiler, cache state, and input. None of these are properties of the algorithm. Asymptotic analysis discards them and asks a sharper question: as input size $n \to \infty$, how does the operation count scale?

Two algorithms running at $100n$ and $n^2$ comparisons are identical for $n = 100$ but differ by a factor of $10^6$ at $n = 10^8$. The second-order behaviour dominates at scale; the constants do not.

## The three notations

Let $f(n)$ be the running time as a function of input size, and $g(n)$ a reference function (typically $n$, $n \log n$, $n^2$ etc.).

| Notation | Meaning | Bound |
|---|---|---|
| $O(g)$ | $f$ grows **at most** like $g$ | upper |
| $\Omega(g)$ | $f$ grows **at least** like $g$ | lower |
| $\Theta(g)$ | $f$ grows **exactly** like $g$ | tight |

Formal definitions:

$$f(n) \in O(g(n)) \iff \exists c > 0, n_0 \geq 0 : \forall n \geq n_0,\; 0 \leq f(n) \leq c \cdot g(n)$$

$$f(n) \in \Omega(g(n)) \iff \exists c > 0, n_0 \geq 0 : \forall n \geq n_0,\; 0 \leq c \cdot g(n) \leq f(n)$$

$$f(n) \in \Theta(g(n)) \iff f \in O(g) \text{ and } f \in \Omega(g)$$

The little-$o$ and little-$\omega$ variants drop the constant: $f \in o(g)$ means $f/g \to 0$ — strictly slower growth.

In practice "$f$ is $O(n^2)$" is conventionally read as "the worst case is $n^2$". This collapses upper bound + worst case in one phrase; CLRS keeps them separate. Worst / average / best refer to which input is being analysed; $O / \Theta / \Omega$ refer to which side the bound is on.

## Common growth classes

| Class | Name | Example |
|---|---|---|
| $O(1)$ | constant | hash lookup, stack push |
| $O(\log n)$ | logarithmic | binary search, balanced BST op |
| $O(n)$ | linear | array scan, linked-list traversal |
| $O(n \log n)$ | linearithmic | merge sort, heap sort, FFT |
| $O(n^2)$ | quadratic | insertion sort, naive matrix-vector |
| $O(n^3)$ | cubic | naive matrix multiply, Floyd-Warshall |
| $O(2^n)$ | exponential | brute-force subsets, naive TSP |
| $O(n!)$ | factorial | brute-force permutations |

The gap between $O(n \log n)$ and $O(n^2)$ is the most consequential boundary in practical algorithms — it determines whether $10^6$ inputs are tractable in seconds or in days.


## Best, average, worst case

| Case | Meaning | Use |
|---|---|---|
| Worst | maximum cost over all inputs of size $n$ | safety guarantee |
| Average | expected cost over a distribution of inputs | typical behaviour |
| Best | minimum cost over all inputs | rarely informative |

Quicksort is $\Theta(n^2)$ worst-case but $\Theta(n \log n)$ average-case under uniform random input or randomised pivots. The worst case matters when an adversary picks inputs; the average matters for benign workloads. Best case is usually a curiosity — a sorted array runs insertion sort in $\Theta(n)$, but you can't rely on that.

## Time vs space

Most analysis focuses on time. **Space complexity** counts extra memory beyond the input — output buffers, auxiliary arrays, recursion stack. Merge sort is $O(n \log n)$ time but $O(n)$ extra space; heap sort is $O(n \log n)$ time and $O(1)$ extra space. The tradeoff often dictates which is preferred in memory-constrained environments.

A recursive algorithm has space cost at least the maximum recursion depth, due to stack frames — see [[Recursion]].

## Dropping constants and lower-order terms

Inside a notation, all of these are equivalent:

$$3n^2 + 5n + 17,\quad 0.001 n^2 + 10^9 n,\quad n^2 - n,\quad \tfrac{1}{2} n^2 \quad\text{all} \in \Theta(n^2)$$

The justification: as $n$ grows, the highest-degree term dominates, and constant factors vanish under any choice of $c$ and $n_0$. The convention is to write $\Theta(n^2)$ — never $\Theta(3 n^2 + 5n)$.

This is also why $\log_2 n$, $\log_{10} n$, and $\ln n$ all belong to $\Theta(\log n)$ — they differ by a constant factor.

## Operations on growth classes

| Rule | Statement |
|---|---|
| Sum | $O(f) + O(g) = O(\max(f, g))$ |
| Product | $O(f) \cdot O(g) = O(f \cdot g)$ |
| Constant | $O(c \cdot f) = O(f)$ |
| Polynomial $\prec$ exponential | $n^k = o(c^n)$ for $c > 1$, any $k$ |
| Logarithm $\prec$ polynomial | $\log^k n = o(n^\varepsilon)$ for $\varepsilon > 0$ |

These let you simplify complex bounds without re-deriving from scratch.

## Amortized complexity

A single operation may be expensive, but its cost averaged over a sequence is cheap. Dynamic-array `push` is $O(n)$ in the worst case (resize) but $O(1)$ amortized. Treated separately in [[Amortized Analysis]].

## Video references

- ![Analyzing algorithms in 6 minutes — Intro](https://www.youtube.com/watch?v=2_Ud0TESsa0)
- ![Analyzing algorithms in 7 minutes — Asymptotic Notation](https://www.youtube.com/watch?v=u8AprTUkJjM)
- ![Big-O notation in 5 minutes](https://www.youtube.com/watch?v=__vX2sjlpXU)

## See also

- [[Recurrence Relations]]
- [[Amortized Analysis]]
- [[Recursion]]
- [[../data_structures/Index|Data Structures]]
- [[Index]]
