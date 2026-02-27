---
tags: [math, trigonometry, basics]
status: complete
---

# Trigonometry Basics

> Core definitions, the unit circle, standard values, and function graphs.

## Right triangle definitions (SOH-CAH-TOA)

![[trig_basics.png]]

For a right triangle with angle θ, opposite side O, adjacent side A, hypotenuse H:

$$\sin(θ) = \frac{O}{H} \qquad \cos(θ) = \frac{A}{H} \qquad \tan(θ) = \frac{O}{A}$$

**SOH-CAH-TOA** — mnemonic for the above.

## Six trigonometric functions

| Function | Definition | Reciprocal of |
|---|---|---|
| $\sin(x)$ | $O/H$ | $\csc(x) = 1/\sin(x)$ |
| $\cos(x)$ | $A/H$ | $\sec(x) = 1/\cos(x)$ |
| $\tan(x)$ | $\sin(x)/\cos(x)$ | $\cot(x) = 1/\tan(x)$ |

## Degrees and radians

$$\text{radians} = \text{degrees} \times \frac{\pi}{180} \qquad \text{degrees} = \text{radians} \times \frac{180}{\pi}$$

Full circle: 360° = 2π rad. Right angle: 90° = π/2 rad.

## The unit circle

![[trig_circle.png]]

A circle of radius 1 centred at the origin. For any angle θ, the point on the circle is **(cos θ, sin θ)**.

## Signs by quadrant (CAST rule)

![[cast.png]]

| Quadrant | Angle range | Positive functions |
|---|---|---|
| I | 0° – 90° | All (sin, cos, tan) |
| II | 90° – 180° | Sin only |
| III | 180° – 270° | Tan only |
| IV | 270° – 360° | Cos only |

**CAST** — reading quadrants IV → I → II → III (or just remember All Students Take Calculus).

## Standard values

| Angle | $0°$ | $30°$ | $45°$ | $60°$ | $90°$ | $120°$ | $135°$ | $150°$ | $180°$ |
|---|---|---|---|---|---|---|---|---|---|
| Radians | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\frac{2\pi}{3}$ | $\frac{3\pi}{4}$ | $\frac{5\pi}{6}$ | $\pi$ |
| $\sin$ | $0$ | $\frac{1}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{3}}{2}$ | $1$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ | $0$ |
| $\cos$ | $1$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ | $0$ | $-\frac{1}{2}$ | $-\frac{\sqrt{2}}{2}$ | $-\frac{\sqrt{3}}{2}$ | $-1$ |
| $\tan$ | $0$ | $\frac{\sqrt{3}}{3}$ | $1$ | $\sqrt{3}$ | undef | $-\sqrt{3}$ | $-1$ | $-\frac{\sqrt{3}}{3}$ | $0$ |
| $\cot$ | undef | $\sqrt{3}$ | $1$ | $\frac{\sqrt{3}}{3}$ | $0$ | $-\frac{\sqrt{3}}{3}$ | $-1$ | $-\sqrt{3}$ | undef |

## Domain and range

| Function | Domain | Range | Period |
|---|---|---|---|
| $\sin(x)$ | $\mathbb{R}$ | $[-1, 1]$ | $2\pi$ |
| $\cos(x)$ | $\mathbb{R}$ | $[-1, 1]$ | $2\pi$ |
| $\tan(x)$ | $x \neq \frac{\pi}{2} + \pi k$ | $\mathbb{R}$ | $\pi$ |
| $\cot(x)$ | $x \neq \pi k$ | $\mathbb{R}$ | $\pi$ |
| $\sec(x)$ | $x \neq \frac{\pi}{2} + \pi k$ | $(-\infty,-1] \cup [1,\infty)$ | $2\pi$ |
| $\csc(x)$ | $x \neq \pi k$ | $(-\infty,-1] \cup [1,\infty)$ | $2\pi$ |

## Graphs

![[sin cos tan graphs.png]]

- **sin** and **cos**: amplitude 1, period 2π, cos is sin shifted left by π/2
- **tan**: vertical asymptotes at x = π/2 + πk, crosses zero at x = πk

## Co-function transformations

| Function | $\frac{\pi}{2} - x$ | $\frac{\pi}{2} + x$ | $\pi - x$ | $\pi + x$ | $\frac{3\pi}{2} - x$ | $\frac{3\pi}{2} + x$ | $2\pi - x$ | $2\pi + x$ |
|---|---|---|---|---|---|---|---|---|
| $\sin$ | $\cos(x)$ | $\cos(x)$ | $\sin(x)$ | $-\sin(x)$ | $-\cos(x)$ | $-\cos(x)$ | $-\sin(x)$ | $\sin(x)$ |
| $\cos$ | $\sin(x)$ | $-\sin(x)$ | $-\cos(x)$ | $-\cos(x)$ | $-\sin(x)$ | $\sin(x)$ | $\cos(x)$ | $\cos(x)$ |
| $\tan$ | $\cot(x)$ | $-\cot(x)$ | $-\tan(x)$ | $\tan(x)$ | $\cot(x)$ | $-\cot(x)$ | $-\tan(x)$ | $\tan(x)$ |
| $\cot$ | $\tan(x)$ | $-\tan(x)$ | $-\cot(x)$ | $\cot(x)$ | $\tan(x)$ | $-\tan(x)$ | $-\cot(x)$ | $\cot(x)$ |

## Euler's formula

$$\boxed{e^{ix} = \cos(x) + i\sin(x)}$$

Special case: $e^{i\pi} + 1 = 0$

## See also

- [[Trigonometric Identities]]
- [[Sine Rule]]
- [[Cosine Rule]]
