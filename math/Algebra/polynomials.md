---
tags: [math, algebra, polynomials]
status: complete
---
# Polynomials

> An algebraic expression of variables and coefficients combined using addition, subtraction, and multiplication, where variables have non-negative integer exponents.

## Definition

$$P(x) = a_nx^n + a_{n-1}x^{n-1} + \cdots + a_2x^2 + a_1x + a_0$$

Where $a_n \neq 0$ is the **leading coefficient**, $n$ is a non-negative integer, and $x$ is the variable.

## Terminology

### Degree

The highest exponent of the variable. Examples: $3x^5 + 2x^3 - 7$ has degree 5; a constant has degree 0.

### Classification by Degree

| Degree | Name | Standard Form |
|--------|------|---------------|
| 0 | Constant | $a$ |
| 1 | Linear | $ax + b$ |
| 2 | Quadratic | $ax^2 + bx + c$ |
| 3 | Cubic | $ax^3 + bx^2 + cx + d$ |
| 4 | Quartic | $ax^4 + \cdots$ |
| 5 | Quintic | $ax^5 + \cdots$ |

### Classification by Number of Terms

| Type | Terms | Example |
|------|-------|---------|
| Monomial | 1 | $5x^3$ |
| Binomial | 2 | $3x^2 + 7$ |
| Trinomial | 3 | $x^2 - 4x + 4$ |

## Operations

### Addition and Subtraction

Combine like terms (same variable and exponent).

$$( 3x^2 + 2x - 5) + (x^2 - 4x + 3) = 4x^2 - 2x - 2$$

### Multiplication

Use the distributive property (FOIL for binomials). Degree rule: $\deg(P \cdot Q) = \deg(P) + \deg(Q)$.

$$(x + 2)(x + 3) = x^2 + 5x + 6$$

### Division

**Division Algorithm:** $P(x) = Q(x) \cdot D(x) + R(x)$ where $\deg(R) < \deg(D)$.

**Long division** works for any divisor. **Synthetic division** applies only when the divisor is of the form $x - c$.

```
# Synthetic division: (2x³ - 5x² + 3x - 2) ÷ (x - 2)
2 |  2  -5   3  -2
  |      4  -2   2
  |________________
     2  -1   1   0
```

Result: $2x^2 - x + 1$, remainder $0$.

## Theorems

### Remainder Theorem

When $P(x)$ is divided by $(x - c)$, the remainder equals $P(c)$.

$$P(x) = (x - c) \cdot Q(x) + P(c)$$

### Factor Theorem

$(x - c)$ is a factor of $P(x)$ if and only if $P(c) = 0$.

### Fundamental Theorem of Algebra

A polynomial of degree $n$ has exactly $n$ complex roots (counting multiplicity).

### Rational Root Theorem

If $\frac{p}{q}$ is a rational root of $P(x) = a_nx^n + \cdots + a_0$, then $p$ divides $a_0$ and $q$ divides $a_n$.

## Factoring

| Technique | Formula |
|-----------|---------|
| GCF | $6x^3 + 9x^2 = 3x^2(2x + 3)$ |
| Difference of squares | $a^2 - b^2 = (a + b)(a - b)$ |
| Sum of cubes | $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$ |
| Difference of cubes | $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$ |
| Quadratic trinomial | $x^2 + bx + c = (x + p)(x + q)$ where $p + q = b$, $pq = c$ |

## Roots and Zeros

A **root** of $P(x)$ is a value $c$ where $P(c) = 0$.

**Multiplicity** determines graph behavior at that root:
- Simple (multiplicity 1): graph crosses x-axis
- Double (multiplicity 2): graph touches and bounces
- Triple (multiplicity 3): graph flattens at crossing

## Special Products

$$( a + b)^2 = a^2 + 2ab + b^2$$
$$(a - b)^2 = a^2 - 2ab + b^2$$
$$(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$$
$$(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$$

## Graph Behavior

### End Behavior

Determined by the leading term $a_nx^n$:

| Leading Term | $x \to -\infty$ | $x \to +\infty$ |
|--------------|-----------------|-----------------|
| $+x^{\text{even}}$ | $+\infty$ | $+\infty$ |
| $-x^{\text{even}}$ | $-\infty$ | $-\infty$ |
| $+x^{\text{odd}}$ | $-\infty$ | $+\infty$ |
| $-x^{\text{odd}}$ | $+\infty$ | $-\infty$ |

A polynomial of degree $n$ has at most $n - 1$ turning points.

## See also

- [[quadratic function]] - Second-degree polynomials
- [[quadratic inequalities]] - Polynomial inequalities
- [[permutations & combinations]] - Binomial theorem
- [[Index]]
