---
tags: [math, linear-algebra, linear-equations]
status: complete
---

# Systems of Linear Equations

> Solving $A\mathbf{x} = \mathbf{b}$ — the central practical problem that motivates linear algebra.

## Matrix form

A system of $m$ equations in $n$ unknowns:

$$\begin{cases} a_{11} x_1 + \cdots + a_{1n} x_n = b_1 \\ \quad\quad\quad \vdots \\ a_{m1} x_1 + \cdots + a_{mn} x_n = b_m \end{cases} \iff A\mathbf{x} = \mathbf{b}$$

Where $A \in \mathbb{R}^{m \times n}$ is the **coefficient matrix**, $\mathbf{x} \in \mathbb{R}^n$ the unknowns, $\mathbf{b} \in \mathbb{R}^m$ the right-hand side.

Two geometric readings of the matrix equation $A\mathbf{x} = \mathbf{b}$ (Strang's "row picture" and "column picture"):

| Picture | Meaning |
|---------|---------|
| **Row picture** | Each equation is a hyperplane in $\mathbb{R}^n$; solution = their intersection |
| **Column picture** | Find weights $x_i$ so columns of $A$ combine to give $\mathbf{b}$ |

The column picture uses the matrix-vector product from [[Matrices]]: $A\mathbf{x}$ is a linear combination of the columns of $A$. Here the question is whether those columns can combine to produce $\mathbf{b}$.

![[row_vs_column_picture.png]]

## Augmented matrix

Attach $\mathbf{b}$ as a final column:

$$[A \mid \mathbf{b}] = \begin{bmatrix} a_{11} & \cdots & a_{1n} & b_1 \\ \vdots & & \vdots & \vdots \\ a_{m1} & \cdots & a_{mn} & b_m \end{bmatrix}$$

All row operations act on this extended matrix.

## Gaussian elimination

Reduce $[A \mid \mathbf{b}]$ to **row echelon form** using three elementary row operations:

| Operation | Effect |
|-----------|--------|
| Swap two rows | Reorder equations |
| Scale a row by $\alpha \neq 0$ | Multiply equation |
| Add multiple of one row to another | Subtract equations |

Each operation preserves the solution set.

### Row echelon form (REF)

- Leading entry (**pivot**) of each non-zero row is strictly right of the pivot above.
- All-zero rows at the bottom.

### Reduced row echelon form (RREF)

REF plus:

- Every pivot equals $1$.
- Pivot is the only non-zero entry in its column.

RREF is unique for a given matrix.

### Back substitution

Once in REF, solve bottom-up — the last pivot gives $x_n$, substitute into the row above, etc.

## LU factorization

Gaussian elimination (without row swaps) factors $A$ into lower and upper triangular pieces:

$$A = LU$$

- $L$: lower triangular with $1$s on the diagonal, off-diagonals are the multipliers used in elimination.
- $U$: upper triangular, the REF of $A$.

With row swaps: $PA = LU$ where $P$ is a **permutation matrix**.

Solving $A\mathbf{x} = \mathbf{b}$ becomes two easy triangular solves:

$$L\mathbf{y} = \mathbf{b} \quad\text{(forward)}, \qquad U\mathbf{x} = \mathbf{y} \quad\text{(back)}$$

This is how production solvers work — factor once, solve many right-hand sides cheaply.

## Rank and consistency

The **rank** $r$ of $A$ is the number of pivots in its REF. Equivalently:

- Number of linearly independent rows.
- Number of linearly independent columns.
- Dimension of the column space.

Rank bounds: $r \leq \min(m, n)$. Full rank means $r = \min(m, n)$.

### Solution types

Let $r = \text{rank}(A)$ and $r' = \text{rank}([A \mid \mathbf{b}])$.

| Condition | Solution |
|-----------|----------|
| $r < r'$ | **Inconsistent** — no solution (a row $[0 \cdots 0 \mid c]$ with $c \neq 0$ appears) |
| $r = r' = n$ | **Unique** solution |
| $r = r' < n$ | **Infinite** solutions, parameterized by $n - r$ free variables |

For square $A$: unique solution iff $\det(A) \neq 0$ iff $A$ is invertible. See [[Determinants]].

## Complete solution to $A\mathbf{x} = \mathbf{b}$

Split unknowns into **pivot variables** (columns with pivots) and **free variables** (the rest).

$$\mathbf{x} = \mathbf{x}_p + \mathbf{x}_n$$

- $\mathbf{x}_p$: any **particular solution** (set free variables to $0$, solve for pivot variables).
- $\mathbf{x}_n$: any element of the **null space** $N(A) = \{\mathbf{x} : A\mathbf{x} = \mathbf{0}\}$, built from **special solutions** (set one free variable to $1$, the rest to $0$).

This decomposition — particular plus homogeneous — is the general pattern for linear equations.

## Solving via inverse

If $A$ is square and invertible:

$$\mathbf{x} = A^{-1} \mathbf{b}$$

Theoretically clean, numerically wasteful — computing $A^{-1}$ takes ~$3\times$ the work of just factoring and solving. Use LU in practice.

## Overdetermined systems — least squares

When $m > n$ and $A\mathbf{x} = \mathbf{b}$ has no solution (generic case), find $\mathbf{x}$ minimizing $\|A\mathbf{x} - \mathbf{b}\|^2$:

$$A^T A \, \hat{\mathbf{x}} = A^T \mathbf{b} \quad\text{(normal equations)}$$

Covered in [[Orthogonality & Projections]].

## Cramer's rule

For $n \times n$ systems with $\det(A) \neq 0$:

$$x_i = \frac{\det(A_i)}{\det(A)}$$

Where $A_i$ is $A$ with column $i$ replaced by $\mathbf{b}$.

![[cramers_rule.png]]

Elegant formula, $O(n! \cdot n)$ via direct determinant — exponentially slower than elimination. Useful for proofs and $2 \times 2$ by hand, never for computation.

## Video references

- ![3Blue1Brown - Inverse matrices, column space and null space | Chapter 7, Essence of linear algebra](https://www.youtube.com/watch?v=uQhTuRlWMxw)
- ![3Blue1Brown - Cramer's rule, explained geometrically | Chapter 12, Essence of linear algebra](https://www.youtube.com/watch?v=jBsC34PxzoM)

## See also

- [[Matrices]]
- [[Determinants]]
- [[Vector Spaces]]
- [[Orthogonality & Projections]]
- [[Index]]
