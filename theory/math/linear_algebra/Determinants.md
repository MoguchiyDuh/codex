---
tags: [math, linear-algebra, determinants]
status: complete
---

# Determinants

> A scalar $\det(A)$ encoding whether a square matrix is invertible and how it scales volume.

## Definition by three properties

Strang's approach: determinant is the unique function $\det: \mathbb{R}^{n \times n} \to \mathbb{R}$ satisfying

1. $\det(I) = 1$.
2. Swapping two rows reverses sign.
3. Linear in each row separately (keeping others fixed).

Everything else follows from these three.

## 2×2 and 3×3 formulas

### 2×2

$$\det \begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc$$

Geometrically: signed area of the parallelogram spanned by the columns.

### 3×3 (Sarrus' rule)

$$\det \begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix} = aei + bfg + cdh - ceg - bdi - afh$$

![[rule_of_sarrus.png]]

Sarrus works **only for 3×3**. For larger matrices use cofactor expansion or elimination.

## Properties

| Property                            | Statement                     |
| ----------------------------------- | ----------------------------- |
| $\det(I) = 1$                       | Identity                      |
| $\det(A^T) = \det(A)$               | Transpose invariant           |
| $\det(AB) = \det(A)\det(B)$         | Product rule                  |
| $\det(A^{-1}) = 1/\det(A)$          | Inverse                       |
| $\det(\alpha A) = \alpha^n \det(A)$ | Scalar (for $n \times n$)     |
| Row swap                            | Flips sign                    |
| Row scale by $\alpha$               | Multiplies $\det$ by $\alpha$ |
| Add multiple of row to another      | Unchanged                     |
| Row/column of zeros                 | $\det = 0$                    |
| Two equal rows                      | $\det = 0$                    |
| Triangular matrix                   | Product of diagonal entries   |

The product rule $\det(AB) = \det(A)\det(B)$ is not obvious but is the most-used identity.

## Cofactor expansion

Expand along any row $i$ or column $j$:

$$\det(A) = \sum_{j=1}^{n} (-1)^{i+j} a_{ij} M_{ij}$$

Where $M_{ij}$ is the **minor** — determinant of the $(n-1) \times (n-1)$ submatrix obtained by deleting row $i$ and column $j$. The signed minor $C_{ij} = (-1)^{i+j} M_{ij}$ is the **cofactor**.

Cost: $O(n!)$ — impractical beyond $n \approx 4$.

## Big formula — sum over permutations

$$\det(A) = \sum_{\sigma \in S_n} \text{sgn}(\sigma) \prod_{i=1}^{n} a_{i,\sigma(i)}$$

Exactly $n!$ terms, one per permutation of $\{1, \dots, n\}$, each a product of $n$ entries taken from distinct rows and columns. The sign $\text{sgn}(\sigma) = \pm 1$ depending on parity.

Theoretical tool — never computed this way.

## Computing via elimination

Practical method: reduce $A$ to upper triangular $U$ via elimination, tracking row operations.

$$\det(A) = (-1)^{\#\text{swaps}} \cdot \prod_i u_{ii}$$

Only row swaps and row scaling affect the determinant; adding multiples of rows does not.

Cost: $O(n^3)$ — same as Gaussian elimination.

## Geometric meaning

$|\det(A)|$ is the **volume scaling factor** of the linear map $\mathbf{x} \mapsto A\mathbf{x}$:

- In 2D: area of the parallelogram with columns of $A$ as sides.
- In 3D: volume of the parallelepiped.
- In $n$D: $n$-dimensional hypervolume.

Sign encodes orientation: $\det > 0$ preserves orientation, $\det < 0$ flips (like a reflection).

![[determinant_geometry.png]]

**$\det(A) = 0$** means the transformation collapses space into a lower dimension — columns are linearly dependent, $A$ is **singular** (non-invertible).

## Inverse via adjugate

$$A^{-1} = \frac{1}{\det(A)} \, \text{adj}(A), \quad \text{adj}(A) = C^T$$

Where $C$ is the matrix of cofactors. Exists iff $\det(A) \neq 0$.

### 2×2 shortcut

$$\begin{bmatrix} a & b \\ c & d \end{bmatrix}^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$

Memorize this; larger inverses come from elimination on $[A \mid I]$.

## Cramer's rule

For $A\mathbf{x} = \mathbf{b}$ with $\det(A) \neq 0$:

$$x_i = \frac{\det(A_i)}{\det(A)}$$

Where $A_i$ is $A$ with column $i$ replaced by $\mathbf{b}$. Derived from the adjugate formula. See [[Systems of Linear Equations]].

## Connection to eigenvalues

$$\det(A) = \prod_i \lambda_i$$

The determinant equals the product of eigenvalues (counted with multiplicity). Makes singular = "has a zero eigenvalue". See [[Eigenvalues & Eigenvectors]].

## Video references

- ![3Blue1Brown - The determinant | Chapter 6, Essence of linear algebra](https://www.youtube.com/watch?v=Ip3X9LOh2dk)
- ![3Blue1Brown - Cramer's rule, explained geometrically | Chapter 12, Essence of linear algebra](https://www.youtube.com/watch?v=jBsC34PxzoM)

- ![18. Properties of Determinants](https://www.youtube.com/watch?v=srxexLishgY)
- ![19. Determinant Formulas and Cofactors](https://www.youtube.com/watch?v=23LLB9mNJvc)
- ![20. Cramer's Rule, Inverse Matrix, and Volume](https://www.youtube.com/watch?v=QNpj-gOXW9M)

## See also

- [[Matrices]]
- [[Systems of Linear Equations]]
- [[Eigenvalues & Eigenvectors]]
- [[Index]]
