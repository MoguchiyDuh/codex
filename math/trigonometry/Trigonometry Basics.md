---
tags: [math, trigonometry, basics]
status: complete
---
# Trigonometry Basics

> Core trigonometric functions, standard values, co-function transformations, and Euler's formula.

## Notation

| Symbol | Meaning |
|---|---|
| $\sin(x)$ | Sine of angle $x$ |
| $\cos(x)$ | Cosine of angle $x$ |
| $\tan(x)$ | Tangent — $\tan(x) = \frac{\sin(x)}{\cos(x)}$ |
| $\cot(x)$ | Cotangent — $\cot(x) = \frac{\cos(x)}{\sin(x)}$ |
| $\pi$ | Pi ($\pi \approx 3.14159$), ratio of circumference to diameter |

## Standard Values (0° to 180°)

| Angle | $0°$ | $30°$ | $45°$ | $60°$ | $90°$ | $120°$ | $135°$ | $150°$ | $180°$ |
|---|---|---|---|---|---|---|---|---|---|
| Radians | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\frac{2\pi}{3}$ | $\frac{3\pi}{4}$ | $\frac{5\pi}{6}$ | $\pi$ |
| $\sin(x)$ | $0$ | $\frac{1}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{3}}{2}$ | $1$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ | $0$ |
| $\cos(x)$ | $1$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ | $0$ | $-\frac{1}{2}$ | $-\frac{\sqrt{2}}{2}$ | $-\frac{\sqrt{3}}{2}$ | $-1$ |
| $\tan(x)$ | $0$ | $\frac{\sqrt{3}}{3}$ | $1$ | $\sqrt{3}$ | undef | $-\sqrt{3}$ | $-1$ | $-\frac{\sqrt{3}}{3}$ | $0$ |
| $\cot(x)$ | undef | $\sqrt{3}$ | $1$ | $\frac{\sqrt{3}}{3}$ | $0$ | $-\frac{\sqrt{3}}{3}$ | $-1$ | $-\sqrt{3}$ | undef |

## Co-Function Transformations

| Function | $\frac{\pi}{2} - x$ | $\frac{\pi}{2} + x$ | $\pi - x$ | $\pi + x$ | $\frac{3\pi}{2} - x$ | $\frac{3\pi}{2} + x$ | $2\pi - x$ | $2\pi + x$ |
|---|---|---|---|---|---|---|---|---|
| $\sin$ | $\cos(x)$ | $\cos(x)$ | $\sin(x)$ | $-\sin(x)$ | $-\cos(x)$ | $-\cos(x)$ | $-\sin(x)$ | $\sin(x)$ |
| $\cos$ | $\sin(x)$ | $-\sin(x)$ | $-\cos(x)$ | $-\cos(x)$ | $-\sin(x)$ | $\sin(x)$ | $\cos(x)$ | $\cos(x)$ |
| $\tan$ | $\cot(x)$ | $-\cot(x)$ | $-\tan(x)$ | $\tan(x)$ | $\cot(x)$ | $-\cot(x)$ | $-\tan(x)$ | $\tan(x)$ |
| $\cot$ | $\tan(x)$ | $-\tan(x)$ | $-\cot(x)$ | $\cot(x)$ | $\tan(x)$ | $-\tan(x)$ | $-\cot(x)$ | $\cot(x)$ |

## Euler's Formula

$$\boxed{e^{ix} = \cos(x) + i \cdot \sin(x)}$$

## See also

- [[Trigonometric Identities]]
- [[Sine Rule]]
- [[Cosine Rule]]
