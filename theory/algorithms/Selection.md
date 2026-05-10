---
tags:
  - algorithms
  - selection
  - order-statistics
  - quickselect
status: complete
---

# Selection

> Find the $k$-th smallest element of an unordered array — the _order statistic_ of rank $k$. Sorting solves it in $\Theta(n \log n)$; specialised algorithms run in $\Theta(n)$.

## The problem

Given $A[1..n]$ and $1 \leq k \leq n$, return the element that would sit at position $k$ in the sorted order. Special cases:

| $k$                                         | Name      |
| ------------------------------------------- | --------- |
| $1$                                         | minimum   |
| $n$                                         | maximum   |
| $\lfloor (n+1)/2 \rfloor$                   | median    |
| $\lfloor n/4 \rfloor, \lfloor 3n/4 \rfloor$ | quartiles |

## Trivial bounds

| Approach         | Time                                       |
| ---------------- | ------------------------------------------ |
| Sort, then index | $\Theta(n \log n)$                         |
| Min/max scan     | $\Theta(n)$ for $k = 1$ or $n$             |
| Heap of size $k$ | $\Theta(n \log k)$ — useful when $k \ll n$ |

For arbitrary $k$, the heap method is fine in practice but still super-linear. The interesting algorithms hit $\Theta(n)$ for any $k$.

## Quickselect

Average-case $\Theta(n)$. Same partition step as quicksort, but recurse into only one side — the side containing the target rank.

```pseudo
quickselect(A, p, r, k):
    if p == r:
        return A[p]
    q = partition(A, p, r)        # same as quicksort
    rank = q - p + 1              # rank of the pivot in A[p..r]
    if k == rank:
        return A[q]
    elif k < rank:
        return quickselect(A, p, q - 1, k)
    else:
        return quickselect(A, q + 1, r, k - rank)
```

**Code:** `theory/algorithms/showcase/sorting/quickselect.py`

The partition lands the pivot at its final sorted position. If that's rank $k$, done. Otherwise recurse only into the side guaranteed to contain rank $k$ — discarding the other half.

### Complexity

Recurrence with a balanced pivot: $T(n) = T(n/2) + \Theta(n)$, giving

$$T(n) = n + n/2 + n/4 + \cdots = \Theta(n)$$

Geometric sum, half the cost of quicksort's $\Theta(n \log n)$ which has both halves contributing.

| Case                                  | Time          |
| ------------------------------------- | ------------- |
| Best                                  | $\Theta(n)$   |
| Average (random pivot)                | $\Theta(n)$   |
| Worst (always smallest/largest pivot) | $\Theta(n^2)$ |

The worst case mirrors quicksort's. Randomised pivot selection makes it vanishingly unlikely on real input.

## Median-of-medians (deterministic linear)

Guaranteed $\Theta(n)$ worst case by choosing a provably good pivot. Algorithm:

1. Divide $A$ into groups of $5$.
2. Find the median of each group ($\Theta(1)$ per group).
3. Recursively select the median of those $\lceil n/5 \rceil$ medians — call it $m$.
4. Partition $A$ around $m$.
5. Recurse into the side containing rank $k$, as in quickselect.

```pseudo
select(A, k):
    if length(A) ≤ 5:
        return sorted(A)[k]
    groups = split A into ⌈n/5⌉ groups of 5
    medians = [median(g) for g in groups]
    m = select(medians, ⌈len(medians)/2⌉)
    L, R = partition A around m
    if k ≤ length(L): return select(L, k)
    elif k == length(L) + 1: return m
    else: return select(R, k - length(L) - 1)
```

![[median_of_medians.png]]

### Why groups of 5

The pivot $m$ — the median of medians — is guaranteed to be greater than at least $3 \lceil n/10 \rceil$ elements and less than at least $3 \lceil n/10 \rceil$ elements. So neither recursive call works on more than $7n/10$ elements.

The recurrence:

$$T(n) \leq T(n/5) + T(7n/10) + \Theta(n)$$

Because $1/5 + 7/10 = 9/10 < 1$, the recurrence solves to $T(n) = \Theta(n)$ by the Akra-Bazzi method or substitution.

Group sizes 3 or 4 give $9/10 \geq 1$ — recurrence does not collapse to linear. Group size 7 also works but with worse constants.

### Practical note

Median-of-medians has large constants — measured constants ~10× quickselect on typical input. Used as a _theoretical_ guarantee and inside introselect (the deterministic fallback in production selection routines).

## Comparison

| Algorithm              | Worst              | Average              | Notes                                       |
| ---------------------- | ------------------ | -------------------- | ------------------------------------------- |
| Sort + index           | $\Theta(n \log n)$ | $\Theta(n \log n)$   | simple, slow                                |
| Heap of size $k$       | $\Theta(n \log k)$ | $\Theta(n \log k)$   | ideal for top-$k$                           |
| Quickselect            | $\Theta(n^2)$      | $\Theta(n)$          | fast in practice                            |
| Randomised quickselect | $\Theta(n^2)$      | $\Theta(n)$ expected | the practical default                       |
| Median-of-medians      | $\Theta(n)$        | $\Theta(n)$          | theoretical guarantee, large constants      |
| Introselect            | $\Theta(n)$        | $\Theta(n)$          | quickselect with median-of-medians fallback |

## Where this matters

- Median computation in statistics, image processing.
- Pivot selection inside other algorithms.
- $k$-th nearest neighbour queries.
- Top-$k$ ranking systems (often heap-based).
- C++ `std::nth_element` is introselect.

## See also

- [[Quick Sort]]
- [[Sorting]]
- [[../data_structures/Heap|Heap]]
- [[Recurrence Relations]]
- [[Index]]
