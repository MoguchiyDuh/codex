---
tags: [math, algebra, calculus, integration, integrals]
status: complete
---

# Integrals

> The inverse of differentiation — accumulates quantities such as area under a curve or total displacement.

## Fundamental Concepts

### Indefinite integral
Family of antiderivatives of $f(x)$:
$$\boxed{\int f(x)\,dx = F(x) + C, \quad F'(x) = f(x)}$$

### Definite integral
Signed area under a curve from $a$ to $b$:
$$\boxed{\int_a^b f(x)\,dx = F(b) - F(a)}$$

### Fundamental Theorem of Calculus
$$\boxed{\frac{d}{dx}\int_a^x f(t)\,dt = f(x)}$$
$$\boxed{\int_a^b f'(x)\,dx = f(b) - f(a)}$$

## Basic Rules

| Rule | Formula |
|------|---------|
| Power ($n \neq -1$) | $\int x^n\,dx = \dfrac{x^{n+1}}{n+1} + C$ |
| Constant multiple | $\int k f(x)\,dx = k\int f(x)\,dx$ |
| Sum / difference | $\int [f \pm g]\,dx = \int f\,dx \pm \int g\,dx$ |

## Standard Integrals

### Polynomial and algebraic
$$\int \frac{1}{x}\,dx = \ln|x| + C \qquad \int \sqrt{x}\,dx = \frac{2x^{3/2}}{3} + C$$

### Exponential
$$\int e^x\,dx = e^x + C \qquad \int a^x\,dx = \frac{a^x}{\ln a} + C \qquad \int e^{kx}\,dx = \frac{e^{kx}}{k} + C$$

### Trigonometric
$$\int \sin x\,dx = -\cos x + C \qquad \int \cos x\,dx = \sin x + C$$
$$\int \sec^2 x\,dx = \tan x + C \qquad \int \csc^2 x\,dx = -\cot x + C$$
$$\int \tan x\,dx = \ln|\sec x| + C \qquad \int \sec x\,dx = \ln|\sec x + \tan x| + C$$

### Inverse trigonometric
$$\int \frac{1}{\sqrt{1-x^2}}\,dx = \arcsin x + C \qquad \int \frac{1}{1+x^2}\,dx = \arctan x + C$$

### Hyperbolic
$$\int \sinh x\,dx = \cosh x + C \qquad \int \cosh x\,dx = \sinh x + C$$

## Integration Techniques

### Substitution (u-substitution)
For $\int f(g(x))\cdot g'(x)\,dx$: let $u = g(x)$, $du = g'(x)\,dx$.

Example: $\int 2x\cos(x^2)\,dx$ — let $u = x^2$, $du = 2x\,dx$ → $\int \cos u\,du = \sin(x^2) + C$

### Integration by parts
$$\boxed{\int u\,dv = uv - \int v\,du}$$

**LIATE** priority for choosing $u$: Logarithmic → Inverse trig → Algebraic → Trigonometric → Exponential

Example: $\int xe^x\,dx$ — $u=x$, $dv=e^x dx$ → $xe^x - e^x + C$

### Trigonometric substitution

| Expression | Substitution | Identity used |
|------------|-------------|---------------|
| $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$ | $1 - \sin^2\theta = \cos^2\theta$ |
| $\sqrt{a^2 + x^2}$ | $x = a\tan\theta$ | $1 + \tan^2\theta = \sec^2\theta$ |
| $\sqrt{x^2 - a^2}$ | $x = a\sec\theta$ | $\sec^2\theta - 1 = \tan^2\theta$ |

### Partial fractions
For $\frac{P(x)}{Q(x)}$ where $\deg P < \deg Q$. Decompose denominator into linear/quadratic factors.

Example: $\int \frac{1}{x^2-1}\,dx = \frac{1}{2}\ln\left|\frac{x-1}{x+1}\right| + C$

### Power-reducing identities
$$\sin^2 x = \frac{1-\cos 2x}{2} \qquad \cos^2 x = \frac{1+\cos 2x}{2}$$

## Special Integrals

$$\int \frac{1}{x^2+a^2}\,dx = \frac{1}{a}\arctan\frac{x}{a} + C$$
$$\int \frac{1}{\sqrt{a^2-x^2}}\,dx = \arcsin\frac{x}{a} + C$$
$$\int e^{ax}\sin(bx)\,dx = \frac{e^{ax}}{a^2+b^2}(a\sin bx - b\cos bx) + C$$

## Definite Integral Properties

$$\int_a^a f\,dx = 0 \qquad \int_a^b f\,dx = -\int_b^a f\,dx$$
$$\int_a^b f\,dx + \int_b^c f\,dx = \int_a^c f\,dx$$

**Symmetry:** even function on $[-a,a]$ → $2\int_0^a f\,dx$; odd function → $0$

## Improper Integrals

**Infinite limits:**
$$\int_a^\infty f(x)\,dx = \lim_{t\to\infty}\int_a^t f(x)\,dx$$

**Discontinuous integrand:** split at discontinuity, take limits from each side.

Example: $\int_1^\infty \frac{1}{x^2}\,dx = 1$

## Applications

| Application | Formula |
|-------------|---------|
| Area under curve | $A = \int_a^b \|f(x)\|\,dx$ |
| Area between curves | $A = \int_a^b [f(x)-g(x)]\,dx$ |
| Volume (disk) | $V = \pi\int_a^b [f(x)]^2\,dx$ |
| Volume (shell) | $V = 2\pi\int_a^b x\cdot f(x)\,dx$ |
| Arc length | $L = \int_a^b \sqrt{1+[f'(x)]^2}\,dx$ |
| Average value | $f_\text{avg} = \frac{1}{b-a}\int_a^b f(x)\,dx$ |

## Numerical Methods

**Trapezoidal rule:**
$$\int_a^b f\,dx \approx \frac{b-a}{2n}\left[f(x_0) + 2\sum_{i=1}^{n-1}f(x_i) + f(x_n)\right]$$

**Simpson's rule:**
$$\int_a^b f\,dx \approx \frac{b-a}{3n}\left[f(x_0) + 4\sum_\text{odd}f(x_i) + 2\sum_\text{even}f(x_i) + f(x_n)\right]$$

## See also

- [[limits]] — definite integrals are defined as limits of Riemann sums
