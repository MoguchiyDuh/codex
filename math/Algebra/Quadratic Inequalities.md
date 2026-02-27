# Quadratic Inequalities

Quadratic inequalities involve comparing a quadratic expression to zero or another expression. They're essential for determining ranges of values and solving optimization problems.

---

## Definition

A **quadratic inequality** is an inequality involving a quadratic expression:
- $ax^2 + bx + c > 0$
- $ax^2 + bx + c \geq 0$
- $ax^2 + bx + c < 0$
- $ax^2 + bx + c \leq 0$

where $a \neq 0$.

**Examples:**
- $x^2 - 5x + 6 < 0$
- $2x^2 + 3x - 2 \geq 0$
- $-x^2 + 4x > 3$

---

## Solution Methods

### Method 1: Interval (Sign) Method

**Steps:**
1. **Move all terms to one side** (make it equal to 0)
2. **Find the roots** (solve $ax^2 + bx + c = 0$)
3. **Plot roots on number line**
   - **Solid dot** (●) for $\leq$ or $\geq$ (included)
   - **Hollow dot** (○) for $<$ or $>$ (excluded)
4. **Test signs in each interval**
5. **Select intervals matching the inequality**

---

### Example 1: $x^2 - 5x + 6 < 0$

**Step 1:** Already in standard form

**Step 2:** Find roots
$$x^2 - 5x + 6 = 0$$
$$(x - 2)(x - 3) = 0$$
$$x = 2, \quad x = 3$$

**Step 3:** Number line with hollow dots (since $<$)

```
----○---------○----
    2         3
```

**Step 4:** Test intervals
- **Interval 1:** $(-\infty, 2)$, test $x = 0$: $(0)^2 - 5(0) + 6 = 6 > 0$ ✗
- **Interval 2:** $(2, 3)$, test $x = 2.5$: $(2.5)^2 - 5(2.5) + 6 = -0.25 < 0$ ✓
- **Interval 3:** $(3, \infty)$, test $x = 4$: $(4)^2 - 5(4) + 6 = 2 > 0$ ✗

**Step 5:** Solution: $\boxed{x \in (2, 3)}$

---

### Quick Sign Method for Simple Inequalities

**Tip:** For $(x - a)(x - b) > 0$ where $a < b$:
- The sign of the product alternates: **+ - +**
- First interval (left): sign of leading coefficient
- Then alternate

**Pattern for $a > 0$:**
```
---[+]---○---[-]---○---[+]---
       x₁       x₂
```

**Pattern for $a < 0$:**
```
---[-]---○---[+]---○---[-]---
       x₁       x₂
```

---

### Method 2: Sign Table/Chart Method

Create a table showing signs of each factor and their product.

**Example:** Solve $(x - 2)(x + 1)(x - 5) < 0$

| Interval | $(-\infty, -1)$ | $(-1, 2)$ | $(2, 5)$ | $(5, \infty)$ |
|----------|-----------------|-----------|----------|---------------|
| $x - 2$ | $-$ | $-$ | $+$ | $+$ |
| $x + 1$ | $-$ | $+$ | $+$ | $+$ |
| $x - 5$ | $-$ | $-$ | $-$ | $+$ |
| **Product** | $-$ | $+$ | $-$ | $+$ |

Solution (where product < 0): $\boxed{x \in (-\infty, -1) \cup (2, 5)}$

---

### Method 3: Graphical Method

Graph $y = ax^2 + bx + c$ and identify where the parabola satisfies the inequality.

**For $ax^2 + bx + c > 0$:**
- Find where parabola is **above** x-axis

**For $ax^2 + bx + c < 0$:**
- Find where parabola is **below** x-axis

**Example:** $x^2 - 4 \geq 0$
- Roots: $x = -2, x = 2$
- Parabola opens upward ($a = 1 > 0$)
- Above x-axis when $x \leq -2$ or $x \geq 2$
- Solution: $\boxed{(-\infty, -2] \cup [2, \infty)}$

---

## Special Cases

### Case 1: No Real Roots ($D < 0$)

**Example:** $x^2 + 2x + 5 > 0$
- $D = 4 - 20 = -16 < 0$ (no real roots)
- $a = 1 > 0$ (opens upward)
- Parabola entirely above x-axis
- Solution: $\boxed{x \in (-\infty, \infty)}$ (all real numbers)

**Example:** $-x^2 - 2x - 5 < 0$
- $D < 0$, $a = -1 < 0$ (opens downward)
- Parabola entirely below x-axis
- Solution: $\boxed{x \in (-\infty, \infty)}$ (all real numbers)

---

### Case 2: One Root ($D = 0$)

**Example:** $x^2 - 6x + 9 \geq 0$
- $(x - 3)^2 \geq 0$
- Root: $x = 3$ (double root)
- Always non-negative, equals 0 only at $x = 3$
- Solution: $\boxed{x \in (-\infty, \infty)}$

**Example:** $(x - 3)^2 > 0$
- Solution: $\boxed{x \in (-\infty, 3) \cup (3, \infty)}$ (all except $x = 3$)

---

### Case 3: Perfect Squares

$$\boxed{(x - a)^2 \geq 0 \text{ for all } x}$$
$$\boxed{(x - a)^2 > 0 \text{ for all } x \neq a}$$
$$\boxed{(x - a)^2 \leq 0 \text{ only when } x = a}$$
$$\boxed{(x - a)^2 < 0 \text{ has no solution}}$$

---

## Inequality Types Summary

### For $ax^2 + bx + c$ with roots $x_1 < x_2$ and $a > 0$:

| Inequality | Solution |
|------------|----------|
| $> 0$ | $(-\infty, x_1) \cup (x_2, \infty)$ |
| $\geq 0$ | $(-\infty, x_1] \cup [x_2, \infty)$ |
| $< 0$ | $(x_1, x_2)$ |
| $\leq 0$ | $[x_1, x_2]$ |

### For $ax^2 + bx + c$ with roots $x_1 < x_2$ and $a < 0$:

| Inequality | Solution |
|------------|----------|
| $> 0$ | $(x_1, x_2)$ |
| $\geq 0$ | $[x_1, x_2]$ |
| $< 0$ | $(-\infty, x_1) \cup (x_2, \infty)$ |
| $\leq 0$ | $(-\infty, x_1] \cup [x_2, \infty)$ |

---

## Complex Examples

### Example 2: $-x^2 + 2x + 3 \geq 0$

**Step 1:** Factor
$$-x^2 + 2x + 3 = -(x^2 - 2x - 3) = -(x - 3)(x + 1)$$

**Step 2:** Find roots: $x = -1, x = 3$

**Step 3:** Test intervals (or note $a = -1 < 0$)
- $a < 0$ means parabola opens downward
- Above x-axis between roots

**Solution:** $\boxed{x \in [-1, 3]}$

---

### Example 3: $2x^2 - 5x < 3$

**Step 1:** Standard form
$$2x^2 - 5x - 3 < 0$$

**Step 2:** Find roots
$$x = \frac{5 \pm \sqrt{25 + 24}}{4} = \frac{5 \pm 7}{4}$$
$$x_1 = -\frac{1}{2}, \quad x_2 = 3$$

**Step 3:** $a = 2 > 0$ (opens upward), need below x-axis

**Solution:** $\boxed{x \in \left(-\frac{1}{2}, 3\right)}$

---

### Example 4: $(x - 1)(x + 2) \geq (x - 1)(x + 5)$

**Step 1:** Rearrange
$$(x - 1)(x + 2) - (x - 1)(x + 5) \geq 0$$
$$(x - 1)[(x + 2) - (x + 5)] \geq 0$$
$$(x - 1)(-3) \geq 0$$
$$-3(x - 1) \geq 0$$
$$x - 1 \leq 0$$

**Solution:** $\boxed{x \leq 1}$ or $\boxed{x \in (-\infty, 1]}$

---

## Rational Inequalities (Bonus)

For inequalities like $\frac{(x-a)(x-b)}{(x-c)} > 0$:

**Steps:**
1. Find critical points (numerator = 0 and denominator = 0)
2. **Exclude** points where denominator = 0 (undefined)
3. Test intervals
4. Select appropriate intervals

**Example:** $\frac{x^2 - 4}{x - 1} \leq 0$

Critical points: $x = -2, 2$ (zeros), $x = 1$ (undefined)

| Interval | $(-\infty, -2)$ | $(-2, 1)$ | $(1, 2)$ | $(2, \infty)$ |
|----------|-----------------|-----------|----------|---------------|
| Sign | $+$ | $-$ | $-$ | $+$ |

Solution (negative or zero, excluding $x = 1$): $\boxed{[-2, 1) \cup (1, 2]}$

---

## Applications

### 1. Range of Values
Find values of $k$ for which $kx^2 - 4x + k > 0$ for all $x$.

**Solution:**
- Need $a > 0$ and $D < 0$
- $k > 0$ and $16 - 4k^2 < 0$
- $k^2 > 4$ and $k > 0$
- $k > 2$

---

### 2. Optimization Constraints
A rectangle has perimeter 40m. Find dimensions when area $> 96$ m².

**Solution:**
- Let width = $x$, length = $20 - x$
- Area: $A = x(20 - x) > 96$
- $20x - x^2 > 96$
- $-x^2 + 20x - 96 > 0$
- $x^2 - 20x + 96 < 0$
- $(x - 8)(x - 12) < 0$
- $8 < x < 12$

---

## Common Mistakes

1. **Forgetting to flip inequality when multiplying by negative** ✗
   - $-x > 5 \Rightarrow x < -5$ ✓

2. **Including/excluding endpoints incorrectly** ✗
   - $\geq$ uses $[$ or $]$ (closed)
   - $>$ uses $($ or $)$ (open) ✓

3. **Not checking for division by zero** ✗
   - Always check denominator $\neq 0$ ✓

4. **Assuming $(x-a)^2 < 0$ has solutions** ✗
   - Squares are always $\geq 0$ ✓

---

## Quick Reference

| Given | Roots $x_1, x_2$ | $a > 0$ Solution | $a < 0$ Solution |
|-------|------------------|------------------|------------------|
| $> 0$ | $x_1 < x_2$ | $x < x_1$ or $x > x_2$ | $x_1 < x < x_2$ |
| $< 0$ | $x_1 < x_2$ | $x_1 < x < x_2$ | $x < x_1$ or $x > x_2$ |
| $D < 0$ | No real roots | All $x$ if $a > 0$ | All $x$ if $a < 0$ |

---

## See Also
- [[Quadratic Function]] - Quadratic equations and discriminant
- [[Parabola]] - Graphical representation
- [[Polynomials]] - General polynomial inequalities
- [[00 - Algebra MOC]] - Algebra topics overview
