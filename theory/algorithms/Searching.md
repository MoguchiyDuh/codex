---
tags:
  - algorithms
  - searching
  - binary-search
status: complete
---

# Searching

> Locate a target in a collection. The choice of algorithm is driven by what structure the collection already has.

## Linear search

Walk the sequence comparing each element to the target.

```pseudo
linear_search(A, target):
    for i = 1 to length(A):
        if A[i] == target:
            return i
    return NOT_FOUND
```

| Property | Value                           |
| -------- | ------------------------------- |
| Worst    | $\Theta(n)$                     |
| Average  | $\Theta(n)$                     |
| Best     | $\Theta(1)$                     |
| Space    | $\Theta(1)$                     |
| Requires | nothing — works on any iterable |

The only general-purpose search when the data is unsorted. Asymptotically optimal on unstructured input — any algorithm must in the worst case examine every element to decide absence.

## Binary search

If the array is sorted, comparing against the middle element halves the search space each step.

```pseudo
binary_search(A, target):
    lo = 1
    hi = length(A)
    while lo ≤ hi:
        mid = lo + (hi - lo) / 2        # integer division; avoids overflow vs (lo+hi)/2
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return NOT_FOUND
```

**Code:** `theory/algorithms/showcase/path_finding/binary_search.py`

| Property | Value                                             |
| -------- | ------------------------------------------------- |
| Worst    | $\Theta(\log n)$                                  |
| Average  | $\Theta(\log n)$                                  |
| Best     | $\Theta(1)$                                       |
| Space    | $\Theta(1)$ iterative, $\Theta(\log n)$ recursive |
| Requires | sorted array, $\Theta(1)$ random access           |

### Loop invariant

The interval `A[lo..hi]` always contains the target if it is present in `A`. Each iteration shrinks `hi - lo + 1` by at least half. The loop terminates when the interval is empty (`lo > hi`).

### Off-by-one discipline

Three common bugs and their fixes:

| Bug                       | Cause                                                 | Fix                                                            |
| ------------------------- | ----------------------------------------------------- | -------------------------------------------------------------- |
| Infinite loop on $n = 1$  | `mid` rounds down, `lo = mid` doesn't shrink interval | use `lo = mid + 1` and `hi = mid - 1`; never reassign to `mid` |
| Misses target at boundary | uses `<` instead of `≤` in `while`                    | the closed interval `[lo, hi]` requires `≤`                    |
| Integer overflow          | `(lo + hi) / 2` on huge arrays                        | `lo + (hi - lo) / 2`                                           |

These are the canonical traps. Knuth's _TAOCP_ notes that binary search wasn't published correctly until 1962, more than a decade after first being described.

### Lower bound

Any comparison-based search on a sorted array requires $\Omega(\log n)$ comparisons in the worst case — by the same decision-tree argument as the comparison-sort lower bound (see [[Sorting]]). Binary search is asymptotically optimal.

## Variants

### Lower bound / upper bound

Find the leftmost (or rightmost) position where the target could be inserted while keeping the array sorted. Useful for handling duplicates and counting occurrences.

```pseudo
lower_bound(A, target):           # smallest i with A[i] ≥ target
    lo = 1; hi = length(A) + 1    # half-open [lo, hi)
    while lo < hi:
        mid = lo + (hi - lo) / 2
        if A[mid] < target: lo = mid + 1
        else:               hi = mid
    return lo
```

`upper_bound` flips the comparison to `≤`. Number of occurrences of `target` is `upper_bound - lower_bound`. C++ STL exposes both directly.

### Binary search on the answer

When the problem itself is monotonic in some parameter $x$ — "is $f(x)$ feasible?" returns yes for all $x \geq x^*$ and no for all $x < x^*$ — binary search the parameter to locate $x^*$ in $\Theta(\log)$ feasibility checks. Used everywhere in competitive programming and optimisation: minimum bandwidth allocation, maximum cookie size, etc.

### Exponential search

Locate the target in an unbounded or very large sorted sequence. Probe at indices $1, 2, 4, 8, \dots$ until you overshoot, then binary search the last bracket. $\Theta(\log p)$ where $p$ is the position — useful when the position is much smaller than the total length.

### Interpolation search

For uniformly distributed sorted numeric data, estimate the target's position by linear interpolation between `A[lo]` and `A[hi]` instead of taking the midpoint. Average $\Theta(\log \log n)$, worst $\Theta(n)$ on skewed data. Rarely worth the complexity in practice.

## Search structures

When you do many searches, build a structure once and amortize.

| Structure                                                     | Build                | Search             | Notes                            |
| ------------------------------------------------------------- | -------------------- | ------------------ | -------------------------------- |
| Sorted array                                                  | $\Theta(n \log n)$   | $\Theta(\log n)$   | static; no inserts               |
| [[../data_structures/Hash Tables\|Hash table]]                | $\Theta(n)$          | $\Theta(1)$ avg    | unordered, fastest typical       |
| [[../data_structures/Binary Search Tree\|Self-balancing BST]] | $\Theta(n \log n)$   | $\Theta(\log n)$   | ordered, supports range queries  |
| [[../data_structures/B-Tree\|B-tree]]                         | $\Theta(n \log_t n)$ | $\Theta(\log_t n)$ | block-friendly; databases / disk |
| [[../data_structures/Bloom Filter\|Bloom filter]]             | $\Theta(n)$          | $\Theta(1)$        | probabilistic, no negatives      |

The right answer depends on workload: dynamic vs static, ordered vs unordered, in-memory vs disk.

## Decision summary

| Situation                                          | Algorithm          |
| -------------------------------------------------- | ------------------ |
| Unsorted array, single search                      | linear search      |
| Unsorted array, repeated searches                  | build a hash table |
| Sorted array, occasional search                    | binary search      |
| Sorted array, ordered queries (range, predecessor) | balanced BST       |
| Disk-resident dataset                              | B-tree             |
| Membership test, large set, false positives ok     | Bloom filter       |

## Video references

- ![Binary search in 4 minutes](https://www.youtube.com/watch?v=fDKIpRe8GW4)

## See also

- [[Sorting]]
- [[Divide and Conquer]]
- [[../data_structures/Hash Tables|Hash Tables]]
- [[../data_structures/Binary Search Tree|Binary Search Tree]]
- [[Index]]
