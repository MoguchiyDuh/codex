---
tags: [math, algebra, sequences, geometric-progression]
status: complete
---

# Geometric Progression

> A sequence where each term is obtained by multiplying the previous term by a constant ratio.

## Definition

A **geometric progression** (GP) is a sequence $a_1, a_1r, a_1r^2, \ldots$ where $r$ is the **common ratio**.

$$\boxed{a_n = a_1 \cdot r^{n-1}}$$

The common ratio is found by:
$$\boxed{r = \frac{a_{n+1}}{a_n}}$$

| Symbol | Meaning |
|--------|---------|
| $a_1$ | First term |
| $r$ | Common ratio |
| $n$ | Position |
| $S_n$ | Sum of first $n$ terms |
| $S_\infty$ | Sum to infinity (convergent only) |

Examples of common ratios: $2, 6, 18, 54\ (r=3)$; $100, 50, 25\ (r=0.5)$; $3, -6, 12\ (r=-2)$

## N-th Term

$$\boxed{a_n = a_1 \cdot r^{n-1}}$$

Example: 8th term of $3, 6, 12, 24, \ldots$ — $a_8 = 3 \cdot 2^7 = 384$

## Sum of First n Terms

For $r \neq 1$:
$$\boxed{S_n = a_1 \cdot \frac{1 - r^n}{1 - r} = a_1 \cdot \frac{r^n - 1}{r - 1}}$$

For $r = 1$:
$$\boxed{S_n = n \cdot a_1}$$

**Derivation:** Multiply $S_n$ by $r$, subtract from $S_n$, solve — telescoping cancels all middle terms.

## Infinite Sum

Converges **only if** $|r| < 1$:

$$\boxed{S_\infty = \frac{a_1}{1 - r}}$$

| Condition | Behavior |
|-----------|----------|
| $\|r\| < 1$ | Converges |
| $\|r\| \geq 1$ | Diverges |

Example: $1 + \frac{1}{2} + \frac{1}{4} + \cdots = \frac{1}{1 - 1/2} = 2$

Repeating decimals: $0.\overline{3} = \frac{0.3}{1 - 0.1} = \frac{1}{3}$

## Properties

**Geometric mean:** if $a, b, c$ are in GP then $b = \sqrt{ac}$

**Three terms in GP** can be written as $\frac{a}{r},\ a,\ ar$ — useful when product or sum is given.

**Product of $n$ terms:** $P_n = (a_1 \cdot a_n)^{n/2}$

## Comparison with Arithmetic Progression

| Feature | Arithmetic | Geometric |
|---------|-----------|-----------|
| Pattern | Add $d$ | Multiply by $r$ |
| General term | $a_1 + (n-1)d$ | $a_1 \cdot r^{n-1}$ |
| Middle term | $\frac{a+c}{2}$ | $\sqrt{ac}$ |
| Growth | Linear | Exponential |
| Sum | $\frac{n(a_1+a_n)}{2}$ | $a_1 \cdot \frac{1-r^n}{1-r}$ |
| Infinite sum | Always diverges | Converges if $\|r\| < 1$ |

## Applications

- **Compound interest:** $A = P(1+r)^n$ — balance forms a GP each period
- **Population growth / bacterial doubling:** GP with $r = 2$
- **Radioactive decay:** GP with $r = \frac{1}{2}$ per half-life
- **Binary search complexity:** $O(\log n)$ — halving at each step

## See also

- [[exponents]] — GP nth-term formula relies on exponent rules
- [[logarithms]] — useful for solving GP equations (e.g. finding $n$)
