---
tags: [math, discrete, functions, cardinality]
status: complete
---

# Functions

> A function is a relation that assigns exactly one output to every input — the formal backbone of computation itself.

## Definition

A **function** $f : A \to B$ is a relation from $A$ to $B$ such that every element of $A$ is related to exactly one element of $B$.

- $A$ is the **domain**, $B$ is the **codomain**.
- $f(a)$ denotes the unique element of $B$ that $a$ maps to.
- The **image** (or range) is $\text{Im}(f) = \{f(a) \mid a \in A\} \subseteq B$.

The codomain and image are distinct: $B$ is what $f$ is allowed to output; $\text{Im}(f)$ is what it actually outputs.

**Example.** $f : \mathbb{Z} \to \mathbb{Z}$, $f(n) = n^2$. Domain $= \mathbb{Z}$, codomain $= \mathbb{Z}$, image $= \{0, 1, 4, 9, \ldots\} \subsetneq \mathbb{Z}$.

## Injectivity, surjectivity, bijectivity

| Property                   | Definition                                       | Informal                      |
| -------------------------- | ------------------------------------------------ | ----------------------------- |
| **Injective** (one-to-one) | $f(a) = f(b) \implies a = b$                     | no two inputs share an output |
| **Surjective** (onto)      | $\forall b \in B,\; \exists a \in A,\; f(a) = b$ | every codomain element is hit |
| **Bijective**              | injective and surjective                         | perfect pairing               |

![[function_types.png]]

**Testing injectivity.** Assume $f(a) = f(b)$ and derive $a = b$ — a direct proof in the domain.

**Testing surjectivity.** Take arbitrary $b \in B$; find (construct) an $a \in A$ with $f(a) = b$.

**Examples on $f : \mathbb{R} \to \mathbb{R}$:**

| Function     | Injective?          | Surjective?                 |
| ------------ | ------------------- | --------------------------- |
| $f(x) = 2x$  | Yes                 | Yes (bijective)             |
| $f(x) = x^2$ | No ($f(1) = f(-1)$) | No (no $x$ with $x^2 = -1$) |
| $f(x) = e^x$ | Yes                 | No (image $= \mathbb{R}^+$) |
| $f(x) = x^3$ | Yes                 | Yes (bijective)             |

## Composition and inverse

**Composition.** $(g \circ f)(x) = g(f(x))$. Requires $\text{Im}(f) \subseteq \text{dom}(g)$. Composition is associative but not commutative.

**Inverse.** $f : A \to B$ has an inverse $f^{-1} : B \to A$ satisfying $f^{-1}(f(a)) = a$ and $f(f^{-1}(b)) = b$ if and only if $f$ is bijective.

When $f$ is bijective, $f^{-1}$ is also bijective. Bijectivity is the exact condition for "undoing" a function to be well-defined.

## Functions and cardinality

Bijections provide the rigorous definition of "same size" for infinite sets.

**Same cardinality.** $|A| = |B|$ iff there exists a bijection $f : A \to B$.

**$A$ is no larger than $B$.** $|A| \leq |B|$ iff there exists an injection $f : A \to B$.

This definition makes surprising equalities precise:

**Claim.** $|\mathbb{N}| = |\mathbb{Z}|$.

**Proof.** Define $f : \mathbb{N} \to \mathbb{Z}$ by

$$f(n) = \begin{cases} n/2 & n \text{ even} \\ -(n+1)/2 & n \text{ odd} \end{cases}$$

This maps $0 \mapsto 0,\; 1 \mapsto -1,\; 2 \mapsto 1,\; 3 \mapsto -2,\; 4 \mapsto 2, \ldots$ and is a bijection.

**Claim.** $|\mathbb{N} \times \mathbb{N}| = |\mathbb{N}|$.

**Proof.** The Cantor pairing function $f(m, n) = \frac{(m+n)(m+n+1)}{2} + m$ is a bijection $\mathbb{N} \times \mathbb{N} \to \mathbb{N}$. Geometrically it traverses $\mathbb{N} \times \mathbb{N}$ along diagonals.

![[cantor_pairing.png]]

**Claim.** $|\mathbb{R}| > |\mathbb{N}|$ — the reals are uncountable.

**Proof (Cantor's diagonal argument).** Suppose $f : \mathbb{N} \to [0, 1)$ is a surjection. Write each $f(n)$ in decimal. Construct $d$ whose $n$-th decimal digit differs from the $n$-th digit of $f(n)$. Then $d \neq f(n)$ for every $n$ — so $d$ is not in the image of $f$, contradicting surjectivity.

## Pigeonhole principle (function view)

If $f : A \to B$ is a function and $|A| > |B|$, then $f$ is not injective — some element of $B$ has at least two pre-images.

This is the function-theoretic form of the pigeonhole principle, proved fully in [[Counting]]. The argument: if every element of $B$ had at most one pre-image, $|\text{Im}(f)| \leq |B| < |A|$, so $f$ could not be injective.

## Floor, ceiling, and standard functions

| Notation            | Definition                                      |
| ------------------- | ----------------------------------------------- |
| $\lfloor x \rfloor$ | largest integer $\leq x$                        |
| $\lceil x \rceil$   | smallest integer $\geq x$                       |
| $\log_b x$          | exponent to which $b$ must be raised to get $x$ |

These appear throughout algorithm analysis and counting arguments. Note $\lfloor x \rfloor$ and $\lceil x \rceil$ are functions $\mathbb{R} \to \mathbb{Z}$; neither is injective (many reals share the same floor).

## See also

- [[Sets]]
- [[Relations]]
- [[Counting]]
- [[../linear_algebra/Linear Transformations|Linear Transformations]]
- [[Index]]
