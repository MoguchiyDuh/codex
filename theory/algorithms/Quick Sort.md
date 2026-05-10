---
tags:
  - algorithms
  - sorting
  - quicksort
  - divide-and-conquer
status: complete
---

# Quick Sort

> Sort by choosing a pivot, partitioning around it, and recursing. $\Theta(n \log n)$ on average and the fastest comparison sort in practice — but $\Theta(n^2)$ worst case.

## Algorithm

```pseudo
quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

partition(A, p, r):              # Lomuto scheme
    pivot = A[r]
    i = p - 1
    for j = p to r - 1:
        if A[j] ≤ pivot:
            i = i + 1
            swap A[i] and A[j]
    swap A[i + 1] and A[r]
    return i + 1
```

**Code:** `theory/algorithms/showcase/sorting/quick_sort.py`

`partition` returns the final index `q` of the pivot, with all elements $\leq$ pivot to its left and all elements $>$ pivot to its right. Both subarrays are then sorted recursively.

## Partition schemes

| Scheme                     | Idea                                                | Notes                                                               |
| -------------------------- | --------------------------------------------------- | ------------------------------------------------------------------- |
| **Lomuto**                 | one pointer scanning forward, last element as pivot | simple to code, more swaps, poor on already-sorted input            |
| **Hoare**                  | two pointers moving inward from the ends            | original 1962 scheme, fewer swaps, slightly more subtle bookkeeping |
| **Three-way (Dutch flag)** | partitions into $<, =, >$ regions                   | wins on inputs with many duplicates                                 |

Hoare's partition is the standard in production implementations.

## Complexity

Recurrence depends on partition balance. With pivot landing at relative rank $\alpha$ (so the two subarrays have sizes $\alpha n$ and $(1-\alpha) n$):

$$T(n) = T(\alpha n) + T((1-\alpha) n) + \Theta(n)$$

| Case    | Pivot rank              | Recurrence                          | Result             |
| ------- | ----------------------- | ----------------------------------- | ------------------ |
| Best    | median ($\alpha = 1/2$) | $T(n) = 2T(n/2) + n$                | $\Theta(n \log n)$ |
| Average | uniform random          | (analyzed via expected comparisons) | $\Theta(n \log n)$ |
| Worst   | min or max each time    | $T(n) = T(n-1) + n$                 | $\Theta(n^2)$      |

The worst case occurs when the pivot is consistently the smallest or largest element — e.g. choosing the last element as pivot on already-sorted input.

| Property | Value                                                                   |
| -------- | ----------------------------------------------------------------------- |
| Worst    | $\Theta(n^2)$                                                           |
| Average  | $\Theta(n \log n)$                                                      |
| Best     | $\Theta(n \log n)$                                                      |
| Space    | $\Theta(\log n)$ recursion depth (with tail-call elim. on smaller side) |
| Stable   | no                                                                      |
| In-place | yes                                                                     |

## Pivot selection

Pivot quality determines which complexity class the algorithm lands in. Strategies:

| Strategy                              | Worst-case behaviour                                                          |
| ------------------------------------- | ----------------------------------------------------------------------------- |
| Last element                          | $\Theta(n^2)$ on sorted, reverse-sorted, all-equal inputs                     |
| Random                                | $\Theta(n^2)$ possible but probability vanishes — $\Theta(n \log n)$ expected |
| Median-of-three (first, middle, last) | $\Theta(n^2)$ on adversarial input but rare in practice                       |
| Median-of-medians (deterministic)     | $\Theta(n \log n)$ guaranteed but with high constants — see [[Selection]]     |

**Randomised quicksort** uses a uniformly random pivot. The expected number of comparisons is $2(n+1) H_n - 4n \approx 1.39 n \log_2 n$, very close to the comparison-sort lower bound. The probability of $\Omega(n^2)$ behaviour drops exponentially with $n$.

## Why quicksort wins in practice

Despite the $\Theta(n^2)$ worst case, quicksort is the fastest comparison sort on most real workloads because:

- **Sequential memory access.** Partition is two linear scans — cache-friendly.
- **In-place.** No auxiliary array allocation.
- **Low constant.** The inner loop is a comparison and possibly a swap; very tight code.
- **Tail-recursion elimination.** Recurse on the smaller side, iterate on the larger — caps stack depth at $\Theta(\log n)$.

Merge sort's stable $\Theta(n \log n)$ is theoretically attractive but loses on these constants for in-memory contiguous data.

## Production hardening

Standard-library quicksorts pre-empt the worst case:

| Implementation                                          | Defense                                                                 |
| ------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Introsort** (C++ `std::sort`)                         | switch to heap sort if recursion depth exceeds $2 \log n$               |
| **Pdqsort** (Rust `sort_unstable`)                      | pattern detection (already-sorted, all-equal) + branchless partitioning |
| **Dual-pivot quicksort** (Java primitive `Arrays.sort`) | two pivots split into three regions, fewer comparisons                  |
| Insertion sort cutoff                                   | switch to insertion sort for subarrays below ~16 elements               |

## Strengths and weaknesses

| Strengths                         | Weaknesses                                                |
| --------------------------------- | --------------------------------------------------------- |
| Fastest in-memory comparison sort | Not stable                                                |
| In-place — $\Theta(\log n)$ space | $\Theta(n^2)$ on adversarial inputs without randomisation |
| Cache-friendly                    | Worst case can be triggered if pivot strategy is naive    |

## Video references

- ![Quick sort in 4 minutes](https://www.youtube.com/watch?v=Hoixgm4-P4M)

## See also

- [[Sorting]]
- [[Merge Sort]]
- [[Heap Sort]]
- [[Selection]]
- [[Recurrence Relations]]
- [[Index]]
