---
tags: [math, linear-algebra, transformations]
status: complete
---

# Linear Transformations

> What matrices actually do — every matrix is a transformation of space that preserves lines through the origin and parallelism.

## Definition

A function $T: V \to W$ between vector spaces is **linear** if for all $\mathbf{u}, \mathbf{v} \in V$ and $\alpha \in \mathbb{R}$:

$$T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}), \qquad T(\alpha \mathbf{v}) = \alpha\, T(\mathbf{v})$$

Equivalently: $T(\alpha \mathbf{u} + \beta \mathbf{v}) = \alpha T(\mathbf{u}) + \beta T(\mathbf{v})$.

**Immediate consequences:** $T(\mathbf{0}) = \mathbf{0}$ and $T$ maps lines through the origin to lines through the origin (or to $\mathbf{0}$).

### Examples and non-examples

| $T: \mathbb{R}^2 \to \mathbb{R}^2$ | Linear? |
|------------------------------------|---------|
| $T(\mathbf{x}) = A\mathbf{x}$ for any $A$ | Yes |
| Rotation by fixed angle | Yes |
| Projection onto a line through origin | Yes |
| Translation $\mathbf{x} \mapsto \mathbf{x} + \mathbf{c}$, $\mathbf{c} \neq \mathbf{0}$ | **No** (violates $T(\mathbf{0}) = \mathbf{0}$) |
| $T(\mathbf{x}) = \|\mathbf{x}\| \mathbf{x}$ | No (not additive) |

## Matrix representation

Every linear $T: \mathbb{R}^n \to \mathbb{R}^m$ is $T(\mathbf{x}) = A\mathbf{x}$ for a unique matrix $A \in \mathbb{R}^{m \times n}$.

**Construction:** column $j$ of $A$ is the image of the $j$-th standard basis vector:

$$A = \begin{bmatrix} T(\mathbf{e}_1) & T(\mathbf{e}_2) & \cdots & T(\mathbf{e}_n) \end{bmatrix}$$

This is the whole point: **a matrix's columns are where the basis vectors land**. Knowing those determines the entire transformation by linearity.

![[basis_vectors_land.png]]

## Composition

If $S: \mathbb{R}^p \to \mathbb{R}^n$ with matrix $B$, and $T: \mathbb{R}^n \to \mathbb{R}^m$ with matrix $A$, then

$$T \circ S \text{ has matrix } AB$$

This is why matrix multiplication is defined the way it is: composition of transformations corresponds to the product, and applying $S$ first means $B$ is on the right.

## Kernel (null space)

$$\ker(T) = \{\mathbf{v} \in V : T(\mathbf{v}) = \mathbf{0}\}$$

For matrix transformations: $\ker(T) = N(A)$. Always a subspace of the domain.

$T$ is **injective** (one-to-one) iff $\ker(T) = \{\mathbf{0}\}$.

![[kernel_image_diagram.png]]

## Image (range, column space)

$$\text{im}(T) = \{T(\mathbf{v}) : \mathbf{v} \in V\}$$

For matrix transformations: $\text{im}(T) = C(A)$. Always a subspace of the codomain.

$T$ is **surjective** (onto) iff $\text{im}(T) = W$.

## Rank-nullity theorem

$$\dim \ker(T) + \dim \text{im}(T) = \dim V$$

For $T: \mathbb{R}^n \to \mathbb{R}^m$: $\dim N(A) + \text{rank}(A) = n$.

## Invertibility

For $T: V \to V$ (same finite-dimensional space on both sides):

$T$ is invertible $\iff \ker(T) = \{\mathbf{0}\} \iff \text{im}(T) = V \iff \det(A) \neq 0$

When invertible, $T^{-1}$ has matrix $A^{-1}$.

## Geometric catalogue in 2D

| Transformation | Matrix |
|----------------|--------|
| **Identity** | $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ |
| **Scaling** by $(s_x, s_y)$ | $\begin{bmatrix} s_x & 0 \\ 0 & s_y \end{bmatrix}$ |
| **Rotation** by $\theta$ CCW | $\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$ |
| **Reflection** across $x$-axis | $\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$ |
| **Reflection** across $y = x$ | $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ |
| **Shear** along $x$ by factor $k$ | $\begin{bmatrix} 1 & k \\ 0 & 1 \end{bmatrix}$ |
| **Projection** onto $x$-axis | $\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ |

Determinants encode the effect on area: rotations and reflections have $|\det| = 1$, scaling by $(s_x, s_y)$ has $\det = s_x s_y$, projection has $\det = 0$.

![[linear_transformations_catalogue.png]]

## Rotation in 3D

Rotation by $\theta$ about each axis (right-hand rule):

$$R_x = \begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{bmatrix}, \; R_y = \begin{bmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{bmatrix}, \; R_z = \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

General 3D rotations compose these — they are non-commutative (this is why 3D orientation is hard).

## Homogeneous coordinates — translations as matrix multiplications

Translation is not linear in $\mathbb{R}^n$, but **is** linear in $\mathbb{R}^{n+1}$ under the embedding $(x, y) \mapsto (x, y, 1)$:

$$\begin{bmatrix} 1 & 0 & t_x \\ 0 & 1 & t_y \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix} = \begin{bmatrix} x + t_x \\ y + t_y \\ 1 \end{bmatrix}$$

This unifies all affine transformations (linear + translation) under matrix multiplication. Ubiquitous in graphics and robotics.

## Change of basis

Given a transformation $T$ with matrix $A$ in the standard basis, and an alternate basis $\mathcal{B}$ with columns $\mathbf{b}_1, \dots, \mathbf{b}_n$ assembled into matrix $P$:

$$[T]_\mathcal{B} = P^{-1} A P$$

Interpretation: $P$ translates $\mathcal{B}$-coordinates to standard, $A$ transforms in standard coordinates, $P^{-1}$ translates back.

Two matrices $A$ and $B$ representing the same transformation in different bases are called **similar**: $B = P^{-1} A P$. Similar matrices share trace, determinant, rank, eigenvalues, and characteristic polynomial.

Diagonalization is the search for a basis in which $T$'s matrix is diagonal — see [[Eigenvalues & Eigenvectors]].

## Video references

- ![3Blue1Brown - Linear transformations and matrices | Chapter 3, Essence of linear algebra](https://www.youtube.com/watch?v=kYB8IZa5AuE)
- ![3Blue1Brown - Matrix multiplication as composition | Chapter 4, Essence of linear algebra](https://www.youtube.com/watch?v=XkY2DOUCWMU)
- ![3Blue1Brown - Three-dimensional linear transformations | Chapter 5, Essence of linear algebra](https://www.youtube.com/watch?v=rHLEWRxRGiM)
- ![3Blue1Brown - Change of basis | Chapter 13, Essence of linear algebra](https://www.youtube.com/watch?v=P2LTAUO1TdA)

## See also

- [[Matrices]]
- [[Vector Spaces]]
- [[Eigenvalues & Eigenvectors]]
- [[Orthogonality & Projections]]
- [[Index]]
