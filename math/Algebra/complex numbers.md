---
tags: [math, algebra, complex-numbers]
status: complete
---
# Complex Numbers

> Extension of the reals by the imaginary unit $i = \sqrt{-1}$, enabling solutions to equations like $x^2 + 1 = 0$.

## Definition

A complex number has the form:
$$\boxed{z = a + bi}$$

where $a = \text{Re}(z)$ is the real part, $b = \text{Im}(z)$ is the imaginary part, and $i^2 = -1$.

**Special cases:**
- $b = 0$: real number
- $a = 0$: purely imaginary
- $a = b = 0$: zero

## Powers of $i$

Cycle repeats with period 4:

| $i^0$ | $i^1$ | $i^2$ | $i^3$ | $i^4$ |
|-------|-------|-------|-------|-------|
| $1$ | $i$ | $-1$ | $-i$ | $1$ |

General formula: $i^n = i^{n \bmod 4}$

## Arithmetic Operations

### Addition and Subtraction
$$\boxed{(a + bi) \pm (c + di) = (a \pm c) + (b \pm d)i}$$

### Multiplication
$$\boxed{(a + bi)(c + di) = (ac - bd) + (ad + bc)i}$$

Uses $i^2 = -1$ to collapse the $bd$ term.

### Division
Multiply numerator and denominator by the conjugate of the denominator:
$$\boxed{\frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{c^2 + d^2}}$$

**Example:**
$$\frac{3 + 2i}{1 - i} = \frac{(3+2i)(1+i)}{2} = \frac{1 + 5i}{2} = \frac{1}{2} + \frac{5}{2}i$$

## Complex Conjugate

$$\boxed{\bar{z} = a - bi}$$

Geometric interpretation: reflection across the real axis.

**Key properties:**

| Property | Formula |
|----------|---------|
| Product with conjugate | $z \cdot \bar{z} = a^2 + b^2$ |
| Sum | $z + \bar{z} = 2\,\text{Re}(z)$ |
| Difference | $z - \bar{z} = 2i\,\text{Im}(z)$ |
| Distributivity | $\overline{z_1 z_2} = \bar{z_1}\bar{z_2}$ |

## Modulus

Distance from the origin in the complex plane:
$$\boxed{|z| = \sqrt{a^2 + b^2}}$$

**Properties:** $|z_1 z_2| = |z_1||z_2|$, $|z_1 + z_2| \leq |z_1| + |z_2|$ (triangle inequality), $|z^n| = |z|^n$

## Polar Form

$$\boxed{z = r(\cos\theta + i\sin\theta) = re^{i\theta}}$$

where $r = |z|$ and $\theta = \arg(z) = \tan^{-1}(b/a)$ (adjusted by quadrant).

**Conversion from rectangular:** $r = \sqrt{a^2 + b^2}$, $\theta$ from the quadrant of $(a, b)$.

## Euler's Formula

$$\boxed{e^{i\theta} = \cos\theta + i\sin\theta}$$

**Special values:**

| Expression | Value |
|------------|-------|
| $e^{i\pi}$ | $-1$ (Euler's identity: $e^{i\pi} + 1 = 0$) |
| $e^{i\pi/2}$ | $i$ |
| $e^{-i\pi/2}$ | $-i$ |

## De Moivre's Theorem

$$\boxed{(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)}$$

In exponential form: $(re^{i\theta})^n = r^n e^{in\theta}$

Used for powers, roots, and deriving trig identities.

**Example:** $(1+i)^{10} = (\sqrt{2}e^{i\pi/4})^{10} = 32e^{i5\pi/2} = 32i$

## Roots of Complex Numbers

The $n$ distinct $n$-th roots of $z = re^{i\theta}$:
$$\boxed{z_k = \sqrt[n]{r} \cdot e^{i(\theta + 2\pi k)/n}, \quad k = 0, 1, \ldots, n-1}$$

Evenly spaced on a circle of radius $\sqrt[n]{r}$, separated by angle $2\pi/n$.

## Quadratic Equations with Complex Roots

For $ax^2 + bx + c = 0$ with discriminant $D = b^2 - 4ac < 0$:
$$\boxed{x = \frac{-b \pm i\sqrt{|D|}}{2a}}$$

Roots are always a conjugate pair.

## Important Identities

$$\text{Re}(z) = \frac{z + \bar{z}}{2} \qquad \text{Im}(z) = \frac{z - \bar{z}}{2i} \qquad \frac{1}{z} = \frac{\bar{z}}{|z|^2}$$

## See also

- [[algebraic identities]]
- [[binomials]]
- [[derivatives]]
