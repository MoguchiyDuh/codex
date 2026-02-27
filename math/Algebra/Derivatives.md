---
tags:
  - math/algebra
  - calculus
  - derivatives
related:
  - "[[Limits]]"
  - "[[00 - Algebra MOC]]"
---
# Derivatives

## Definition
The **derivative** of a function measures the rate at which the function's value changes with respect to a change in its input.

### $$\boxed{f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}}$$

**Alternative notations:**
- $f'(x)$ (Lagrange notation)
- $\frac{df}{dx}$ (Leibniz notation)
- $\dot{f}$ (Newton notation - for time derivatives)
- $D_x f$ (Euler notation)

---

## Geometric Interpretation

The derivative at a point is the **slope of the tangent line** to the function at that point.

<img src="Pictures/graph_of_tangent.jpg" width=500 height="auto" style="display: block; margin: auto">

---

## Basic Derivative Rules

### Constant Rule
### $$\boxed{\frac{d}{dx}(c) = 0}$$

### Power Rule
### $$\boxed{\frac{d}{dx}(x^n) = nx^{n-1}}$$

**Example:** $\frac{d}{dx}(x^3) = 3x^2$

### Constant Multiple Rule
### $$\boxed{\frac{d}{dx}[cf(x)] = c \cdot f'(x)}$$

### Sum/Difference Rule
### $$\boxed{\frac{d}{dx}[f(x) \pm g(x)] = f'(x) \pm g'(x)}$$

---

## Product and Quotient Rules

### Product Rule
### $$\boxed{\frac{d}{dx}[f(x) \cdot g(x)] = f'(x) \cdot g(x) + f(x) \cdot g'(x)}$$

### Quotient Rule
### $$\boxed{\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x) \cdot g(x) - f(x) \cdot g'(x)}{[g(x)]^2}}$$

---

## Chain Rule

For composite functions:
### $$\boxed{\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)}$$

**Example:** $\frac{d}{dx}[\sin(x^2)] = \cos(x^2) \cdot 2x = 2x\cos(x^2)$

---

## Common Derivatives Table

<img src="Pictures/table_of_derivative.png" width=500 height="auto" style="display: block; margin: auto">

### Polynomial and Power Functions
| Function | Derivative |
|----------|------------|
| $x^n$ | $nx^{n-1}$ |
| $\sqrt{x}$ | $\frac{1}{2\sqrt{x}}$ |
| $\frac{1}{x}$ | $-\frac{1}{x^2}$ |

### Exponential Functions
| Function | Derivative |
|----------|------------|
| $e^x$ | $e^x$ |
| $a^x$ | $a^x \ln(a)$ |

### Logarithmic Functions
| Function | Derivative |
|----------|------------|
| $\ln(x)$ | $\frac{1}{x}$ |
| $\log_a(x)$ | $\frac{1}{x \ln(a)}$ |

### Trigonometric Functions
| Function | Derivative |
|----------|------------|
| $\sin(x)$ | $\cos(x)$ |
| $\cos(x)$ | $-\sin(x)$ |
| $\tan(x)$ | $\sec^2(x) = \frac{1}{\cos^2(x)}$ |
| $\cot(x)$ | $-\csc^2(x) = -\frac{1}{\sin^2(x)}$ |
| $\sec(x)$ | $\sec(x)\tan(x)$ |
| $\csc(x)$ | $-\csc(x)\cot(x)$ |

### Inverse Trigonometric Functions
| Function | Derivative |
|----------|------------|
| $\arcsin(x)$ | $\frac{1}{\sqrt{1-x^2}}$ |
| $\arccos(x)$ | $-\frac{1}{\sqrt{1-x^2}}$ |
| $\arctan(x)$ | $\frac{1}{1+x^2}$ |

---

## Higher-Order Derivatives

**Second derivative:**
### $$\boxed{f''(x) = \frac{d^2f}{dx^2} = \frac{d}{dx}\left[\frac{df}{dx}\right]}$$

**n-th derivative:**
### $$\boxed{f^{(n)}(x) = \frac{d^nf}{dx^n}}$$

**Physical interpretation:**
- First derivative: velocity (if $f$ is position)
- Second derivative: acceleration

---

## Implicit Differentiation

When $y$ is defined implicitly by an equation involving $x$ and $y$:

**Example:** For $x^2 + y^2 = 25$
1. Differentiate both sides with respect to $x$
2. Apply chain rule to $y$ terms: $\frac{d}{dx}(y^2) = 2y\frac{dy}{dx}$
3. Solve for $\frac{dy}{dx}$

Result: $2x + 2y\frac{dy}{dx} = 0 \implies \frac{dy}{dx} = -\frac{x}{y}$

---

## Applications

### 1. Finding Critical Points
Critical points occur where $f'(x) = 0$ or $f'(x)$ is undefined.

### 2. Determining Increasing/Decreasing Intervals
- $f'(x) > 0$: function is increasing
- $f'(x) < 0$: function is decreasing

<img src="Pictures/derivatives_and_graph_shares.jpg" width=500 height="auto" style="display: block; margin: auto">

### 3. Finding Local Extrema (Maxima/Minima)

**First Derivative Test:**
- If $f'$ changes from positive to negative at $x = c$: local maximum
- If $f'$ changes from negative to positive at $x = c$: local minimum

**Second Derivative Test:**
- If $f'(c) = 0$ and $f''(c) > 0$: local minimum
- If $f'(c) = 0$ and $f''(c) < 0$: local maximum

### 4. Concavity

- $f''(x) > 0$: concave up (curves upward) ∪
- $f''(x) < 0$: concave down (curves downward) ∩

**Inflection points:** where $f''(x) = 0$ and concavity changes

<img src="Pictures/types_of_concavity.png" width=500 height="auto" style="display: block; margin: auto">

### 5. Optimization Problems

Steps:
1. Define the function to optimize
2. Find derivative
3. Set $f'(x) = 0$ and solve
4. Verify it's a maximum/minimum using first or second derivative test
5. Check endpoints if applicable

---

## Related Rates

When two or more quantities are related and changing with respect to time:

**Steps:**
1. Write equation relating variables
2. Differentiate both sides with respect to time $t$
3. Substitute known values
4. Solve for unknown rate

**Example:** Ladder sliding down wall - relate height $y$ and distance from wall $x$ using Pythagorean theorem, then differentiate.

---

## L'Hôpital's Rule

For indeterminate forms $\frac{0}{0}$ or $\frac{\infty}{\infty}$:
### $$\boxed{\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}}$$

---

## Mean Value Theorem

If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, then there exists $c \in (a,b)$ such that:
### $$\boxed{f'(c) = \frac{f(b) - f(a)}{b - a}}$$

<img src="Pictures/secant_tangent_lines.png" width=500 height="auto" style="display: block; margin: auto">


---

## Differential

The differential $dy$ represents an infinitesimal change:
### $$\boxed{dy = f'(x) \cdot dx}$$

Used for linear approximation:
### $$\boxed{f(x + \Delta x) \approx f(x) + f'(x) \cdot \Delta x}$$

---

## See Also
- [[Limits]] - Foundation of derivatives
- [[00 - Algebra MOC]] - Algebra topics overview
