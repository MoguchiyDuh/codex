---
tags: [math, algebra, calculus, limits]
status: complete
---

# Limits

> The value a function approaches as its input gets arbitrarily close to some point — the foundation of calculus.

## Definition

$$\boxed{\lim_{x \to a} f(x) = L}$$

As $x$ gets arbitrarily close to $a$ (but not necessarily equal), $f(x)$ gets arbitrarily close to $L$.

Examples: $\lim_{x\to 2}(3x+1)=7$, $\lim_{x\to 0}\frac{\sin x}{x}=1$, $\lim_{x\to\infty}\frac{1}{x}=0$

## Limit Laws

| Law | Formula |
|-----|---------|
| Sum / difference | $\lim[f \pm g] = \lim f \pm \lim g$ |
| Product | $\lim[f \cdot g] = \lim f \cdot \lim g$ |
| Quotient | $\lim\frac{f}{g} = \frac{\lim f}{\lim g}$ (if $\lim g \neq 0$) |
| Constant multiple | $\lim[c\cdot f] = c\cdot\lim f$ |
| Power | $\lim[f]^n = [\lim f]^n$ |
| Root | $\lim\sqrt[n]{f} = \sqrt[n]{\lim f}$ |

For any polynomial $p(x)$: $\lim_{x\to a} p(x) = p(a)$

## Indeterminate Forms

Forms that require further analysis before evaluating:

$\frac{0}{0}$, $\frac{\infty}{\infty}$, $0\cdot\infty$, $\infty-\infty$, $0^0$, $1^\infty$, $\infty^0$

## Evaluation Techniques

### Direct substitution
Plug in the value directly. Works whenever $f$ is continuous at $a$.

### Factoring
Cancel common factors to resolve $\frac{0}{0}$:
$$\lim_{x\to 3}\frac{x^2-9}{x-3} = \lim_{x\to 3}(x+3) = 6$$

### Rationalization
Multiply by conjugate to eliminate radicals:
$$\lim_{x\to 0}\frac{\sqrt{x+1}-1}{x} = \lim_{x\to 0}\frac{1}{\sqrt{x+1}+1} = \frac{1}{2}$$

### L'Hopital's Rule
For $\frac{0}{0}$ or $\frac{\infty}{\infty}$:
$$\boxed{\lim_{x\to a}\frac{f(x)}{g(x)} = \lim_{x\to a}\frac{f'(x)}{g'(x)}}$$

Example: $\lim_{x\to 0}\frac{\sin x}{x} = \lim_{x\to 0}\frac{\cos x}{1} = 1$

## One-Sided Limits

Left-hand limit ($x$ approaches from below): $\lim_{x\to a^-} f(x)$

Right-hand limit ($x$ approaches from above): $\lim_{x\to a^+} f(x)$

Two-sided limit exists iff both one-sided limits exist and are equal:
$$\lim_{x\to a}f(x) = L \iff \lim_{x\to a^-}f(x) = \lim_{x\to a^+}f(x) = L$$

## Limits at Infinity

For rational functions $\frac{a_n x^n + \cdots}{b_m x^m + \cdots}$:

| Degrees | Result |
|---------|--------|
| $n < m$ | $0$ |
| $n = m$ | $a_n / b_m$ |
| $n > m$ | $\pm\infty$ |

## Special Limits

$$\lim_{x\to 0}\frac{\sin x}{x} = 1 \qquad \lim_{x\to 0}\frac{1-\cos x}{x} = 0 \qquad \lim_{x\to 0}\frac{\tan x}{x} = 1$$

$$\lim_{x\to 0}\frac{e^x-1}{x} = 1 \qquad \lim_{x\to\infty}\left(1+\frac{1}{x}\right)^x = e \qquad \lim_{x\to 0}(1+x)^{1/x} = e$$

![[vertical_asymptote.jpg]]

## Infinite Limits and Asymptotes

$\lim_{x\to a}f(x) = \infty$ indicates a **vertical asymptote** at $x = a$.

$\lim_{x\to\pm\infty}f(x) = L$ indicates a **horizontal asymptote** at $y = L$.

![[discontinuity.png]]

## Continuity

$f$ is continuous at $x = a$ iff:
$$\boxed{\lim_{x\to a}f(x) = f(a)}$$

Three conditions: $f(a)$ defined, limit exists, limit equals $f(a)$.

**Discontinuity types:** removable (limit exists, $\neq f(a)$), jump (one-sided limits differ), infinite (vertical asymptote).

## Squeeze Theorem

If $g(x) \leq f(x) \leq h(x)$ near $a$ and $\lim g = \lim h = L$, then $\lim f = L$.

Example: $\lim_{x\to 0} x^2\sin\frac{1}{x} = 0$ (squeezed between $-x^2$ and $x^2$)

## Intermediate Value Theorem

If $f$ is continuous on $[a,b]$ and $N$ is between $f(a)$ and $f(b)$, then $\exists\, c\in(a,b)$ with $f(c)=N$.

Used to prove roots exist without finding them explicitly.

## Applications

- **Derivative definition:** $f'(x) = \lim_{h\to 0}\frac{f(x+h)-f(x)}{h}$
- **Riemann integral:** $\int_a^b f\,dx = \lim_{n\to\infty}\sum f(x_i^*)\Delta x$
- **Asymptote analysis:** vertical where limit is $\pm\infty$, horizontal from limits at $\pm\infty$

## Common Mistakes

- Quotient law only valid when denominator limit $\neq 0$
- $\lim_{x\to a}f(x) = f(a)$ only when $f$ is continuous at $a$
- $\lim_{x\to\infty}\sin x$ does not exist (oscillates)

## See also

- [[integrals]] — defined using limits of Riemann sums
