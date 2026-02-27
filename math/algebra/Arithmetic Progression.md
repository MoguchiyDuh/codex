---
tags: [math, algebra, sequences]
status: complete
---
# Arithmetic Progression

> A sequence where consecutive terms differ by a fixed constant, the common difference $d$.

## Definition

A sequence $a_1, a_2, \ldots, a_n$ is an arithmetic progression (AP) if:
$$\boxed{a_{n+1} - a_n = d \quad \text{(constant for all } n\text{)}}$$

General form: $a_1, \quad a_1 + d, \quad a_1 + 2d, \quad \ldots, \quad a_1 + (n-1)d$

## Notation

| Symbol | Meaning |
|--------|---------|
| $a_1$ | First term |
| $d$ | Common difference |
| $n$ | Term position |
| $a_n$ | The $n$-th term |
| $S_n$ | Sum of first $n$ terms |

## N-th Term Formula

$$\boxed{a_n = a_1 + (n - 1)d}$$

**Examples:**
- Sequence $2, 5, 8, 11, \ldots$ ($d = 3$): $a_{10} = 2 + 9 \cdot 3 = 29$
- Sequence $100, 95, 90, \ldots$ ($d = -5$): $a_{50} = 100 + 49 \cdot (-5) = -145$

**Finding position:** $n = \dfrac{a_n - a_1}{d} + 1$

## Sum Formulas

### Using first and last term
$$\boxed{S_n = \frac{n(a_1 + a_n)}{2}}$$

### Using first term and common difference
$$\boxed{S_n = \frac{n[2a_1 + (n-1)d]}{2}}$$

**Derivation (Gauss's method):**
$$
\begin{align*}
S_n &= a_1 + (a_1+d) + \cdots + a_n \\
S_n &= a_n + (a_n-d) + \cdots + a_1 \\
2S_n &= n(a_1 + a_n)
\end{align*}
$$

**Examples:**
- First 20 terms of $3, 7, 11, \ldots$: $a_{20} = 79$, $S_{20} = \frac{20(3+79)}{2} = 820$
- Sum $1 + 2 + \cdots + 100$: $S_{100} = \frac{100 \cdot 101}{2} = 5050$

## Properties

### Arithmetic mean
If $a, b, c$ are in AP: $\boxed{b = \dfrac{a + c}{2}}$

### Three terms in AP
Can be written as $a - d, \; a, \; a + d$ — simplifies sum/product problems.

### Equidistant terms
$$\boxed{a_k + a_{n-k+1} = a_1 + a_n}$$

## Special Sums

| Series | Formula |
|--------|---------|
| $1 + 2 + \cdots + n$ | $\dfrac{n(n+1)}{2}$ |
| $1 + 3 + \cdots + (2n-1)$ | $n^2$ |
| $2 + 4 + \cdots + 2n$ | $n(n+1)$ |

## Comparison with Geometric Progression

| Feature | Arithmetic | Geometric |
|---------|------------|-----------|
| Pattern | Add constant $d$ | Multiply by constant $r$ |
| General term | $a_1 + (n-1)d$ | $a_1 \cdot r^{n-1}$ |
| Middle term | Arithmetic mean | Geometric mean |
| Growth | Linear | Exponential |

## See also

- [[algebraic identities]]
- [[binomials]]
