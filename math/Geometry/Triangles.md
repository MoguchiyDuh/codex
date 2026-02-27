---
tags:
  - math/geometry
  - triangles
related:
  - "[[Sine Rule]]"
  - "[[Cosine Rule]]"
  - "[[Trigonometry Basics]]"
  - "[[Vectors]]"
  - "[[00 - Geometry MOC]]"
---


## Basic Definitions

- **Triangle**: A polygon with 3 sides and 3 angles.
- **Vertices**: Points where two sides meet (A, B, C).
- **Sides**: Line segments connecting vertices (a, b, c), opposite their respective angles.
- **Interior Angles**: The three internal angles (∠A, ∠B, ∠C).

---

## Types of Triangles

### By Sides:

<img src="Pictures/triangle_types.png" width=300 height="auto" style="display: block; margin: auto">

### By Angles:

<img src="Pictures/triangle_types_angle.png" width=300 height="auto" style="display: block; margin: auto">

---

## Angle Properties
1. **Sum of Interior Angles**  
### $$\boxed{\angle A + \angle B + \angle C = 180^\circ}$$

2. **Exterior Angle Theorem**  
An exterior angle equals the sum of the two non-adjacent interior angles:  
### $$\boxed{\text{Exterior Angle} = \angle A + \angle B}$$

---

## Perimeter & Area #area #perimeter #formula

1. **Perimeter**  
### $$\boxed{P = a + b + c}$$

2. **Area Using Base and Height**  
### $$\boxed{A = \frac{1}{2} \cdot \text{base} \cdot \text{height}}$$

3. **Heron’s Formula**  
Let semi-perimeter:  
### $$\boxed{s = \frac{a + b + c}{2}}$$  
Then area is:  
### $$\boxed{A = \sqrt{s(s - a)(s - b)(s - c)}}$$

4. **Area Using Two Sides and Included Angle (SAS)**  
### $$\boxed{A = \frac{1}{2}ab\sin(C)}$$

5. **Area of an Equilateral Triangle**  
### $$\boxed{A = \frac{\sqrt{3}}{4} a^2}$$

---

## Pythagorean Theorem (Right Triangles)

For right triangle with hypotenuse $c$, and legs $a, b$:  
### $$\boxed{c^2 = a^2 + b^2}$$

---

## Special Right Triangles

| Triangle Type | Side Ratios | Notes |
|---------------|-------------|-------|
| **30°–60°–90°** | $1 : \sqrt{3} : 2$ | Opposite angles respectively |
| **45°–45°–90°** | $1 : 1 : \sqrt{2}$ | Isosceles right triangle |

---

## [[Sine Rule]]

---

## [[Cosine Rule]]

---

## Triangle Similarity Criteria

Two triangles are similar if they meet any of these:

| Rule | Description |
|------|-------------|
| **AA** | Two corresponding angles are equal |
| **SAS** | Two sides in proportion, included angle equal |
| **SSS** | All three sides in proportion |

Similar triangles have:
- Equal corresponding angles
- Proportional corresponding sides

---

## Triangle Congruence Criteria

Two triangles are congruent if they meet any of these:

| Rule | Description |
|------|-------------|
| **SSS** | All three sides equal |
| **SAS** | Two sides and included angle equal |
| **ASA** | Two angles and included side equal |
| **AAS** | Two angles and a non-included side equal |
| **HL** | Hypotenuse and leg equal in right triangles |

---

## Median, Altitude, and Angle Bisector

- **Median**: Segment from vertex to midpoint of opposite side
- **Altitude**: Perpendicular segment from vertex to opposite side
- **Angle Bisector**: Line dividing angle into two equal parts

---

## Centroid, Incenter, Circumcenter, Orthocenter

| Center | Definition | Property |
|--------|------------|----------|
| **Centroid** | Intersection of medians | Divides each median in ratio 2:1 |
| **Incenter** | Intersection of angle bisectors | Center of incircle (tangent to all sides) |
| **Circumcenter** | Intersection of perpendicular bisectors | Center of circumcircle (passes through all vertices) |
| **Orthocenter** | Intersection of altitudes | Lies inside for acute, on for right, outside for obtuse triangles |

<img src="Pictures/triangle_centers.svg" width=600 height="auto" style="display: block; margin: auto">

---

## Triangle Inequality Theorem

The sum of any two sides must be greater than the third:  
### $a + b > c,\quad b + c > a,\quad c + a > b$

---

## Area Using Coordinates (Shoelace Formula) #coordinates #formula

Given vertices at $(x_1, y_1), (x_2, y_2), (x_3, y_3)$:  
### $$\boxed{A = \frac{1}{2} \left| x_1y_2 + x_2y_3 + x_3y_1 - y_1x_2 - y_2x_3 - y_3x_1 \right|}$$

---

## Triangle-Circle Connections

These formulas relate a triangle to circles associated with it.

### Circumcircle (Circle around the triangle) #circumcircle #radius #formula

- **Definition**: Circle passing through all three vertices.
- **Circumradius (R)**:  
### $$\boxed{R = \frac{a}{2\sin A} = \frac{b}{2\sin B} = \frac{c}{2\sin C}}$$ 
Also:  
### $$\boxed{R = \frac{abc}{4A}}$$
where $A$ is the area of the triangle.

- **Circumcenter**: Intersection point of perpendicular bisectors of the sides.

---

### Incircle (Circle inside the triangle) #incircle #radius #formula

- **Definition**: Circle tangent to all three sides.
- **Inradius (r)**:  
### $$\boxed{r = \frac{A}{s}}$$  
where $A$ is the area, and $s$ is the semi-perimeter:  
### $$\boxed{s = \frac{a + b + c}{2}}$$

- **Incenter**: Intersection point of angle bisectors.


---

## See Also
- [[Sine Rule]] - Solving triangles with sine
- [[Cosine Rule]] - Solving triangles with cosine
- [[Trigonometry Basics]] - Trigonometric functions
- [[Vectors]] - Vector operations in geometry
- [[00 - Geometry MOC]] - Geometry topics overview
