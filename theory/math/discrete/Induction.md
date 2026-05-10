---
tags: [math, discrete, induction, proofs]
status: complete
---

# Induction

> A proof technique for universal claims over the natural numbers — and the foundation for reasoning about recursive programs.

## Ordinary induction

To prove $\forall n \geq 0,\; P(n)$:

1. **Base case.** Prove $P(0)$.
2. **Inductive step.** Assume $P(n)$ (the **inductive hypothesis**); prove $P(n+1)$.

The structure works like dominoes: proving the base case stands the first one up; proving the inductive step guarantees each one knocks over the next.

![[induction_dominoes.png]]

**Claim.** For all $n \geq 0$,

$$\sum_{i=0}^{n} i = \frac{n(n+1)}{2}.$$

**Proof.**

_Base case ($n = 0$)._ $\sum_{i=0}^{0} i = 0 = \frac{0 \cdot 1}{2}$. ✓

_Inductive step._ Assume $\sum_{i=0}^{n} i = \frac{n(n+1)}{2}$. Then

$$\sum_{i=0}^{n+1} i = \left(\sum_{i=0}^{n} i\right) + (n+1) = \frac{n(n+1)}{2} + (n+1) = (n+1)\!\left(\frac{n}{2} + 1\right) = \frac{(n+1)(n+2)}{2}.$$

### Pitfall — not establishing a true base case

A faulty inductive step that works vacuously can prove false statements unless the base case is actually checked. The classic "all horses are the same colour" fallacy has a correct inductive step but a broken base case at $n = 1 \to 2$. Always verify the base case explicitly.

## Strong induction

The inductive hypothesis is strengthened: assume $P(k)$ holds for **all** $k \leq n$, then prove $P(n+1)$.

Ordinary induction is the special case where only $P(n)$ is needed. Use strong induction when $P(n+1)$ depends on more than just the immediately preceding step.

**Claim.** Every integer $n \geq 2$ is a product of primes.

**Proof.**

_Base case ($n = 2$)._ $2$ is prime, hence trivially a product of one prime. ✓

_Inductive step._ Assume every integer $2 \leq k \leq n$ is a product of primes. Consider $n+1$.

- If $n+1$ is prime: done.
- If $n+1$ is composite: $n+1 = ab$ with $2 \leq a, b \leq n$. By the strong inductive hypothesis both $a$ and $b$ are products of primes, so $n+1$ is too.

This proof uses both branches of the strong hypothesis — it could not be done with ordinary induction, which only gives $P(n)$.

## Structural induction

Induction over a **recursively defined structure** (list, tree, expression, string) rather than over $\mathbb{N}$ directly.

Schema:

1. **Base case.** Prove $P$ holds for every base-case structure.
2. **Inductive step.** Assume $P$ holds for all sub-structures (the **structural inductive hypothesis**); prove $P$ holds for any structure built from them.

**Example — binary trees.** Define binary trees recursively: a leaf is a binary tree; if $L$ and $R$ are binary trees then $\text{Node}(L, R)$ is a binary tree.

**Claim.** A binary tree with $n$ internal nodes has exactly $n + 1$ leaves.

**Proof.**

_Base case._ A leaf has $0$ internal nodes and $1$ leaf. $0 + 1 = 1$. ✓

_Inductive step._ Let $T = \text{Node}(L, R)$. By the structural hypothesis, $L$ has $\ell_1$ internal nodes and $\ell_1 + 1$ leaves; $R$ has $\ell_2$ internal nodes and $\ell_2 + 1$ leaves. Then $T$ has $\ell_1 + \ell_2 + 1$ internal nodes (the two subtrees' internal nodes plus the root) and $(\ell_1 + 1) + (\ell_2 + 1) = \ell_1 + \ell_2 + 2 = (\ell_1 + \ell_2 + 1) + 1$ leaves.

![[binary_tree_induction.png]]

Structural induction is the mathematical backbone of every recursive program's correctness proof.

## Invariants

An **invariant** is a predicate that is true before and after every step of a process. Proving an invariant holds is exactly an induction on the number of steps.

The pattern:

1. **Establish.** Prove the invariant holds at the start (base case).
2. **Maintain.** Prove that if the invariant holds before a step it holds after (inductive step).
3. **Exploit.** Draw a conclusion from the invariant holding at the end.

**Example — die game.** Start with $n$ coins in a pile. A move splits one pile into two non-empty piles. Each move scores $ab$ points where $a$ and $b$ are the sizes of the new piles. Claim: no matter how you split, the final score is always $\binom{n}{2}$.

**Proof by invariant.** Let the invariant be: if the piles currently have sizes $x_1, x_2, \ldots, x_k$, the score so far plus $\sum_i \binom{x_i}{2}$ always equals $\binom{n}{2}$.

_Establish._ Initially one pile of size $n$: score $= 0$, $\binom{n}{2}$ added. Sum $= \binom{n}{2}$. ✓

_Maintain._ Splitting a pile of size $x$ into $a$ and $b$ adds $ab$ to the score and replaces $\binom{x}{2}$ with $\binom{a}{2} + \binom{b}{2}$. Since $ab = \binom{x}{2} - \binom{a}{2} - \binom{b}{2}$ (verify algebraically: $\frac{x(x-1)}{2} - \frac{a(a-1)}{2} - \frac{b(b-1)}{2} = ab$ when $x = a + b$), the invariant sum is unchanged. ✓

_Exploit._ At the end every pile has size $1$ and $\binom{1}{2} = 0$, so the score equals $\binom{n}{2}$.

This is the CS payoff of invariants: the same technique proves loop correctness, protocol safety, and compiler transformation soundness.

## Induction and recursion

Every recursive program has a corresponding induction structure. If `f(n)` calls `f(n-1)`, the correctness proof is ordinary induction. If `f(n)` calls `f(k)` for arbitrary $k < n$, use strong induction. If the recursion is over a data structure, use structural induction.

**Example.** Prove `sum(n) = n*(n+1)//2` correct for the recursive definition `sum(0) = 0`, `sum(n) = n + sum(n-1)`.

_Base case._ `sum(0) = 0 = 0*1//2`. ✓

_Inductive step._ Assume `sum(n-1) = (n-1)*n//2`. Then `sum(n) = n + sum(n-1) = n + (n-1)*n//2 = n*(n+1)//2`.

## Well-ordering and induction equivalence

Ordinary induction, strong induction, and the well-ordering principle are all equivalent — each implies the others. The choice between them is one of proof convenience:

| Technique            | Best when                                                               |
| -------------------- | ----------------------------------------------------------------------- |
| Ordinary induction   | $P(n+1)$ follows cleanly from $P(n)$ alone                              |
| Strong induction     | $P(n+1)$ depends on several or all earlier values                       |
| Well-ordering        | Easiest to set up a proof by contradiction via a minimal counterexample |
| Structural induction | The domain is a recursively defined structure                           |

## Video references

- ![Lecture 2: Induction](https://www.youtube.com/watch?v=z8HKWUWS-lA)
- ![Lecture 3: Strong Induction](https://www.youtube.com/watch?v=NuGDkmwEObM)

## See also

- [[Logic & Proofs]]
- [[Number Theory]]
- [[State Machines]]
- [[Index]]
