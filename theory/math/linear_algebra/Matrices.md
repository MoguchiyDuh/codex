---
tags: [math, linear-algebra, matrices]
status: complete
---

# Matrices

> Rectangular arrays of numbers encoding linear transformations — columns are where basis vectors land.

## Notation

An $m \times n$ matrix has $m$ rows and $n$ columns:

$$A \in \mathbb{R}^{m \times n}, \quad A = \begin{bmatrix} a_{11} & \cdots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{m1} & \cdots & a_{mn} \end{bmatrix}$$

Element $a_{ij}$ lives in row $i$, column $j$. A matrix is **square** when $m = n$.

### Column view

$A$ can be read as $n$ column vectors side by side:

$$A = \begin{bmatrix} \mathbf{a}_1 & \mathbf{a}_2 & \cdots & \mathbf{a}_n \end{bmatrix}, \quad \mathbf{a}_j \in \mathbb{R}^m$$

This view makes matrix-vector multiplication a linear combination of columns — the core geometric intuition for how matrices act as transformations.

## Addition and scalar multiplication

Both are element-wise. Addition requires matching dimensions.

$$(A + B)_{ij} = a_{ij} + b_{ij}, \qquad (\alpha A)_{ij} = \alpha \, a_{ij}$$

Properties: commutative, associative, distributive over scalars. These make $\mathbb{R}^{m \times n}$ itself a vector space of dimension $mn$.

## Matrix-vector product

For $A \in \mathbb{R}^{m \times n}$ and $\mathbf{x} \in \mathbb{R}^n$:

$$A\mathbf{x} = x_1 \mathbf{a}_1 + x_2 \mathbf{a}_2 + \cdots + x_n \mathbf{a}_n$$

The output is a **linear combination of $A$'s columns**, weighted by $\mathbf{x}$. Equivalently, the row-dot form:

$$(A\mathbf{x})_i = \sum_{j=1}^{n} a_{ij} x_j$$

This is how a matrix acts as a linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$. For the row picture vs. column picture of solving $A\mathbf{x} = \mathbf{b}$, see [[Systems of Linear Equations]]. See also [[Linear Transformations]].

$$
\underbrace{\begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix}}_{A}
\underbrace{\begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}}_{\mathbf{x}}
=
x_1 \underbrace{\begin{bmatrix} a_{11} \\ a_{21} \\ \vdots \\ a_{m1} \end{bmatrix}}_{\mathbf{a}_1}
+ x_2 \underbrace{\begin{bmatrix} a_{12} \\ a_{22} \\ \vdots \\ a_{m2} \end{bmatrix}}_{\mathbf{a}_2}
+ \cdots +
x_n \underbrace{\begin{bmatrix} a_{1n} \\ a_{2n} \\ \vdots \\ a_{mn} \end{bmatrix}}_{\mathbf{a}_n}
$$

**Concrete example** ($2 \times 2$):

$$
\begin{bmatrix} 2 & 1 \\ 0 & 3 \end{bmatrix}
\begin{bmatrix} 2 \\ 1 \end{bmatrix}
= 2\begin{bmatrix} 2 \\ 0 \end{bmatrix}
+ 1\begin{bmatrix} 1 \\ 3 \end{bmatrix}
= \begin{bmatrix} 4 \\ 0 \end{bmatrix}
+ \begin{bmatrix} 1 \\ 3 \end{bmatrix}
= \begin{bmatrix} 5 \\ 3 \end{bmatrix}
$$

## Matrix multiplication

For $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{n \times p}$, the product $AB \in \mathbb{R}^{m \times p}$:

$$(AB)_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}$$

Inner dimensions must match: $(m \times \underline{n})(\underline{n} \times p) = (m \times p)$.

**Row $\times$ column view** — $(AB)_{ij}$ is the dot product of row $i$ of $A$ with column $j$ of $B$:

$$
(AB)_{ij}
= \begin{bmatrix} a_{i1} & a_{i2} & \cdots & a_{in} \end{bmatrix}
  \begin{bmatrix} b_{1j} \\ b_{2j} \\ \vdots \\ b_{nj} \end{bmatrix}
= \sum_{k=1}^{n} a_{ik}\, b_{kj}
$$

**Column view** — each column of $AB$ is $A$ times the corresponding column of $B$:

$$
AB = \begin{bmatrix} A\mathbf{b}_1 & A\mathbf{b}_2 & \cdots & A\mathbf{b}_p \end{bmatrix}
$$

**Concrete example** ($2 \times 2$):

$$
\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}
\begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}
=
\begin{bmatrix}
1 \cdot 5 + 2 \cdot 7 & 1 \cdot 6 + 2 \cdot 8 \\
3 \cdot 5 + 4 \cdot 7 & 3 \cdot 6 + 4 \cdot 8
\end{bmatrix}
=
\begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}
$$

Three equivalent interpretations:

| View | Meaning |
|------|---------|
| Row × column | $(AB)_{ij}$ = dot product of row $i$ of $A$ with column $j$ of $B$ |
| Column combinations | Column $j$ of $AB$ = $A$ applied to column $j$ of $B$ |
| Composition | $AB$ represents applying $B$ then $A$ to any input vector |

### Properties

| Property | Expression |
|----------|------------|
| Non-commutative | $AB \neq BA$ in general |
| Associative | $(AB)C = A(BC)$ |
| Distributive | $A(B + C) = AB + AC$ |
| Scalar | $\alpha(AB) = (\alpha A)B = A(\alpha B)$ |
| Identity | $AI = IA = A$ |

**Non-commutativity** is fundamental — rotating then scaling differs from scaling then rotating. Matrix multiplication encodes function composition, and composition of transformations is order-dependent.

![[matrix_non_commutativity.png]]

## Transpose

$A^T$ swaps rows and columns: $(A^T)_{ij} = a_{ji}$. If $A \in \mathbb{R}^{m \times n}$ then $A^T \in \mathbb{R}^{n \times m}$.

| Property | Expression |
|----------|------------|
| Involution | $(A^T)^T = A$ |
| Sum | $(A + B)^T = A^T + B^T$ |
| Scalar | $(\alpha A)^T = \alpha A^T$ |
| Product (reversed) | $(AB)^T = B^T A^T$ |

The reversed product rule is the one people forget — it falls out of the index definition.

## Special matrices

| Type | Definition | Example |
|------|------------|---------|
| **Identity** $I_n$ | $1$ on diagonal, $0$ elsewhere | $I_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ |
| **Zero** $O$ | All entries $0$ | $\begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$ |
| **Diagonal** | $a_{ij} = 0$ for $i \neq j$ | $\begin{bmatrix} 2 & 0 \\ 0 & 5 \end{bmatrix}$ |
| **Upper triangular** | $a_{ij} = 0$ for $i > j$ | $\begin{bmatrix} 1 & 2 \\ 0 & 3 \end{bmatrix}$ |
| **Lower triangular** | $a_{ij} = 0$ for $i < j$ | $\begin{bmatrix} 1 & 0 \\ 2 & 3 \end{bmatrix}$ |
| **Symmetric** | $A^T = A$ | $\begin{bmatrix} 1 & 2 \\ 2 & 3 \end{bmatrix}$ |
| **Skew-symmetric** | $A^T = -A$ (diagonal is $0$) | $\begin{bmatrix} 0 & 2 \\ -2 & 0 \end{bmatrix}$ |
| **Orthogonal** | $A^T A = I$ (columns orthonormal) | Rotation matrices |

Identity acts as "do nothing"; zero collapses everything to the origin; diagonal scales each axis independently.

## Block matrices

A matrix can be partitioned into submatrix blocks and multiplied block-wise, provided block dimensions are conformable:

$$\begin{bmatrix} A & B \\ C & D \end{bmatrix} \begin{bmatrix} E & F \\ G & H \end{bmatrix} = \begin{bmatrix} AE + BG & AF + BH \\ CE + DG & CF + DH \end{bmatrix}$$

## Matrix as a transformation

Every matrix $A \in \mathbb{R}^{m \times n}$ defines a function $\mathbf{x} \mapsto A\mathbf{x}$. Two key facts:

- The $j$-th column of $A$ is $A \mathbf{e}_j$ — the image of the $j$-th standard basis vector.
- Composing transformations corresponds to multiplying their matrices.

A matrix is fully determined by where it sends the basis — geometry lives in [[Linear Transformations]]. Determinants, inverse, and rank are developed in Phase 4; the mechanics start in [[Systems of Linear Equations]].

## Video references

- ![3Blue1Brown - Linear transformations and matrices | Chapter 3, Essence of linear algebra](https://www.youtube.com/watch?v=kYB8IZa5AuE)
- ![3Blue1Brown - Matrix multiplication as composition | Chapter 4, Essence of linear algebra](https://www.youtube.com/watch?v=XkY2DOUCWMU)
- ![3Blue1Brown - Three-dimensional linear transformations | Chapter 5, Essence of linear algebra](https://www.youtube.com/watch?v=rHLEWRxRGiM)
- ![3Blue1Brown - Nonsquare matrices as transformations between dimensions | Chapter 8, Essence of linear algebra](https://www.youtube.com/watch?v=v8VSDg_WQlA)

## See also

- [[Vectors]]
- [[Linear Transformations]]
- [[Systems of Linear Equations]]
- [[Vector Spaces]]
- [[Eigenvalues & Eigenvectors]]
- [[Index]]
