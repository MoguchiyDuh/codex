---
tags: [math, linear-algebra, eigenvalues]
status: complete
---

# Eigenvalues & Eigenvectors

> Special vectors that a linear transformation only stretches or shrinks — never rotates off their own line.

## Definition

For a square matrix $A \in \mathbb{R}^{n \times n}$, a non-zero vector $\mathbf{v}$ and scalar $\lambda$ satisfying

$$A\mathbf{v} = \lambda \mathbf{v}$$

make $\lambda$ an **eigenvalue** and $\mathbf{v}$ a corresponding **eigenvector**. The pair $(\lambda, \mathbf{v})$ is an **eigenpair**.

Geometrically: $\mathbf{v}$ points along an axis that $A$ leaves invariant (up to scaling). If $\lambda > 0$, direction preserved; $\lambda < 0$, direction flipped; $|\lambda| > 1$, stretched; $|\lambda| < 1$, shrunk; $\lambda = 0$, collapsed to origin.

![[eigenvector_action.png]]

## Finding eigenvalues — characteristic equation

Rewrite $A\mathbf{v} = \lambda \mathbf{v}$ as $(A - \lambda I)\mathbf{v} = \mathbf{0}$. A non-zero $\mathbf{v}$ exists iff $A - \lambda I$ is singular:

$$\boxed{\det(A - \lambda I) = 0}$$

This expands to a polynomial of degree $n$ in $\lambda$ — the **characteristic polynomial** $p_A(\lambda)$. Its $n$ roots (counting multiplicity, possibly complex) are the eigenvalues.

### Example — 2×2

$$A = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix} \;\Rightarrow\; \det \begin{bmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{bmatrix} = (4-\lambda)(3-\lambda) - 2 = \lambda^2 - 7\lambda + 10$$

Roots: $\lambda_1 = 5$, $\lambda_2 = 2$.

## Finding eigenvectors

For each eigenvalue $\lambda_i$, solve $(A - \lambda_i I)\mathbf{v} = \mathbf{0}$. The solution space is the **eigenspace** $E_{\lambda_i}$ — a subspace (the null space of $A - \lambda_i I$).

**Algebraic multiplicity** of $\lambda$: its multiplicity as a root of $p_A$.
**Geometric multiplicity** of $\lambda$: $\dim E_\lambda$.

Always $1 \leq \text{geometric} \leq \text{algebraic}$. When they match for every eigenvalue, $A$ is diagonalizable.

## Key properties

| Property                 | Statement                                     |
| ------------------------ | --------------------------------------------- |
| Trace                    | $\text{tr}(A) = \sum_i \lambda_i$             |
| Determinant              | $\det(A) = \prod_i \lambda_i$                 |
| Triangular matrix        | Eigenvalues = diagonal entries                |
| $A$ and $A^T$            | Same eigenvalues                              |
| $A^k$                    | Eigenvalues $\lambda_i^k$ (same eigenvectors) |
| $A^{-1}$ (if invertible) | Eigenvalues $1/\lambda_i$                     |
| $A + cI$                 | Eigenvalues $\lambda_i + c$                   |
| Singular $A$             | Has eigenvalue $\lambda = 0$                  |

Eigenvalues of $AB$ vs $A$ and $B$: **no simple relation** in general.

## Diagonalization

If $A$ has $n$ linearly independent eigenvectors, assemble them as columns of $P$ and eigenvalues on the diagonal of $D$:

$$A = PDP^{-1}, \quad P = [\mathbf{v}_1 \cdots \mathbf{v}_n], \quad D = \text{diag}(\lambda_1, \dots, \lambda_n)$$

This is a **change of basis** to the eigenbasis, where $A$ acts as pure coordinate-wise scaling.

### When diagonalization fails

- Distinct eigenvalues ⟹ always diagonalizable.
- Repeated eigenvalue with geometric multiplicity < algebraic multiplicity ⟹ **defective** matrix, cannot be diagonalized. Example: $\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ (Jordan block).

### Fast powers

Diagonalization makes $A^k$ trivial:

$$A^k = PD^kP^{-1}, \quad D^k = \text{diag}(\lambda_1^k, \dots, \lambda_n^k)$$

This is how difference equations $\mathbf{x}_{k+1} = A\mathbf{x}_k$ get closed-form solutions.

## Symmetric matrices — spectral theorem

If $A$ is real and symmetric ($A^T = A$):

1. All eigenvalues are **real**.
2. Eigenvectors from different eigenvalues are **orthogonal**.
3. $A$ can be orthogonally diagonalized: $A = Q \Lambda Q^T$ where $Q$ is orthogonal ($Q^T Q = I$).

This is the **spectral theorem** — one of the cleanest results in linear algebra, the backbone of PCA and many numerical methods.

### Positive definite matrices

Symmetric $A$ is **positive definite** if $\mathbf{x}^T A \mathbf{x} > 0$ for all $\mathbf{x} \neq \mathbf{0}$. Equivalent:

- All eigenvalues $> 0$.
- All leading principal minors $> 0$ (Sylvester's criterion).
- $A = R^T R$ for some $R$ with independent columns.

Positive semidefinite replaces $>$ with $\geq$.

## Markov matrices

A **Markov matrix** has non-negative entries and columns summing to $1$. Such matrices always have $\lambda_1 = 1$ as an eigenvalue, with all other $|\lambda_i| \leq 1$.

Repeatedly applying $A$ converges: $A^k \mathbf{x}_0 \to \mathbf{x}_\infty$ where $\mathbf{x}_\infty$ is the eigenvector for $\lambda = 1$ (the **stationary distribution**).

Powers PageRank, random walks, equilibrium models.

## Complex eigenvalues

Real matrices can have complex eigenvalues — they come in conjugate pairs $\lambda, \bar{\lambda}$. Geometrically they encode **rotation** combined with scaling.

Example — 2D rotation by $\theta$:

$$R = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}, \quad \lambda = e^{\pm i\theta}$$

No real eigenvectors (nothing stays on its own line in 2D rotation), but complex ones exist.

## Applications

| Area                                                   | Role of eigenvalues                                                              |
| ------------------------------------------------------ | -------------------------------------------------------------------------------- |
| **PCA**                                                | Principal components = eigenvectors of covariance matrix; variance = eigenvalues |
| **Google PageRank**                                    | Stationary eigenvector of link matrix                                            |
| **Vibrations**                                         | Eigenvalues = resonant frequencies; eigenvectors = mode shapes                   |
| **Stability of ODEs** $\dot{\mathbf{x}} = A\mathbf{x}$ | Stable iff all $\text{Re}(\lambda_i) < 0$                                        |
| **Markov chains**                                      | Long-run behavior                                                                |
| **Quantum mechanics**                                  | Observables = Hermitian operators; measured values = eigenvalues                 |
| **Image compression / SVD**                            | Singular values are eigenvalues of $A^T A$                                       |

## Video references

- ![3Blue1Brown - Eigenvectors and eigenvalues | Chapter 14, Essence of linear algebra](https://www.youtube.com/watch?v=PFDu9oVAE-g)
- ![3Blue1Brown - A quick trick for computing eigenvalues | Chapter 15, Essence of linear algebra](https://www.youtube.com/watch?v=e50Bj7jn9IQ)

- ![21. Eigenvalues and Eigenvectors](https://www.youtube.com/watch?v=cdZnhQjJu4I)
- ![22. Diagonalization and Powers of A](https://www.youtube.com/watch?v=13r9QY6cmjc)
- ![23. Differential Equations and exp(At)](https://www.youtube.com/watch?v=IZqwi0wJovM)
- ![24. Markov Matrices; Fourier Series](https://www.youtube.com/watch?v=lGGDIGizcQ0)
- ![24b. Quiz 2 Review](https://www.youtube.com/watch?v=QuZL5IKpO_U)
- ![25. Symmetric Matrices and Positive Definiteness](https://www.youtube.com/watch?v=UCc9q_cAhho)
- ![26. Complex Matrices; Fast Fourier Transform](https://www.youtube.com/watch?v=M0Sa8fLOajA)
- ![27. Positive Definite Matrices and Minima](https://www.youtube.com/watch?v=vF7eyJ2g3kU)
- ![28. Similar Matrices and Jordan Form](https://www.youtube.com/watch?v=TSdXJw83kyA)

## See also

- [[Matrices]]
- [[Linear Transformations]]
- [[Determinants]]
- [[Vector Spaces]]
- [[Orthogonality & Projections]]
- [[Index]]
