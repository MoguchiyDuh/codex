---
tags:
  - math
  - discrete
  - functions
status: complete
---

# Functions

> A function $f : A \to B$ assigns to each element of $A$ exactly one element of $B$.

---

## Terminology

| term          | definition                                                        |
| ------------- | ----------------------------------------------------------------- |
| **domain**    | the set $A$ — inputs                                              |
| **codomain**  | the set $B$ — declared output space                               |
| **range**     | $\{f(a) \mid a \in A\}$ — actual images; range $\subseteq$ codomain |
| **image**     | $b = f(a)$ — $b$ is the image of $a$                             |
| **pre-image** | $a$ is a pre-image of $b$ when $f(a) = b$                        |

---

## Function types

| type            | condition                                              | cardinality     |
| --------------- | ------------------------------------------------------ | --------------- |
| **Injective**   | $f(x) = f(y) \Rightarrow x = y$ (no two inputs share an output) | \|$A$\| $\leq$ \|$B$\| |
| **Surjective**  | $\forall b \in B,\ \exists a \in A : f(a) = b$ (every codomain element is hit) | \|$A$\| $\geq$ \|$B$\| |
| **Bijective**   | injective **and** surjective — perfect pairing, inverse exists | \|$A$\| $=$ \|$B$\| |

**Trap (finite sets):** $f : A \to A$ injective $\Leftrightarrow$ surjective. This equivalence breaks for infinite sets.

### Quick examples

| function                            | domain / codomain         | verdict                                              |
| ----------------------------------- | ------------------------- | ---------------------------------------------------- |
| $f(1)=c,\ f(2)=a,\ f(3)=c$        | $A=\{1,2,3\},\ B=\{a,b,c\}$ | neither — not injective ($f(1)=f(3)$), not surjective ($b$ uncovered) |
| $f(1)=c,\ f(2)=a,\ f(3)=b$        | same                      | bijective                                            |
| $g(x) = 2x - 1$                    | $\mathbb{Z} \to \mathbb{Z}$ | injective only                                       |
| $g(x) = x \bmod 3$                 | $\{0,\ldots,9\} \to \{0,1,2\}$ | surjective only                                 |

---

## Image of a subset

For $S \subseteq A$:

$$f(S) = \{f(x) \in B \mid x \in S\}$$

Example: $A = \{1,2,3\}$, $f(1)=c,\ f(2)=a,\ f(3)=c$

- $S = \{1,2\} \Rightarrow f(S) = \{a, c\}$
- $S = \{1,3\} \Rightarrow f(S) = \{c\}$

---

## Inverse functions

$f^{-1} : B \to A$ exists **only if $f$ is bijective**.

$$f^{-1}(b) = a \iff f(a) = b$$

Finding $f^{-1}$: write $y = f(x)$, solve for $x$, swap variable names.

$$f(x) = 2x - 1 \implies y = 2x-1 \implies x = \frac{y+1}{2} \implies f^{-1}(y) = \frac{y+1}{2}$$

Verify: $f(3) = 5,\quad f^{-1}(5) = 3\ \checkmark$

---

## Composition

$$f : A \to B,\quad g : B \to C \implies (g \circ f) : A \to C$$

$$(g \circ f)(x) = g(f(x))$$

Apply $f$ first, then $g$. **Order matters** — $g \circ f \neq f \circ g$ in general.

Example: $f(x) = 2x,\quad g(x) = x^2$

$$
(f \circ g)(x) = f(x^2) = 2x^2 \qquad
(g \circ f)(x) = g(2x) = 4x^2
$$

$2x^2 \neq 4x^2$ — composition is not commutative.


---

## See also

- [[Sets]]
- [[Logic & Proofs]]
- [[Combinatorics]]
