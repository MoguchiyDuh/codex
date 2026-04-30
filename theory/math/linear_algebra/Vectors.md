---
tags: [math, linear-algebra, vectors]
status: complete
---

# Vectors

> Quantities with magnitude and direction — the building blocks of linear algebra.

## Notation and representation

A vector in $\mathbb{R}^n$ is an ordered $n$-tuple of real numbers. Default form is the **column vector**:

$$\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix}, \qquad \mathbf{v}^T = \begin{bmatrix} v_1 & v_2 & \cdots & v_n \end{bmatrix}$$

The row vector $\mathbf{v}^T$ is the transpose. Column-vs-row matters for matrix products, not for the underlying geometric object.

### Geometric interpretation

In 2D/3D, a vector is an **arrow from the origin** to a point. Position is irrelevant — two arrows with the same length and direction are the same vector.

![[vector_2d_3d.png]]

## Operations

### Addition and subtraction

Component-wise, requires matching dimension:

$$\mathbf{u} + \mathbf{v} = \begin{bmatrix} u_1 + v_1 \\ \vdots \\ u_n + v_n \end{bmatrix}$$

Geometrically: **tip-to-tail** (parallelogram rule). Subtraction $\mathbf{u} - \mathbf{v}$ is the vector from $\mathbf{v}$'s tip to $\mathbf{u}$'s tip.

![[vector_addition.png]]

### Scalar multiplication

$$\alpha \mathbf{v} = \begin{bmatrix} \alpha v_1 \\ \vdots \\ \alpha v_n \end{bmatrix}$$

Stretches (|α| > 1), shrinks (|α| < 1), or flips direction (α < 0).

### Magnitude (norm)

The **Euclidean norm** measures length:

$$\|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2} = \sqrt{\mathbf{v} \cdot \mathbf{v}}$$

Properties: $\|\mathbf{v}\| \geq 0$, $\|\alpha \mathbf{v}\| = |\alpha|\,\|\mathbf{v}\|$, triangle inequality $\|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|$.

### Unit vector

Any non-zero vector divided by its magnitude:

$$\hat{\mathbf{v}} = \frac{\mathbf{v}}{\|\mathbf{v}\|}, \quad \|\hat{\mathbf{v}}\| = 1$$

Encodes pure direction. Standard basis vectors $\mathbf{e}_1, \mathbf{e}_2, \dots$ are unit vectors along each axis.

## Dot product

Also called scalar product or inner product.

### Algebraic definition

$$\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^{n} u_i v_i = u_1 v_1 + u_2 v_2 + \cdots + u_n v_n$$

Output is a scalar.

### Geometric definition

$$\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\|\,\|\mathbf{v}\| \cos \theta$$

Where $\theta$ is the angle between the two vectors.

### Angle and orthogonality

$$\cos \theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|\,\|\mathbf{v}\|}$$

| Dot product | Geometric meaning |
|-------------|-------------------|
| $> 0$ | Acute angle (pointing similar direction) |
| $= 0$ | **Orthogonal** (perpendicular) |
| $< 0$ | Obtuse angle (pointing opposite) |

### Projection

The projection of $\mathbf{u}$ onto $\mathbf{v}$:

$$\text{proj}_{\mathbf{v}} \mathbf{u} = \frac{\mathbf{u} \cdot \mathbf{v}}{\mathbf{v} \cdot \mathbf{v}} \mathbf{v}$$

The **scalar projection** (signed length of the shadow) is $\dfrac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|}$.

![[vector_projection.png]]

### Properties

| Property | Expression |
|----------|------------|
| Commutative | $\mathbf{u} \cdot \mathbf{v} = \mathbf{v} \cdot \mathbf{u}$ |
| Distributive | $\mathbf{u} \cdot (\mathbf{v} + \mathbf{w}) = \mathbf{u} \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{w}$ |
| Scalar | $(\alpha \mathbf{u}) \cdot \mathbf{v} = \alpha (\mathbf{u} \cdot \mathbf{v})$ |
| Self | $\mathbf{v} \cdot \mathbf{v} = \|\mathbf{v}\|^2$ |
| Cauchy-Schwarz | $|\mathbf{u} \cdot \mathbf{v}| \leq \|\mathbf{u}\|\,\|\mathbf{v}\|$ |

## Cross product (3D only)

Defined only in $\mathbb{R}^3$. Output is a **vector** perpendicular to both inputs.

$$\mathbf{u} \times \mathbf{v} = \begin{bmatrix} u_2 v_3 - u_3 v_2 \\ u_3 v_1 - u_1 v_3 \\ u_1 v_2 - u_2 v_1 \end{bmatrix}$$

Equivalently, as a symbolic determinant:

$$\mathbf{u} \times \mathbf{v} = \det \begin{bmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{bmatrix}$$

### Magnitude — parallelogram area

$$\|\mathbf{u} \times \mathbf{v}\| = \|\mathbf{u}\|\,\|\mathbf{v}\| \sin \theta$$

This equals the area of the parallelogram spanned by $\mathbf{u}$ and $\mathbf{v}$.

### Right-hand rule

Direction follows the right hand: fingers curl from $\mathbf{u}$ to $\mathbf{v}$, thumb points along $\mathbf{u} \times \mathbf{v}$.

![[right_hand_rule.png]]

### Properties

| Property | Expression |
|----------|------------|
| Anti-commutative | $\mathbf{u} \times \mathbf{v} = -(\mathbf{v} \times \mathbf{u})$ |
| Distributive | $\mathbf{u} \times (\mathbf{v} + \mathbf{w}) = \mathbf{u} \times \mathbf{v} + \mathbf{u} \times \mathbf{w}$ |
| Zero on parallel | $\mathbf{u} \times \mathbf{u} = \mathbf{0}$ |
| Non-associative | $(\mathbf{u} \times \mathbf{v}) \times \mathbf{w} \neq \mathbf{u} \times (\mathbf{v} \times \mathbf{w})$ |

## Linear combination and span

A **linear combination** of $\mathbf{v}_1, \dots, \mathbf{v}_k$ is any expression

$$\alpha_1 \mathbf{v}_1 + \alpha_2 \mathbf{v}_2 + \cdots + \alpha_k \mathbf{v}_k, \quad \alpha_i \in \mathbb{R}$$

The **span** is the set of all such combinations — geometrically, the smallest subspace containing those vectors (a line, plane, or higher). Full treatment in [[Vector Spaces]].

## Video references

- ![3Blue1Brown - Vectors | Chapter 1, Essence of linear algebra](https://www.youtube.com/watch?v=fNk_zzaMoSs)
- ![3Blue1Brown - Linear combinations, span, and basis vectors | Chapter 2, Essence of linear algebra](https://www.youtube.com/watch?v=k7RM-ot2NWY)
- ![3Blue1Brown - Dot products and duality | Chapter 9, Essence of linear algebra](https://www.youtube.com/watch?v=LyGKycYT2v0)
- ![3Blue1Brown - Cross products | Chapter 10, Essence of linear algebra](https://www.youtube.com/watch?v=eu6i7WJeinw)
- ![3Blue1Brown - Cross products in the light of linear transformations | Chapter 11, Essence of linear algebra](https://www.youtube.com/watch?v=BaM7OCEm3G0)

## See also

- [[Matrices]]
- [[Linear Transformations]]
- [[Vector Spaces]]
- [[../../theory/architecture/ALU|ALU]]
- [[Index]]
