# Complex Numbers

Complex numbers extend the real number system by introducing the imaginary unit, enabling solutions to equations that have no real solutions (like $x^2 + 1 = 0$).

---

## Definition

A **complex number** is a number of the form:
$$\boxed{z = a + bi}$$

Where:
- $a$ is the **real part**: $\text{Re}(z) = a$
- $b$ is the **imaginary part**: $\text{Im}(z) = b$
- $i$ is the **imaginary unit**: $i^2 = -1$
- $a, b \in \mathbb{R}$ (real numbers)

**Examples:**
- $3 + 4i$ (real part = 3, imaginary part = 4)
- $-2 + 5i$ (real part = -2, imaginary part = 5)
- $7i$ (real part = 0, imaginary part = 7) — **purely imaginary**
- $5$ (real part = 5, imaginary part = 0) — **real number**
- $0$ (real part = 0, imaginary part = 0) — **zero**

---

## Imaginary Unit

The imaginary unit $i$ is defined by:
$$\boxed{i = \sqrt{-1}, \quad i^2 = -1}$$

**Powers of $i$ (cyclical pattern with period 4):**
- $i^0 = 1$
- $i^1 = i$
- $i^2 = -1$
- $i^3 = -i$
- $i^4 = 1$ (pattern repeats)

**General formula:**
$$\boxed{i^n = i^{n \bmod 4}}$$

**Examples:**
- $i^5 = i^{5 \bmod 4} = i^1 = i$
- $i^{10} = i^{10 \bmod 4} = i^2 = -1$
- $i^{100} = i^{100 \bmod 4} = i^0 = 1$
- $i^{-1} = \frac{1}{i} = \frac{i}{i^2} = \frac{i}{-1} = -i$

---

## Complex Plane (Argand Diagram)

Complex numbers can be represented geometrically on the **complex plane**:
- **Horizontal axis (real axis)**: represents $\text{Re}(z)$
- **Vertical axis (imaginary axis)**: represents $\text{Im}(z)$
- Point $(a, b)$ represents $z = a + bi$

**Example:** $z = 3 + 2i$ is plotted at coordinates $(3, 2)$

<img src="Pictures/complex_plain.jpg" width=500 height="auto" style="display: block; margin: auto">

---

## Operations on Complex Numbers

### 1. Addition
Add corresponding real and imaginary parts:
$$\boxed{(a + bi) + (c + di) = (a + c) + (b + d)i}$$

**Example:**
$$(3 + 4i) + (1 - 2i) = (3+1) + (4-2)i = 4 + 2i$$

**Geometric interpretation:** Vector addition in the complex plane

---

### 2. Subtraction
Subtract corresponding parts:
$$\boxed{(a + bi) - (c + di) = (a - c) + (b - d)i}$$

**Example:**
$$(5 + 3i) - (2 + 7i) = (5-2) + (3-7)i = 3 - 4i$$

---

### 3. Multiplication
Use the distributive property and $i^2 = -1$:
$$\boxed{(a + bi)(c + di) = (ac - bd) + (ad + bc)i}$$

**Derivation:**
$$
\begin{align*}
(a + bi)(c + di) &= ac + adi + bci + bdi^2 \\
&= ac + adi + bci - bd \\
&= (ac - bd) + (ad + bc)i
\end{align*}
$$

**Examples:**
1. $(2 + 3i)(1 + 4i) = (2 - 12) + (8 + 3)i = -10 + 11i$
2. $(3 + 2i)(3 - 2i) = 9 - 6i + 6i - 4i^2 = 9 + 4 = 13$
3. $i \cdot i = i^2 = -1$

---

### 4. Division
Multiply numerator and denominator by the **conjugate** of the denominator:
$$\boxed{\frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{(c + di)(c - di)} = \frac{(ac + bd) + (bc - ad)i}{c^2 + d^2}}$$

**Steps:**
1. Multiply by conjugate: $\frac{c - di}{c - di}$
2. Simplify numerator using multiplication
3. Simplify denominator using $z \cdot \bar{z} = |z|^2$

**Example:**
$$
\begin{align*}
\frac{3 + 2i}{1 - i} &= \frac{(3 + 2i)(1 + i)}{(1 - i)(1 + i)} \\
&= \frac{3 + 3i + 2i + 2i^2}{1 - i^2} \\
&= \frac{3 + 5i - 2}{1 + 1} \\
&= \frac{1 + 5i}{2} \\
&= \frac{1}{2} + \frac{5}{2}i
\end{align*}
$$

---

## Complex Conjugate

The **complex conjugate** of $z = a + bi$ is:
$$\boxed{\bar{z} = a - bi}$$

**Geometric interpretation:** Reflection across the real axis

**Properties:**
1. $\overline{z_1 + z_2} = \bar{z_1} + \bar{z_2}$
2. $\overline{z_1 \cdot z_2} = \bar{z_1} \cdot \bar{z_2}$
3. $\overline{\left(\frac{z_1}{z_2}\right)} = \frac{\bar{z_1}}{\bar{z_2}}$
4. $\overline{(\bar{z})} = z$ (double conjugate)
5. $z + \bar{z} = 2\text{Re}(z)$ (always real)
6. $z - \bar{z} = 2i\text{Im}(z)$ (purely imaginary)
7. $z \cdot \bar{z} = a^2 + b^2 \geq 0$ (always real and non-negative)

**Examples:**
- $\overline{3 + 4i} = 3 - 4i$
- $\overline{-2 - 5i} = -2 + 5i$
- $\overline{6} = 6$ (real numbers are self-conjugate)

---

## Modulus (Absolute Value)

The **modulus** (or **absolute value**) of $z = a + bi$ is its distance from the origin:
$$\boxed{|z| = \sqrt{a^2 + b^2} = \sqrt{z \cdot \bar{z}}}$$

**Properties:**
1. $|z| \geq 0$, and $|z| = 0 \Leftrightarrow z = 0$
2. $|z_1 \cdot z_2| = |z_1| \cdot |z_2|$
3. $\left|\frac{z_1}{z_2}\right| = \frac{|z_1|}{|z_2|}$ (for $z_2 \neq 0$)
4. $|z_1 + z_2| \leq |z_1| + |z_2|$ (triangle inequality)
5. $|\bar{z}| = |z|$
6. $|z^n| = |z|^n$

**Examples:**
- $|3 + 4i| = \sqrt{9 + 16} = \sqrt{25} = 5$
- $|-2 + 2i| = \sqrt{4 + 4} = \sqrt{8} = 2\sqrt{2}$
- $|5| = 5$
- $|6i| = 6$

---

## Polar Form

A complex number can be represented in **polar form**:
$$\boxed{z = r(\cos\theta + i\sin\theta) = r\text{cis}(\theta)}$$

Where:
- $r = |z| = \sqrt{a^2 + b^2}$ is the **modulus**
- $\theta = \arg(z) = \tan^{-1}\left(\frac{b}{a}\right)$ is the **argument** (angle)

**Conversion from rectangular to polar:**
1. $r = \sqrt{a^2 + b^2}$
2. $\theta = \begin{cases}
\tan^{-1}\left(\frac{b}{a}\right) & \text{if } a > 0 \\
\tan^{-1}\left(\frac{b}{a}\right) + \pi & \text{if } a < 0, b \geq 0 \\
\tan^{-1}\left(\frac{b}{a}\right) - \pi & \text{if } a < 0, b < 0 \\
\frac{\pi}{2} & \text{if } a = 0, b > 0 \\
-\frac{\pi}{2} & \text{if } a = 0, b < 0
\end{cases}$

**Example:** Convert $z = 1 + i$ to polar form
- $r = \sqrt{1^2 + 1^2} = \sqrt{2}$
- $\theta = \tan^{-1}(1) = \frac{\pi}{4}$
- $z = \sqrt{2}\left(\cos\frac{\pi}{4} + i\sin\frac{\pi}{4}\right)$

<img src="Pictures/polar_representation.png" width=500 height="auto" style="display: block; margin: auto">

---

## Euler's Formula

$$\boxed{e^{i\theta} = \cos\theta + i\sin\theta}$$

This leads to the **exponential form** of complex numbers:
$$\boxed{z = re^{i\theta}}$$

**Special cases:**
- $e^{i\pi} = -1$ (Euler's identity: $e^{i\pi} + 1 = 0$)
- $e^{i\pi/2} = i$
- $e^{-i\pi/2} = -i$

**Properties:**
- $e^{i\theta_1} \cdot e^{i\theta_2} = e^{i(\theta_1 + \theta_2)}$
- $\frac{e^{i\theta_1}}{e^{i\theta_2}} = e^{i(\theta_1 - \theta_2)}$
- $(e^{i\theta})^n = e^{in\theta}$

---

## De Moivre's Theorem

For any integer $n$:
$$\boxed{(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)}$$

**In exponential form:**
$$\boxed{(re^{i\theta})^n = r^n e^{in\theta}}$$

**Applications:**
- Finding powers of complex numbers
- Finding $n$-th roots of complex numbers
- Deriving trigonometric identities

**Example:** $(1 + i)^{10}$
1. Convert to polar: $1 + i = \sqrt{2}e^{i\pi/4}$
2. Apply De Moivre: $(1 + i)^{10} = (\sqrt{2})^{10}e^{i \cdot 10\pi/4} = 32e^{i5\pi/2}$
3. Simplify: $e^{i5\pi/2} = e^{i\pi/2} = i$
4. Result: $32i$

---

## Roots of Complex Numbers

The $n$-th roots of a complex number $z = re^{i\theta}$ are:
$$\boxed{z_k = \sqrt[n]{r} \cdot e^{i(\theta + 2\pi k)/n}, \quad k = 0, 1, 2, \ldots, n-1}$$

**Properties:**
- There are exactly $n$ distinct $n$-th roots
- They are evenly spaced around a circle of radius $\sqrt[n]{r}$
- Angles between consecutive roots: $\frac{2\pi}{n}$

**Example:** Find all cube roots of $8$
- $8 = 8e^{i \cdot 0}$
- $z_0 = 2e^{i \cdot 0} = 2$
- $z_1 = 2e^{i \cdot 2\pi/3} = 2\left(-\frac{1}{2} + i\frac{\sqrt{3}}{2}\right) = -1 + i\sqrt{3}$
- $z_2 = 2e^{i \cdot 4\pi/3} = 2\left(-\frac{1}{2} - i\frac{\sqrt{3}}{2}\right) = -1 - i\sqrt{3}$

---

## Solving Quadratic Equations with Complex Roots

For $ax^2 + bx + c = 0$ with $D = b^2 - 4ac < 0$:
$$\boxed{x = \frac{-b \pm i\sqrt{|D|}}{2a} = \frac{-b \pm i\sqrt{4ac - b^2}}{2a}}$$

**Example:** Solve $x^2 + 2x + 5 = 0$
- $D = 4 - 20 = -16 < 0$
- $x = \frac{-2 \pm \sqrt{-16}}{2} = \frac{-2 \pm 4i}{2} = -1 \pm 2i$

**Roots:** $x_1 = -1 + 2i$, $x_2 = -1 - 2i$ (complex conjugates)

---

## Applications

### 1. Electrical Engineering
**Impedance** in AC circuits:
$$Z = R + iX$$
where $R$ = resistance, $X$ = reactance

---

### 2. Signal Processing
**Fourier Transform** uses complex exponentials:
$$F(\omega) = \int_{-\infty}^{\infty} f(t)e^{-i\omega t}dt$$

---

### 3. Quantum Mechanics
Wave functions are complex-valued:
$$\psi(x,t) = Ae^{i(kx - \omega t)}$$

---

### 4. Fractals
**Mandelbrot set** defined using complex number iteration:
$$z_{n+1} = z_n^2 + c$$

---

### 5. Control Theory
Analysis of system stability using complex poles and zeros.

---

## Important Identities

$$\boxed{\text{Re}(z) = \frac{z + \bar{z}}{2}}$$

$$\boxed{\text{Im}(z) = \frac{z - \bar{z}}{2i}}$$

$$\boxed{|z|^2 = z \cdot \bar{z} = a^2 + b^2}$$

$$\boxed{\frac{1}{z} = \frac{\bar{z}}{|z|^2}}$$

---

## Common Mistakes

1. **$i^2 = 1$** ✗
   - Correct: $i^2 = -1$ ✓

2. **$\sqrt{-4} = 2i$ or $-2i$?**
   - By convention: $\sqrt{-4} = 2i$ (principal root) ✓

3. **$(a + bi)^2 = a^2 + b^2$** ✗
   - Correct: $(a + bi)^2 = a^2 - b^2 + 2abi$ ✓

4. **$|z_1 + z_2| = |z_1| + |z_2|$** ✗
   - Correct: $|z_1 + z_2| \leq |z_1| + |z_2|$ (triangle inequality) ✓

---

## See Also
- [[Quadratic Function]] - Quadratic equations with complex roots
- [[Polynomials]] - Complex roots of polynomials
- [[00 - Algebra MOC]] - Algebra topics overview
