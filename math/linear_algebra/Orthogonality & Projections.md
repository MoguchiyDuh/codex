---
tags: [math, linear-algebra, orthogonality, projections, least-squares]
status: complete
---

# Orthogonality & Projections

> Perpendicularity generalized — the geometric backbone of least squares, Fourier analysis, and numerical stability.

## Orthogonal vectors

$\mathbf{u} \perp \mathbf{v} \iff \mathbf{u} \cdot \mathbf{v} = 0$. See [[Vectors]] for the dot product.

The zero vector is orthogonal to everything. Two non-zero vectors are orthogonal iff the angle between them is $90°$.

### Pythagoras

If $\mathbf{u} \perp \mathbf{v}$: $\|\mathbf{u} + \mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2$.

## Orthogonal complement

For a subspace $W \subseteq \mathbb{R}^n$:

$$W^\perp = \{\mathbf{v} \in \mathbb{R}^n : \mathbf{v} \cdot \mathbf{w} = 0 \text{ for all } \mathbf{w} \in W\}$$

$W^\perp$ is a subspace. Key facts:

- $\dim W + \dim W^\perp = n$.
- $(W^\perp)^\perp = W$.
- $W \cap W^\perp = \{\mathbf{0}\}$.
- Every $\mathbf{v} \in \mathbb{R}^n$ decomposes uniquely as $\mathbf{v} = \mathbf{w} + \mathbf{w}^\perp$ with $\mathbf{w} \in W$, $\mathbf{w}^\perp \in W^\perp$.

### Fundamental theorem — the four subspaces pair up

For $A \in \mathbb{R}^{m \times n}$:

$$N(A) = C(A^T)^\perp, \qquad N(A^T) = C(A)^\perp$$

Null space is perpendicular to row space; left null space is perpendicular to column space. See [[Vector Spaces]].

## Orthonormal sets

Vectors $\mathbf{q}_1, \dots, \mathbf{q}_k$ are **orthonormal** if

$$\mathbf{q}_i \cdot \mathbf{q}_j = \begin{cases} 1 & i = j \\ 0 & i \neq j \end{cases}$$

Advantages: they are automatically independent, and computing coordinates in an orthonormal basis is just dot products — no matrix inversion needed.

## Orthogonal matrices

A square matrix $Q$ with orthonormal columns satisfies

$$Q^T Q = Q Q^T = I \iff Q^{-1} = Q^T$$

Geometric meaning: $Q$ preserves lengths and angles — rotations, reflections, and their combinations. $\det(Q) = \pm 1$.

Preservation identities: $\|Q\mathbf{x}\| = \|\mathbf{x}\|$, $(Q\mathbf{x}) \cdot (Q\mathbf{y}) = \mathbf{x} \cdot \mathbf{y}$.

## Projection onto a line

Project $\mathbf{b}$ onto the line spanned by $\mathbf{a}$:

$$\mathbf{p} = \frac{\mathbf{a}^T \mathbf{b}}{\mathbf{a}^T \mathbf{a}} \mathbf{a} = P\mathbf{b}, \quad P = \frac{\mathbf{a} \mathbf{a}^T}{\mathbf{a}^T \mathbf{a}}$$

$P$ is the **projection matrix** — rank 1, $P^2 = P$, $P^T = P$.

## Projection onto a subspace

Project $\mathbf{b}$ onto $C(A)$ where $A$ has independent columns:

$$\mathbf{p} = A(A^T A)^{-1} A^T \mathbf{b} = P\mathbf{b}, \quad P = A(A^T A)^{-1} A^T$$

Properties of every projection matrix:

| Property | Statement |
|----------|-----------|
| Idempotent | $P^2 = P$ |
| Symmetric | $P^T = P$ |
| Eigenvalues | only $0$ and $1$ |
| $I - P$ | Projection onto the orthogonal complement |

![[projection_onto_subspace.png]]

If the columns of $A$ are already orthonormal ($A = Q$, so $Q^T Q = I$), projection simplifies dramatically:

$$P = QQ^T$$

## Least squares

When $A\mathbf{x} = \mathbf{b}$ has no solution (too many equations), find $\hat{\mathbf{x}}$ that minimizes $\|A\mathbf{x} - \mathbf{b}\|^2$.

Geometric insight: the best $A\hat{\mathbf{x}}$ is the projection of $\mathbf{b}$ onto $C(A)$. The residual $\mathbf{b} - A\hat{\mathbf{x}}$ lives in $C(A)^\perp = N(A^T)$, so $A^T(\mathbf{b} - A\hat{\mathbf{x}}) = \mathbf{0}$.

### Normal equations

$$\boxed{A^T A \, \hat{\mathbf{x}} = A^T \mathbf{b}}$$

If $A$ has independent columns, $A^T A$ is invertible and

$$\hat{\mathbf{x}} = (A^T A)^{-1} A^T \mathbf{b}$$

### Application — line fitting

Fit $y = c + dt$ to data $(t_i, y_i)$:

$$A = \begin{bmatrix} 1 & t_1 \\ \vdots & \vdots \\ 1 & t_m \end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix} y_1 \\ \vdots \\ y_m \end{bmatrix}$$

$\hat{\mathbf{x}} = (c, d)^T$ minimizes total squared error. This is **linear regression** in matrix form.

![[least_squares_line.png]]

## Gram-Schmidt

Turn any basis $\{\mathbf{a}_1, \dots, \mathbf{a}_n\}$ into an orthonormal basis $\{\mathbf{q}_1, \dots, \mathbf{q}_n\}$:

$$\mathbf{u}_k = \mathbf{a}_k - \sum_{i=1}^{k-1} (\mathbf{q}_i^T \mathbf{a}_k)\, \mathbf{q}_i, \qquad \mathbf{q}_k = \frac{\mathbf{u}_k}{\|\mathbf{u}_k\|}$$

Subtract off components along already-orthonormal directions, then normalize.

## QR factorization

Gram-Schmidt, packaged as matrices:

$$A = QR$$

- $Q$: columns are the orthonormal vectors produced.
- $R$: upper triangular, entries are the coefficients $\mathbf{q}_i^T \mathbf{a}_k$.

Least squares via QR is numerically stabler than forming $A^T A$ directly. Most production solvers use it.

## Why it matters

| Area | Why orthogonality |
|------|-------------------|
| Least squares / regression | Projection onto column space |
| PCA / SVD | Orthonormal eigenbases of symmetric matrices |
| Fourier analysis | Orthogonal basis of sines/cosines |
| Numerical stability | Orthogonal matrices don't amplify rounding error |
| Quantum mechanics | Eigenstates of Hermitian operators are orthogonal |

## Video references

- ![3Blue1Brown - Dot products and duality | Chapter 9, Essence of linear algebra](https://www.youtube.com/watch?v=LyGKycYT2v0)

## See also

- [[Vectors]]
- [[Matrices]]
- [[Vector Spaces]]
- [[Systems of Linear Equations]]
- [[Eigenvalues & Eigenvectors]]
- [[SVD]]
- [[Index]]
