# Arithmetic Progression (AP)

An **arithmetic progression** (also called arithmetic sequence) is a sequence of numbers where the difference between consecutive terms is constant.

---

## Definition

A sequence where each term after the first is obtained by adding a fixed constant called the **common difference**.

$$\boxed{a_1, a_2, a_3, \ldots, a_n = a_1, a_1 + d, a_1 + 2d, \ldots, a_1 + (n-1)d}$$

**General pattern:**
$$a_1, \quad a_1 + d, \quad a_1 + 2d, \quad a_1 + 3d, \quad \ldots$$

---

## Notation

| Symbol | Meaning |
|--------|---------|
| $a_n$ | The $n$-th term of the sequence |
| $a_1$ | First term |
| $d$ | Common difference |
| $n$ | Number of terms (position) |
| $S_n$ | Sum of first $n$ terms |

---

## Common Difference

The common difference $d$ is found by subtracting any term from the next term:
$$\boxed{d = a_{n+1} - a_n}$$

**Examples:**
- Sequence: $3, 7, 11, 15, 19, \ldots$ → $d = 7 - 3 = 4$
- Sequence: $20, 15, 10, 5, 0, \ldots$ → $d = 15 - 20 = -5$
- Sequence: $1, 1.5, 2, 2.5, 3, \ldots$ → $d = 1.5 - 1 = 0.5$

---

## N-th Term Formula

The formula to find the $n$-th term of an arithmetic progression:
$$\boxed{a_n = a_1 + (n - 1)d}$$

**Derivation:**
- $a_1 = a_1$
- $a_2 = a_1 + d = a_1 + (2-1)d$
- $a_3 = a_1 + 2d = a_1 + (3-1)d$
- $a_n = a_1 + (n-1)d$

**Examples:**

1. Find the 10th term of the sequence: $2, 5, 8, 11, \ldots$
   - $a_1 = 2$, $d = 3$
   - $a_{10} = 2 + (10-1) \cdot 3 = 2 + 27 = 29$

2. Find the 50th term of: $100, 95, 90, \ldots$
   - $a_1 = 100$, $d = -5$
   - $a_{50} = 100 + (50-1)(-5) = 100 - 245 = -145$

---

## Sum of First n Terms

The sum of the first $n$ terms can be calculated using either formula:

### Formula 1: Using First and Last Term
$$\boxed{S_n = \frac{n(a_1 + a_n)}{2}}$$

This represents: **Number of terms × Average of first and last terms**

### Formula 2: Using First Term and Common Difference
$$\boxed{S_n = \frac{n[2a_1 + (n-1)d]}{2}}$$

**Derivation of Formula 1:**
$$
\begin{align*}
S_n &= a_1 + a_2 + a_3 + \cdots + a_n \\
S_n &= a_n + a_{n-1} + a_{n-2} + \cdots + a_1 \\
\hline
2S_n &= (a_1 + a_n) + (a_2 + a_{n-1}) + \cdots + (a_n + a_1) \\
2S_n &= n(a_1 + a_n) \\
S_n &= \frac{n(a_1 + a_n)}{2}
\end{align*}
$$

**Examples:**

1. Find sum of first 20 terms: $3, 7, 11, 15, \ldots$
   - $a_1 = 3$, $d = 4$, $n = 20$
   - First find $a_{20} = 3 + 19(4) = 79$
   - $S_{20} = \frac{20(3 + 79)}{2} = \frac{20 \cdot 82}{2} = 820$

2. Sum of first 100 natural numbers: $1 + 2 + 3 + \cdots + 100$
   - $a_1 = 1$, $a_n = 100$, $n = 100$
   - $S_{100} = \frac{100(1 + 100)}{2} = \frac{100 \cdot 101}{2} = 5050$

3. Using Formula 2 for: $5, 10, 15, \ldots$ (first 30 terms)
   - $a_1 = 5$, $d = 5$, $n = 30$
   - $S_{30} = \frac{30[2(5) + (30-1)(5)]}{2} = \frac{30[10 + 145]}{2} = 2325$

---

## Properties of AP

### 1. Middle Term
If $a, b, c$ are in AP, then $b$ is the arithmetic mean:
$$\boxed{b = \frac{a + c}{2}}$$

**Example:** In sequence $5, 9, 13$:
- $9 = \frac{5 + 13}{2} = 9$ ✓

### 2. Three Terms in AP
If three numbers form an AP, they can be written as:
$$\boxed{a - d, \quad a, \quad a + d}$$

**Example:** Find three numbers in AP with sum 15 and product 80.
- Let the numbers be: $a - d, a, a + d$
- Sum: $(a-d) + a + (a+d) = 3a = 15$ → $a = 5$
- Product: $(5-d) \cdot 5 \cdot (5+d) = 80$ → $5(25 - d^2) = 80$ → $d = 3$
- Numbers: $2, 5, 8$

### 3. Equidistant Terms
In an AP, the sum of terms equidistant from the beginning and end is constant:
$$\boxed{a_k + a_{n-k+1} = a_1 + a_n}$$

---

## Special Cases

### Sum of First n Natural Numbers
$$\boxed{1 + 2 + 3 + \cdots + n = \frac{n(n+1)}{2}}$$

### Sum of First n Odd Numbers
$$\boxed{1 + 3 + 5 + \cdots + (2n-1) = n^2}$$

**Example:** $1 + 3 + 5 + 7 + 9 = 5^2 = 25$

### Sum of First n Even Numbers
$$\boxed{2 + 4 + 6 + \cdots + 2n = n(n+1)}$$

**Example:** $2 + 4 + 6 + 8 = 4(5) = 20$

---

## Applications

### 1. Real-World Problems

**Example:** A theater has 20 rows. The first row has 15 seats, and each subsequent row has 2 more seats than the previous. How many seats total?
- $a_1 = 15$, $d = 2$, $n = 20$
- $S_{20} = \frac{20[2(15) + 19(2)]}{2} = \frac{20[30 + 38]}{2} = 680$ seats

### 2. Finding Position

Find which term equals a specific value:
$$\boxed{n = \frac{a_n - a_1}{d} + 1}$$

**Example:** In sequence $7, 11, 15, 19, \ldots$, which term equals 99?
- $a_1 = 7$, $d = 4$, $a_n = 99$
- $99 = 7 + (n-1)(4)$ → $92 = 4(n-1)$ → $n = 24$

---

## Comparison with Geometric Progression

| Feature | Arithmetic Progression | Geometric Progression |
|---------|------------------------|------------------------|
| Pattern | Add constant $d$ | Multiply by constant $r$ |
| General Term | $a_n = a_1 + (n-1)d$ | $a_n = a_1 \cdot r^{n-1}$ |
| Middle Term | Arithmetic mean | Geometric mean |
| Growth | Linear | Exponential |

---

## Practice Problems

1. **Find the 15th term:** $4, 9, 14, 19, \ldots$
   - Answer: $a_{15} = 4 + 14(5) = 74$

2. **Sum of integers from 1 to 50**
   - Answer: $S_{50} = \frac{50(51)}{2} = 1275$

3. **How many terms sum to 210:** $3, 6, 9, 12, \ldots$
   - $210 = \frac{n[2(3) + (n-1)(3)]}{2}$ → $n = 12$

---

## See Also
- [[Geometric Progression]] - Exponential sequences
- [[00 - Algebra MOC]] - Algebra topics overview
