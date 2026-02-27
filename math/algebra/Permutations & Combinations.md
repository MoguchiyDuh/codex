---
tags: [math, algebra, combinatorics]
status: complete
---
# Permutations & Combinations

> Counting techniques for determining the number of ways objects can be arranged (ordered) or selected (unordered).

## Factorial Notation

$$n! = n \times (n-1) \times (n-2) \times \cdots \times 1$$

Special cases: $0! = 1$, $1! = 1$. Recursive: $n! = n \times (n-1)!$

## Fundamental Counting Principle

If one event can occur in $m$ ways and another independent event in $n$ ways, both can occur in $m \times n$ ways.

## Permutations

A **permutation** is an ordered arrangement — order matters.

### $r$ of $n$ Objects

$$P(n, r) = \frac{n!}{(n-r)!}$$

Also written as $_nP_r$ or $P_r^n$.

**Example:** $P(5, 3) = \frac{5!}{2!} = 60$

### All $n$ Objects

$$P(n, n) = n!$$

### With Identical Objects

When some objects are identical:

$$P = \frac{n!}{n_1! \times n_2! \times \cdots \times n_k!}$$

**Example:** "MISSISSIPPI" (11 letters, I×4, S×4, P×2, M×1):
$$P = \frac{11!}{4! \times 4! \times 2! \times 1!} = 34{,}650$$

### Circular Permutations

Arranging $n$ objects in a circle (one position fixed to eliminate rotational duplicates):

$$( n-1)!$$

If reflections are also identical (e.g., a necklace): $\frac{(n-1)!}{2}$

## Combinations

A **combination** is an unordered selection — order does not matter.

### $r$ of $n$ Objects

$$C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}$$

Also written as $_nC_r$ or $C_r^n$.

**Example:** $C(5, 3) = \frac{5!}{3! \times 2!} = 10$

### With Repetition

Selecting $r$ objects from $n$ types with replacement:

$$C(n+r-1, r)$$

## Key Properties

| Property | Formula |
|----------|---------|
| Choosing all | $C(n, n) = 1$ |
| Choosing none | $C(n, 0) = 1$ |
| Choosing one | $C(n, 1) = n$ |
| Symmetry | $C(n, r) = C(n, n-r)$ |
| Pascal's identity | $C(n, r) = C(n-1, r-1) + C(n-1, r)$ |
| Relation to permutations | $P(n,r) = r! \times C(n,r)$ |

## Permutations vs Combinations

| Feature | Permutations | Combinations |
|---------|--------------|--------------|
| Order | Matters | Does not matter |
| Formula | $\frac{n!}{(n-r)!}$ | $\frac{n!}{r!(n-r)!}$ |
| Example | Arranging 3 in a line | Selecting 3 for a team |
| ABC vs BCA | Different | Same |

## Formula Summary

| Concept | Formula |
|---------|---------|
| $P(n, r)$ | $\frac{n!}{(n-r)!}$ |
| $P(n, n)$ | $n!$ |
| With identical objects | $\frac{n!}{n_1! \cdots n_k!}$ |
| Circular | $(n-1)!$ |
| $C(n, r)$ | $\frac{n!}{r!(n-r)!}$ |
| With repetition | $C(n+r-1, r)$ |

## See also

- [[polynomials]] - Binomial coefficients in binomial theorem
- [[Index]]
