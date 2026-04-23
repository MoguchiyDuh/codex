---
tags: [math, linear-algebra, vector-spaces]
status: complete
---

# Vector Spaces

> The abstract framework unifying vectors, matrices, functions, and polynomials under one set of rules.

## Definition — the 8 axioms

A **vector space** $V$ over $\mathbb{R}$ is a set with two operations (addition, scalar multiplication) satisfying, for all $\mathbf{u}, \mathbf{v}, \mathbf{w} \in V$ and $\alpha, \beta \in \mathbb{R}$:

| # | Axiom | Statement |
|---|-------|-----------|
| 1 | Closure (add) | $\mathbf{u} + \mathbf{v} \in V$ |
| 2 | Commutative | $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$ |
| 3 | Associative (add) | $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$ |
| 4 | Zero | $\exists \mathbf{0} \in V$ with $\mathbf{v} + \mathbf{0} = \mathbf{v}$ |
| 5 | Inverse | $\forall \mathbf{v}, \exists -\mathbf{v}$ with $\mathbf{v} + (-\mathbf{v}) = \mathbf{0}$ |
| 6 | Closure (scale) | $\alpha \mathbf{v} \in V$ |
| 7 | Distributive | $\alpha(\mathbf{u} + \mathbf{v}) = \alpha \mathbf{u} + \alpha \mathbf{v}$, $(\alpha + \beta)\mathbf{v} = \alpha\mathbf{v} + \beta\mathbf{v}$ |
| 8 | Scalar identity | $1 \cdot \mathbf{v} = \mathbf{v}$, $\alpha(\beta \mathbf{v}) = (\alpha\beta)\mathbf{v}$ |

### Examples beyond $\mathbb{R}^n$

| Space | Elements |
|-------|----------|
| $\mathbb{R}^{m \times n}$ | All $m \times n$ real matrices |
| $P_n$ | Polynomials of degree $\leq n$ |
| $C[a, b]$ | Continuous functions on $[a, b]$ |
| Solutions of a homogeneous linear ODE | Functions |

The abstraction pays off: results proven for "vector spaces" apply to all of these.

## Subspaces

A subset $W \subseteq V$ is a **subspace** if it is a vector space under $V$'s operations.

### Subspace test

$W$ is a subspace iff all three hold:

1. $\mathbf{0} \in W$.
2. Closed under addition: $\mathbf{u}, \mathbf{v} \in W \Rightarrow \mathbf{u} + \mathbf{v} \in W$.
3. Closed under scalar multiplication: $\mathbf{v} \in W, \alpha \in \mathbb{R} \Rightarrow \alpha \mathbf{v} \in W$.

The zero vector check is the cheapest disqualifier — use it first.

### Examples

- Lines and planes **through the origin** in $\mathbb{R}^3$.
- $\{\mathbf{0}\}$ (the trivial subspace) and $V$ itself.
- Solutions of a homogeneous system $A\mathbf{x} = \mathbf{0}$.

Non-examples: lines not through origin, first quadrant (not closed under negation).

## Linear independence

Vectors $\mathbf{v}_1, \dots, \mathbf{v}_k$ are **linearly independent** if

$$\alpha_1 \mathbf{v}_1 + \cdots + \alpha_k \mathbf{v}_k = \mathbf{0} \implies \alpha_1 = \cdots = \alpha_k = 0$$

Otherwise **linearly dependent** — at least one vector is a combination of the others.

Test in practice: form matrix $A = [\mathbf{v}_1 \cdots \mathbf{v}_k]$. Columns are independent iff $N(A) = \{\mathbf{0}\}$ iff $\text{rank}(A) = k$.

## Span

The **span** of $S = \{\mathbf{v}_1, \dots, \mathbf{v}_k\}$ is the set of all linear combinations:

$$\text{span}(S) = \{\alpha_1 \mathbf{v}_1 + \cdots + \alpha_k \mathbf{v}_k : \alpha_i \in \mathbb{R}\}$$

This is always a subspace — the smallest one containing $S$.

## Basis

A **basis** of $V$ is a set of vectors that is:

1. Linearly independent.
2. Spans $V$.

Equivalently: every vector in $V$ has a **unique** representation as a combination of basis vectors.

### Coordinates

Given basis $\mathcal{B} = \{\mathbf{b}_1, \dots, \mathbf{b}_n\}$, every $\mathbf{v} \in V$ has unique coordinates:

$$[\mathbf{v}]_\mathcal{B} = \begin{bmatrix} c_1 \\ \vdots \\ c_n \end{bmatrix} \iff \mathbf{v} = c_1 \mathbf{b}_1 + \cdots + c_n \mathbf{b}_n$$

The **standard basis** of $\mathbb{R}^n$ is $\{\mathbf{e}_1, \dots, \mathbf{e}_n\}$.

Change of basis and its matrix representation are covered in [[Linear Transformations]].

## Dimension

Every basis of $V$ has the same size. That number is the **dimension**:

$$\dim(V) = |\mathcal{B}|$$

| Space | Dimension |
|-------|-----------|
| $\mathbb{R}^n$ | $n$ |
| $\mathbb{R}^{m \times n}$ | $mn$ |
| $P_n$ (polynomials of deg $\leq n$) | $n + 1$ |
| $\{\mathbf{0}\}$ | $0$ |

Infinite-dimensional spaces exist (e.g. $C[a,b]$) but are outside this course's scope.

## The four fundamental subspaces

For $A \in \mathbb{R}^{m \times n}$ with rank $r$:

| Subspace | Symbol | Lives in | Dimension | Built from |
|----------|--------|----------|-----------|------------|
| **Column space** | $C(A)$ | $\mathbb{R}^m$ | $r$ | Pivot columns of $A$ |
| **Null space** | $N(A)$ | $\mathbb{R}^n$ | $n - r$ | Special solutions to $A\mathbf{x} = \mathbf{0}$ |
| **Row space** | $C(A^T)$ | $\mathbb{R}^n$ | $r$ | Non-zero rows of RREF |
| **Left null space** | $N(A^T)$ | $\mathbb{R}^m$ | $m - r$ | Solutions to $A^T \mathbf{y} = \mathbf{0}$ |

![[four_fundamental_subspaces.png]]

Column space = reachable outputs of $\mathbf{x} \mapsto A\mathbf{x}$ (so $A\mathbf{x} = \mathbf{b}$ has a solution iff $\mathbf{b} \in C(A)$).

Null space = inputs that map to zero (kernel of the transformation).

### Orthogonality relations

Fundamental theorem of linear algebra (Strang): the four subspaces pair up orthogonally.

$$N(A) \perp C(A^T), \qquad N(A^T) \perp C(A)$$

In $\mathbb{R}^n$: $N(A)$ and $C(A^T)$ are orthogonal complements. In $\mathbb{R}^m$: $N(A^T)$ and $C(A)$ are orthogonal complements. See [[Orthogonality & Projections]].

## Rank-nullity theorem

$$\text{rank}(A) + \dim N(A) = n$$

For $A \in \mathbb{R}^{m \times n}$. Pivot columns count toward rank, free columns toward nullity — together they partition all $n$ columns.

## Video references

- ![3Blue1Brown - Linear combinations, span, and basis vectors | Chapter 2, Essence of linear algebra](https://www.youtube.com/watch?v=k7RM-ot2NWY)
- ![3Blue1Brown - Inverse matrices, column space and null space | Chapter 7, Essence of linear algebra](https://www.youtube.com/watch?v=uQhTuRlWMxw)
- ![3Blue1Brown - Abstract vector spaces | Chapter 16, Essence of linear algebra](https://www.youtube.com/watch?v=TgKwz5Ikpc8)

## See also

- [[Vectors]]
- [[Matrices]]
- [[Linear Transformations]]
- [[Systems of Linear Equations]]
- [[Orthogonality & Projections]]
- [[Index]]
