---
tags: [math, trigonometry, sine-rule]
status: complete
---

# Sine Rule

> Relates each side of a triangle to the sine of its opposite angle.

## Formula

$$\boxed{\frac{a}{\sin(A)} = \frac{b}{\sin(B)} = \frac{c}{\sin(C)} = 2R}$$

Where $R$ is the circumradius (radius of the circumscribed circle).

## When to use

| Known | Find |
|---|---|
| Two angles + any side (AAS or ASA) | Remaining sides |
| Two sides + non-included angle (SSA) | Remaining angle — **check ambiguous case** |

## Ambiguous case (SSA)

When given two sides and a non-included angle, there may be **0, 1, or 2 valid triangles**:

Given sides $a$, $b$ and angle $A$ (opposite to $a$):

| Condition | Triangles |
|---|---|
| $a < b \sin(A)$ | 0 — no triangle exists |
| $a = b \sin(A)$ | 1 — right triangle |
| $b \sin(A) < a < b$ | 2 — two valid triangles |
| $a \geq b$ | 1 — unique triangle |

## Area using sine rule

$$\boxed{\text{Area} = \frac{1}{2}ab\sin(C) = \frac{1}{2}bc\sin(A) = \frac{1}{2}ac\sin(B)}$$

Also: $\text{Area} = \frac{abc}{4R}$

## See also

- [[Cosine Rule]]
- [[Trigonometry Basics]]
