---
tags: [math, linear-algebra, svd, decomposition]
status: complete
---

# SVD

> Singular value decomposition — every matrix factors as rotation · stretch · rotation. The most useful matrix factorization in applied mathematics.

## Statement

For any $A \in \mathbb{R}^{m \times n}$ (any shape, any rank):

$$A = U \Sigma V^T$$

Where:

| Factor | Shape | Role |
|--------|-------|------|
| $U$ | $m \times m$ orthogonal | Left singular vectors as columns |
| $\Sigma$ | $m \times n$ diagonal | **Singular values** $\sigma_1 \geq \sigma_2 \geq \cdots \geq 0$ |
| $V$ | $n \times n$ orthogonal | Right singular vectors as columns |

Singular values are always real and non-negative, ordered largest to smallest.

![[svd_decomposition.png]]

## Geometric picture

Every linear map $\mathbf{x} \mapsto A\mathbf{x}$ decomposes as:

1. $V^T$: rotation/reflection in the input space.
2. $\Sigma$: scaling along each axis by $\sigma_i$ (and dimension change).
3. $U$: rotation/reflection in the output space.

The unit ball in $\mathbb{R}^n$ maps to an $r$-dimensional ellipsoid in $\mathbb{R}^m$ with semi-axes $\sigma_1, \dots, \sigma_r$ (where $r = \text{rank}(A)$).

## Relation to eigendecomposition

Singular values are **eigenvalues of $A^T A$, square-rooted**:

$$A^T A = V \Sigma^T \Sigma V^T, \qquad A A^T = U \Sigma \Sigma^T U^T$$

- Columns of $V$ are eigenvectors of $A^T A$ (right singular vectors).
- Columns of $U$ are eigenvectors of $A A^T$ (left singular vectors).
- $\sigma_i = \sqrt{\lambda_i(A^T A)}$.

Unlike eigendecomposition, SVD exists for every matrix — no squareness or diagonalizability required.

## Rank and the four subspaces

Let $r$ be the number of non-zero singular values. Then $\text{rank}(A) = r$ and:

| Subspace | Basis from SVD |
|----------|----------------|
| Column space $C(A)$ | First $r$ columns of $U$ |
| Left null space $N(A^T)$ | Last $m - r$ columns of $U$ |
| Row space $C(A^T)$ | First $r$ columns of $V$ |
| Null space $N(A)$ | Last $n - r$ columns of $V$ |

SVD produces orthonormal bases for all four fundamental subspaces simultaneously. See [[Vector Spaces]].

## Low-rank approximation — Eckart-Young

Truncate to the top $k$ singular values:

$$A_k = \sum_{i=1}^{k} \sigma_i \mathbf{u}_i \mathbf{v}_i^T$$

$A_k$ is the **best rank-$k$ approximation** of $A$ in both the Frobenius norm and spectral norm:

$$\|A - A_k\|_F^2 = \sum_{i=k+1}^{r} \sigma_i^2$$

This is why SVD is the engine of dimensionality reduction: keep the top few $\sigma_i$, discard the rest, lose the least information possible.

## Applications

| Area | Role of SVD |
|------|-------------|
| **PCA** | Principal components = right singular vectors of centered data; variance = $\sigma_i^2 / (n-1)$ |
| **Image compression** | Store only top-$k$ singular triplets |
| **Latent semantic analysis** | SVD of term-document matrix |
| **Recommender systems** | Low-rank factorization of user-item matrix |
| **Pseudoinverse** | $A^+ = V \Sigma^+ U^T$ — solves least squares for any shape $A$ |
| **Condition number** | $\kappa(A) = \sigma_1 / \sigma_r$ — measures numerical sensitivity |
| **Noise reduction** | Small $\sigma_i$ often correspond to noise; zero them out |

## Pseudoinverse (Moore-Penrose)

$$A^+ = V \Sigma^+ U^T$$

Where $\Sigma^+$ inverts the non-zero singular values and transposes. Properties:

- If $A$ is invertible, $A^+ = A^{-1}$.
- For overdetermined systems, $\hat{\mathbf{x}} = A^+ \mathbf{b}$ is the least-squares solution.
- For underdetermined systems, $A^+ \mathbf{b}$ is the minimum-norm solution.

One formula handles every shape and rank — it's why SVD is the solver of last resort.

## See also

- [[Matrices]]
- [[Eigenvalues & Eigenvectors]]
- [[Orthogonality & Projections]]
- [[Vector Spaces]]
- [[Linear Transformations]]
- [[Index]]
