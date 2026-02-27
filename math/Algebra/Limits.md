# Limits

**Limits** are the foundation of calculus, describing the behavior of functions as their inputs approach specific values. They enable us to analyze continuity, derivatives, and integrals.

---

## Definition

A **limit** describes the value that a function approaches as the input approaches some value.

$$\boxed{\lim_{x \to a} f(x) = L}$$

**Read as:** "The limit of $f(x)$ as $x$ approaches $a$ is $L$"

**Meaning:** As $x$ gets arbitrarily close to $a$ (but not necessarily equal to $a$), $f(x)$ gets arbitrarily close to $L$.

**Examples:**
- $\lim_{x \to 2} (3x + 1) = 7$
- $\lim_{x \to 0} \frac{\sin x}{x} = 1$
- $\lim_{x \to \infty} \frac{1}{x} = 0$

---

## Basic Limit Laws

### 1. Sum/Difference Law
$$\boxed{\lim_{x \to a} [f(x) \pm g(x)] = \lim_{x \to a} f(x) \pm \lim_{x \to a} g(x)}$$

**Example:**
$$\lim_{x \to 2} (x^2 + 3x) = \lim_{x \to 2} x^2 + \lim_{x \to 2} 3x = 4 + 6 = 10$$

---

### 2. Product Law
$$\boxed{\lim_{x \to a} [f(x) \cdot g(x)] = \lim_{x \to a} f(x) \cdot \lim_{x \to a} g(x)}$$

**Example:**
$$\lim_{x \to 3} (x \cdot x^2) = \lim_{x \to 3} x \cdot \lim_{x \to 3} x^2 = 3 \cdot 9 = 27$$

---

### 3. Quotient Law
$$\boxed{\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{\lim_{x \to a} f(x)}{\lim_{x \to a} g(x)}, \quad \text{if } \lim_{x \to a} g(x) \neq 0}$$

**Example:**
$$\lim_{x \to 2} \frac{x^2 + 1}{x - 1} = \frac{4 + 1}{2 - 1} = 5$$

---

### 4. Constant Multiple Law
$$\boxed{\lim_{x \to a} [c \cdot f(x)] = c \cdot \lim_{x \to a} f(x)}$$

**Example:**
$$\lim_{x \to 1} (5x^2) = 5 \cdot \lim_{x \to 1} x^2 = 5 \cdot 1 = 5$$

---

### 5. Power Law
$$\boxed{\lim_{x \to a} [f(x)]^n = \left[\lim_{x \to a} f(x)\right]^n}$$

**Example:**
$$\lim_{x \to 2} (x + 1)^3 = (2 + 1)^3 = 27$$

---

### 6. Root Law
$$\boxed{\lim_{x \to a} \sqrt[n]{f(x)} = \sqrt[n]{\lim_{x \to a} f(x)}}$$
(provided the limit and root exist)

---

## Common Basic Limits

### Constant Function
$$\boxed{\lim_{x \to a} c = c}$$

**Example:** $\lim_{x \to 5} 7 = 7$

---

### Identity Function
$$\boxed{\lim_{x \to a} x = a}$$

**Example:** $\lim_{x \to 3} x = 3$

---

### Polynomial Function
For any polynomial $p(x)$:
$$\boxed{\lim_{x \to a} p(x) = p(a)}$$

**Example:** $\lim_{x \to 2} (x^3 - 3x + 1) = 8 - 6 + 1 = 3$

---

## Indeterminate Forms

Common forms that require special techniques:
- $\frac{0}{0}$ (most common)
- $\frac{\infty}{\infty}$
- $0 \cdot \infty$
- $\infty - \infty$
- $0^0$, $1^\infty$, $\infty^0$

**These forms are "indeterminate" because they don't have a clear value without further analysis.**

---

## Techniques for Evaluating Limits

### 1. Direct Substitution
Simply substitute the value into the function.

**Example:**
$$\lim_{x \to 3} (x^2 + 2x - 1) = 9 + 6 - 1 = 14$$

---

### 2. Factoring
Factor and cancel common terms to eliminate indeterminate forms.

**Example:**
$$\lim_{x \to 3} \frac{x^2 - 9}{x - 3} = \lim_{x \to 3} \frac{(x-3)(x+3)}{x-3} = \lim_{x \to 3} (x+3) = 6$$

---

### 3. Rationalization
Multiply by the conjugate to eliminate radicals.

**Example:**
$$
\begin{align*}
\lim_{x \to 0} \frac{\sqrt{x+1} - 1}{x} &= \lim_{x \to 0} \frac{(\sqrt{x+1} - 1)(\sqrt{x+1} + 1)}{x(\sqrt{x+1} + 1)} \\
&= \lim_{x \to 0} \frac{x+1-1}{x(\sqrt{x+1} + 1)} \\
&= \lim_{x \to 0} \frac{x}{x(\sqrt{x+1} + 1)} \\
&= \lim_{x \to 0} \frac{1}{\sqrt{x+1} + 1} = \frac{1}{2}
\end{align*}
$$

---

### 4. L'Hôpital's Rule
For indeterminate forms $\frac{0}{0}$ or $\frac{\infty}{\infty}$:
$$\boxed{\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}}$$

**Example:**
$$\lim_{x \to 0} \frac{\sin x}{x} = \lim_{x \to 0} \frac{\cos x}{1} = 1$$

**Note:** Can be applied repeatedly if needed.

---

## One-Sided Limits

### Left-Hand Limit
Approaching from the **left** (values less than $a$):
$$\boxed{\lim_{x \to a^-} f(x)}$$

**Notation:** $a^-$ means approaching from below

---

### Right-Hand Limit
Approaching from the **right** (values greater than $a$):
$$\boxed{\lim_{x \to a^+} f(x)}$$

**Notation:** $a^+$ means approaching from above

---

### Limit Exists If and Only If
$$\boxed{\lim_{x \to a} f(x) = L \quad \Leftrightarrow \quad \lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x) = L}$$

**Example:** Piecewise function
$$f(x) = \begin{cases} x + 1 & \text{if } x < 2 \\ 5 & \text{if } x = 2 \\ x^2 & \text{if } x > 2 \end{cases}$$

- $\lim_{x \to 2^-} f(x) = 3$
- $\lim_{x \to 2^+} f(x) = 4$
- $\lim_{x \to 2} f(x)$ **does not exist** (left ≠ right)

---

## Limits at Infinity

Describes behavior as $x$ grows without bound.

$$\boxed{\lim_{x \to \infty} f(x), \quad \lim_{x \to -\infty} f(x)}$$

**Common limits at infinity:**
- $\lim_{x \to \infty} \frac{1}{x} = 0$
- $\lim_{x \to \infty} \frac{1}{x^n} = 0$ (for $n > 0$)
- $\lim_{x \to \infty} e^x = \infty$
- $\lim_{x \to -\infty} e^x = 0$
- $\lim_{x \to \infty} \frac{P(x)}{Q(x)}$ depends on degrees of $P$ and $Q$

**For rational functions:**
$$\lim_{x \to \infty} \frac{a_nx^n + \cdots}{b_mx^m + \cdots} = \begin{cases}
0 & \text{if } n < m \\
\frac{a_n}{b_m} & \text{if } n = m \\
\pm\infty & \text{if } n > m
\end{cases}$$

**Examples:**
1. $\lim_{x \to \infty} \frac{3x^2 + 5}{x^2 - 1} = \frac{3}{1} = 3$ (same degree)
2. $\lim_{x \to \infty} \frac{x + 1}{x^2} = 0$ (numerator degree < denominator)
3. $\lim_{x \to \infty} \frac{x^3}{x^2 + 1} = \infty$ (numerator degree > denominator)

---

## Special Trigonometric Limits

$$\boxed{\lim_{x \to 0} \frac{\sin x}{x} = 1}$$

**Derivation:** Uses squeeze theorem

$$\boxed{\lim_{x \to 0} \frac{1 - \cos x}{x} = 0}$$

$$\boxed{\lim_{x \to 0} \frac{\tan x}{x} = 1}$$

**Examples using these:**
- $\lim_{x \to 0} \frac{\sin 3x}{x} = \lim_{x \to 0} 3 \cdot \frac{\sin 3x}{3x} = 3 \cdot 1 = 3$
- $\lim_{x \to 0} \frac{\sin 5x}{\sin 2x} = \lim_{x \to 0} \frac{5x}{2x} = \frac{5}{2}$

---

## Special Exponential Limit

$$\boxed{\lim_{x \to 0} \frac{e^x - 1}{x} = 1}$$

$$\boxed{\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e}$$

**Generalization:**
$$\boxed{\lim_{x \to 0} (1 + x)^{1/x} = e}$$

---

## Infinite Limits

When a function grows without bound:

$$\boxed{\lim_{x \to a} f(x) = \infty}$$

**Means:** $f(x)$ increases without bound as $x \to a$

**Example:**
$$\lim_{x \to 0^+} \frac{1}{x} = \infty$$
$$\lim_{x \to 0^-} \frac{1}{x} = -\infty$$

<img src="Pictures/vertical_asymptote.jpg" width=500 height="auto" style="display: block; margin: auto">

---

## Continuity

A function $f(x)$ is **continuous** at $x = a$ if:
$$\boxed{\lim_{x \to a} f(x) = f(a)}$$

**Three conditions for continuity:**
1. $f(a)$ is defined
2. $\lim_{x \to a} f(x)$ exists
3. The limit equals the function value

**Types of discontinuity:**
- **Removable:** Limit exists but $\neq f(a)$ (or $f(a)$ undefined)
- **Jump:** Left and right limits exist but differ
- **Infinite:** Function has vertical asymptote

<img src="Pictures/discontinuity.png" width=500 height="auto" style="display: block; margin: auto">

---

## Squeeze (Sandwich) Theorem

If $g(x) \leq f(x) \leq h(x)$ for all $x$ near $a$, and:
$$\lim_{x \to a} g(x) = \lim_{x \to a} h(x) = L$$

Then:
$$\boxed{\lim_{x \to a} f(x) = L}$$

**Example:** Prove $\lim_{x \to 0} x^2 \sin\frac{1}{x} = 0$
- $-1 \leq \sin\frac{1}{x} \leq 1$
- $-x^2 \leq x^2\sin\frac{1}{x} \leq x^2$
- $\lim_{x \to 0} (-x^2) = \lim_{x \to 0} x^2 = 0$
- Therefore: $\lim_{x \to 0} x^2\sin\frac{1}{x} = 0$

---

## Intermediate Value Theorem

If $f$ is continuous on $[a,b]$ and $N$ is between $f(a)$ and $f(b)$, then there exists $c \in (a,b)$ such that $f(c) = N$.

**Application:** Proving roots exist

**Example:** Show $x^3 - x - 1 = 0$ has a solution in $[1,2]$
- $f(1) = -1 < 0$
- $f(2) = 5 > 0$
- By IVT, $\exists c \in (1,2)$ where $f(c) = 0$ ✓

---

## Applications of Limits

### 1. Defining the Derivative
$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

### 2. Defining the Integral
$$\int_a^b f(x)dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*)\Delta x$$

### 3. Finding Asymptotes
- Vertical asymptotes: where limits are $\pm\infty$
- Horizontal asymptotes: limits at $\pm\infty$

### 4. Analyzing Function Behavior
- End behavior
- Continuity
- Points of discontinuity

---

## Common Mistakes

1. **Assuming $\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{\lim_{x \to a} f(x)}{\lim_{x \to a} g(x)}$ always** ✗
   - Only valid when denominator limit $\neq 0$ ✓

2. **$\lim_{x \to a} f(x) = f(a)$ always** ✗
   - Only if function is continuous at $a$ ✓

3. **Confusing $\lim_{x \to 0^+}$ with $\lim_{x \to 0}$** ✗
   - One-sided vs two-sided limits are different ✓

4. **$\lim_{x \to \infty} \sin x = ?$** ✗
   - This limit does not exist (oscillates) ✓

---

## Quick Reference Table

| Limit | Value |
|-------|-------|
| $\lim_{x \to 0} \frac{\sin x}{x}$ | $1$ |
| $\lim_{x \to 0} \frac{e^x - 1}{x}$ | $1$ |
| $\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x$ | $e$ |
| $\lim_{x \to 0} (1 + x)^{1/x}$ | $e$ |
| $\lim_{x \to \infty} \frac{1}{x}$ | $0$ |
| $\lim_{x \to a} c$ | $c$ |
| $\lim_{x \to a} x$ | $a$ |

---

## See Also
- [[Derivatives]] - Built on the concept of limits
- [[Integrals]] - Defined using limits
- [[00 - Algebra MOC]] - Algebra topics overview
