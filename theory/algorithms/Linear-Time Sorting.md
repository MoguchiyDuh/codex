---
tags:
  - algorithms
  - sorting
  - counting-sort
  - radix-sort
  - bucket-sort
status: complete
---

# Linear-Time Sorting

> When keys have exploitable structure — bounded integer range, fixed digit length — sorting can run in $\Theta(n)$, beating the $\Omega(n \log n)$ comparison-sort lower bound.

## How the lower bound is bypassed

The $\Omega(n \log n)$ bound (see [[Sorting]]) applies only to sorts that read keys via $\leq$ comparisons. Linear-time sorts inspect keys directly — counting occurrences, indexing by digits — and so are not constrained by the decision-tree argument.

The price: each algorithm assumes something about the keys (range, digit count, distribution).

## Counting sort

Sorts $n$ integers drawn from $\{0, 1, \dots, k\}$.

```pseudo
counting_sort(A, k):
    count[0..k] = 0
    for x in A: count[x] += 1
    for i = 1 to k: count[i] += count[i-1]      # prefix sums
    output[1..n]
    for j = length(A) down to 1:
        output[count[A[j]]] = A[j]
        count[A[j]] -= 1
    return output
```

**Code:** `theory/algorithms/showcase/sorting/counting_sort.py`

**Idea.** Count how many of each key, convert to prefix sums (giving each key's final ending index), then place each input element at its position.

| Property | Value |
|---|---|
| Time | $\Theta(n + k)$ |
| Space | $\Theta(n + k)$ |
| Stable | yes (when iterating right-to-left as above) |
| In-place | no |

**When applicable.** Keys are integers (or mappable to integers) in a known small range. Useful as a subroutine in radix sort. Becomes wasteful when $k \gg n$.

## Radix sort

Sorts $n$ keys, each a $d$-digit number in base $b$, by repeatedly stable-sorting on one digit at a time.

### LSD (least significant digit first)

```pseudo
radix_sort_lsd(A, d):
    for i = 1 to d:                  # i = digit position, 1 = least significant
        stable_sort A by digit i     # typically counting sort
```

**Code:** `theory/algorithms/showcase/sorting/radix_sort.py`

After all $d$ passes, the array is fully sorted. Stability of the inner sort is essential — earlier digits' order must survive later passes.

| Property | Value |
|---|---|
| Time | $\Theta(d (n + b))$ |
| Space | $\Theta(n + b)$ |
| Stable | yes |
| In-place | no |

For 32-bit integers with $b = 256$, $d = 4$ — runs in roughly $4(n + 256) = \Theta(n)$ for any reasonably large $n$.

### MSD (most significant digit first)

Sort on the most significant digit, then recurse into each digit-bucket. Useful for variable-length keys (strings) — each prefix is sorted independently. More complex to implement.

![[radix_sort_passes.png]]

### When radix sort wins

- Fixed-width integers (32- or 64-bit, IPv4 addresses, hashes).
- Strings of bounded length (DNA sequences, fixed-format identifiers).
- Floating-point numbers via bit-pattern tricks.

It loses to quicksort when keys are long and the digit count $d$ is comparable to $\log n$.

## Bucket sort

Distributes $n$ keys into $k$ buckets by a hash-like function, then sorts each bucket.

```pseudo
bucket_sort(A, k):
    buckets[0..k-1] = empty lists
    for x in A:
        buckets[hash(x)].append(x)
    for i = 0 to k-1:
        insertion_sort(buckets[i])
    return concatenate(buckets[0..k-1])
```

**Code:** `theory/algorithms/showcase/sorting/bucket_sort.py`

| Property | Value |
|---|---|
| Time (uniform input) | $\Theta(n)$ expected |
| Time (adversarial) | $\Theta(n^2)$ |
| Space | $\Theta(n + k)$ |
| Stable | yes (with stable per-bucket sort) |

The expected linear time depends on inputs being approximately uniformly distributed across buckets. Real-valued inputs in $[0, 1)$ with a uniform distribution are the textbook case.

## Comparison

| Sort | Assumption | Time | Space | Stable |
|---|---|---|---|---|
| **Counting** | integer keys in $[0, k]$ | $\Theta(n + k)$ | $\Theta(n + k)$ | yes |
| **Radix (LSD)** | $d$-digit keys, base $b$ | $\Theta(d(n + b))$ | $\Theta(n + b)$ | yes |
| **Bucket** | uniform distribution over a known range | $\Theta(n)$ expected | $\Theta(n + k)$ | yes |

## When *not* to use linear-time sorts

- Keys have no exploitable structure (general comparable objects).
- Range $k$ or digit count $d$ is comparable to or larger than $n$ — the asymptotic advantage disappears.
- Memory is tight — these sorts allocate.
- Stability isn't needed and quicksort/heapsort already meet performance goals.

For typical mixed-type sorting in standard libraries, comparison sorts win on flexibility. Linear-time sorts shine in specialised pipelines: hash-bucketing for joins in databases, radix sort over IDs, distribution sorts in HPC.

## See also

- [[Sorting]]
- [[Selection]]
- [[Complexity]]
- [[Index]]
