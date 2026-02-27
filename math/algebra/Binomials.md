---
tags: [math, algebra, binomial-theorem]
status: complete
---
# Binomials

> The Binomial Theorem gives a closed-form expansion for $(a + b)^n$ using binomial coefficients.

## Binomial Theorem

For any positive integer $n$:
$$\boxed{(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k}$$

**Pattern in each term:**
- Exponent of $a$ decreases from $n$ to $0$
- Exponent of $b$ increases from $0$ to $n$
- Sum of exponents = $n$
- Total terms = $n + 1$

## Binomial Coefficient

$$\boxed{\binom{n}{k} = \frac{n!}{k!(n-k)!}}$$

**Also written as:** $C(n, k)$, $C_n^k$, $_nC_k$

**Key properties:**

| Property | Formula |
|----------|---------|
| Boundary | $\binom{n}{0} = \binom{n}{n} = 1$ |
| Symmetry | $\binom{n}{k} = \binom{n}{n-k}$ |
| Pascal's identity | $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$ |
| Sum of row | $\sum_{k=0}^{n} \binom{n}{k} = 2^n$ |
| Alternating sum | $\sum_{k=0}^{n} (-1)^k \binom{n}{k} = 0$ |

## General Term

The $(k+1)$-th term in $(a + b)^n$:
$$\boxed{T_{k+1} = \binom{n}{k} a^{n-k} b^k}$$

**Example:** 4th term of $(x + 2y)^6$ ($k = 3$):
$$T_4 = \binom{6}{3} x^3 (2y)^3 = 20 \cdot x^3 \cdot 8y^3 = 160x^3y^3$$

## Standard Expansions

| Power | Expansion |
|-------|-----------|
| $(a+b)^2$ | $a^2 + 2ab + b^2$ |
| $(a+b)^3$ | $a^3 + 3a^2b + 3ab^2 + b^3$ |
| $(a+b)^4$ | $a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4$ |
| $(a+b)^5$ | $a^5 + 5a^4b + 10a^3b^2 + 10a^2b^3 + 5ab^4 + b^5$ |

## Pascal's Triangle

Each row gives the coefficients for $(a + b)^n$; each interior entry is the sum of the two above it.

```
Row 0:          1
Row 1:        1   1
Row 2:      1   2   1
Row 3:    1   3   3   1
Row 4:  1   4   6   4   1
Row 5: 1  5  10  10   5   1
```

**Pascal's identity:** $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$

## Generalized Binomial Theorem

For $|x| < 1$ and any real $r$:
$$\boxed{(1 + x)^r = 1 + rx + \frac{r(r-1)}{2!}x^2 + \frac{r(r-1)(r-2)}{3!}x^3 + \cdots}$$

Infinite series; reduces to polynomial when $r$ is a non-negative integer.

## Advanced Identities

| Identity | Formula |
|----------|---------|
| Vandermonde | $\sum_{k=0}^{r} \binom{m}{k}\binom{n}{r-k} = \binom{m+n}{r}$ |
| Hockey stick | $\sum_{i=0}^{n} \binom{i}{k} = \binom{n+1}{k+1}$ |
| Even/odd split | $\binom{n}{0} + \binom{n}{2} + \cdots = \binom{n}{1} + \binom{n}{3} + \cdots = 2^{n-1}$ |

## Applications

**Finding a specific term:** Set exponent of desired variable and solve for $k$, then evaluate $T_{k+1}$.

**Approximation:** $(1.02)^5 = (1 + 0.02)^5 \approx 1 + 5(0.02) + 10(0.0004) = 1.104$

**Probability:** Binomial distribution $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$

## See also

- [[algebraic identities]]
- [[arithmetic progression]]
- [[complex numbers]]
