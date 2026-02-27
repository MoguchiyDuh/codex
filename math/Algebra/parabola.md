---
tags: [math, algebra, quadratics, parabola, conic-sections]
status: complete
---

# Parabola

> The graph of a quadratic function — a conic section defined by equal distance from a focus and directrix.

## Definition

A **parabola** is the set of all points equidistant from a fixed point (focus) and a fixed line (directrix).

Algebraically, it is the graph of:
$$\boxed{y = ax^2 + bx + c \quad (a \neq 0)}$$

## Standard Forms

### Vertex form (vertical parabola)
$$\boxed{y = a(x-h)^2 + k}$$

- Vertex: $(h, k)$
- Axis of symmetry: $x = h$
- Opens up if $a > 0$, down if $a < 0$

### Horizontal parabola
$$\boxed{x = a(y-k)^2 + h}$$

- Vertex: $(h, k)$
- Axis of symmetry: $y = k$
- Opens right if $a > 0$, left if $a < 0$

## Components

### Vertex
The turning point (minimum or maximum).

For $y = ax^2 + bx + c$:
$$\boxed{h = -\frac{b}{2a}, \qquad k = c - \frac{b^2}{4a}}$$

### Axis of symmetry
$$\boxed{x = -\frac{b}{2a}}$$

### Focus and directrix
For $y = a(x-h)^2 + k$:
$$\text{Focus: } \left(h,\ k + \frac{1}{4a}\right) \qquad \text{Directrix: } y = k - \frac{1}{4a}$$

Every point on the parabola is equidistant from the focus and directrix.

### Focal length
$$p = \frac{1}{4a}$$

## Effect of Parameters

| Parameter | Effect |
|-----------|--------|
| $a > 0$ | Opens up; vertex is minimum |
| $a < 0$ | Opens down; vertex is maximum |
| $\|a\| > 1$ | Narrow (steep) |
| $\|a\| < 1$ | Wide (flat) |
| $b$ | Shifts vertex horizontally: $h = -b/(2a)$ |
| $c$ | Sets y-intercept at $(0, c)$ |

## Key Features

**Domain / Range** for $y = a(x-h)^2 + k$:
- Domain: $(-\infty, \infty)$
- Range: $[k, \infty)$ if $a>0$; $(-\infty, k]$ if $a<0$

**X-intercepts** (set $y=0$, use quadratic formula):
$$x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$$

Discriminant $D = b^2 - 4ac$: $D>0$ → two roots; $D=0$ → one root; $D<0$ → no real roots.

**Y-intercept:** $(0, c)$

## Standard Equations Table

| Orientation | Equation | Focus | Directrix |
|-------------|----------|-------|-----------|
| Up | $y = ax^2$ | $(0,\ \frac{1}{4a})$ | $y = -\frac{1}{4a}$ |
| Down | $y = -ax^2$ | $(0,\ -\frac{1}{4a})$ | $y = \frac{1}{4a}$ |
| Right | $x = ay^2$ | $(\frac{1}{4a},\ 0)$ | $x = -\frac{1}{4a}$ |
| Left | $x = -ay^2$ | $(-\frac{1}{4a},\ 0)$ | $x = \frac{1}{4a}$ |

## Transformations of $y = x^2$

- $y = ax^2$: vertical stretch/compress ($|a|>1$ narrow, $|a|<1$ wide)
- $y = -x^2$: reflection across x-axis
- $y = (x-h)^2$: horizontal shift by $h$
- $y = x^2 + k$: vertical shift by $k$
- $y = a(x-h)^2 + k$: all combined (apply in order listed)

## Worked Examples

**Find all features of $f(x) = 2x^2 - 8x + 6$:**
- Vertex: $h = 2$, $k = -2$ → $(2, -2)$
- Axis of symmetry: $x = 2$
- Opens upward ($a=2>0$)
- Y-intercept: $(0, 6)$
- X-intercepts: $x=1, x=3$

**Equation from vertex $(3,-4)$ through $(1,0)$:**
- Vertex form: $y = a(x-3)^2 - 4$
- Sub $(1,0)$: $0 = 4a - 4 \Rightarrow a = 1$
- Result: $y = (x-3)^2 - 4$

## Applications

- **Projectile motion:** $h(t) = -\frac{1}{2}gt^2 + v_0 t + h_0$
- **Parabolic reflectors:** focus property concentrates parallel rays (satellite dishes, telescopes, headlights)
- **Suspension bridges:** parabolic cable profile under uniform load
- **Optimization:** revenue/cost functions maximized/minimized at vertex

## See also

- [[exponents]] — vertex and discriminant formulas involve squared terms
- [[limits]] — analyzing parabola behavior near roots or at infinity
