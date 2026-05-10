---
tags: [math, discrete, number-theory, modular-arithmetic]
status: complete
---

# Number Theory

> The study of integers — divisibility, primes, and modular arithmetic — and the mathematical engine behind modern cryptography.

## Divisibility

For integers $a$ and $b$ with $b \neq 0$, we say $b$ **divides** $a$ (written $b \mid a$) if there exists an integer $k$ such that $a = kb$. Otherwise $b \nmid a$.

| Property           | Statement                                                                          |
| ------------------ | ---------------------------------------------------------------------------------- |
| Reflexive          | $a \mid a$                                                                         |
| Transitive         | $a \mid b$ and $b \mid c$ implies $a \mid c$                                       |
| Linear combination | $a \mid b$ and $a \mid c$ implies $a \mid (sb + tc)$ for any $s, t \in \mathbb{Z}$ |

The linear combination property is the workhorse — most divisibility proofs reduce to it.

### Division algorithm

For any $a \in \mathbb{Z}$ and $d \in \mathbb{Z}^+$ there exist **unique** $q, r \in \mathbb{Z}$ with $0 \leq r < d$ such that

$$a = qd + r.$$

$q$ is the **quotient** and $r$ is the **remainder**. In most languages: `q = a // d`, `r = a % d`.

**Example.** $a = 47$, $d = 5$: $47 = 9 \cdot 5 + 2$, so $q = 9$, $r = 2$.

## Greatest common divisor

The **gcd** of $a$ and $b$, written $\gcd(a, b)$, is the largest positive integer dividing both. By convention $\gcd(a, 0) = a$.

### Euclid's algorithm

Based on the key identity $\gcd(a, b) = \gcd(b,\, a \bmod b)$:

```pseudo
gcd(a, b):
    while b ≠ 0:
        a, b = b, a mod b
    return a
```

**Example.** $\gcd(252, 198)$:

$$252 = 1 \cdot 198 + 54 \implies \gcd(252,198) = \gcd(198,54)$$
$$198 = 3 \cdot 54 + 36 \implies \gcd(198,54) = \gcd(54,36)$$
$$54 = 1 \cdot 36 + 18 \implies \gcd(54,36) = \gcd(36,18)$$
$$36 = 2 \cdot 18 + 0 \implies \gcd(36,18) = 18$$

**Correctness.** At each step $\gcd(a,b) = \gcd(b, a \bmod b)$ because any common divisor of $a$ and $b$ also divides $a \bmod b = a - qb$, and vice versa. The algorithm terminates because $a \bmod b < b$ strictly, so the second argument decreases each step.

**Complexity.** $O(\log \min(a,b))$ steps — the Fibonacci numbers are the worst case, requiring the most iterations for their size.

### Bezout's identity

For any integers $a$ and $b$, not both zero:

$$\gcd(a, b) = sa + tb \quad \text{for some } s, t \in \mathbb{Z}.$$

The coefficients $s$ and $t$ are found by running the **extended Euclidean algorithm** — substituting remainders back through the gcd computation.

**Example.** From above, back-substituting through $\gcd(252, 198) = 18$:

$$18 = 54 - 1 \cdot 36 = 54 - 1 \cdot (198 - 3 \cdot 54) = 4 \cdot 54 - 1 \cdot 198 = 4(252 - 198) - 198 = 4 \cdot 252 - 5 \cdot 198.$$

So $s = 4$, $t = -5$: $\gcd(252,198) = 4 \cdot 252 + (-5) \cdot 198 = 18$.

Bezout's identity is the key tool for proving properties of modular inverses and solving linear Diophantine equations.

### Relative primality

$a$ and $b$ are **relatively prime** (or **coprime**) if $\gcd(a,b) = 1$. Bezout then gives $sa + tb = 1$ for some integers $s, t$ — this is used repeatedly in modular arithmetic proofs.

## Primes

An integer $p \geq 2$ is **prime** if its only positive divisors are $1$ and $p$. Otherwise $p \geq 2$ is **composite**.

**Fundamental theorem of arithmetic.** Every integer $n \geq 2$ has a unique factorisation into primes (up to order). Existence was proved by strong induction in [[Induction]]; uniqueness follows from the lemma that if $p \mid ab$ and $p$ is prime then $p \mid a$ or $p \mid b$.

**Infinitude of primes.** Suppose there are finitely many primes $p_1, \ldots, p_k$. Let $N = p_1 p_2 \cdots p_k + 1$. Then $N$ is not divisible by any $p_i$ (remainder $1$ in each case), so $N$ has a prime factor not in the list — contradiction.

## Modular arithmetic

Fix a positive integer $m$ called the **modulus**. Write $a \equiv b \pmod{m}$ (read "$a$ is congruent to $b$ mod $m$") if $m \mid (a - b)$, equivalently if $a$ and $b$ have the same remainder when divided by $m$.

![[modular_clock.png]]

Congruence mod $m$ is an equivalence relation (see [[Relations]]). The **residue classes** $\{0, 1, \ldots, m-1\}$ form $\mathbb{Z}_m$, the integers mod $m$.

### Arithmetic rules

If $a \equiv a' \pmod{m}$ and $b \equiv b' \pmod{m}$ then:

$$a + b \equiv a' + b' \pmod{m}$$
$$a \cdot b \equiv a' \cdot b' \pmod{m}$$

This makes $\mathbb{Z}_m$ a proper algebraic structure — addition and multiplication are well-defined on residue classes.

**Example.** $7 \equiv 2 \pmod{5}$ and $11 \equiv 1 \pmod{5}$, so $7 \cdot 11 = 77 \equiv 2 \cdot 1 = 2 \pmod{5}$. Check: $77 = 15 \cdot 5 + 2$. ✓

### Modular inverse

The **modular inverse** of $a$ mod $m$ is an integer $a^{-1}$ such that $a \cdot a^{-1} \equiv 1 \pmod{m}$.

An inverse exists if and only if $\gcd(a, m) = 1$. When it exists, it is found via Bezout: from $sa + tm = 1$ take $a^{-1} \equiv s \pmod{m}$.

**Example.** Find $3^{-1} \pmod{7}$. Extended Euclidean on $\gcd(3,7)$: $7 = 2 \cdot 3 + 1$, so $1 = 7 - 2 \cdot 3$, giving $s = -2 \equiv 5 \pmod{7}$. Check: $3 \cdot 5 = 15 \equiv 1 \pmod{7}$. ✓

Modular inverses are the discrete analogue of division — used wherever you need to "divide" in $\mathbb{Z}_m$.

## Fermat's little theorem

If $p$ is prime and $\gcd(a, p) = 1$ then

$$a^{p-1} \equiv 1 \pmod{p}.$$

Equivalently, $a^p \equiv a \pmod{p}$ for any $a$.

**Proof sketch.** Consider the $p-1$ non-zero residues $\{1, 2, \ldots, p-1\}$. Multiplication by $a$ permutes them (since $\gcd(a,p) = 1$ means $ax \equiv ay \pmod p$ implies $x \equiv y$). So $a \cdot 2a \cdot 3a \cdots (p-1)a \equiv 1 \cdot 2 \cdots (p-1) \pmod{p}$, i.e. $a^{p-1}(p-1)! \equiv (p-1)! \pmod{p}$. Dividing both sides by $(p-1)!$ (valid since $\gcd((p-1)!, p) = 1$) gives $a^{p-1} \equiv 1$.

**Application — fast exponentiation.** To compute $a^k \bmod p$, reduce the exponent mod $p-1$: $a^k \equiv a^{k \bmod (p-1)} \pmod{p}$.

## Euler's theorem

Fermat's theorem generalises to composite moduli. Define Euler's **totient function** $\phi(m)$ as the count of integers in $\{1, \ldots, m\}$ coprime to $m$.

For prime $p$: $\phi(p) = p - 1$ (all non-zero residues are coprime to $p$).

**Euler's theorem.** If $\gcd(a, m) = 1$ then $a^{\phi(m)} \equiv 1 \pmod{m}$.

Fermat is the special case $m = p$ prime.

## RSA cryptography

RSA is the direct CS application of the number theory above. Key generation:

1. Choose large distinct primes $p$ and $q$. Let $n = pq$.
2. Compute $\phi(n) = (p-1)(q-1)$.
3. Choose $e$ with $1 < e < \phi(n)$ and $\gcd(e, \phi(n)) = 1$ (the **public exponent**, commonly $e = 65537$).
4. Find $d \equiv e^{-1} \pmod{\phi(n)}$ via extended Euclidean (the **private exponent**).

**Encryption.** $c \equiv m^e \pmod{n}$.

**Decryption.** $m \equiv c^d \pmod{n}$.

**Why it works.** $c^d \equiv m^{ed} \pmod{n}$. Since $ed \equiv 1 \pmod{\phi(n)}$, we have $ed = 1 + k\phi(n)$ for some $k$, so $m^{ed} = m \cdot (m^{\phi(n)})^k \equiv m \cdot 1^k = m \pmod{n}$ by Euler's theorem (when $\gcd(m, n) = 1$).

**Security** rests on the hardness of factoring $n$ — given $n = pq$ it is computationally infeasible to recover $p$ and $q$ for large primes, and without $p$ and $q$ you cannot compute $\phi(n)$ or $d$.

## Chinese remainder theorem

If $m_1, m_2, \ldots, m_k$ are pairwise coprime, the system

$$x \equiv a_1 \pmod{m_1},\quad x \equiv a_2 \pmod{m_2},\quad \ldots,\quad x \equiv a_k \pmod{m_k}$$

has a unique solution modulo $M = m_1 m_2 \cdots m_k$.

The CRT lets you split computation mod $M$ into smaller independent computations mod each $m_i$ — useful in efficient arithmetic and in some distributed computing schemes.

## Video references

- ![Lecture 4: Number Theory I](https://www.youtube.com/watch?v=NuY7szYSXSw)
- ![Lecture 5: Number Theory II](https://www.youtube.com/watch?v=XX7ePR21Ook)

## See also

- [[Induction]]
- [[Relations]]
- [[Counting]]
- [[Index]]
