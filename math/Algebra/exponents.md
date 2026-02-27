---
tags: [math, algebra, exponents, powers]
status: complete
---

# Exponents and Powers

> Repeated multiplication expressed compactly — the foundation of exponential and logarithmic functions.

## Definition

An **exponent** (or **power**) indicates how many times a base is multiplied by itself.

$$\boxed{a^n = \underbrace{a \cdot a \cdot a \cdot \ldots \cdot a}_{n \text{ times}}}$$

Where:
- $a$ is the **base**
- $n$ is the **exponent**
- $a^n$ is read as "$a$ to the power of $n$"

## Special Cases

### Zero exponent
$$\boxed{a^0 = 1 \quad \text{for any } a \neq 0}$$

### First power
$$\boxed{a^1 = a}$$

### Negative exponents
$$\boxed{a^{-n} = \frac{1}{a^n} \quad \text{for } a \neq 0}$$

### Fractional exponents
$$\boxed{a^{\frac{m}{n}} = \sqrt[n]{a^m} = (\sqrt[n]{a})^m}$$

Examples: $8^{1/3} = 2$, $16^{1/2} = 4$, $27^{2/3} = 9$

## Laws of Exponents

| Rule | Formula | Example |
|------|---------|---------|
| Product | $a^m \cdot a^n = a^{m+n}$ | $2^3 \cdot 2^2 = 2^5$ |
| Quotient | $\dfrac{a^m}{a^n} = a^{m-n}$ | $\dfrac{3^5}{3^2} = 3^3$ |
| Power | $(a^m)^n = a^{mn}$ | $(4^2)^3 = 4^6$ |
| Product power | $(ab)^n = a^n b^n$ | $(2x)^3 = 8x^3$ |
| Quotient power | $\left(\dfrac{a}{b}\right)^n = \dfrac{a^n}{b^n}$ | $\left(\dfrac{x}{2}\right)^2 = \dfrac{x^2}{4}$ |
| Negative quotient | $\left(\dfrac{a}{b}\right)^{-n} = \left(\dfrac{b}{a}\right)^n$ | $\left(\dfrac{2}{3}\right)^{-2} = \dfrac{9}{4}$ |

## Common Patterns

Powers of 2: $2^1=2,\ 2^2=4,\ 2^3=8,\ 2^4=16,\ 2^8=256,\ 2^{10}=1024$

Powers of 10: $10^{-3}=0.001\ \text{(milli)},\ 10^3=1000\ \text{(kilo)},\ 10^6=1{,}000{,}000\ \text{(mega)}$

## Scientific Notation

$$\boxed{a \times 10^n}, \quad 1 \leq |a| < 10,\ n \in \mathbb{Z}$$

Examples: $3{,}000{,}000 = 3 \times 10^6$, $0.00045 = 4.5 \times 10^{-4}$

## Worked Examples

**Simplify** $\dfrac{(2x^3y^{-2})^4 \cdot x^{-5}}{(xy)^3}$:

$$
\frac{16 \cdot x^{12} \cdot y^{-8} \cdot x^{-5}}{x^3 \cdot y^3}
= \frac{16 x^7 y^{-8}}{x^3 y^3}
= \frac{16x^4}{y^{11}}
$$

**Solve** $2^{x+1} = 32$:

$$2^{x+1} = 2^5 \implies x + 1 = 5 \implies x = 4$$

## Common Mistakes

- $(a + b)^2 \neq a^2 + b^2$ — correct form is $a^2 + 2ab + b^2$
- $a^m + a^n \neq a^{m+n}$ — product rule only applies to multiplication
- $\frac{1}{a^{-n}} = a^n$, not $a^{-n}$

## See also

- [[logarithms]] — inverse operation of exponentiation
- [[geometric progression]] — sequences based on exponential growth
