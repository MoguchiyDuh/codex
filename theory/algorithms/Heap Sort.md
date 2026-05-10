---
tags:
  - algorithms
  - sorting
  - heap-sort
status: complete
---

# Heap Sort

> Sort in place by building a max-heap, then repeatedly extracting the maximum to the back of the array. $\Theta(n \log n)$ worst case with $\Theta(1)$ extra space.

## Algorithm

```pseudo
heap_sort(A):
    build_max_heap(A)              # in-place, Θ(n)
    for i = length(A) down to 2:
        swap A[1] and A[i]         # move current max to its final position
        A.heap_size = A.heap_size - 1
        sift_down(A, 1)            # restore heap property on A[1..i-1]

build_max_heap(A):
    A.heap_size = length(A)
    for i = ⌊length(A)/2⌋ down to 1:
        sift_down(A, i)
```

**Code:** `theory/algorithms/showcase/sorting/heap_sort.py`

`sift_down` (also called `max-heapify`) is defined in [[../data_structures/Heap|Heap]]. Phase 1 builds the heap in $\Theta(n)$. Phase 2 runs $n - 1$ extractions, each $\Theta(\log n)$, totalling $\Theta(n \log n)$.

## How it works

A max-heap stored as an array has the maximum at index 1. Swap it with the last element — the max is now in its sorted position. Shrink the heap (logically; the array stays the same length) and sift the new root down to restore the heap property. Repeat.

After the main loop, the array is sorted ascending. The heap progressively shrinks from the front while the sorted suffix grows from the back.

## Complexity

| Property | Value              |
| -------- | ------------------ |
| Worst    | $\Theta(n \log n)$ |
| Average  | $\Theta(n \log n)$ |
| Best     | $\Theta(n \log n)$ |
| Space    | $\Theta(1)$        |
| Stable   | no                 |
| In-place | yes                |

The bound is tight in all cases — no input speeds it up. Build-heap is $\Theta(n)$ (not $\Theta(n \log n)$ — see [[../data_structures/Heap|Heap]]); the dominant cost is the $n - 1$ sift-downs in phase 2.

## Strengths

- **Worst-case $\Theta(n \log n)$.** Unlike quicksort, no adversarial input degrades it.
- **In-place, $\Theta(1)$ extra space.** No recursion stack — the implementation is iterative.
- **Useful as a fallback.** Introsort uses heap sort to bound recursion depth in quicksort.

## Weaknesses

- **Cache-unfriendly.** Sift-down jumps between parent and child indices spaced $2i$ apart — poor locality compared to quicksort's linear scans.
- **Higher constant** than quicksort on typical input. Empirically about 2× slower despite the same asymptotic bound.
- **Not stable.** Equal keys can be reordered by the heap operations.

## When to choose heap sort

| Situation                                     | Reason                                                        |
| --------------------------------------------- | ------------------------------------------------------------- |
| Need worst-case $\Theta(n \log n)$ guaranteed | Quicksort's $\Theta(n^2)$ worst case is unacceptable          |
| Memory is tight                               | $\Theta(1)$ extra space, no recursion                         |
| Embedded / kernel context                     | Predictable behaviour, no allocation                          |
| Top-$k$ instead of full sort                  | Use the heap directly — see [[../data_structures/Heap\|Heap]] |

## Heap sort vs the alternatives

|                 | Heap sort            | Quick sort       | Merge sort         |
| --------------- | -------------------- | ---------------- | ------------------ |
| Worst           | $\Theta(n \log n)$   | $\Theta(n^2)$    | $\Theta(n \log n)$ |
| Space           | $\Theta(1)$          | $\Theta(\log n)$ | $\Theta(n)$        |
| Stable          | no                   | no               | yes                |
| In-place        | yes                  | yes              | no                 |
| Cache           | poor                 | excellent        | moderate           |
| Practical speed | slowest of the three | fastest          | middle             |

## Video references

- ![Heap sort in 4 minutes](https://www.youtube.com/watch?v=2DmK_H7IdTo)

## See also

- [[Sorting]]
- [[../data_structures/Heap|Heap]]
- [[Quick Sort]]
- [[Merge Sort]]
- [[Index]]
