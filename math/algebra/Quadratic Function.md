---
tags: [math, algebra, quadratic]
status: complete
---
# Quadratic Function

> A second-degree polynomial function forming a parabola when graphed, defined as $f(x) = ax^2 + bx + c$ with $a \neq 0$.

## Forms

| Form | Expression | Advantage |
|------|------------|-----------|
| **Standard** | $f(x) = ax^2 + bx + c$ | Easy to identify coefficients, y-intercept |
| **Vertex** | $f(x) = a(x - h)^2 + k$ | Vertex $(h, k)$ immediately visible |
| **Factored** | $f(x) = a(x - x_1)(x - x_2)$ | Roots $x_1$, $x_2$ immediately visible |

Convert standard → vertex form by completing the square.

## Discriminant

$$D = b^2 - 4ac$$

| $D$ | Roots | Graph |
|-----|-------|-------|
| $D > 0$ | Two distinct real roots | Crosses x-axis twice |
| $D = 0$ | One repeated root | Touches x-axis at vertex |
| $D < 0$ | No real roots (complex conjugates) | Does not intersect x-axis |

## Quadratic Formula

$$x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

## Vieta's Formulas

For roots $x_1$, $x_2$ of $ax^2 + bx + c = 0$:

$$x_1 + x_2 = -\frac{b}{a} \qquad x_1 \cdot x_2 = \frac{c}{a}$$

**Use case:** Given roots $x_1 = 3$, $x_2 = -2$: sum $= 1$, product $= -6$, equation is $x^2 - x - 6 = 0$.

## Vertex and Axis of Symmetry

$$h = -\frac{b}{2a} \qquad k = f(h) = -\frac{D}{4a}$$

Axis of symmetry: $x = -\frac{b}{2a}$

- $a > 0$: parabola opens upward, vertex is minimum
- $a < 0$: parabola opens downward, vertex is maximum

## Intercepts

**Y-intercept:** $(0, c)$

**X-intercepts:** set $f(x) = 0$, solve by factoring, quadratic formula, or completing the square.

## Completing the Square

Converts standard form to vertex form. For $f(x) = 2x^2 - 8x + 6$:

$$f(x) = 2(x^2 - 4x) + 6 = 2(x^2 - 4x + 4 - 4) + 6 = 2(x-2)^2 - 2$$

## Graph Characteristics

| Feature | Formula |
|---------|---------|
| Vertex | $\left(-\frac{b}{2a},\, -\frac{D}{4a}\right)$ |
| Axis of symmetry | $x = -\frac{b}{2a}$ |
| Y-intercept | $(0, c)$ |
| X-intercepts | $\left(\frac{-b \pm \sqrt{D}}{2a},\, 0\right)$ |
| Opens upward | $a > 0$ |
| Narrower | Larger $|a|$ |

## Solving Methods

| Method | When to Use |
|--------|-------------|
| Factoring | Easily factorable trinomials |
| Square root | Form $ax^2 + c = 0$ |
| Completing the square | Deriving vertex form |
| Quadratic formula | Universal |

## See also

- [[polynomials]] - General polynomial theory
- [[quadratic inequalities]] - Solving inequalities with quadratics
- [[matrices]] - Matrix form of quadratic systems
- [[Index]]
