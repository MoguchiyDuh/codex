# Geometric Progression (GP)

A **geometric progression** (also called geometric sequence) is a sequence where each term after the first is found by multiplying the previous term by a fixed, non-zero number called the **common ratio**.

---

## Definition

A sequence where each term is obtained by multiplying the previous term by a constant ratio.

$$\boxed{a_1, a_2, a_3, \ldots, a_n = a_1, a_1r, a_1r^2, \ldots, a_1r^{n-1}}$$

**General pattern:**
$$a_1, \quad a_1r, \quad a_1r^2, \quad a_1r^3, \quad \ldots$$

---

## Notation

| Symbol | Meaning |
|--------|---------|
| $a_n$ | The $n$-th term of the sequence |
| $a_1$ | First term |
| $r$ | Common ratio |
| $n$ | Number of terms (position) |
| $S_n$ | Sum of first $n$ terms |
| $S_\infty$ | Sum to infinity (for convergent series) |

---

## Common Ratio

The common ratio $r$ is found by dividing any term by the previous term:
$$\boxed{r = \frac{a_{n+1}}{a_n}}$$

**Examples:**
- Sequence: $2, 6, 18, 54, \ldots$ → $r = \frac{6}{2} = 3$
- Sequence: $100, 50, 25, 12.5, \ldots$ → $r = \frac{50}{100} = 0.5$
- Sequence: $3, -6, 12, -24, \ldots$ → $r = \frac{-6}{3} = -2$
- Sequence: $1, \frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \ldots$ → $r = \frac{1}{2}$

---

## N-th Term Formula

The formula to find the $n$-th term of a geometric progression:
$$\boxed{a_n = a_1 \cdot r^{n-1}}$$

**Derivation:**
- $a_1 = a_1$
- $a_2 = a_1 \cdot r = a_1 \cdot r^{2-1}$
- $a_3 = a_1 \cdot r^2 = a_1 \cdot r^{3-1}$
- $a_n = a_1 \cdot r^{n-1}$

**Examples:**

1. Find the 8th term of: $3, 6, 12, 24, \ldots$
   - $a_1 = 3$, $r = 2$
   - $a_8 = 3 \cdot 2^{8-1} = 3 \cdot 128 = 384$

2. Find the 10th term of: $1000, 100, 10, 1, \ldots$
   - $a_1 = 1000$, $r = 0.1$
   - $a_{10} = 1000 \cdot (0.1)^9 = 1000 \cdot 10^{-9} = 10^{-6} = 0.000001$

3. Find the 5th term of: $2, -6, 18, -54, \ldots$
   - $a_1 = 2$, $r = -3$
   - $a_5 = 2 \cdot (-3)^4 = 2 \cdot 81 = 162$

---

## Sum of First n Terms

The sum of the first $n$ terms depends on the value of $r$:

### For $r \neq 1$:
$$\boxed{S_n = a_1 \cdot \frac{1 - r^n}{1 - r} = a_1 \cdot \frac{r^n - 1}{r - 1}}$$

**Alternative forms:**
- If $r < 1$: Use $S_n = a_1 \cdot \frac{1 - r^n}{1 - r}$
- If $r > 1$: Use $S_n = a_1 \cdot \frac{r^n - 1}{r - 1}$

### For $r = 1$:
$$\boxed{S_n = n \cdot a_1}$$

**Derivation (for $r \neq 1$):**
$$
\begin{align*}
S_n &= a_1 + a_1r + a_1r^2 + \cdots + a_1r^{n-1} \\
rS_n &= a_1r + a_1r^2 + a_1r^3 + \cdots + a_1r^n \\
\hline
S_n - rS_n &= a_1 - a_1r^n \\
S_n(1 - r) &= a_1(1 - r^n) \\
S_n &= a_1 \cdot \frac{1 - r^n}{1 - r}
\end{align*}
$$

**Examples:**

1. Find sum of first 6 terms: $2, 6, 18, 54, \ldots$
   - $a_1 = 2$, $r = 3$, $n = 6$
   - $S_6 = 2 \cdot \frac{3^6 - 1}{3 - 1} = 2 \cdot \frac{729 - 1}{2} = 728$

2. Find sum: $100 + 50 + 25 + 12.5 + \cdots$ (10 terms)
   - $a_1 = 100$, $r = 0.5$, $n = 10$
   - $S_{10} = 100 \cdot \frac{1 - 0.5^{10}}{1 - 0.5} = 100 \cdot \frac{1 - 0.000977}{0.5} \approx 199.8$

3. Constant sequence: $5 + 5 + 5 + \cdots$ (20 terms)
   - $a_1 = 5$, $r = 1$, $n = 20$
   - $S_{20} = 20 \cdot 5 = 100$

---

## Infinite Geometric Series (Sum to Infinity)

For an infinite GP, the sum converges **only if** $|r| < 1$.

$$\boxed{S_\infty = \frac{a_1}{1 - r} \quad \text{for } |r| < 1}$$

**Derivation:**
As $n \to \infty$ and $|r| < 1$:
- $r^n \to 0$
- $S_n = a_1 \cdot \frac{1 - r^n}{1 - r} \to a_1 \cdot \frac{1}{1 - r}$

**Convergence conditions:**
- $|r| < 1$: Series **converges**
- $|r| \geq 1$: Series **diverges**

**Examples:**

1. Find sum to infinity: $1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots$
   - $a_1 = 1$, $r = \frac{1}{2}$
   - $S_\infty = \frac{1}{1 - \frac{1}{2}} = \frac{1}{\frac{1}{2}} = 2$

2. Find sum: $9 + 3 + 1 + \frac{1}{3} + \cdots$
   - $a_1 = 9$, $r = \frac{1}{3}$
   - $S_\infty = \frac{9}{1 - \frac{1}{3}} = \frac{9}{\frac{2}{3}} = 13.5$

3. Convert repeating decimal to fraction: $0.333\ldots$
   - $0.333\ldots = 0.3 + 0.03 + 0.003 + \cdots$
   - $a_1 = 0.3$, $r = 0.1$
   - $S_\infty = \frac{0.3}{1 - 0.1} = \frac{0.3}{0.9} = \frac{1}{3}$

4. Series $2 - 1 + \frac{1}{2} - \frac{1}{4} + \cdots$
   - $a_1 = 2$, $r = -\frac{1}{2}$
   - $S_\infty = \frac{2}{1 - (-\frac{1}{2})} = \frac{2}{1.5} = \frac{4}{3}$

---

## Properties of GP

### 1. Geometric Mean
If $a, b, c$ are in GP, then $b$ is the geometric mean:
$$\boxed{b = \sqrt{ac}}$$

**Example:** In sequence $2, 6, 18$:
- $6 = \sqrt{2 \cdot 18} = \sqrt{36} = 6$ ✓

### 2. Three Terms in GP
If three numbers form a GP, they can be written as:
$$\boxed{\frac{a}{r}, \quad a, \quad ar}$$

**Example:** Find three numbers in GP with product 64 and sum 14.
- Let the numbers be: $\frac{a}{r}, a, ar$
- Product: $\frac{a}{r} \cdot a \cdot ar = a^3 = 64$ → $a = 4$
- Sum: $\frac{4}{r} + 4 + 4r = 14$ → $\frac{4}{r} + 4r = 10$
- Solving: $r = 2$ or $r = \frac{1}{2}$
- Numbers: $2, 4, 8$ or $8, 4, 2$

### 3. Product of Terms
The product of $n$ terms of a GP can be calculated:
$$\boxed{P_n = (a_1 \cdot a_n)^{n/2}}$$

---

## Special Patterns

### Powers of 2
$$2, 4, 8, 16, 32, 64, 128, 256, \ldots \quad (r = 2)$$

### Powers of 10
$$1, 10, 100, 1000, 10000, \ldots \quad (r = 10)$$

### Halving Sequence
$$1, \frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \frac{1}{16}, \ldots \quad (r = \frac{1}{2})$$

### Alternating Signs
$$1, -2, 4, -8, 16, -32, \ldots \quad (r = -2)$$

---

## Comparison with Arithmetic Progression

| Feature | Arithmetic Progression | Geometric Progression |
|---------|------------------------|------------------------|
| Pattern | Add constant $d$ | Multiply by constant $r$ |
| General Term | $a_n = a_1 + (n-1)d$ | $a_n = a_1 \cdot r^{n-1}$ |
| Middle Term | Arithmetic mean: $\frac{a+c}{2}$ | Geometric mean: $\sqrt{ac}$ |
| Growth | Linear | Exponential |
| Sum Formula | $S_n = \frac{n(a_1 + a_n)}{2}$ | $S_n = a_1 \cdot \frac{1-r^n}{1-r}$ |
| Infinite Sum | Always diverges | Converges if $\|r\| < 1$ |

---

## Applications

### 1. Compound Interest
$$A = P(1 + r)^n$$

**Example:** $1000 invested at 10% annual interest
- After 1 year: $1000 \cdot 1.1 = 1100$
- After 2 years: $1000 \cdot 1.1^2 = 1210$
- After 3 years: $1000 \cdot 1.1^3 = 1331$
- Sequence: $1100, 1210, 1331, \ldots$ (GP with $r = 1.1$)

### 2. Population Growth
$$P(n) = P_0 \cdot r^n$$

**Example:** Bacteria doubling every hour
- Initial: 100
- After 1h: 200
- After 2h: 400
- After 3h: 800
- Sequence: $100, 200, 400, 800, \ldots$ (GP with $r = 2$)

### 3. Radioactive Decay
$$N(t) = N_0 \cdot \left(\frac{1}{2}\right)^{t/t_{1/2}}$$

**Example:** Half-life decay
- Start: 1000g
- After 1 half-life: 500g
- After 2 half-lives: 250g
- Sequence: $1000, 500, 250, 125, \ldots$ (GP with $r = 0.5$)

### 4. Fractals & Geometry
- Koch snowflake perimeter
- Sierpinski triangle area
- Binary tree nodes

### 5. Computer Science
- Binary search complexity: $O(\log n)$
- Memory allocation
- Data structures (binary trees)

---

## Practice Problems

1. **Find the 12th term:** $5, 15, 45, 135, \ldots$
   - Answer: $a_{12} = 5 \cdot 3^{11} = 885,735$

2. **Sum of first 8 terms:** $1, 2, 4, 8, \ldots$
   - Answer: $S_8 = 1 \cdot \frac{2^8 - 1}{2 - 1} = 255$

3. **Sum to infinity:** $10 + 5 + 2.5 + 1.25 + \cdots$
   - Answer: $S_\infty = \frac{10}{1 - 0.5} = 20$

4. **Does this converge?** $3, 6, 12, 24, \ldots$
   - Answer: No, $r = 2 > 1$, series diverges

5. **Convert to fraction:** $0.272727\ldots$
   - Answer: $0.27 + 0.0027 + \cdots = \frac{0.27}{1 - 0.01} = \frac{27}{99} = \frac{3}{11}$

---

## See Also
- [[Arithmetic Progression]] - Linear sequences
- [[Exponents]] - Fundamental to GP formulas
- [[Logarithms]] - Useful for solving GP equations
- [[00 - Algebra MOC]] - Algebra topics overview
