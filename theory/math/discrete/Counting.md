---
tags: [math, discrete, counting, combinatorics, permutations, combinations]
status: complete
---

# Counting

> Counting is not arithmetic — it is a proof technique. The rules below are theorems, and every formula follows from them.

## The four basic rules

### Sum rule

If $A$ and $B$ are disjoint finite sets, $|A \cup B| = |A| + |B|$.

More generally, if $A_1, A_2, \ldots, A_k$ are pairwise disjoint:

$$|A_1 \cup A_2 \cup \cdots \cup A_k| = |A_1| + |A_2| + \cdots + |A_k|.$$

**Use it when** the thing being counted splits into non-overlapping cases.

### Product rule

If $A$ and $B$ are finite sets, $|A \times B| = |A| \cdot |B|$.

More generally: $|A_1 \times A_2 \times \cdots \times A_k| = |A_1| \cdot |A_2| \cdots |A_k|$.

**Use it when** a choice is made in independent stages — the total count is the product of per-stage counts.

**Example.** How many 8-character passwords use uppercase letters and digits? $36^8$. Each of 8 positions independently chooses from 36 symbols.

### Bijection rule

If $f : A \to B$ is a bijection then $|A| = |B|$.

**Use it when** you want to count $A$ but $B$ is easier to count — exhibit a bijection to transfer the count. This is the most powerful technique and underlies the proofs of the permutation and combination formulas.

### Division rule

If $f : A \to B$ is a $k$-to-$1$ function (every element of $B$ has exactly $k$ pre-images), then $|A| = k \cdot |B|$, i.e. $|B| = |A| / k$.

**Use it when** a construction overcounts by a fixed factor — divide out the overcount.

**Example.** How many ways to seat $n$ people around a circular table? Arrange them in a line: $n!$ ways. But each circular seating corresponds to $n$ linear arrangements (rotations). By the division rule: $n! / n = (n-1)!$.

## Permutations

A **permutation** of $n$ distinct objects is an ordered arrangement of all $n$. There are $n!$ permutations.

**Proof via product rule.** $n$ choices for position 1, $n-1$ for position 2, …, $1$ for position $n$: $n \cdot (n-1) \cdots 1 = n!$.

A **$k$-permutation** is an ordered selection of $k$ objects from $n$ (without repetition):

$$P(n, k) = \frac{n!}{(n-k)!} = n(n-1)\cdots(n-k+1).$$

**Example.** How many ways to award gold, silver, bronze from 10 athletes? $P(10,3) = 10 \cdot 9 \cdot 8 = 720$. Order matters (gold $\neq$ silver).

### Permutations with identical objects

If $n$ objects have $n_1$ identical objects of type 1, $n_2$ of type 2, …, $n_k$ of type $k$ (with $n_1 + \cdots + n_k = n$), the number of distinct arrangements is

$$\frac{n!}{n_1!\, n_2!\, \cdots\, n_k!}.$$

**Proof.** Arrange all $n$ objects as if they were distinct: $n!$ ways. Each distinct arrangement is counted $n_1! \cdot n_2! \cdots n_k!$ times (the ways to permute identical objects among themselves). Divide by this overcount.

**Example.** Arrangements of MISSISSIPPI: $11$ letters, M×1, I×4, S×4, P×2.

$$\frac{11!}{1!\,4!\,4!\,2!} = \frac{39{,}916{,}800}{1 \cdot 24 \cdot 24 \cdot 2} = 34{,}650.$$

## Combinations

A **combination** is an unordered selection of $k$ objects from $n$. The binomial coefficient:

$$\binom{n}{k} = \frac{n!}{k!\,(n-k)!}.$$

**Proof via bijection + division.** Count ordered $k$-selections: $P(n,k) = n!/(n-k)!$. Each unordered selection corresponds to exactly $k!$ ordered ones (the permutations of the chosen $k$). By the division rule:

$$\binom{n}{k} = \frac{P(n,k)}{k!} = \frac{n!}{k!\,(n-k)!}.$$

**Example.** A committee of 3 from 10 people: $\binom{10}{3} = 120$. Order does not matter (unlike the medal example above).

### Key identities

| Identity          | Formula                                                      | Proof idea                                                                        |
| ----------------- | ------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| Symmetry          | $\binom{n}{k} = \binom{n}{n-k}$                              | choosing $k$ to include = choosing $n-k$ to exclude                               |
| Pascal's identity | $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$           | fix element $x$: either include it ($\binom{n-1}{k-1}$) or not ($\binom{n-1}{k}$) |
| Row sum           | $\sum_{k=0}^{n} \binom{n}{k} = 2^n$                          | each subset of $\{1,\ldots,n\}$ is counted once                                   |
| Vandermonde       | $\sum_{k=0}^{r} \binom{m}{k}\binom{n}{r-k} = \binom{m+n}{r}$ | count $r$-subsets of an $(m+n)$-set by split                                      |

Pascal's identity gives Pascal's triangle row by row: each interior entry is the sum of the two above it.

![[pascals_triangle.png]]

## Binomial theorem

$$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k.$$

**Proof by counting.** Expand $(a+b)^n$ as a product of $n$ factors $(a+b)(a+b)\cdots(a+b)$. Each term in the expansion is formed by choosing $a$ or $b$ from each factor. A term with exactly $k$ copies of $b$ (and $n-k$ copies of $a$) is $a^{n-k}b^k$. The number of ways to choose which $k$ factors contribute $b$ is $\binom{n}{k}$. Summing over $k$ gives the formula.

**Special cases:**

| Substitution      | Result                                      |
| ----------------- | ------------------------------------------- |
| $a = b = 1$       | $\sum_{k=0}^{n} \binom{n}{k} = 2^n$         |
| $a = 1,\, b = -1$ | $\sum_{k=0}^{n} (-1)^k \binom{n}{k} = 0$    |
| $a = 1,\, b = x$  | $(1+x)^n = \sum_{k=0}^{n} \binom{n}{k} x^k$ |

**Example.** Coefficient of $x^3$ in $(2x + 3)^7$: term with $k=3$ is $\binom{7}{3}(2x)^4 \cdot 3^3 = 35 \cdot 16x^4 \cdot 27$. Wait — we want $x^3$, so $k=3$ gives $(2x)^3 \cdot 3^4 \cdot \binom{7}{3}$... restructure: $(a+b)^7$ with $a = 3$, $b = 2x$. Term $k=3$: $\binom{7}{3} \cdot 3^4 \cdot (2x)^3 = 35 \cdot 81 \cdot 8x^3 = 22{,}680\, x^3$.

## Multinomial theorem

Generalises the binomial theorem to $r$ terms:

$$(x_1 + x_2 + \cdots + x_r)^n = \sum_{\substack{k_1+k_2+\cdots+k_r=n \\ k_i \geq 0}} \binom{n}{k_1,\, k_2,\, \ldots,\, k_r}\, x_1^{k_1} x_2^{k_2} \cdots x_r^{k_r},$$

where the **multinomial coefficient** is

$$\binom{n}{k_1, k_2, \ldots, k_r} = \frac{n!}{k_1!\, k_2!\, \cdots\, k_r!}.$$

This is exactly the "identical objects" formula — the multinomial coefficient counts the number of ways to arrange $n$ objects with $k_i$ of type $i$.

## Stars and bars

The number of ways to place $n$ indistinguishable balls into $k$ distinguishable bins (allowing empty bins) is

$$\binom{n + k - 1}{k - 1}.$$

**Proof.** Represent any distribution as a sequence of $n$ stars and $k-1$ bars, e.g. $\star\star|\star|\,|\star\star\star$ for bins of size $2,1,0,3$ with $k=4$. Each distinct sequence of $n$ stars and $k-1$ bars is a unique distribution, so the count equals $\binom{n+k-1}{k-1}$ (choose which $k-1$ of the $n+k-1$ positions are bars).

![[stars_and_bars.png]]

**Example.** How many non-negative integer solutions to $x_1 + x_2 + x_3 = 10$? Stars and bars with $n=10$, $k=3$: $\binom{12}{2} = 66$.

**CS application.** Counting the number of distinct multisets of size $n$ from $k$ types, distributing cache lines among processors, or allocating tokens to threads — all reduce to stars and bars.

## Pigeonhole principle

If $n$ objects are placed into $k$ bins and $n > k$, then at least one bin contains more than one object.

**Proof.** Suppose for contradiction every bin has at most one object. Then $n = \sum_{\text{bins}} |\text{bin}| \leq k \cdot 1 = k$, contradicting $n > k$.

**Generalised form.** If $n$ objects are placed into $k$ bins, some bin contains at least $\lceil n/k \rceil$ objects.

**Proof.** If every bin had fewer than $\lceil n/k \rceil$ objects, each bin would have at most $\lceil n/k \rceil - 1$ objects, giving total $\leq k(\lceil n/k \rceil - 1) < k \cdot (n/k) = n$ — contradiction.

**Examples:**

| Claim                                                                               | Argument                                                                     |
| ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Among any 13 people, two share a birth month                                        | 13 people, 12 months — one month has $\geq 2$                                |
| Any sequence of $n^2+1$ distinct numbers has a monotone subsequence of length $n+1$ | Erdős–Szekeres; bin by longest increasing subsequence ending at each element |
| In any set of $n+1$ integers from $\{1,\ldots,2n\}$, two are consecutive            | $n$ consecutive pairs; $n+1$ numbers must share a pair                       |

**CS application.** The pigeonhole principle proves that no lossless compression algorithm can compress every possible input — there are $2^n$ strings of length $n$ but only $\sum_{k=0}^{n-1} 2^k = 2^n - 1$ shorter strings to map them to.

## Inclusion-exclusion

For two sets: $|A \cup B| = |A| + |B| - |A \cap B|$.

For three sets: $|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$.

**General formula.** For sets $A_1, \ldots, A_n$:

$$\left|\bigcup_{i=1}^n A_i\right| = \sum_{i}|A_i| - \sum_{i < j}|A_i \cap A_j| + \sum_{i<j<k}|A_i \cap A_j \cap A_k| - \cdots + (-1)^{n+1}|A_1 \cap \cdots \cap A_n|.$$

**Proof.** Each element $x$ in exactly $m$ of the sets is counted $\binom{m}{1} - \binom{m}{2} + \binom{m}{3} - \cdots + (-1)^{m+1}\binom{m}{m}$ times on the right-hand side. By the binomial theorem with $a=1$, $b=-1$: $\sum_{k=0}^{m}(-1)^k\binom{m}{k} = 0$, so $\sum_{k=1}^{m}(-1)^{k+1}\binom{m}{k} = 1$. Each element is counted exactly once.

![[inclusion_exclusion.png]]

**Example.** How many integers from 1 to 100 are divisible by 2 or 3?

$|A| = 50$ (div by 2), $|B| = 33$ (div by 3), $|A \cap B| = 16$ (div by 6).

$$|A \cup B| = 50 + 33 - 16 = 67.$$

**CS application.** Counting passwords that violate at least one rule (must have uppercase, digit, symbol) by inclusion-exclusion over the three violation events. Inclusion-exclusion also underlies the sieve of Eratosthenes and the formula for Euler's totient $\phi(n)$.

## Counting summary

| Scenario                                           | Formula                       |
| -------------------------------------------------- | ----------------------------- |
| Ordered sequences of $k$ from $n$ (no repeat)      | $P(n,k) = \dfrac{n!}{(n-k)!}$ |
| Ordered sequences of $k$ from $n$ (with repeat)    | $n^k$                         |
| Unordered selections of $k$ from $n$ (no repeat)   | $\dbinom{n}{k}$               |
| Unordered selections of $k$ from $n$ (with repeat) | $\dbinom{n+k-1}{k}$           |
| Arrangements of $n$ with repeats $n_1,\ldots,n_r$  | $\dfrac{n!}{n_1!\cdots n_r!}$ |
| Circular arrangements of $n$                       | $(n-1)!$                      |
| $n$ balls into $k$ bins (any empty)                | $\dbinom{n+k-1}{k-1}$         |

## Video references

- ![Lecture 12: Sums](https://www.youtube.com/watch?v=fAeShezAGLE)
- ![Lecture 13: Sums and Asymptotics](https://www.youtube.com/watch?v=X9eErxRjQEI)
- ![Lecture 14: Divide and Conquer Recurrences](https://www.youtube.com/watch?v=Kqf0uO0oV6s)
- ![Lecture 15: Linear Recurrences](https://www.youtube.com/watch?v=TWBB-JlmYUc)
- ![Lecture 16: Counting Rules I](https://www.youtube.com/watch?v=pNt5Ll6hGqo)
- ![Lecture 17: Counting Rules II](https://www.youtube.com/watch?v=09yIb3VHhMI)

## See also

- [[Functions]]
- [[Probability]]
- [[Graphs]]
- [[../algebra/Index|Algebra]]
- [[Index]]
