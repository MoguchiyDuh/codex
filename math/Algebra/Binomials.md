# Binomial Theorem

The **Binomial Theorem** provides a formula for expanding powers of binomials and is fundamental to combinatorics, probability, and algebra.

---

## Definition

A **binomial** is a [[Polynomials|polynomial]] with exactly two terms:
$$a + b$$

**Examples:**
- $x + 3$
- $2y - 5$
- $m + n$

---

## Binomial Theorem

The Binomial Theorem states that for any positive integer $n$:

$$\boxed{(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k}$$

Where $\binom{n}{k}$ is the **binomial coefficient** (read as "$n$ choose $k$").

---

## Binomial Coefficient

The binomial coefficient represents the number of ways to choose $k$ items from $n$ items:

$$\boxed{\binom{n}{k} = \frac{n!}{k!(n-k)!} = C(n, k)}$$

**Alternative notation:** $C_n^k$, $C(n, k)$, $_nC_k$

**Properties:**
- $\binom{n}{0} = 1$
- $\binom{n}{n} = 1$
- $\binom{n}{k} = \binom{n}{n-k}$ (symmetry)
- $\binom{n}{1} = n$
- $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$ (Pascal's identity)

**Examples:**
- $\binom{5}{2} = \frac{5!}{2!3!} = \frac{120}{2 \cdot 6} = 10$
- $\binom{6}{3} = \frac{6!}{3!3!} = 20$
- $\binom{4}{0} = 1$
- $\binom{7}{7} = 1$

---

## Expanded Form

The binomial expansion of $(a + b)^n$ is:

$$\boxed{(a + b)^n = \binom{n}{0}a^n + \binom{n}{1}a^{n-1}b + \binom{n}{2}a^{n-2}b^2 + \cdots + \binom{n}{n}b^n}$$

**Pattern:**
- Exponent of $a$ **decreases** from $n$ to $0$
- Exponent of $b$ **increases** from $0$ to $n$
- Sum of exponents in each term = $n$
- There are $n + 1$ terms total

---

## Examples of Binomial Expansions

### $(a + b)^2$
$$\boxed{(a + b)^2 = a^2 + 2ab + b^2}$$

**Coefficients:** $1, 2, 1$

---

### $(a + b)^3$
$$\boxed{(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3}$$

**Coefficients:** $1, 3, 3, 1$

---

### $(a + b)^4$
$$
\begin{align*}
(a + b)^4 &= \binom{4}{0}a^4 + \binom{4}{1}a^3b + \binom{4}{2}a^2b^2 + \binom{4}{3}ab^3 + \binom{4}{4}b^4 \\
&= a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4
\end{align*}
$$

**Coefficients:** $1, 4, 6, 4, 1$

---

### $(a + b)^5$
$$\boxed{(a + b)^5 = a^5 + 5a^4b + 10a^3b^2 + 10a^2b^3 + 5ab^4 + b^5}$$

**Coefficients:** $1, 5, 10, 10, 5, 1$

---

## General Term (k-th Term)

The **$(k+1)$-th term** in the expansion of $(a + b)^n$ is:

$$\boxed{T_{k+1} = \binom{n}{k} a^{n-k} b^k}$$

Where $k$ ranges from $0$ to $n$.

**Note:** The term number is $k+1$ because we start counting from $k=0$.

**Example:** Find the 4th term of $(x + 2y)^6$
- 4th term means $k = 3$
- $T_4 = \binom{6}{3} x^{6-3} (2y)^3 = 20 \cdot x^3 \cdot 8y^3 = 160x^3y^3$

---

## Pascal's Triangle

Pascal's Triangle is a triangular array where each number is the sum of the two numbers directly above it. The $n$-th row contains the binomial coefficients for $(a + b)^n$.

```
Row 0:                    1
Row 1:                  1   1
Row 2:                1   2   1
Row 3:              1   3   3   1
Row 4:            1   4   6   4   1
Row 5:          1   5  10  10   5   1
Row 6:        1   6  15  20  15   6   1
Row 7:      1   7  21  35  35  21   7   1
```

**Properties:**
- Each row starts and ends with **1**
- Each interior number = sum of two numbers above it
- Row $n$ has $n+1$ numbers
- Row $n$ gives coefficients for $(a + b)^n$
- Symmetric: reads same forwards and backwards

**Pascal's Identity:**
$$\boxed{\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}}$$


---

## Special Cases

### Sum of Coefficients

Setting $a = b = 1$ in $(a + b)^n$:
$$\boxed{\sum_{k=0}^{n} \binom{n}{k} = 2^n}$$

**Example:** For $(a + b)^5$:
$$1 + 5 + 10 + 10 + 5 + 1 = 32 = 2^5$$

---

### Alternating Sum

Setting $a = 1, b = -1$:
$$\boxed{\sum_{k=0}^{n} (-1)^k \binom{n}{k} = 0 \text{ for } n \geq 1}$$

**Example:** For $n = 4$:
$$1 - 4 + 6 - 4 + 1 = 0$$

---

### Sum of Even-Indexed Coefficients = Sum of Odd-Indexed Coefficients

$$\boxed{\binom{n}{0} + \binom{n}{2} + \binom{n}{4} + \cdots = \binom{n}{1} + \binom{n}{3} + \binom{n}{5} + \cdots = 2^{n-1}}$$

---

## Binomial Theorem for Negative/Fractional Exponents

For $|x| < 1$ and any real number $r$:

$$\boxed{(1 + x)^r = 1 + rx + \frac{r(r-1)}{2!}x^2 + \frac{r(r-1)(r-2)}{3!}x^3 + \cdots}$$

**Infinite series** (converges for $|x| < 1$)

**Example:** $(1 + x)^{-1} = 1 - x + x^2 - x^3 + \cdots$ for $|x| < 1$

---

## Applications

### 1. Finding Specific Terms

**Example:** Find the coefficient of $x^5$ in $(2x + 3)^8$

The general term is:
$$T_{k+1} = \binom{8}{k} (2x)^{8-k} \cdot 3^k$$

For $x^5$, we need $8 - k = 5$, so $k = 3$:
$$T_4 = \binom{8}{3} (2x)^5 \cdot 3^3 = 56 \cdot 32x^5 \cdot 27 = 48384x^5$$

Coefficient: **48,384**

---

### 2. Expanding Binomials

**Example:** Expand $(2x - 3y)^4$

$$
\begin{align*}
(2x - 3y)^4 &= \binom{4}{0}(2x)^4 + \binom{4}{1}(2x)^3(-3y) + \binom{4}{2}(2x)^2(-3y)^2 \\
&\quad + \binom{4}{3}(2x)(-3y)^3 + \binom{4}{4}(-3y)^4 \\
&= 16x^4 - 96x^3y + 216x^2y^2 - 216xy^3 + 81y^4
\end{align*}
$$

---

### 3. Approximations

**Example:** Approximate $(1.02)^5$ using binomial theorem

$$
\begin{align*}
(1.02)^5 &= (1 + 0.02)^5 \\
&\approx 1 + 5(0.02) + \binom{5}{2}(0.02)^2 \\
&= 1 + 0.1 + 10(0.0004) \\
&= 1 + 0.1 + 0.004 \\
&= 1.104
\end{align*}
$$

(Actual value: 1.10408...)

---

### 4. Probability Theory

Binomial distribution uses binomial coefficients:
$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

---

### 5. Combinatorics

Number of ways to select $k$ objects from $n$ objects = $\binom{n}{k}$

---

## Properties of Binomial Coefficients

### Symmetry
$$\boxed{\binom{n}{k} = \binom{n}{n-k}}$$

**Example:** $\binom{7}{3} = \binom{7}{4} = 35$

---

### Sum Property
$$\boxed{\binom{n}{k} + \binom{n}{k+1} = \binom{n+1}{k+1}}$$

**Example:** $\binom{5}{2} + \binom{5}{3} = 10 + 10 = 20 = \binom{6}{3}$

---

### Vandermonde's Identity
$$\boxed{\sum_{k=0}^{r} \binom{m}{k}\binom{n}{r-k} = \binom{m+n}{r}}$$

---

### Hockey Stick Identity
$$\boxed{\sum_{i=0}^{n} \binom{i}{k} = \binom{n+1}{k+1}}$$

---

## Complex Examples

### Example 1: Middle Term

Find the middle term of $(3x - 2y)^8$

- Total terms = $8 + 1 = 9$ (odd number)
- Middle term is the 5th term ($k = 4$)
- $T_5 = \binom{8}{4}(3x)^4(-2y)^4 = 70 \cdot 81x^4 \cdot 16y^4 = 90720x^4y^4$

---

### Example 2: Constant Term

Find the constant term in the expansion of $\left(x^2 + \frac{1}{x}\right)^9$

General term: $T_{k+1} = \binom{9}{k}(x^2)^{9-k}\left(\frac{1}{x}\right)^k = \binom{9}{k}x^{18-2k-k} = \binom{9}{k}x^{18-3k}$

For constant term, $18 - 3k = 0 \Rightarrow k = 6$

$T_7 = \binom{9}{6} = 84$

---

### Example 3: Coefficient of $x^n$

Find coefficient of $x^{10}$ in $(1 + x)^{15}$

From binomial theorem: coefficient = $\binom{15}{10} = \binom{15}{5} = 3003$

---

## Common Patterns

### $(1 + x)^n$
Simple coefficients from Pascal's triangle row $n$

---

### $(1 - x)^n$
Alternating signs: $+, -, +, -, \ldots$

---

### $(a - b)^n$
$$= \sum_{k=0}^{n} \binom{n}{k} a^{n-k} (-b)^k = \sum_{k=0}^{n} (-1)^k \binom{n}{k} a^{n-k} b^k$$

---

## See Also
- [[Algebraic Identities]] - Special cases of binomial expansion
- [[Polynomials]] - Binomials as special polynomials
- [[Permutations & Combinations]] - Binomial coefficients in combinatorics
- [[00 - Algebra MOC]] - Algebra topics overview
