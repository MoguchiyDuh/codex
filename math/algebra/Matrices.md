---
tags: [math, algebra, matrices]
status: complete
---
# Matrices

> A rectangular array of numbers arranged in rows and columns, fundamental to linear algebra.

## Definition

A **matrix** is a rectangular array of numbers:

$$A \in \mathbb{R}^{m \times n}$$

$$A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix}$$

Where $m$ is the number of rows, $n$ is the number of columns, and $a_{ij}$ is the element in row $i$, column $j$.

## Basic Operations

### Addition and Subtraction

Element-wise operation requiring same dimensions:

$$(A \pm B)_{ij} = a_{ij} \pm b_{ij}$$

### Scalar Multiplication

$$(\alpha A)_{ij} = \alpha \cdot a_{ij}$$

### Matrix Multiplication

For $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{n \times p}$, the product $AB \in \mathbb{R}^{m \times p}$:

$$(AB)_{ij} = \sum_{k=1}^{n} a_{ik}b_{kj}$$

The number of columns in $A$ must equal the number of rows in $B$.

**Properties:**

| Property | Expression |
|----------|------------|
| Non-commutative | $AB \neq BA$ (generally) |
| Associative | $(AB)C = A(BC)$ |
| Distributive | $A(B+C) = AB + AC$ |
| Identity | $AI = IA = A$ |

## Special Matrices

| Type | Definition | Example |
|------|------------|---------|
| **Identity** | Diagonal of 1s: $AI = IA = A$ | $I_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ |
| **Zero** | All elements = 0 | $O = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$ |
| **Diagonal** | Non-zero only on main diagonal | $\begin{bmatrix} 1 & 0 \\ 0 & 5 \end{bmatrix}$ |
| **Symmetric** | $A^T = A$ | $\begin{bmatrix} 1 & 2 \\ 2 & 3 \end{bmatrix}$ |
| **Skew-symmetric** | $A^T = -A$ | $\begin{bmatrix} 0 & 2 \\ -2 & 0 \end{bmatrix}$ |
| **Orthogonal** | $A^TA = AA^T = I$ | Rotation matrices |

## Transpose

The **transpose** swaps rows and columns:

$$(A^T)_{ij} = a_{ji}$$

**Properties:** $(A^T)^T = A$, $(AB)^T = B^TA^T$, $(A+B)^T = A^T + B^T$, $(\alpha A)^T = \alpha A^T$

## Determinant

A scalar value associated with square matrices.

### 2×2

$$\det(A) = ad - bc \quad \text{for } A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$$

### 3×3 (Sarrus' Rule / Cofactor Expansion)

![[rule_of_sarrus.png]]

$$\det\begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix} = a\begin{vmatrix} e & f \\ h & i \end{vmatrix} - b\begin{vmatrix} d & f \\ g & i \end{vmatrix} + c\begin{vmatrix} d & e \\ g & h \end{vmatrix}$$

**Properties:** $\det(AB) = \det(A)\det(B)$, $\det(A^T) = \det(A)$, $\det(I) = 1$

## Inverse Matrix

The **inverse** satisfies $AA^{-1} = A^{-1}A = I$. Exists if and only if $\det(A) \neq 0$.

### 2×2 Formula

$$A^{-1} = \frac{1}{\det(A)} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix} \quad \text{for } A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$$

**Properties:** $(AB)^{-1} = B^{-1}A^{-1}$, $(A^T)^{-1} = (A^{-1})^T$, $(A^{-1})^{-1} = A$

## Rank

The number of linearly independent rows (or columns):

- $\text{rank}(A) \leq \min(m,n)$ for an $m \times n$ matrix
- **Full rank:** $\text{rank}(A) = \min(m,n)$

## Eigenvalues & Eigenvectors

For a non-zero vector $v$ and scalar $\lambda$ satisfying $Av = \lambda v$, $\lambda$ is an **eigenvalue** and $v$ is the **eigenvector**.

Find eigenvalues by solving the characteristic equation:

$$\det(A - \lambda I) = 0$$

**Properties:** $\text{tr}(A) = \sum_{i} \lambda_i$, $\det(A) = \prod_{i} \lambda_i$

## Matrix Decompositions

| Decomposition | Form | Use |
|---------------|------|-----|
| **LU** | $A = LU$ | Solving $Ax = b$ efficiently |
| **QR** | $A = QR$ | Least squares, eigenvalue algorithms |
| **SVD** | $A = U\Sigma V^T$ | Dimensionality reduction, PCA |
| **Eigendecomposition** | $A = PDP^{-1}$ | Computing $A^n$, differential equations |

## Solving Linear Systems

General form $Ax = b$ where $A$ is the coefficient matrix, $x$ is the variable vector, $b$ is the constant vector.

### Inverse Matrix Method

If $\det(A) \neq 0$: $x = A^{-1}b$

### Gaussian Elimination

Transform augmented matrix $[A|b]$ to row echelon form using row operations: swap rows, multiply by scalar, add multiple of one row to another.

### Cramer's Rule

![[cramers_rule.png]]

For $n \times n$ systems with $\det(A) \neq 0$:

$$x_i = \frac{\det(A_i)}{\det(A)}$$

Where $A_i$ is matrix $A$ with column $i$ replaced by $b$.

### Solution Types

| Type | Condition |
|------|-----------|
| Unique solution | $\det(A) \neq 0$ |
| No solution | Inconsistent system |
| Infinite solutions | $\det(A) = 0$ and consistent |

For overdetermined systems (more equations than unknowns), use least squares: $x = (A^TA)^{-1}A^Tb$

## Key Theorems

**Rank-Nullity Theorem:** $\text{rank}(A) + \text{nullity}(A) = n$

**Cayley-Hamilton Theorem:** Every square matrix satisfies its own characteristic equation.

**Spectral Theorem:** Real symmetric matrices are orthogonally diagonalizable.

## See also

- [[quadratic function]] - Matrix form of quadratics
- [[polynomials]] - Characteristic polynomial
- [[Index]]
