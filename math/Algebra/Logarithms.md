# Logarithms

Logarithms are the inverse operation of exponentiation. They answer the fundamental question: "To what power must we raise a base to obtain a given number?"

---

## Definition

A **logarithm** is the exponent to which a base must be raised to produce a given number.

$$\boxed{\log_a{x} = y \quad \Leftrightarrow \quad a^y = x}$$

Where:
- $a$ is the **base** ($a > 0, a \neq 1$)
- $x$ is the **argument** ($x > 0$)
- $y$ is the **logarithm** (the result)

**Read as:** "log base $a$ of $x$ equals $y$"

**Examples:**
- $\log_2{8} = 3$ because $2^3 = 8$
- $\log_{10}{100} = 2$ because $10^2 = 100$
- $\log_5{125} = 3$ because $5^3 = 125$
- $\log_3{\frac{1}{9}} = -2$ because $3^{-2} = \frac{1}{9}$

---

## Common Types of Logarithms

### 1. Common Logarithm (Base 10)
$$\boxed{\log_{10}{x} = \log{x}}$$

**Uses:** Engineering, pH scale, decibels, Richter scale

**Examples:**
- $\log{1000} = 3$ because $10^3 = 1000$
- $\log{0.01} = -2$ because $10^{-2} = 0.01$

---

### 2. Natural Logarithm (Base e)
$$\boxed{\log_e{x} = \ln{x}}$$

Where $e \approx 2.71828$ (Euler's number)

**Uses:** Calculus, continuous growth/decay, probability

**Examples:**
- $\ln{e} = 1$ because $e^1 = e$
- $\ln{1} = 0$ because $e^0 = 1$
- $\ln{e^3} = 3$ because $e^3 = e^3$

---

### 3. Binary Logarithm (Base 2)
$$\boxed{\log_2{x} = \lg{x}}$$

**Uses:** Computer science, information theory, algorithm complexity

**Examples:**
- $\log_2{16} = 4$ because $2^4 = 16$
- $\log_2{1024} = 10$ because $2^{10} = 1024$

---

## Fundamental Properties

### 1. Logarithm of 1
$$\boxed{\log_a{1} = 0}$$

**Reason:** $a^0 = 1$ for any $a$

**Examples:**
- $\log{1} = 0$
- $\ln{1} = 0$
- $\log_5{1} = 0$

---

### 2. Logarithm of the Base
$$\boxed{\log_a{a} = 1}$$

**Reason:** $a^1 = a$

**Examples:**
- $\log_{10}{10} = 1$
- $\ln{e} = 1$
- $\log_7{7} = 1$

---

### 3. Logarithm of a Power of the Base
$$\boxed{\log_a{a^n} = n}$$

**Examples:**
- $\log_2{2^5} = 5$
- $\ln{e^{-3}} = -3$
- $\log{10^{100}} = 100$

---

### 4. Base to a Logarithm Power
$$\boxed{a^{\log_a{x}} = x}$$

**Examples:**
- $10^{\log{5}} = 5$
- $e^{\ln{7}} = 7$
- $2^{\log_2{x}} = x$

---

## Logarithm Laws

### 1. Product Rule
$$\boxed{\log_a{(mn)} = \log_a{m} + \log_a{n}}$$

**Derivation:**
Let $\log_a{m} = p$ and $\log_a{n} = q$
- Then $a^p = m$ and $a^q = n$
- So $mn = a^p \cdot a^q = a^{p+q}$
- Therefore $\log_a{(mn)} = p + q = \log_a{m} + \log_a{n}$

**Examples:**
- $\log_2{(8 \cdot 4)} = \log_2{8} + \log_2{4} = 3 + 2 = 5$
- $\ln{(xy)} = \ln{x} + \ln{y}$
- $\log{(100 \cdot 1000)} = \log{100} + \log{1000} = 2 + 3 = 5$

---

### 2. Quotient Rule
$$\boxed{\log_a{\left(\frac{m}{n}\right)} = \log_a{m} - \log_a{n}}$$

**Examples:**
- $\log_5{\frac{125}{25}} = \log_5{125} - \log_5{25} = 3 - 2 = 1$
- $\ln{\frac{x}{y}} = \ln{x} - \ln{y}$
- $\log{\frac{1000}{10}} = \log{1000} - \log{10} = 3 - 1 = 2$

---

### 3. Power Rule
$$\boxed{\log_a{m^n} = n \cdot \log_a{m}}$$

**Examples:**
- $\log_2{16} = \log_2{2^4} = 4 \cdot \log_2{2} = 4 \cdot 1 = 4$
- $\ln{x^3} = 3\ln{x}$
- $\log{100^5} = 5 \cdot \log{100} = 5 \cdot 2 = 10$
- $\log{\sqrt{x}} = \log{x^{1/2}} = \frac{1}{2}\log{x}$

---

### 4. Change of Base Formula
$$\boxed{\log_a{b} = \frac{\log_c{b}}{\log_c{a}} = \frac{\ln{b}}{\ln{a}} = \frac{\log{b}}{\log{a}}}$$

**Use:** Convert between different logarithm bases

**Examples:**
- $\log_2{10} = \frac{\log{10}}{\log{2}} = \frac{1}{0.301} \approx 3.32$
- $\log_5{7} = \frac{\ln{7}}{\ln{5}} \approx \frac{1.946}{1.609} \approx 1.21$

---

### 5. Logarithm of Reciprocal
$$\boxed{\log_a{\frac{1}{x}} = -\log_a{x}}$$

**Examples:**
- $\log_2{\frac{1}{8}} = -\log_2{8} = -3$
- $\ln{\frac{1}{e}} = -\ln{e} = -1$

---

### 6. Root Rule
$$\boxed{\log_a{\sqrt[n]{x}} = \frac{1}{n}\log_a{x}}$$

**Examples:**
- $\log{\sqrt{100}} = \frac{1}{2}\log{100} = \frac{1}{2} \cdot 2 = 1$
- $\log_2{\sqrt[3]{8}} = \frac{1}{3}\log_2{8} = \frac{1}{3} \cdot 3 = 1$

---

### 7. Power of Base Rule
$$\boxed{\log_{a^n}{m} = \frac{1}{n} \cdot \log_a{m}}$$

**Example:**
- $\log_{2^3}{64} = \frac{1}{3}\log_2{64} = \frac{1}{3} \cdot 6 = 2$

---

## Quick Reference Table

| Law | Formula | Example |
|-----|---------|---------|
| Product | $\log_a{(mn)} = \log_a{m} + \log_a{n}$ | $\log{(10 \cdot 100)} = 1 + 2$ |
| Quotient | $\log_a{\frac{m}{n}} = \log_a{m} - \log_a{n}$ | $\log{\frac{100}{10}} = 2 - 1$ |
| Power | $\log_a{m^n} = n\log_a{m}$ | $\log{x^3} = 3\log{x}$ |
| Change of Base | $\log_a{b} = \frac{\log{b}}{\log{a}}$ | $\log_2{10} = \frac{1}{0.301}$ |
| Identity 1 | $\log_a{1} = 0$ | $\ln{1} = 0$ |
| Identity 2 | $\log_a{a} = 1$ | $\log{10} = 1$ |
| Identity 3 | $\log_a{a^n} = n$ | $\log{10^5} = 5$ |
| Identity 4 | $a^{\log_a{x}} = x$ | $e^{\ln{5}} = 5$ |

---

## Solving Logarithmic Equations

### Type 1: Single Logarithm
$$\log_a{x} = b \quad \Rightarrow \quad x = a^b$$

**Example:** Solve $\log_2{x} = 5$
- $x = 2^5 = 32$

---

### Type 2: Two Logarithms (Same Base)
$$\log_a{f(x)} = \log_a{g(x)} \quad \Rightarrow \quad f(x) = g(x)$$

**Example:** Solve $\log{(x+2)} = \log{(3x-4)}$
- $x + 2 = 3x - 4$
- $6 = 2x$
- $x = 3$

---

### Type 3: Sum/Difference of Logarithms
Use product/quotient rules to combine.

**Example:** Solve $\log_3{x} + \log_3{(x-2)} = 1$
- $\log_3{[x(x-2)]} = 1$
- $x(x-2) = 3^1 = 3$
- $x^2 - 2x - 3 = 0$
- $(x-3)(x+1) = 0$
- $x = 3$ (reject $x = -1$ as log argument must be positive)

---

## Applications

### 1. pH Scale (Chemistry)
$$\text{pH} = -\log{[\text{H}^+]}$$

**Example:** If $[\text{H}^+] = 10^{-7}$ M, then pH $= -\log{10^{-7}} = 7$ (neutral)

---

### 2. Richter Scale (Earthquakes)
$$M = \log{\frac{I}{I_0}}$$

**Example:** Earthquake 100 times more intense: $M = \log{100} = 2$ units higher

---

### 3. Decibels (Sound Intensity)
$$\beta = 10\log{\frac{I}{I_0}}$$

**Example:** Sound 1000 times more intense: $\beta = 10\log{1000} = 30$ dB

---

### 4. Compound Interest (Continuous)
$$t = \frac{\ln{\frac{A}{P}}}{r}$$

**Example:** Time to double investment at 5% continuous interest:
- $t = \frac{\ln{2}}{0.05} \approx 13.86$ years

---

### 5. Half-Life Problems
$$t = \frac{\ln{2}}{\lambda}$$

---

### 6. Moore's Law (Technology)
Computing power doubles approximately every 2 years (exponential growth modeled with logarithms).

---

## Logarithmic Graphs

### Graph of $y = \log_a{x}$

**Properties:**
- Domain: $(0, \infty)$
- Range: $(-\infty, \infty)$
- Vertical asymptote: $x = 0$
- Passes through $(1, 0)$ and $(a, 1)$
- If $a > 1$: increasing
- If $0 < a < 1$: decreasing

<img src="Pictures/logarithm_graphs.png" width=500 height="auto" style="display: block; margin: auto">

---

## Common Mistakes

1. **$\log{(a + b)} \neq \log{a} + \log{b}$** ✗
   - Correct: $\log{(ab)} = \log{a} + \log{b}$ ✓

2. **$\frac{\log{a}}{\log{b}} \neq \log{\frac{a}{b}}$** ✗
   - These are different operations ✓

3. **$\log_a{x^n} \neq (\log_a{x})^n$** ✗
   - Correct: $\log_a{x^n} = n\log_a{x}$ ✓

4. **$\log{(-5)}$** is undefined ✗
   - Logarithms only defined for positive arguments ✓

---

## Special Values to Remember

| Expression | Value | Reason |
|------------|-------|--------|
| $\log{1}$ | $0$ | $10^0 = 1$ |
| $\log{10}$ | $1$ | $10^1 = 10$ |
| $\log{100}$ | $2$ | $10^2 = 100$ |
| $\log{1000}$ | $3$ | $10^3 = 1000$ |
| $\ln{1}$ | $0$ | $e^0 = 1$ |
| $\ln{e}$ | $1$ | $e^1 = e$ |
| $\log_2{2}$ | $1$ | $2^1 = 2$ |
| $\log_2{8}$ | $3$ | $2^3 = 8$ |
| $\log_2{1024}$ | $10$ | $2^{10} = 1024$ |

---

## See Also
- [[Exponents]] - Inverse operation of logarithms
- [[00 - Algebra MOC]] - Algebra topics overview
