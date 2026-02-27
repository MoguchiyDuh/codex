---
created: '2025-12-16'
tags:
  - linear-algebra
  - math
  - university
status: complete
---
# Matrices

A matrix is a rectangular array of numbers arranged in rows and columns, fundamental to linear algebra and used extensively across mathematics, physics, computer science, and engineering.

---

## Definition

A **matrix** is a rectangular array of numbers arranged in rows and columns:

### $$\boxed{A \in \mathbb{R}^{m \times n}}$$

$$A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix}$$

Where:
- $m$ is the **number of rows**
- $n$ is the **number of columns**
- $a_{ij}$ is the element in row $i$, column $j$

**Examples:**
- $2 \times 3$ matrix: $\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$
- $3 \times 2$ matrix: $\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}$

---

## Basic Operations

### Addition and Subtraction

Element-wise operation (requires same dimensions):

### $$\boxed{(A \pm B)_{ij} = a_{ij} \pm b_{ij}}$$

**Example:**
$$\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} + \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} = \begin{bmatrix} 6 & 8 \\ 10 & 12 \end{bmatrix}$$

---

### Scalar Multiplication

Multiply each element by a scalar:

### $$\boxed{(\alpha A)_{ij} = \alpha \cdot a_{ij}}$$

**Example:**
$$3 \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} = \begin{bmatrix} 3 & 6 \\ 9 & 12 \end{bmatrix}$$

---

### Matrix Multiplication

For $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{n \times p}$, the product $AB \in \mathbb{R}^{m \times p}$:

### $$\boxed{(AB)_{ij} = \sum_{k=1}^{n} a_{ik}b_{kj}}$$

**Important:** The number of columns in $A$ must equal the number of rows in $B$.

**Example (2×2 × 2×2):**
$$\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} = \begin{bmatrix} 1·5+2·7 & 1·6+2·8 \\ 3·5+4·7 & 3·6+4·8 \end{bmatrix} = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}$$

**Example (3×2 × 2×3):**
$$\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}_{3 \times 2} \begin{bmatrix} 7 & 8 & 9 \\ 10 & 11 & 12 \end{bmatrix}_{2 \times 3} = \begin{bmatrix} 1·7+2·10 & 1·8+2·11 & 1·9+2·12 \\ 3·7+4·10 & 3·8+4·11 & 3·9+4·12 \\ 5·7+6·10 & 5·8+6·11 & 5·9+6·12 \end{bmatrix} = \begin{bmatrix} 27 & 30 & 33 \\ 61 & 68 & 75 \\ 95 & 106 & 117 \end{bmatrix}_{3 \times 3}$$

Result is a $3 \times 3$ matrix.

**Properties:**
- **Non-commutative:** $AB \neq BA$ (generally)
- **Associative:** $(AB)C = A(BC)$
- **Distributive:** $A(B+C) = AB + AC$
- **Identity:** $AI = IA = A$

---

## Special Matrices

| Type | Definition | Example |
|------|------------|---------|
| **Identity** | Diagonal of 1s: $AI = IA = A$ | $I_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ |
| **Zero** | All elements = 0 | $O = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$ |
| **Diagonal** | Non-zero only on main diagonal | $\begin{bmatrix} 1 & 0 \\ 0 & 5 \end{bmatrix}$ |
| **Symmetric** | $A^T = A$ | $\begin{bmatrix} 1 & 2 \\ 2 & 3 \end{bmatrix}$ |
| **Skew-symmetric** | $A^T = -A$ | $\begin{bmatrix} 0 & 2 \\ -2 & 0 \end{bmatrix}$ |
| **Orthogonal** | $A^TA = AA^T = I$ | Rotation matrices |

---

## Transpose

The **transpose** of a matrix $A$ is obtained by swapping rows and columns:

### $$\boxed{(A^T)_{ij} = a_{ji}}$$

**Example:**
$$\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}^T = \begin{bmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{bmatrix}$$

**Properties:**
- $(A^T)^T = A$
- $(AB)^T = B^TA^T$
- $(A+B)^T = A^T + B^T$
- $(\alpha A)^T = \alpha A^T$

---

## Determinant

The **determinant** is a scalar value associated with square matrices:

### 2×2 Matrix
### $$\boxed{\det(A) = ad - bc} \quad \text{for } A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$$

**Example:**
$$\det\begin{bmatrix} 3 & 7 \\ 2 & 5 \end{bmatrix} = 3·5 - 7·2 = 15 - 14 = 1$$

### 3×3 Matrix (Cofactor Expansion)
$$\det\begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix} = a\begin{vmatrix} e & f \\ h & i \end{vmatrix} - b\begin{vmatrix} d & f \\ g & i \end{vmatrix} + c\begin{vmatrix} d & e \\ g & h \end{vmatrix}$$

**Properties:**
- $\det(AB) = \det(A)\det(B)$
- $\det(A^T) = \det(A)$
- $\det(A^{-1}) = \frac{1}{\det(A)}$
- $\det(\alpha A) = \alpha^n \det(A)$ for $n \times n$ matrix
- $\det(I) = 1$

---

## Inverse Matrix

The **inverse** of a matrix $A$ (if it exists) is denoted $A^{-1}$ and satisfies:

### $$\boxed{AA^{-1} = A^{-1}A = I}$$

**Existence:** $A^{-1}$ exists if and only if $\det(A) \neq 0$ (non-singular)

### 2×2 Inverse Formula
### $$\boxed{A^{-1} = \frac{1}{\det(A)} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}} \quad \text{for } A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$$

**Example:**
$$A = \begin{bmatrix} 2 & 3 \\ 1 & -1 \end{bmatrix}, \quad \det(A) = -5$$

$$A^{-1} = \frac{1}{-5} \begin{bmatrix} -1 & -3 \\ -1 & 2 \end{bmatrix} = \begin{bmatrix} 1/5 & 3/5 \\ 1/5 & -2/5 \end{bmatrix}$$

**Properties:**
- $(AB)^{-1} = B^{-1}A^{-1}$
- $(A^T)^{-1} = (A^{-1})^T$
- $(A^{-1})^{-1} = A$
- $\det(A^{-1}) = \frac{1}{\det(A)}$

---

## Rank

The **rank** of a matrix is the number of linearly independent rows (or columns):

### $$\boxed{\text{rank}(A) = \text{number of linearly independent rows/columns}}$$

**Properties:**
- $\text{rank}(A) \leq \min(m,n)$ for $m \times n$ matrix
- $\text{rank}(AB) \leq \min(\text{rank}(A), \text{rank}(B))$
- **Full rank:** $\text{rank}(A) = \min(m,n)$

---

## Eigenvalues & Eigenvectors

For a square matrix $A$, if there exists a non-zero vector $v$ and scalar $\lambda$ such that:

### $$\boxed{Av = \lambda v}$$

Then $\lambda$ is an **eigenvalue** and $v$ is the corresponding **eigenvector**.

**Finding eigenvalues:** Solve the characteristic equation:

### $$\boxed{\det(A - \lambda I) = 0}$$

**Properties:**
- **Trace:** $\text{tr}(A) = \sum_{i} \lambda_i$
- **Determinant:** $\det(A) = \prod_{i} \lambda_i$
- Symmetric matrices have real eigenvalues and orthogonal eigenvectors

---

## Matrix Decompositions

### LU Decomposition
### $$\boxed{A = LU}$$

Where $L$ is lower triangular, $U$ is upper triangular

**Use:** Solving $Ax = b$ efficiently

---

### QR Decomposition
### $$\boxed{A = QR}$$

Where $Q$ is orthogonal, $R$ is upper triangular

**Use:** Least squares problems, eigenvalue algorithms

---

### SVD (Singular Value Decomposition)
### $$\boxed{A = U\Sigma V^T}$$

Where $U, V$ are orthogonal, $\Sigma$ is diagonal

**Use:** Dimensionality reduction, pseudoinverse, data compression, PCA

---

### Eigendecomposition
### $$\boxed{A = PDP^{-1}}$$

Where $D$ is diagonal (eigenvalues), $P$ is eigenvectors (if diagonalizable)

**Use:** Computing $A^n$, solving differential equations

---

## Solving Systems of Linear Equations

General form of a system:

### $$\boxed{Ax = b}$$

Where:
- $A$ is the coefficient matrix
- $x$ is the variable vector
- $b$ is the constant vector

---

### Method 1: Inverse Matrix Method

If $\det(A) \neq 0$:

### $$\boxed{x = A^{-1}b}$$

**Example (2 variables):**

$$\begin{cases} 2x + 3y = 8 \\ x - y = -1 \end{cases}$$

Matrix form: 
$$\begin{bmatrix} 2 & 3 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 8 \\ -1 \end{bmatrix}$$

Find inverse: 
$$A^{-1} = \frac{1}{-5} \begin{bmatrix} -1 & -3 \\ -1 & 2 \end{bmatrix} = \begin{bmatrix} 1/5 & 3/5 \\ 1/5 & -2/5 \end{bmatrix}$$

Solution: 
$$\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 1/5 & 3/5 \\ 1/5 & -2/5 \end{bmatrix} \begin{bmatrix} 8 \\ -1 \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$$

Therefore: $x = 1, y = 2$

**Example (3 variables):**

$$\begin{cases} x + 2y + z = 6 \\ 2x - y + 3z = 9 \\ x + y + z = 5 \end{cases}$$

Matrix form: 
$$\begin{bmatrix} 1 & 2 & 1 \\ 2 & -1 & 3 \\ 1 & 1 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 6 \\ 9 \\ 5 \end{bmatrix}$$

Compute $A^{-1}$ and multiply: $x = A^{-1}b$ to get $x = 2, y = 1, z = 2$

---

### Method 2: Gaussian Elimination

Transform augmented matrix $[A|b]$ to row echelon form (REF) or reduced row echelon form (RREF).

**Row operations:**
1. Swap rows
2. Multiply row by non-zero scalar
3. Add multiple of one row to another

**Example (2 variables):**

$$\begin{cases} 2x + 3y = 8 \\ x - y = -1 \end{cases}$$

Augmented matrix:
$$\left[\begin{array}{cc|c} 2 & 3 & 8 \\ 1 & -1 & -1 \end{array}\right]$$

$R_1 \leftrightarrow R_2$:
$$\left[\begin{array}{cc|c} 1 & -1 & -1 \\ 2 & 3 & 8 \end{array}\right]$$

$R_2 - 2R_1 \to R_2$:
$$\left[\begin{array}{cc|c} 1 & -1 & -1 \\ 0 & 5 & 10 \end{array}\right]$$

$R_2 / 5 \to R_2$:
$$\left[\begin{array}{cc|c} 1 & -1 & -1 \\ 0 & 1 & 2 \end{array}\right]$$

**Back substitution:** $y = 2$, then $x - 2 = -1 \Rightarrow x = 1$

**Example (3 variables):**

$$\begin{cases} x + 2y + z = 6 \\ 2x - y + 3z = 9 \\ x + y + z = 5 \end{cases}$$

Augmented matrix:
$$\left[\begin{array}{ccc|c} 1 & 2 & 1 & 6 \\ 2 & -1 & 3 & 9 \\ 1 & 1 & 1 & 5 \end{array}\right]$$

$R_2 - 2R_1 \to R_2$, $R_3 - R_1 \to R_3$:
$$\left[\begin{array}{ccc|c} 1 & 2 & 1 & 6 \\ 0 & -5 & 1 & -3 \\ 0 & -1 & 0 & -1 \end{array}\right]$$

$R_2 \leftrightarrow R_3$:
$$\left[\begin{array}{ccc|c} 1 & 2 & 1 & 6 \\ 0 & -1 & 0 & -1 \\ 0 & -5 & 1 & -3 \end{array}\right]$$

$R_3 - 5R_2 \to R_3$:
$$\left[\begin{array}{ccc|c} 1 & 2 & 1 & 6 \\ 0 & -1 & 0 & -1 \\ 0 & 0 & 1 & 2 \end{array}\right]$$

**Back substitution:** $z = 2$, $-y = -1 \Rightarrow y = 1$, $x + 2 + 2 = 6 \Rightarrow x = 2$

---

### Method 3: Cramer's Rule

For $n \times n$ systems with $\det(A) \neq 0$:

### $$\boxed{x_i = \frac{\det(A_i)}{\det(A)}}$$

Where $A_i$ is matrix $A$ with column $i$ replaced by vector $b$.

**Example (2 variables):**

$$\begin{cases} 2x + 3y = 8 \\ x - y = -1 \end{cases}$$

$$\det(A) = \begin{vmatrix} 2 & 3 \\ 1 & -1 \end{vmatrix} = -5$$

$$x = \frac{\begin{vmatrix} 8 & 3 \\ -1 & -1 \end{vmatrix}}{-5} = \frac{-5}{-5} = 1$$

$$y = \frac{\begin{vmatrix} 2 & 8 \\ 1 & -1 \end{vmatrix}}{-5} = \frac{-10}{-5} = 2$$

**Example (3 variables):**

$$\begin{cases} x + 2y + z = 6 \\ 2x - y + 3z = 9 \\ x + y + z = 5 \end{cases}$$

$$\det(A) = \begin{vmatrix} 1 & 2 & 1 \\ 2 & -1 & 3 \\ 1 & 1 & 1 \end{vmatrix} = 1$$

$$x = \frac{\begin{vmatrix} 6 & 2 & 1 \\ 9 & -1 & 3 \\ 5 & 1 & 1 \end{vmatrix}}{1} = 2$$

$$y = \frac{\begin{vmatrix} 1 & 6 & 1 \\ 2 & 9 & 3 \\ 1 & 5 & 1 \end{vmatrix}}{1} = 1$$

$$z = \frac{\begin{vmatrix} 1 & 2 & 6 \\ 2 & -1 & 9 \\ 1 & 1 & 5 \end{vmatrix}}{1} = 2$$

---

### Solution Types

| Type | Condition | Meaning |
|------|-----------|---------|
| **Unique solution** | $\det(A) \neq 0$ | System is consistent and independent |
| **No solution** | Inconsistent | Parallel planes/lines (no intersection) |
| **Infinite solutions** | $\det(A) = 0$ and consistent | Dependent equations (overlapping) |

For **overdetermined systems** (more equations than unknowns), use **least squares**:
### $$\boxed{x = (A^TA)^{-1}A^Tb}$$

---

## Matrix Norms

**Frobenius norm:**
### $$\boxed{\|A\|_F = \sqrt{\sum_{i,j} a_{ij}^2}}$$

**Operator norm (induced p-norm):**
### $$\boxed{\|A\|_p = \sup_{x \neq 0} \frac{\|Ax\|_p}{\|x\|_p}}$$

---

## Applications

### 1. Computer Graphics
Transformations: rotation, scaling, translation, projection matrices

---

### 2. Machine Learning
- Data representation (features × samples)
- Neural networks (weight matrices)
- Principal Component Analysis (PCA)

---

### 3. Differential Equations
Matrix exponentials: $e^{At}$ for solving systems

---

### 4. Physics
- Quantum mechanics (operators as matrices)
- Mechanics (stress tensors, inertia tensors)

---

### 5. Optimization
- Gradient descent
- Hessian matrices (second derivatives)

---

### 6. Signal Processing
- Filters
- Discrete Fourier Transform (DFT)
- Discrete Cosine Transform (DCT)

---

## Key Theorems

**Rank-Nullity Theorem:**
### $$\boxed{\text{rank}(A) + \text{nullity}(A) = n}$$

**Cayley-Hamilton Theorem:**
Every square matrix satisfies its own characteristic equation

**Spectral Theorem:**
Real symmetric matrices are orthogonally diagonalizable

---

## See Also
- [[Complex Numbers]] - Matrices over complex numbers
- [[Quadratic Function]] - Matrix form of quadratics
- [[00 - Algebra MOC]] - Algebra topics overview
