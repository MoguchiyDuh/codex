---
tags:
  - algorithms
  - sorting
status: complete
---

# Sorting

> Rearranging elements into a defined order. The most-studied problem in algorithms — every paradigm has a sorting algorithm built on it.

## What "sorted" means

For a sequence $A[1..n]$ and a total order $\leq$, a sort produces a permutation of $A$ satisfying $A[1] \leq A[2] \leq \cdots \leq A[n]$. The total-order requirement is real: partially-ordered data (e.g. version numbers with branches) needs topological sort, not comparison sort.

## Classification

Sorts vary along several axes; understanding them is more important than memorising any specific algorithm.

| Axis | Variants |
|---|---|
| Comparison-based vs not | reads keys via $\leq$ only / exploits key structure (digits, bits) |
| Stability | preserves order of equal keys / does not |
| In-place | uses $O(1)$ or $O(\log n)$ extra space / uses $\Theta(n)$ |
| Adaptive | runs faster on already-sorted or nearly-sorted input / does not |
| Online | processes one element at a time / needs the full input upfront |

A **stable** sort matters when sorting by a secondary key: sort by name, then by department — a stable sort by department preserves the name order within each department. An unstable sort would not.

## Elementary sorts

Quadratic sorts; useful for small inputs, as building blocks, or when memory is extremely tight.

### Insertion sort

Maintain a sorted prefix; for each new element, slide it left into position.

```pseudo
insertion_sort(A):
    for i = 2 to length(A):
        key = A[i]
        j = i - 1
        while j ≥ 1 and A[j] > key:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key
```

**Code:** `theory/algorithms/showcase/sorting/insertion_sort.py`

| Property | Value |
|---|---|
| Worst | $\Theta(n^2)$ |
| Average | $\Theta(n^2)$ |
| Best (sorted input) | $\Theta(n)$ |
| Space | $\Theta(1)$ in-place |
| Stable | yes |
| Adaptive | yes |

The best practical $n^2$ sort. Used inside hybrid sorts (Timsort, introsort) for small subarrays where its low constant beats $n \log n$ algorithms.

### Selection sort

Repeatedly find the minimum of the unsorted suffix and swap it to the front.

| Property | Value |
|---|---|
| All cases | $\Theta(n^2)$ |
| Space | $\Theta(1)$ in-place |
| Stable | no (swap can leapfrog equal keys) |

Worst inversions count, fewest swaps ($\Theta(n)$). Useful when writes are expensive (flash memory).

### Bubble sort

Repeatedly swap adjacent out-of-order pairs. Same $\Theta(n^2)$ as the others, dominated by insertion sort in practice. Pedagogical; not used in real systems.

**Code:** `theory/algorithms/showcase/sorting/bubble_sort.py`

## Comparison-sort lower bound

Any deterministic comparison-based sort must, in the worst case, perform $\Omega(n \log n)$ comparisons.

**Proof sketch.** A comparison sort's execution on length-$n$ input is a binary decision tree where each internal node is a $\leq$ comparison and each leaf is a permutation. With $n!$ possible orderings, the tree must have $\geq n!$ leaves, so its height is $\geq \log_2 n! = \Theta(n \log n)$ by Stirling.

Consequence: merge sort, heap sort, and average-case quicksort are asymptotically optimal among comparison sorts. To go faster requires exploiting key structure — see [[Linear-Time Sorting]].

## The main comparison sorts

| Sort | Worst | Average | Space | Stable | In-place | Notes |
|---|---|---|---|---|---|---|
| [[Merge Sort]] | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n)$ | yes | no | predictable, good for linked lists / external |
| [[Quick Sort]] | $\Theta(n^2)$ | $\Theta(n \log n)$ | $\Theta(\log n)$ | no | yes | fastest in practice with randomised pivots |
| [[Heap Sort]] | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(1)$ | no | yes | only $n \log n$ in-place sort with no recursion stack |
| Insertion sort | $\Theta(n^2)$ | $\Theta(n^2)$ | $\Theta(1)$ | yes | yes | best on tiny / nearly-sorted input |

## Linear-time sorts

When keys come from a bounded range or have a small digit-structure, the comparison lower bound is sidestepped. Counting, radix, and bucket sort run in $\Theta(n + k)$ where $k$ depends on the key universe. See [[Linear-Time Sorting]].

## Hybrid sorts in practice

Real-world standard libraries use hybrid algorithms that switch strategy based on input:

| Implementation | Strategy |
|---|---|
| **Timsort** (Python `list.sort`, Java `Arrays.sort` for objects) | merge sort with run detection + insertion sort on short runs |
| **Introsort** (C++ `std::sort`) | quicksort, switches to heap sort if recursion depth exceeds $2 \log n$ |
| **Pdqsort** (Rust `slice::sort_unstable`) | introsort variant with pattern detection and branchless partitioning |
| **Dual-pivot quicksort** (Java `Arrays.sort` for primitives) | quicksort with two pivots, fewer swaps |

The takeaway: no single sort is best. Production sorts pick the right tool per input region.

## Choosing a sort

| Situation | Choice |
|---|---|
| General in-memory | introsort / pdqsort (the language default) |
| Need stability (e.g. multi-key sort) | merge sort / Timsort |
| Memory-constrained, no recursion stack | heap sort |
| Nearly-sorted input | insertion sort or Timsort |
| Tiny input ($n < 16$ or so) | insertion sort |
| Keys are small integers in $[0, k]$, $k = O(n)$ | counting sort |
| External sort (data > RAM) | merge sort with $k$-way merge |

## Video references

- ![Bubble sort in 2 minutes](https://www.youtube.com/watch?v=xli_FI7CuzA)
- ![Insertion sort in 2 minutes](https://www.youtube.com/watch?v=JU767SDMDvA)
- ![Selection sort in 3 minutes](https://www.youtube.com/watch?v=g-PGLbMth_g)

## See also

- [[Merge Sort]]
- [[Quick Sort]]
- [[Heap Sort]]
- [[Linear-Time Sorting]]
- [[Selection]]
- [[Complexity]]
- [[Index]]
