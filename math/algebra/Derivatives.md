---
tags: [math, algebra, calculus]
status: complete
---
# Derivatives

> The derivative measures instantaneous rate of change; geometrically, the slope of the tangent line to a curve.

## Definition

$$\boxed{f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}}$$

![[graph_of_tangent.jpg]]

**Notations:** $f'(x)$ (Lagrange), $\dfrac{df}{dx}$ (Leibniz), $\dot{f}$ (Newton, for time), $D_x f$ (Euler)

## Basic Rules

| Rule | Formula |
|------|---------|
| Constant | $\dfrac{d}{dx}(c) = 0$ |
| Power | $\dfrac{d}{dx}(x^n) = nx^{n-1}$ |
| Constant multiple | $\dfrac{d}{dx}[cf(x)] = c\,f'(x)$ |
| Sum/difference | $\dfrac{d}{dx}[f \pm g] = f' \pm g'$ |
| Product | $\dfrac{d}{dx}[fg] = f'g + fg'$ |
| Quotient | $\dfrac{d}{dx}\!\left[\dfrac{f}{g}\right] = \dfrac{f'g - fg'}{g^2}$ |

## Chain Rule

For composite functions:
$$\boxed{\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)}$$

**Example:** $\dfrac{d}{dx}[\sin(x^2)] = \cos(x^2) \cdot 2x$

## Common Derivatives

### Polynomial and Power

| $f(x)$ | $f'(x)$ |
|--------|---------|
| $x^n$ | $nx^{n-1}$ |
| $\sqrt{x}$ | $\frac{1}{2\sqrt{x}}$ |
| $\frac{1}{x}$ | $-\frac{1}{x^2}$ |

### Exponential and Logarithmic

| $f(x)$ | $f'(x)$ |
|--------|---------|
| $e^x$ | $e^x$ |
| $a^x$ | $a^x \ln a$ |
| $\ln x$ | $\frac{1}{x}$ |
| $\log_a x$ | $\frac{1}{x \ln a}$ |

### Trigonometric

| $f(x)$ | $f'(x)$ |
|--------|---------|
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2 x$ |
| $\cot x$ | $-\csc^2 x$ |
| $\sec x$ | $\sec x \tan x$ |
| $\csc x$ | $-\csc x \cot x$ |

### Inverse Trigonometric

| $f(x)$ | $f'(x)$ |
|--------|---------|
| $\arcsin x$ | $\frac{1}{\sqrt{1-x^2}}$ |
| $\arccos x$ | $-\frac{1}{\sqrt{1-x^2}}$ |
| $\arctan x$ | $\frac{1}{1+x^2}$ |

![[table_of_derivative.png]]

## Higher-Order Derivatives

$$\boxed{f''(x) = \frac{d^2f}{dx^2}} \qquad \boxed{f^{(n)}(x) = \frac{d^nf}{dx^n}}$$

**Physical interpretation:** if $f$ is position, $f'$ is velocity, $f''$ is acceleration.

## Implicit Differentiation

Differentiate both sides with respect to $x$, applying chain rule to $y$ terms.

**Example:** $x^2 + y^2 = 25$
$$2x + 2y\frac{dy}{dx} = 0 \implies \frac{dy}{dx} = -\frac{x}{y}$$

## Applications

### Critical Points and Extrema

Critical points: $f'(x) = 0$ or $f'$ undefined.

**First Derivative Test:**
- $f'$ changes $+ \to -$ at $c$: local maximum
- $f'$ changes $- \to +$ at $c$: local minimum

**Second Derivative Test:**
- $f'(c) = 0$ and $f''(c) > 0$: local minimum
- $f'(c) = 0$ and $f''(c) < 0$: local maximum

### Concavity

- $f''(x) > 0$: concave up
- $f''(x) < 0$: concave down
- $f''(x) = 0$ with sign change: inflection point

![[types_of_concavity.png]]
![[derivatives_and_graph_shares.jpg]]

### Linear Approximation

$$\boxed{f(x + \Delta x) \approx f(x) + f'(x) \cdot \Delta x}$$

Expressed as differential: $dy = f'(x)\,dx$

## Key Theorems

### Mean Value Theorem
If $f$ is continuous on $[a, b]$ and differentiable on $(a, b)$:
$$\boxed{f'(c) = \frac{f(b) - f(a)}{b - a}} \quad \text{for some } c \in (a, b)$$

![[secant_tangent_lines.png]]

### L'Hopital's Rule
For $\frac{0}{0}$ or $\frac{\infty}{\infty}$ indeterminate forms:
$$\boxed{\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}}$$

## Related Rates

When quantities are related and change with time: write the relation, differentiate both sides w.r.t. $t$, substitute knowns, solve for the unknown rate.

## See also

- [[complex numbers]]
- [[algebraic identities]]
