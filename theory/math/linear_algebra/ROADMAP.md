# Linear Algebra — Course Roadmap

Structured after **MIT 18.06 — Linear Algebra** (Strang, Spring 2010). Free lecture videos and problem sets on MIT OCW. Nine notes split into seven phases following Strang's arc: solve systems → understand structure → decompose → apply.

The course builds the operational vocabulary for ML, graphics, systems programming, and numerical methods. Notes flag applications inline (least squares as linear regression, eigenvalues as PCA, SVD as the engine of dimensionality reduction).

## Phases

### Phase 1 — Vectors and matrices

*18.06 Lectures 1–3*

Vector operations, norms, dot and cross products, projection. Matrix notation, addition, scalar multiplication, matrix-vector and matrix-matrix products. Transpose, special matrices (identity, diagonal, triangular, symmetric, orthogonal). Column view of $A\mathbf{x}$ as linear combinations.

- [[Vectors]]
- [[Matrices]]

### Phase 2 — Solving $A\mathbf{x} = \mathbf{b}$

*18.06 Lectures 4–8*

Row and column pictures. Augmented matrix and Gaussian elimination to REF and RREF. Back substitution. LU and PA=LU factorization. Rank, pivot variables, free variables. Complete solution $\mathbf{x} = \mathbf{x}_p + \mathbf{x}_n$. Overdetermined systems and the normal equations.

- [[Systems of Linear Equations]]

### Phase 3 — Determinants

*18.06 Lectures 18–20*

Three defining properties. 2×2 and 3×3 formulas. Properties: product rule, transpose invariance, row operations. Cofactor expansion. Big formula (permutations). Computing via elimination. Geometric meaning: signed volume scaling. Inverse via adjugate. Connection to eigenvalues.

- [[Determinants]]

### Phase 4 — Vector spaces and structure

*18.06 Lectures 9–14*

The eight axioms. Subspaces, subspace test. Linear independence, span, basis, dimension. The four fundamental subspaces (column space, null space, row space, left null space) and their dimensions. Rank-nullity theorem.

- [[Vector Spaces]]

### Phase 5 — Linear transformations

*18.06 Lectures 26–28*

Definition and consequences. Matrix representation: columns are images of basis vectors. Composition = matrix product. Kernel and image. Rank-nullity in transformation language. Invertibility. Geometric catalogue in 2D and 3D. Homogeneous coordinates for affine maps. Change of basis and similarity.

- [[Linear Transformations]]

### Phase 6 — Orthogonality and least squares

*18.06 Lectures 14–17*

Orthogonal complements. Fundamental theorem: null space ⊥ row space, left null space ⊥ column space. Orthonormal sets and orthogonal matrices. Projection onto a line and onto a subspace. Projection matrix: idempotent and symmetric. Least squares via normal equations. Gram-Schmidt and QR factorization.

- [[Orthogonality & Projections]]

### Phase 7 — Spectral theory

*18.06 Lectures 21–25, 29–33*

Eigenvalue equation and characteristic polynomial. Finding eigenvalues and eigenvectors. Algebraic and geometric multiplicity. Diagonalization $A = PDP^{-1}$; fast matrix powers. Symmetric matrices and the spectral theorem ($A = Q\Lambda Q^T$). Positive definite matrices. Markov matrices and stationary distributions. Complex eigenvalues as rotation-scaling. SVD: $A = U\Sigma V^T$ for any shape matrix. Relation to eigendecomposition of $A^TA$. Low-rank approximation (Eckart-Young). Pseudoinverse.

- [[Eigenvalues & Eigenvectors]]
- [[SVD]]

## Status

**Complete.** Final grade: **B** (university exam, 2026-04-29)

## Reference materials

- Lecture videos: [MIT OCW 18.06 Spring 2010 (Strang)](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- Textbook (book website, sample sections + solutions): [Introduction to Linear Algebra, 5e — Strang](https://math.mit.edu/~gs/linearalgebra/)
- Supplementary visual intuition: [3Blue1Brown — Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- Lookup textbook (broader): Lay, *Linear Algebra and Its Applications*, 5e

## See also

- [[Index]]
- [[../discrete/Index|Discrete Math]]
- [[../../algorithms/ROADMAP|Algorithms — Course Roadmap]]
