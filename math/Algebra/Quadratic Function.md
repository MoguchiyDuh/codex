# Quadratic Function

A **quadratic function** is a second-degree polynomial function that forms a parabola when graphed. It's one of the most fundamental functions in algebra with applications across mathematics, physics, engineering, and economics.

---

## Definition

A quadratic function is a function of the form:
$$\boxed{f(x) = ax^2 + bx + c}$$

where $a, b, c$ are real constants and $a \neq 0$.

A **quadratic equation** is formed when the function equals zero:
$$\boxed{ax^2 + bx + c = 0 \quad (a \neq 0)}$$

**Examples:**
- $f(x) = x^2 - 5x + 6$
- $f(x) = 2x^2 + 3x - 1$
- $f(x) = -x^2 + 4$
- $f(x) = 3x^2$ (no linear or constant term)

---

## Forms of Quadratic Functions

### 1. Standard Form
$$\boxed{f(x) = ax^2 + bx + c}$$

**Advantages:** Easy to identify coefficients, find y-intercept

**Example:** $f(x) = 2x^2 - 8x + 6$

---

### 2. Vertex Form
$$\boxed{f(x) = a(x - h)^2 + k}$$

Where $(h, k)$ is the vertex of the parabola.

**Advantages:** Immediately shows vertex location

**Example:** $f(x) = 2(x - 2)^2 - 2$
- Vertex: $(2, -2)$

**Converting to vertex form:** Complete the square

---

### 3. Factored Form
$$\boxed{f(x) = a(x - x_1)(x - x_2)}$$

Where $x_1$ and $x_2$ are the roots (zeros).

**Advantages:** Immediately shows roots

**Example:** $f(x) = (x - 2)(x - 3) = x^2 - 5x + 6$
- Roots: $x = 2$ and $x = 3$

---

## Discriminant

The **discriminant** determines the nature and number of roots:
$$\boxed{D = b^2 - 4ac}$$

### Case 1: $D > 0$
- **Two distinct real roots**
- Parabola crosses x-axis twice
- Can be factored: $ax^2 + bx + c = a(x - x_1)(x - x_2)$

**Example:** $x^2 - 5x + 6 = 0$
- $D = (-5)^2 - 4(1)(6) = 25 - 24 = 1 > 0$
- Roots: $x = 2, x = 3$

---

### Case 2: $D = 0$
- **One real root** (repeated/double root)
- Parabola touches x-axis at one point (vertex on x-axis)
- Perfect square trinomial

**Example:** $x^2 - 6x + 9 = 0$
- $D = (-6)^2 - 4(1)(9) = 36 - 36 = 0$
- Root: $x = 3$ (double root)
- $(x - 3)^2 = 0$

---

### Case 3: $D < 0$
- **No real roots** (two complex conjugate roots)
- Parabola doesn't intersect x-axis
- $\varnothing$ in real numbers

**Example:** $x^2 + 2x + 5 = 0$
- $D = 2^2 - 4(1)(5) = 4 - 20 = -16 < 0$
- No real solutions

---

## Quadratic Formula

The roots of $ax^2 + bx + c = 0$ are given by:
$$\boxed{x_{1,2} = \frac{-b \pm \sqrt{D}}{2a} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}}$$

**Derivation (Completing the Square):**
$$
\begin{align*}
ax^2 + bx + c &= 0 \\
x^2 + \frac{b}{a}x + \frac{c}{a} &= 0 \\
x^2 + \frac{b}{a}x &= -\frac{c}{a} \\
x^2 + \frac{b}{a}x + \frac{b^2}{4a^2} &= -\frac{c}{a} + \frac{b^2}{4a^2} \\
\left(x + \frac{b}{2a}\right)^2 &= \frac{b^2 - 4ac}{4a^2} \\
x + \frac{b}{2a} &= \pm \frac{\sqrt{b^2 - 4ac}}{2a} \\
x &= \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\end{align*}
$$

**Examples:**

1. Solve $x^2 - 7x + 10 = 0$
   - $a = 1, b = -7, c = 10$
   - $x = \frac{7 \pm \sqrt{49 - 40}}{2} = \frac{7 \pm 3}{2}$
   - $x_1 = 5, x_2 = 2$

2. Solve $2x^2 + 3x - 2 = 0$
   - $a = 2, b = 3, c = -2$
   - $x = \frac{-3 \pm \sqrt{9 + 16}}{4} = \frac{-3 \pm 5}{4}$
   - $x_1 = \frac{1}{2}, x_2 = -2$

---

## Vieta's Formulas

For equation $ax^2 + bx + c = 0$ with roots $x_1$ and $x_2$:

### Sum of Roots
$$\boxed{x_1 + x_2 = -\frac{b}{a}}$$

### Product of Roots
$$\boxed{x_1 \cdot x_2 = \frac{c}{a}}$$

**Proof:**
From $(x - x_1)(x - x_2) = x^2 - (x_1 + x_2)x + x_1x_2$

Comparing with $x^2 + \frac{b}{a}x + \frac{c}{a}$:
- $x_1 + x_2 = -\frac{b}{a}$
- $x_1 \cdot x_2 = \frac{c}{a}$

**Applications:**

1. Find equation given roots $x_1 = 3, x_2 = -2$:
   - Sum: $3 + (-2) = 1$
   - Product: $3 \cdot (-2) = -6$
   - Equation: $x^2 - x - 6 = 0$

2. If roots of $2x^2 - 6x + k = 0$ are equal, find $k$:
   - For equal roots: $D = 0$
   - $36 - 8k = 0 \Rightarrow k = 4.5$

---

## Vertex of Parabola

The vertex $(h, k)$ is the maximum or minimum point:

### X-coordinate of Vertex
$$\boxed{h = -\frac{b}{2a}}$$

### Y-coordinate of Vertex
$$\boxed{k = f(h) = f\left(-\frac{b}{2a}\right) = c - \frac{b^2}{4a} = -\frac{D}{4a}}$$

**Example:** Find vertex of $f(x) = 2x^2 - 8x + 6$
- $h = -\frac{-8}{2(2)} = 2$
- $k = 2(2)^2 - 8(2) + 6 = 8 - 16 + 6 = -2$
- Vertex: $(2, -2)$

---

## Axis of Symmetry

The vertical line passing through the vertex:
$$\boxed{x = -\frac{b}{2a}}$$

**Properties:**
- Parabola is symmetric about this line
- Every point has a mirror image across this line

---

## Maximum/Minimum Value

### If $a > 0$:
- Parabola opens **upward** (U-shaped)
- Vertex is the **minimum point**
- Minimum value: $f_{\min} = k = -\frac{D}{4a}$

### If $a < 0$:
- Parabola opens **downward** (∩-shaped)
- Vertex is the **maximum point**
- Maximum value: $f_{\max} = k = -\frac{D}{4a}$

---

## Intercepts

### Y-intercept
Set $x = 0$:
$$\boxed{f(0) = c}$$

Point: $(0, c)$

---

### X-intercepts (Roots)
Set $f(x) = 0$ and solve using:
- Factoring
- Quadratic formula
- Completing the square

Points: $(x_1, 0)$ and $(x_2, 0)$

---

## Completing the Square

Method to convert from standard to vertex form.

**Steps:**
1. Factor out $a$ from $x^2$ and $x$ terms
2. Complete the square inside parentheses
3. Simplify

**Example:** Convert $f(x) = 2x^2 - 8x + 6$ to vertex form

$$
\begin{align*}
f(x) &= 2x^2 - 8x + 6 \\
&= 2(x^2 - 4x) + 6 \\
&= 2(x^2 - 4x + 4 - 4) + 6 \\
&= 2[(x - 2)^2 - 4] + 6 \\
&= 2(x - 2)^2 - 8 + 6 \\
&= 2(x - 2)^2 - 2
\end{align*}
$$

Vertex form: $f(x) = 2(x - 2)^2 - 2$, vertex at $(2, -2)$

---

## Solving Methods

### 1. Factoring
$$x^2 + 5x + 6 = 0 \Rightarrow (x + 2)(x + 3) = 0 \Rightarrow x = -2 \text{ or } x = -3$$

---

### 2. Square Root Method (for $ax^2 + c = 0$)
$$x^2 = 9 \Rightarrow x = \pm 3$$

---

### 3. Completing the Square
See above section.

---

### 4. Quadratic Formula
Universal method for all quadratic equations.

---

## Applications

### 1. Projectile Motion
$$h(t) = -\frac{1}{2}gt^2 + v_0t + h_0$$

Where:
- $h(t)$ = height at time $t$
- $g$ = acceleration due to gravity
- $v_0$ = initial velocity
- $h_0$ = initial height

**Example:** Ball thrown upward at 20 m/s from 10m height
- $h(t) = -5t^2 + 20t + 10$
- Maximum height at $t = -\frac{20}{2(-5)} = 2$ seconds
- Max height: $h(2) = -5(4) + 40 + 10 = 30$ meters

---

### 2. Area and Perimeter Problems
**Example:** Maximize area with fixed perimeter

---

### 3. Revenue/Profit Maximization
$$\text{Profit} = \text{Revenue} - \text{Cost}$$

---

### 4. Optimization Problems
Find maximum or minimum values subject to constraints.

---

## Graph Characteristics

| Feature | Formula/Description |
|---------|-------------------|
| **Vertex** | $\left(-\frac{b}{2a}, -\frac{D}{4a}\right)$ |
| **Axis of symmetry** | $x = -\frac{b}{2a}$ |
| **Y-intercept** | $(0, c)$ |
| **X-intercepts** | $\left(\frac{-b \pm \sqrt{D}}{2a}, 0\right)$ |
| **Opens upward** | $a > 0$ |
| **Opens downward** | $a < 0$ |
| **Width** | Larger $\|a\|$ → narrower |

---

## Common Mistakes

1. **Forgetting $a \neq 0$** ✗
   - If $a = 0$, it's linear, not quadratic ✓

2. **$x^2 = 4 \Rightarrow x = 2$** ✗
   - Correct: $x = \pm 2$ ✓

3. **Using wrong sign in quadratic formula** ✗
   - Correct: $\frac{-b \pm \sqrt{D}}{2a}$ (negative $b$) ✓

4. **$(x + 3)^2 = x^2 + 9$** ✗
   - Correct: $(x + 3)^2 = x^2 + 6x + 9$ ✓

---

## Practice Problems

1. **Solve:** $x^2 - 3x - 10 = 0$
   - Answer: $x = 5$ or $x = -2$

2. **Find vertex:** $f(x) = -x^2 + 6x - 5$
   - Answer: $(3, 4)$

3. **Discriminant:** $2x^2 + 5x + 3 = 0$
   - Answer: $D = 1$ (two distinct real roots)

4. **Vieta's formulas:** If roots are 4 and -3, find equation
   - Answer: $x^2 - x - 12 = 0$

---

## See Also
- [[Polynomials]] - General polynomial theory
- [[Parabola]] - Geometric properties and graphing
- [[Quadratic Inequalities]] - Solving inequalities
- [[Algebraic Identities]] - Square identities
- [[00 - Algebra MOC]] - Algebra topics overview
