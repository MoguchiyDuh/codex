---
tags: [math, algebra, inequalities]
status: complete
---
# Quadratic Inequalities

> Inequalities involving a quadratic expression, solved by finding roots and testing sign intervals.

## Definition

A quadratic inequality takes one of these forms (with $a \neq 0$):

- $ax^2 + bx + c > 0$
- $ax^2 + bx + c \geq 0$
- $ax^2 + bx + c < 0$
- $ax^2 + bx + c \leq 0$

## Solution Methods

### Interval (Sign) Method

1. Move all terms to one side
2. Find the roots (solve $ax^2 + bx + c = 0$)
3. Plot roots on number line — solid dot for $\leq$/$\geq$, hollow for $<$/$>$
4. Test a value in each interval for sign
5. Select intervals matching the inequality direction

**Example:** $x^2 - 5x + 6 < 0$

Roots: $(x-2)(x-3) = 0 \Rightarrow x = 2, x = 3$

```
----○---------○----
    2         3
```

Test $x = 2.5$: $(2.5)^2 - 5(2.5) + 6 = -0.25 < 0$ — interval $(2, 3)$ satisfies the inequality.

Solution: $x \in (2, 3)$

### Sign Table Method

Create a table of factor signs across intervals.

**Example:** $(x - 2)(x + 1)(x - 5) < 0$

| Interval | $(-\infty, -1)$ | $(-1, 2)$ | $(2, 5)$ | $(5, \infty)$ |
|----------|:---:|:---:|:---:|:---:|
| $x - 2$ | $-$ | $-$ | $+$ | $+$ |
| $x + 1$ | $-$ | $+$ | $+$ | $+$ |
| $x - 5$ | $-$ | $-$ | $-$ | $+$ |
| **Product** | $-$ | $+$ | $-$ | $+$ |

Solution: $x \in (-\infty, -1) \cup (2, 5)$

### Graphical Method

Graph $y = ax^2 + bx + c$ and read off where the parabola is above or below the x-axis.

## Quick Reference by Root Type

### Two Real Roots ($D > 0$), $x_1 < x_2$

| $a > 0$ | $a < 0$ | Inequality |
|---------|---------|------------|
| $(-\infty, x_1) \cup (x_2, \infty)$ | $(x_1, x_2)$ | $> 0$ |
| $(-\infty, x_1] \cup [x_2, \infty)$ | $[x_1, x_2]$ | $\geq 0$ |
| $(x_1, x_2)$ | $(-\infty, x_1) \cup (x_2, \infty)$ | $< 0$ |
| $[x_1, x_2]$ | $(-\infty, x_1] \cup [x_2, \infty)$ | $\leq 0$ |

### No Real Roots ($D < 0$)

| Condition | Solution |
|-----------|----------|
| $a > 0$, any $>0$ inequality | All real numbers $\mathbb{R}$ |
| $a < 0$, any $<0$ inequality | All real numbers $\mathbb{R}$ |
| Otherwise | No solution |

### One Root ($D = 0$), root at $x_0$

| Expression | Solution |
|------------|----------|
| $(x - x_0)^2 \geq 0$ | All real numbers |
| $(x - x_0)^2 > 0$ | $\mathbb{R} \setminus \{x_0\}$ |
| $(x - x_0)^2 \leq 0$ | $x = x_0$ only |
| $(x - x_0)^2 < 0$ | No solution |

## Rational Inequalities

For inequalities like $\frac{f(x)}{g(x)} > 0$: find critical points from both numerator zeros and denominator zeros. **Exclude** denominator zeros from the solution.

**Example:** $\frac{x^2 - 4}{x - 1} \leq 0$

Critical points: $x = -2, 2$ (zeros), $x = 1$ (undefined)

| Interval | Sign |
|----------|------|
| $(-\infty, -2)$ | $+$ |
| $(-2, 1)$ | $-$ |
| $(1, 2)$ | $-$ |
| $(2, \infty)$ | $+$ |

Solution: $[-2, 1) \cup (1, 2]$

## See also

- [[quadratic function]] - Discriminant and root types
- [[polynomials]] - General polynomial inequalities
- [[Index]]
