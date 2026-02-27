# Polynomials

A **polynomial** is an algebraic expression consisting of variables and coefficients combined using addition, subtraction, and multiplication operations, where variables have non-negative integer exponents.

---

## Definition

A polynomial is an expression of the form:
$$\boxed{P(x) = a_nx^n + a_{n-1}x^{n-1} + \cdots + a_2x^2 + a_1x + a_0}$$

Where:
- $a_n, a_{n-1}, \ldots, a_0$ are **coefficients** (real or complex numbers)
- $n$ is a **non-negative integer**
- $a_n \neq 0$ (for the leading coefficient)
- $x$ is the **variable**

**Examples:**
- $P(x) = 3x^4 - 2x^2 + 7x - 5$
- $Q(x) = x^3 + 1$
- $R(x) = 5x - 3$
- $S(x) = 2$ (constant polynomial)

---

## Terminology

### Degree
The **degree** of a polynomial is the highest exponent of the variable.

**Examples:**
- $3x^5 + 2x^3 - 7$ has degree **5**
- $x^2 - 4x + 4$ has degree **2**
- $7$ has degree **0**

### Leading Coefficient
The coefficient of the term with the highest degree.

**Example:** In $5x^4 - 3x^2 + 2x - 1$, the leading coefficient is **5**.

### Constant Term
The term without a variable (degree 0).

**Example:** In $x^3 - 2x + 7$, the constant term is **7**.

### Standard Form
Polynomial written with terms in descending order of degree:
$$a_nx^n + a_{n-1}x^{n-1} + \cdots + a_1x + a_0$$

---

## Classification by Number of Terms

| Type | Number of Terms | Example |
|------|-----------------|---------|
| **Monomial** | 1 | $5x^3$ |
| **Binomial** | 2 | $3x^2 + 7$ |
| **Trinomial** | 3 | $x^2 - 4x + 4$ |
| **Polynomial** | 2 or more | $x^3 + 2x^2 - x + 5$ |

---

## Classification by Degree

| Degree | Name | Standard Form | Example |
|--------|------|---------------|---------|
| **0** | Constant | $a$ | $5$ |
| **1** | Linear | $ax + b$ | $2x + 3$ |
| **2** | Quadratic | $ax^2 + bx + c$ | $x^2 - 5x + 6$ |
| **3** | Cubic | $ax^3 + bx^2 + cx + d$ | $2x^3 + x - 1$ |
| **4** | Quartic | $ax^4 + \cdots$ | $x^4 - 16$ |
| **5** | Quintic | $ax^5 + \cdots$ | $x^5 + 2x^2$ |
| **n** | n-th degree | $a_nx^n + \cdots$ | - |

---

## Operations on Polynomials

### 1. Addition
Combine like terms (terms with the same variable and exponent).

**Example:**
$$
\begin{align*}
&(3x^2 + 2x - 5) + (x^2 - 4x + 3) \\
&= (3x^2 + x^2) + (2x - 4x) + (-5 + 3) \\
&= 4x^2 - 2x - 2
\end{align*}
$$

---

### 2. Subtraction
Distribute the negative sign and combine like terms.

**Example:**
$$
\begin{align*}
&(5x^3 + 2x - 1) - (2x^3 - 3x + 4) \\
&= 5x^3 + 2x - 1 - 2x^3 + 3x - 4 \\
&= 3x^3 + 5x - 5
\end{align*}
$$

---

### 3. Multiplication
Use the distributive property (FOIL for binomials).

**Example 1 (Binomials):**
$$
\begin{align*}
(x + 2)(x + 3) &= x \cdot x + x \cdot 3 + 2 \cdot x + 2 \cdot 3 \\
&= x^2 + 3x + 2x + 6 \\
&= x^2 + 5x + 6
\end{align*}
$$

**Example 2 (General):**
$$
\begin{align*}
(x^2 + 2x)(3x - 1) &= x^2(3x - 1) + 2x(3x - 1) \\
&= 3x^3 - x^2 + 6x^2 - 2x \\
&= 3x^3 + 5x^2 - 2x
\end{align*}
$$

**Degree rule:** $\deg(P \cdot Q) = \deg(P) + \deg(Q)$

---

### 4. Division
Two methods: **Long Division** and **Synthetic Division**.

#### Long Division

**Example:** Divide $x^3 + 2x^2 - x - 2$ by $x - 1$

```
         x^2 + 3x + 2
       ________________
x - 1 | x^3 + 2x^2 - x - 2
        x^3 - x^2
        ___________
             3x^2 - x
             3x^2 - 3x
             __________
                   2x - 2
                   2x - 2
                   ______
                      0
```

Result: $x^2 + 3x + 2$ with remainder $0$

---

#### Synthetic Division (for divisors of the form $x - c$)

**Example:** Divide $2x^3 - 5x^2 + 3x - 2$ by $x - 2$

```
2 |  2  -5   3  -2
  |      4  -2   2
  |________________
     2  -1   1   0
```

Result: $2x^2 - x + 1$ with remainder $0$

---

### Division Algorithm
$$\boxed{P(x) = Q(x) \cdot D(x) + R(x)}$$

Where:
- $P(x)$ is the dividend
- $D(x)$ is the divisor
- $Q(x)$ is the quotient
- $R(x)$ is the remainder (degree < degree of $D(x)$)

---

## Polynomial Theorems

### 1. Remainder Theorem
When polynomial $P(x)$ is divided by $(x - c)$, the remainder is $P(c)$.

$$\boxed{P(x) = (x - c) \cdot Q(x) + P(c)}$$

**Example:** Find remainder when $x^3 - 2x^2 + 3$ is divided by $x - 2$
- $P(2) = 2^3 - 2(2^2) + 3 = 8 - 8 + 3 = 3$
- Remainder = **3**

---

### 2. Factor Theorem
$(x - c)$ is a factor of $P(x)$ **if and only if** $P(c) = 0$.

**Example:** Is $(x - 1)$ a factor of $x^3 - 3x + 2$?
- $P(1) = 1^3 - 3(1) + 2 = 0$
- Yes, $(x - 1)$ is a factor ✓

---

### 3. Fundamental Theorem of Algebra
A polynomial of degree $n$ has exactly $n$ complex roots (counting multiplicity).

**Example:** $x^3 - 6x^2 + 11x - 6 = 0$ has **3 roots** (which are $1, 2, 3$)

---

### 4. Rational Root Theorem
If $\frac{p}{q}$ is a rational root of $P(x) = a_nx^n + \cdots + a_0$, then:
- $p$ divides $a_0$ (constant term)
- $q$ divides $a_n$ (leading coefficient)

**Example:** Find possible rational roots of $2x^3 - 3x^2 - 11x + 6 = 0$
- Factors of $a_0 = 6$: $\pm 1, \pm 2, \pm 3, \pm 6$
- Factors of $a_n = 2$: $\pm 1, \pm 2$
- Possible roots: $\pm 1, \pm 2, \pm 3, \pm 6, \pm \frac{1}{2}, \pm \frac{3}{2}$

---

## Factoring Polynomials

### 1. Greatest Common Factor (GCF)
$$6x^3 + 9x^2 = 3x^2(2x + 3)$$

---

### 2. Difference of Squares
$$\boxed{a^2 - b^2 = (a + b)(a - b)}$$

**Example:** $x^2 - 25 = (x + 5)(x - 5)$

---

### 3. Sum/Difference of Cubes
$$\boxed{a^3 + b^3 = (a + b)(a^2 - ab + b^2)}$$
$$\boxed{a^3 - b^3 = (a - b)(a^2 + ab + b^2)}$$

**Example:** $x^3 - 8 = (x - 2)(x^2 + 2x + 4)$

---

### 4. Quadratic Trinomials
$$\boxed{x^2 + bx + c = (x + p)(x + q)}$$
where $p + q = b$ and $p \cdot q = c$

**Example:** $x^2 + 5x + 6 = (x + 2)(x + 3)$

---

### 5. Grouping
$$
\begin{align*}
x^3 + 3x^2 + 2x + 6 &= (x^3 + 3x^2) + (2x + 6) \\
&= x^2(x + 3) + 2(x + 3) \\
&= (x^2 + 2)(x + 3)
\end{align*}
$$

---

## Roots and Zeros

A **root** (or **zero**) of $P(x)$ is a value $c$ such that $P(c) = 0$.

### Multiplicity
- **Simple root:** appears once, graph crosses x-axis
- **Double root:** appears twice, graph touches x-axis
- **Triple root:** appears three times, graph flattens at x-axis

**Example:** $P(x) = (x - 2)^2(x + 1)$
- $x = 2$ is a root with multiplicity **2**
- $x = -1$ is a root with multiplicity **1**

---

## Special Products

### Perfect Square Trinomials
$$\boxed{(a + b)^2 = a^2 + 2ab + b^2}$$
$$\boxed{(a - b)^2 = a^2 - 2ab + b^2}$$

---

### Binomial Cubes
$$\boxed{(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3}$$
$$\boxed{(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3}$$

---

## Polynomial Graphs

### End Behavior
Determined by the **leading term** $a_nx^n$:

| Leading Term | As $x \to -\infty$ | As $x \to +\infty$ |
|--------------|-------------------|-------------------|
| $+x^{\text{even}}$ | $+\infty$ | $+\infty$ |
| $-x^{\text{even}}$ | $-\infty$ | $-\infty$ |
| $+x^{\text{odd}}$ | $-\infty$ | $+\infty$ |
| $-x^{\text{odd}}$ | $+\infty$ | $-\infty$ |

---

### Turning Points
A polynomial of degree $n$ has at most $n - 1$ turning points.

---

## Applications

### 1. Physics
- Projectile motion: $h(t) = -16t^2 + v_0t + h_0$

### 2. Economics
- Cost, revenue, profit functions

### 3. Engineering
- Signal processing
- Control systems

### 4. Computer Graphics
- Bezier curves
- Splines

---

## Common Mistakes

1. **$(x + 3)^2 \neq x^2 + 9$** ✗
   - Correct: $(x + 3)^2 = x^2 + 6x + 9$ ✓

2. **$\frac{x^2 + 3x}{x} \neq x + 3$** (if $x = 0$) ✗
   - Correct: $\frac{x^2 + 3x}{x} = \frac{x(x + 3)}{x} = x + 3$ for $x \neq 0$ ✓

3. **$(x + 2)(x + 3) \neq x^2 + 6$** ✗
   - Correct: $(x + 2)(x + 3) = x^2 + 5x + 6$ ✓

---

## See Also
- [[Algebraic Identities]] - Common polynomial identities
- [[Quadratic Function]] - Second-degree polynomials
- [[Binomials]] - Two-term polynomials
- [[Quadratic Inequalities]] - Polynomial inequalities
- [[00 - Algebra MOC]] - Algebra topics overview
