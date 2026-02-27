# Parabola

A **parabola** is the U-shaped curve that represents the graph of a quadratic function. It's a fundamental conic section with unique geometric and algebraic properties.

---

## Definition

A **parabola** is the set of all points in a plane that are equidistant from a fixed point (focus) and a fixed line (directrix).

**Algebraically**, a parabola is the graph of a [[Quadratic Function]]:
$$\boxed{y = ax^2 + bx + c \quad (a \neq 0)}$$

---

## Standard Forms

### Vertical Parabola (opens up/down)
$$\boxed{y = a(x - h)^2 + k}$$

- **Vertex:** $(h, k)$
- **Axis of symmetry:** $x = h$ (vertical line)
- Opens **upward** if $a > 0$
- Opens **downward** if $a < 0$

---

### Horizontal Parabola (opens left/right)
$$\boxed{x = a(y - k)^2 + h}$$

- **Vertex:** $(h, k)$
- **Axis of symmetry:** $y = k$ (horizontal line)
- Opens **rightward** if $a > 0$
- Opens **leftward** if $a < 0$

---

## Components of a Parabola

### 1. Vertex $(h, k)$
The **turning point** of the parabola (maximum or minimum).

For $y = ax^2 + bx + c$:
$$\boxed{h = -\frac{b}{2a}, \quad k = c - \frac{b^2}{4a}}$$

**Examples:**
- $y = x^2 - 4x + 3$ → Vertex: $(2, -1)$
- $y = -2x^2 + 8x - 5$ → Vertex: $(2, 3)$

---

### 2. Axis of Symmetry
A vertical line passing through the vertex that divides the parabola into two mirror images.

$$\boxed{x = h = -\frac{b}{2a}}$$

**Property:** For any point $(x, y)$ on the parabola, the point $(2h - x, y)$ is also on the parabola.

<img src="Pictures/axis_of_symmetry.jpg" width=500 height="auto" style="display: block; margin: auto">

---

### 3. Focus
A fixed point inside the parabola.

For $y = ax^2$:
$$\boxed{\text{Focus: } \left(0, \frac{1}{4a}\right)}$$

For $y = a(x - h)^2 + k$:
$$\boxed{\text{Focus: } \left(h, k + \frac{1}{4a}\right)}$$

---

### 4. Directrix
A fixed line outside the parabola.

For $y = ax^2$:
$$\boxed{\text{Directrix: } y = -\frac{1}{4a}}$$

For $y = a(x - h)^2 + k$:
$$\boxed{\text{Directrix: } y = k - \frac{1}{4a}}$$

**Property:** Every point on the parabola is equidistant from the focus and directrix.

---

### 5. Focal Length (p)
Distance from vertex to focus (or vertex to directrix).

$$\boxed{p = \frac{1}{4a}}$$

---

## Parameter Analysis

### Parameter $a$: Direction and Width

#### Direction of Opening
- **$a > 0$**: Parabola opens **upward** (∪)
  - Vertex is **minimum point**
  - $y \geq k$ (range)

- **$a < 0$**: Parabola opens **downward** (∩)
  - Vertex is **maximum point**
  - $y \leq k$ (range)

---

#### Width/Narrowness
- **$|a| > 1$**: Parabola is **narrow** (steep)
- **$|a| < 1$**: Parabola is **wide** (flat)
- **$|a| = 1$**: Standard width

**Examples:**
- $y = 2x^2$ (narrow)
- $y = x^2$ (standard)
- $y = 0.5x^2$ (wide)

---

### Parameter $b$: Horizontal Position

The coefficient $b$ affects the **horizontal shift** of the vertex and axis of symmetry.

**X-coordinate of vertex:**
$$\boxed{h = -\frac{b}{2a}}$$

**Axis of symmetry:**
$$\boxed{x = -\frac{b}{2a}}$$

**Effect of $b$:**
- $b > 0$ with $a > 0$: Vertex shifts **left**
- $b < 0$ with $a > 0$: Vertex shifts **right**
- $b = 0$: Vertex on y-axis (symmetric about y-axis)

---

### Parameter $c$: Vertical Shift (Y-Intercept)

The constant $c$ determines the **y-intercept** (where the parabola crosses the y-axis).

$$\boxed{\text{Y-intercept: } (0, c)}$$

**Effect of $c$:**
- $c > 0$: Parabola shifts **upward**
- $c < 0$: Parabola shifts **downward**
- $c = 0$: Passes through origin

---

## Key Features

### Domain and Range

**Vertical Parabola** $y = a(x - h)^2 + k$:
- **Domain:** $(-\infty, \infty)$ (all real numbers)
- **Range:** 
  - If $a > 0$: $[k, \infty)$
  - If $a < 0$: $(-\infty, k]$

**Horizontal Parabola** $x = a(y - k)^2 + h$:
- **Domain:**
  - If $a > 0$: $[h, \infty)$
  - If $a < 0$: $(-\infty, h]$
- **Range:** $(-\infty, \infty)$

---

### Intercepts

#### X-intercepts (Roots)
Points where parabola crosses x-axis (set $y = 0$).

Solve $ax^2 + bx + c = 0$ using quadratic formula:
$$\boxed{x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}}$$

**Number of x-intercepts:**
- $D > 0$: **Two** x-intercepts
- $D = 0$: **One** x-intercept (vertex on x-axis)
- $D < 0$: **Zero** x-intercepts

---

#### Y-intercept
Point where parabola crosses y-axis (set $x = 0$).

$$\boxed{y = c}$$

Point: $(0, c)$

---

### Increasing and Decreasing Intervals

For $y = a(x - h)^2 + k$:

**If $a > 0$** (opens upward):
- **Decreasing:** $(-\infty, h)$
- **Increasing:** $(h, \infty)$

**If $a < 0$** (opens downward):
- **Increasing:** $(-\infty, h)$
- **Decreasing:** $(h, \infty)$

---

## Transformations

Starting with basic parabola $y = x^2$:

### Vertical Stretch/Compression
$$y = ax^2$$
- $|a| > 1$: Vertical stretch (narrower)
- $0 < |a| < 1$: Vertical compression (wider)

---

### Reflection
$$y = -x^2$$
- Reflects across x-axis

---

### Horizontal Shift
$$y = (x - h)^2$$
- $h > 0$: Shift **right** by $h$ units
- $h < 0$: Shift **left** by $|h|$ units

---

### Vertical Shift
$$y = x^2 + k$$
- $k > 0$: Shift **up** by $k$ units
- $k < 0$: Shift **down** by $|k|$ units

---

### Combined Transformations
$$y = a(x - h)^2 + k$$

**Order of transformations:**
1. Horizontal shift by $h$
2. Vertical stretch/compression by $|a|$
3. Reflection if $a < 0$
4. Vertical shift by $k$

---

## Applications

### 1. Projectile Motion
The path of a thrown object follows a parabolic trajectory:
$$h(t) = -\frac{1}{2}gt^2 + v_0t + h_0$$

---

### 2. Satellite Dishes & Reflectors
Parabolic shape focuses all parallel rays to a single point (focus).

**Applications:**
- Satellite dishes
- Telescopes
- Car headlights
- Solar collectors

---

### 3. Architecture
- Parabolic arches (bridges, buildings)
- Parabolic cables (suspension bridges)

---

### 4. Business & Economics
- Revenue maximization
- Cost minimization
- Profit optimization

**Example:** Revenue function $R(x) = -2x^2 + 100x$
- Maximum revenue at vertex: $x = -\frac{100}{2(-2)} = 25$ units

---

## Geometric Definition

A parabola is the locus of points equidistant from:
- **Focus** $F$
- **Directrix** (a line)

For any point $P$ on the parabola:
$$\boxed{\text{Distance}(P, F) = \text{Distance}(P, \text{directrix})}$$

---

## Standard Parabola Equations

| Orientation | Equation | Vertex | Focus | Directrix | Opens |
|-------------|----------|--------|-------|-----------|-------|
| Vertical (up) | $y = ax^2$ | $(0,0)$ | $(0, \frac{1}{4a})$ | $y = -\frac{1}{4a}$ | Up |
| Vertical (down) | $y = -ax^2$ | $(0,0)$ | $(0, -\frac{1}{4a})$ | $y = \frac{1}{4a}$ | Down |
| Horizontal (right) | $x = ay^2$ | $(0,0)$ | $(\frac{1}{4a}, 0)$ | $x = -\frac{1}{4a}$ | Right |
| Horizontal (left) | $x = -ay^2$ | $(0,0)$ | $(-\frac{1}{4a}, 0)$ | $x = \frac{1}{4a}$ | Left |

---

## Examples

### Example 1: Find all features
Given $f(x) = 2x^2 - 8x + 6$

1. **Vertex:**
   - $h = -\frac{-8}{2(2)} = 2$
   - $k = 2(2)^2 - 8(2) + 6 = -2$
   - Vertex: $(2, -2)$

2. **Axis of symmetry:** $x = 2$

3. **Direction:** $a = 2 > 0$ → Opens upward

4. **Y-intercept:** $(0, 6)$

5. **X-intercepts:** Solve $2x^2 - 8x + 6 = 0$
   - $x^2 - 4x + 3 = 0$
   - $(x-1)(x-3) = 0$
   - $x = 1, x = 3$

---

### Example 2: Write equation from vertex and point
Vertex at $(3, -4)$, passes through $(1, 0)$

1. Use vertex form: $y = a(x - 3)^2 - 4$
2. Substitute $(1, 0)$: $0 = a(1-3)^2 - 4$
3. $0 = 4a - 4 \Rightarrow a = 1$
4. Equation: $y = (x - 3)^2 - 4$

---

## Quick Reference

| Feature | Formula |
|---------|---------|
| Vertex (x-coord) | $h = -\frac{b}{2a}$ |
| Vertex (y-coord) | $k = c - \frac{b^2}{4a}$ |
| Axis of symmetry | $x = -\frac{b}{2a}$ |
| Y-intercept | $(0, c)$ |
| Discriminant | $D = b^2 - 4ac$ |
| Focus | $\left(h, k + \frac{1}{4a}\right)$ |
| Directrix | $y = k - \frac{1}{4a}$ |

---

## See Also
- [[Quadratic Function]] - Algebraic treatment of quadratic equations
- [[Quadratic Inequalities]] - Solving parabola-based inequalities
- [[Polynomials]] - General polynomial theory
- [[00 - Algebra MOC]] - Algebra topics overview
