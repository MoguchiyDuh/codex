---
tags:
  - algorithms
  - sorting
  - merge-sort
  - divide-and-conquer
status: complete
---

# Merge Sort

> Sort by recursively splitting the array in two, sorting each half, and merging the sorted halves. $\Theta(n \log n)$ in every case, stable, but not in-place.

## Algorithm

Three lines of recursion, plus a linear merge:

```pseudo
merge_sort(A, p, r):
    if p < r:
        q = ⌊(p + r) / 2⌋
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

merge(A, p, q, r):
    L = A[p..q]                # left half
    R = A[q+1..r]              # right half
    i = j = 1
    for k = p to r:
        if i ≤ length(L) and (j > length(R) or L[i] ≤ R[j]):
            A[k] = L[i]; i = i + 1
        else:
            A[k] = R[j]; j = j + 1
```

**Code:** `theory/algorithms/showcase/sorting/merge_sort.py`

The `merge` step assumes both halves are already sorted. It walks them with two pointers, always taking the smaller front element. The `≤` (not `<`) is what makes the sort **stable** — when equal, the left half's element wins, preserving original order.

## Complexity

Recurrence: $T(n) = 2T(n/2) + \Theta(n)$ — two subproblems of half size plus a linear merge.

By the master theorem (Case 2 with $a = b = 2$, $f(n) = n$):

$$T(n) \in \Theta(n \log n)$$

Same bound on every input — there is no best/worst-case asymmetry. Detailed in [[Recurrence Relations]].

| Property | Value                 |
| -------- | --------------------- |
| Worst    | $\Theta(n \log n)$    |
| Average  | $\Theta(n \log n)$    |
| Best     | $\Theta(n \log n)$    |
| Space    | $\Theta(n)$ auxiliary |
| Stable   | yes                   |
| In-place | no                    |

## Correctness

By induction on subarray length. Base case ($p = r$): a one-element subarray is trivially sorted. Inductive step: assume the two recursive calls correctly sort their halves; `merge` produces a sorted union (loop invariant: after iteration $k$, `A[p..k]` contains the $k - p + 1$ smallest elements of $L \cup R$ in sorted order).

## Why $O(n)$ extra space

`merge` cannot run in place over arrays without disrupting the unwritten elements: the `i`-th output position may need a value still sitting at the `j`-th input position. The standard implementation copies one or both halves into auxiliary buffers.

In-place merge in $\Theta(n)$ extra time and $\Theta(1)$ extra space exists (Kronrod's algorithm) but with prohibitive constants — not used in practice.

## Strengths

- **Predictable.** $\Theta(n \log n)$ regardless of input distribution.
- **Stable.** Useful when sorting by multiple keys.
- **External sort.** Works on data larger than RAM — sort chunks that fit, merge from disk in $k$-way passes.
- **Linked lists.** Merge sort doesn't need random access; it is the natural sort for linked structures.

## Weaknesses

- **$O(n)$ extra space** disqualifies it in memory-constrained settings.
- **Worse cache behaviour** than quicksort on contiguous arrays — merge writes to a separate buffer.
- **Higher constant** than quicksort on average inputs.

## Variants

| Variant              | Idea                                                                                           |
| -------------------- | ---------------------------------------------------------------------------------------------- |
| Bottom-up merge sort | iterative; merge runs of length $1, 2, 4, \dots$. No recursion stack                           |
| Natural merge sort   | detects already-sorted "runs" in the input, merges those                                       |
| Timsort              | natural merge sort + galloping merge + insertion sort for short runs; Python and Java standard |
| $k$-way merge sort   | external; merge $k$ sorted runs at once using a min-heap                                       |

## Video references

- ![Merge sort in 3 minutes](https://www.youtube.com/watch?v=4VqmGXwpLqc)

## See also

- [[Sorting]]
- [[Quick Sort]]
- [[Heap Sort]]
- [[Recurrence Relations]]
- [[Divide and Conquer]]
- [[Index]]
