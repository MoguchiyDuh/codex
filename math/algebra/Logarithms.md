---
tags: [math, algebra, logarithms]
status: complete
---

# Logarithms

> The inverse of exponentiation — answers "to what power must we raise the base to get this number?"

## Definition

$$\boxed{\log_a x = y \iff a^y = x}$$

Where $a > 0$, $a \neq 1$ (base) and $x > 0$ (argument).

Examples: $\log_2 8 = 3$ (since $2^3=8$), $\log_{10} 100 = 2$, $\log_3 \frac{1}{9} = -2$

## Common Types

| Name | Notation | Base | Primary use |
|------|----------|------|-------------|
| Common log | $\log x$ | $10$ | Engineering, pH, decibels |
| Natural log | $\ln x$ | $e \approx 2.718$ | Calculus, continuous growth |
| Binary log | $\lg x$ or $\log_2 x$ | $2$ | CS, algorithm complexity |

## Fundamental Identities

$$\log_a 1 = 0 \qquad \log_a a = 1 \qquad \log_a a^n = n \qquad a^{\log_a x} = x$$

## Laws of Logarithms

| Law | Formula |
|-----|---------|
| Product | $\log_a(mn) = \log_a m + \log_a n$ |
| Quotient | $\log_a\!\left(\frac{m}{n}\right) = \log_a m - \log_a n$ |
| Power | $\log_a m^n = n\log_a m$ |
| Root | $\log_a \sqrt[n]{x} = \frac{1}{n}\log_a x$ |
| Reciprocal | $\log_a \frac{1}{x} = -\log_a x$ |
| Change of base | $\log_a b = \dfrac{\ln b}{\ln a} = \dfrac{\log b}{\log a}$ |
| Power of base | $\log_{a^n} m = \frac{1}{n}\log_a m$ |

## Solving Logarithmic Equations

**Single log:** $\log_a x = b \implies x = a^b$

**Equal logs (same base):** $\log_a f(x) = \log_a g(x) \implies f(x) = g(x)$

**Sum/difference:** combine with product/quotient law first.

Example: $\log_3 x + \log_3(x-2) = 1$
→ $\log_3[x(x-2)] = 1$ → $x(x-2) = 3$ → $x^2-2x-3=0$ → $x=3$ (reject $x=-1$, argument must be positive)

## Graph of $y = \log_a x$

- Domain: $(0, \infty)$, Range: $(-\infty, \infty)$
- Vertical asymptote at $x = 0$
- Passes through $(1, 0)$ and $(a, 1)$
- Increasing if $a > 1$, decreasing if $0 < a < 1$

## Special Values

| Expression | Value |
|------------|-------|
| $\log 1$ | $0$ |
| $\log 10$ | $1$ |
| $\log 100$ | $2$ |
| $\ln 1$ | $0$ |
| $\ln e$ | $1$ |
| $\log_2 8$ | $3$ |
| $\log_2 1024$ | $10$ |

## Applications

- **pH:** $\text{pH} = -\log[\text{H}^+]$ — neutral water at pH 7
- **Richter scale:** $M = \log(I/I_0)$ — each unit = 10× intensity
- **Decibels:** $\beta = 10\log(I/I_0)$
- **Doubling time:** $t = \frac{\ln 2}{r}$ (continuous growth rate $r$)
- **Half-life:** $t_{1/2} = \frac{\ln 2}{\lambda}$

## Common Mistakes

- $\log(a+b) \neq \log a + \log b$ — product rule needs multiplication
- $\frac{\log a}{\log b} \neq \log\frac{a}{b}$ — this is change of base, not quotient rule
- $\log(-x)$ is undefined — argument must be positive

## See also

- [[exponents]] — inverse operation; $\log_a x = y \iff a^y = x$
- [[geometric progression]] — logarithms solve for position $n$ in a GP
