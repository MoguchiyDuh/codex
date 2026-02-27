---
tags:
  - math/geometry
  - vectors
  - linear-algebra
related:
  - "[[Matrices]]"
  - "[[Trigonometry Basics]]"
  - "[[00 - Geometry MOC]]"
  - "[[00 - Math MOC]]"
---

## What is a Vector?

A **vector** is a mathematical object that has both **magnitude** (length) and **direction**.

### Examples:
- Displacement: `5 km East`
- Velocity: `20 m/s North`
- Force: `10 N at 30° above horizontal`

Vectors are often represented as:
### $$\vec{v} = \langle x, y \rangle \quad \text{or} \quad \vec{v} = \begin{bmatrix} x \\ y \end{bmatrix}$$

---

## Vector Operations

### 1. **Vector Addition**
Given:
### $$\vec{a} = \langle a_1, a_2 \rangle,\quad \vec{b} = \langle b_1, b_2 \rangle$$
Then:
### $$\boxed{\vec{a} + \vec{b} = \langle a_1 + b_1, a_2 + b_2 \rangle}$$

### 2. **Vector Subtraction**
### $$\boxed{\vec{a} - \vec{b} = \langle a_1 - b_1, a_2 - b_2 \rangle}$$

### 3. **Scalar Multiplication**
Multiply a vector by a scalar $k$:
### $$\boxed{k\vec{a} = \langle ka_1, ka_2 \rangle}$$

- Scales the vector’s magnitude.
- If $k < 0$, reverses the direction.

---

## Magnitude (Length) of a Vector

For a 2D vector $\vec{v} = \langle x, y \rangle$:
### $$\boxed{|\vec{v}| = \sqrt{x^2 + y^2}}$$

For a 3D vector $\vec{v} = \langle x, y, z \rangle$:
### $$\boxed{|\vec{v}| = \sqrt{x^2 + y^2 + z^2}}$$

---

## Unit Vector

To find the unit vector in the direction of $\vec{v}$:
### $$\boxed{\hat{v} = \frac{\vec{v}}{|\vec{v}|}}$$

---

## Components of a Vector

Any vector can be expressed in terms of its **horizontal** and **vertical** components:
### $$\vec{v} = v_x \hat{i} + v_y \hat{j}$$

Where:
- $\hat{i}$ = unit vector along x-axis
- $\hat{j}$ = unit vector along y-axis  
(And $\hat{k}$ for z-axis in 3D)

---

##  Direction Angle of a Vector (2D)

If $\vec{v} = \langle x, y \rangle$, then:
### $$\theta = \tan^{-1}\left(\frac{y}{x}\right)$$

---

## Dot Product

The dot product of two vectors:
### $$\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos(\theta)$$
Or component-wise:
### $$\vec{a} \cdot \vec{b} = a_x b_x + a_y b_y$$

### Properties:
- Commutative: $\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a}$
- Distributive over addition
- $\vec{a} \cdot \vec{a} = |\vec{a}|^2$

### Perpendicular Vectors:
### $$\vec{a} \perp \vec{b} \iff \vec{a} \cdot \vec{b} = 0$$

---

## Cross Product (3D Only)

$$
\vec{a} \times \vec{b} = 
\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
a_x & a_y & a_z \\
b_x & b_y & b_z \\
\end{vmatrix}
= \hat{i}(a_y b_z - a_z b_y) - \hat{j}(a_x b_z - a_z b_x) + \hat{k}(a_x b_y - a_y b_x)
$$

### Result:
- A vector perpendicular to both $\vec{a}$ and $\vec{b}$
- Direction follows the **Right-Hand Rule**

### Magnitude:
### $$|\vec{a} \times \vec{b}| = |\vec{a}||\vec{b}|\sin(\theta)$$

Useful for:
- Finding area of parallelogram: $A = |\vec{a} \times \vec{b}|$
- Torque, angular momentum, etc.


---

## See Also
- [[Matrices]] - Matrix operations in linear algebra
- [[Trigonometry Basics]] - Angles and trigonometric functions
- [[00 - Geometry MOC]] - Geometry topics overview
- [[00 - Math MOC]] - Mathematics overview
