---
tags:
  - math/calculus
  - integrals
  - integration
related:
  - '[[Derivatives]]'
  - '[[Limits]]'
  - '[[00 - Algebra MOC]]'
  - '[[00 - Math MOC]]'
---

## Introduction
**Integration** is the inverse operation of differentiation. An integral represents the accumulation of quantities, such as areas under curves, total displacement, or accumulated change. There are two main types: **indefinite integrals** (antiderivatives) and **definite integrals** (area under a curve).

---

## Fundamental Concepts

### Indefinite Integral
An indefinite integral represents a family of functions whose derivative is the integrand:
$$
\boxed{\int f(x) \, dx = F(x) + C}
$$
Where $F'(x) = f(x)$ and $C$ is the constant of integration.

### Definite Integral
A definite integral computes the signed area under a curve from $a$ to $b$:
$$
\boxed{\int_a^b f(x) \, dx = F(b) - F(a)}
$$
Where $F(x)$ is an antiderivative of $f(x)$.

### Fundamental Theorem of Calculus
$$
\boxed{\frac{d}{dx} \int_a^x f(t) \, dt = f(x)}
$$
$$
\boxed{\int_a^b f'(x) \, dx = f(b) - f(a)}
$$

---

## Basic Integration Rules

### Power Rule
$$
\boxed{\int x^n \, dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)}
$$

### Constant Multiple Rule
$$
\boxed{\int k \cdot f(x) \, dx = k \int f(x) \, dx}
$$

### Sum/Difference Rule
$$
\boxed{\int [f(x) \pm g(x)] \, dx = \int f(x) \, dx \pm \int g(x) \, dx}
$$

---

## Standard Integrals

### Polynomial and Algebraic Functions
$$
\boxed{\int 1 \, dx = x + C}
$$
$$
\boxed{\int x \, dx = \frac{x^2}{2} + C}
$$
$$
\boxed{\int \frac{1}{x} \, dx = \ln|x| + C}
$$
$$
\boxed{\int \sqrt{x} \, dx = \frac{2x^{3/2}}{3} + C}
$$
$$
\boxed{\int \frac{1}{\sqrt{x}} \, dx = 2\sqrt{x} + C}
$$

### Exponential Functions
$$
\boxed{\int e^x \, dx = e^x + C}
$$
$$
\boxed{\int a^x \, dx = \frac{a^x}{\ln a} + C \quad (a > 0, a \neq 1)}
$$
$$
\boxed{\int e^{kx} \, dx = \frac{e^{kx}}{k} + C}
$$

### Trigonometric Functions
$$
\boxed{\int \sin x \, dx = -\cos x + C}
$$
$$
\boxed{\int \cos x \, dx = \sin x + C}
$$
$$
\boxed{\int \tan x \, dx = -\ln|\cos x| + C = \ln|\sec x| + C}
$$
$$
\boxed{\int \cot x \, dx = \ln|\sin x| + C}
$$
$$
\boxed{\int \sec x \, dx = \ln|\sec x + \tan x| + C}
$$
$$
\boxed{\int \csc x \, dx = -\ln|\csc x + \cot x| + C}
$$
$$
\boxed{\int \sec^2 x \, dx = \tan x + C}
$$
$$
\boxed{\int \csc^2 x \, dx = -\cot x + C}
$$
$$
\boxed{\int \sec x \tan x \, dx = \sec x + C}
$$
$$
\boxed{\int \csc x \cot x \, dx = -\csc x + C}
$$

### Inverse Trigonometric Functions
$$
\boxed{\int \frac{1}{\sqrt{1-x^2}} \, dx = \arcsin x + C = -\arccos x + C}
$$
$$
\boxed{\int \frac{1}{1+x^2} \, dx = \arctan x + C}
$$
$$
\boxed{\int \frac{1}{x\sqrt{x^2-1}} \, dx = \text{arcsec}|x| + C}
$$

### Hyperbolic Functions
$$
\boxed{\int \sinh x \, dx = \cosh x + C}
$$
$$
\boxed{\int \cosh x \, dx = \sinh x + C}
$$
$$
\boxed{\int \tanh x \, dx = \ln(\cosh x) + C}
$$

---

## Integration Techniques

### 1. Substitution Method (u-substitution)
For integrals of the form $\int f(g(x)) \cdot g'(x) \, dx$:

**Steps:**
1. Let $u = g(x)$
2. Then $du = g'(x) \, dx$
3. Replace and integrate: $\int f(u) \, du$
4. Substitute back: replace $u$ with $g(x)$

**Example:**
$$
\int 2x \cos(x^2) \, dx
$$
Let $u = x^2$, then $du = 2x \, dx$
$$
= \int \cos u \, du = \sin u + C = \sin(x^2) + C
$$

### 2. Integration by Parts
Based on the product rule for differentiation:
$$
\boxed{\int u \, dv = uv - \int v \, du}
$$

**LIATE Priority** (choose $u$ in this order):
- **L**ogarithmic: $\ln x$
- **I**nverse trig: $\arctan x, \arcsin x$
- **A**lgebraic: $x^2, x, \sqrt{x}$
- **T**rigonometric: $\sin x, \cos x$
- **E**xponential: $e^x, a^x$

**Example:**
$$
\int x e^x \, dx
$$
Let $u = x$, $dv = e^x dx$  
Then $du = dx$, $v = e^x$
$$
= xe^x - \int e^x \, dx = xe^x - e^x + C = e^x(x-1) + C
$$

### 3. Trigonometric Substitution
For integrals involving $\sqrt{a^2 - x^2}$, $\sqrt{a^2 + x^2}$, or $\sqrt{x^2 - a^2}$:

| Expression | Substitution | Identity |
|------------|-------------|----------|
| $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$ | $1 - \sin^2\theta = \cos^2\theta$ |
| $\sqrt{a^2 + x^2}$ | $x = a\tan\theta$ | $1 + \tan^2\theta = \sec^2\theta$ |
| $\sqrt{x^2 - a^2}$ | $x = a\sec\theta$ | $\sec^2\theta - 1 = \tan^2\theta$ |

### 4. Partial Fractions
For rational functions $\frac{P(x)}{Q(x)}$ where degree of $P < $ degree of $Q$:

**Decomposition forms:**
- Linear factor: $\frac{A}{x-a}$
- Repeated linear: $\frac{A}{x-a} + \frac{B}{(x-a)^2}$
- Quadratic: $\frac{Ax+B}{x^2+bx+c}$

**Example:**
$$
\int \frac{1}{x^2-1} \, dx = \int \frac{1}{(x-1)(x+1)} \, dx
$$
Decompose: $\frac{1}{(x-1)(x+1)} = \frac{A}{x-1} + \frac{B}{x+1}$  
Solving: $A = \frac{1}{2}$, $B = -\frac{1}{2}$
$$
= \frac{1}{2}\ln|x-1| - \frac{1}{2}\ln|x+1| + C = \frac{1}{2}\ln\left|\frac{x-1}{x+1}\right| + C
$$

### 5. Trigonometric Identities
Use identities to simplify integrals:

**Power-reducing formulas:**
$$
\sin^2 x = \frac{1 - \cos 2x}{2}
$$
$$
\cos^2 x = \frac{1 + \cos 2x}{2}
$$
$$
\tan^2 x = \sec^2 x - 1
$$

**Example:**
$$
\int \sin^2 x \, dx = \int \frac{1 - \cos 2x}{2} \, dx = \frac{x}{2} - \frac{\sin 2x}{4} + C
$$

---

## Special Integrals

### Rational Functions
$$
\boxed{\int \frac{1}{x^2 + a^2} \, dx = \frac{1}{a} \arctan\left(\frac{x}{a}\right) + C}
$$
$$
\boxed{\int \frac{1}{x^2 - a^2} \, dx = \frac{1}{2a} \ln\left|\frac{x-a}{x+a}\right| + C}
$$
$$
\boxed{\int \frac{1}{\sqrt{a^2 - x^2}} \, dx = \arcsin\left(\frac{x}{a}\right) + C}
$$
$$
\boxed{\int \frac{1}{\sqrt{x^2 + a^2}} \, dx = \ln\left|x + \sqrt{x^2 + a^2}\right| + C}
$$
$$
\boxed{\int \frac{1}{\sqrt{x^2 - a^2}} \, dx = \ln\left|x + \sqrt{x^2 - a^2}\right| + C}
$$

### Products of Functions
$$
\boxed{\int e^{ax}\sin(bx) \, dx = \frac{e^{ax}}{a^2+b^2}(a\sin(bx) - b\cos(bx)) + C}
$$
$$
\boxed{\int e^{ax}\cos(bx) \, dx = \frac{e^{ax}}{a^2+b^2}(a\cos(bx) + b\sin(bx)) + C}
$$

---

## Definite Integral Properties

### Basic Properties
$$
\boxed{\int_a^a f(x) \, dx = 0}
$$
$$
\boxed{\int_a^b f(x) \, dx = -\int_b^a f(x) \, dx}
$$
$$
\boxed{\int_a^b f(x) \, dx + \int_b^c f(x) \, dx = \int_a^c f(x) \, dx}
$$
$$
\boxed{\int_a^b k \cdot f(x) \, dx = k \int_a^b f(x) \, dx}
$$

### Symmetry Properties
**Even function** ($f(-x) = f(x)$):
$$
\boxed{\int_{-a}^a f(x) \, dx = 2\int_0^a f(x) \, dx}
$$

**Odd function** ($f(-x) = -f(x)$):
$$
\boxed{\int_{-a}^a f(x) \, dx = 0}
$$

### Comparison Properties
If $f(x) \geq 0$ on $[a,b]$:
$$
\boxed{\int_a^b f(x) \, dx \geq 0}
$$

If $f(x) \geq g(x)$ on $[a,b]$:
$$
\boxed{\int_a^b f(x) \, dx \geq \int_a^b g(x) \, dx}
$$

---

## Improper Integrals

### Type 1: Infinite Limits
$$
\boxed{\int_a^\infty f(x) \, dx = \lim_{t \to \infty} \int_a^t f(x) \, dx}
$$
$$
\boxed{\int_{-\infty}^b f(x) \, dx = \lim_{t \to -\infty} \int_t^b f(x) \, dx}
$$

**Example:**
$$
\int_1^\infty \frac{1}{x^2} \, dx = \lim_{t \to \infty} \left[-\frac{1}{x}\right]_1^t = \lim_{t \to \infty} \left(-\frac{1}{t} + 1\right) = 1
$$

### Type 2: Discontinuous Integrand
If $f(x)$ has a discontinuity at $x = c$ in $[a,b]$:
$$
\boxed{\int_a^b f(x) \, dx = \lim_{\epsilon \to 0^+} \int_a^{c-\epsilon} f(x) \, dx + \lim_{\delta \to 0^+} \int_{c+\delta}^b f(x) \, dx}
$$

---

## Applications of Integrals

### 1. Area Under a Curve
Area between $f(x)$ and the x-axis from $a$ to $b$:
$$
\boxed{A = \int_a^b |f(x)| \, dx}
$$

### 2. Area Between Two Curves
Area between $f(x)$ and $g(x)$ where $f(x) \geq g(x)$:
$$
\boxed{A = \int_a^b [f(x) - g(x)] \, dx}
$$

### 3. Volume of Revolution
**Disk method** (rotation about x-axis):
$$
\boxed{V = \pi \int_a^b [f(x)]^2 \, dx}
$$

**Shell method** (rotation about y-axis):
$$
\boxed{V = 2\pi \int_a^b x \cdot f(x) \, dx}
$$

### 4. Arc Length
Length of curve $y = f(x)$ from $x = a$ to $x = b$:
$$
\boxed{L = \int_a^b \sqrt{1 + [f'(x)]^2} \, dx}
$$

### 5. Average Value of a Function
$$
\boxed{f_{\text{avg}} = \frac{1}{b-a} \int_a^b f(x) \, dx}
$$

### 6. Work Done by a Variable Force
$$
\boxed{W = \int_a^b F(x) \, dx}
$$

---

## Numerical Integration Methods

### Trapezoidal Rule
$$
\boxed{\int_a^b f(x) \, dx \approx \frac{b-a}{2n} \left[f(x_0) + 2\sum_{i=1}^{n-1}f(x_i) + f(x_n)\right]}
$$

### Simpson's Rule
$$
\boxed{\int_a^b f(x) \, dx \approx \frac{b-a}{3n} \left[f(x_0) + 4\sum_{\text{odd } i}f(x_i) + 2\sum_{\text{even } i}f(x_i) + f(x_n)\right]}
$$

---

## Common Integration Tricks

### 1. Add and Subtract
Add and subtract the same term to create a recognizable pattern.

### 2. Multiply by Conjugate
For expressions like $\frac{1}{\sqrt{a} + \sqrt{b}}$, multiply by $\frac{\sqrt{a} - \sqrt{b}}{\sqrt{a} - \sqrt{b}}$.

### 3. Completing the Square
For quadratics in the denominator: $ax^2 + bx + c = a\left[\left(x + \frac{b}{2a}\right)^2 + \left(\frac{c}{a} - \frac{b^2}{4a^2}\right)\right]$

### 4. Weierstrass Substitution
For rational trigonometric functions:
$$
t = \tan\left(\frac{x}{2}\right), \quad \sin x = \frac{2t}{1+t^2}, \quad \cos x = \frac{1-t^2}{1+t^2}, \quad dx = \frac{2}{1+t^2}dt
$$

---

## See Also
- [[Derivatives]] - The inverse operation of integration
- [[Limits]] - Fundamental to understanding definite integrals
- [[00 - Algebra MOC]] - Algebra topics overview
- [[00 - Math MOC]] - Mathematics overview
