---
tags: [math, discrete, probability, random-variables, expectation]
status: complete
---

# Random Variables

> A random variable turns an outcome into a number — and expectation tells you its long-run average.

## Definition

A **random variable** $X$ is a function $X : \Omega \to \mathbb{R}$ mapping each outcome of a sample space to a real number. It is not itself random — it is a deterministic function; the randomness comes from the underlying sample space.

**Example.** Roll two fair dice. $\Omega = \{(i,j) \mid 1 \leq i,j \leq 6\}$. Define $X(i,j) = i + j$ (the sum). $X$ takes values $2, 3, \ldots, 12$.

## Probability mass function

For a **discrete** random variable (countable range), the **probability mass function** (PMF) is

$$p_X(k) = \Pr[X = k] = \sum_{\omega : X(\omega) = k} \Pr[\omega].$$

Properties: $p_X(k) \geq 0$ for all $k$, and $\sum_k p_X(k) = 1$.

**PMF of the dice sum:**

| $k$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $p_X(k)$ | $\frac{1}{36}$ | $\frac{2}{36}$ | $\frac{3}{36}$ | $\frac{4}{36}$ | $\frac{5}{36}$ | $\frac{6}{36}$ | $\frac{5}{36}$ | $\frac{4}{36}$ | $\frac{3}{36}$ | $\frac{2}{36}$ | $\frac{1}{36}$ |

![[discrete_pmf.png]]

## Cumulative distribution function

The **CDF** $F_X(k) = \Pr[X \leq k] = \sum_{j \leq k} p_X(j)$.

The CDF is non-decreasing, right-continuous, $F_X(-\infty) = 0$, $F_X(+\infty) = 1$.

## Expectation

The **expectation** (or expected value, mean) of $X$:

$$\mathbb{E}[X] = \sum_{k} k \cdot p_X(k) = \sum_{\omega \in \Omega} X(\omega)\,\Pr[\omega].$$

Expectation is the probability-weighted average value. It need not be a value $X$ actually takes.

**Example.** Expected dice sum: $\mathbb{E}[X] = \sum_{k=2}^{12} k \cdot p_X(k) = 7$. By symmetry the distribution is centred at $7$.

### Linearity of expectation

For any random variables $X$ and $Y$ (on the same space) and constants $a, b$:

$$\mathbb{E}[aX + bY] = a\,\mathbb{E}[X] + b\,\mathbb{E}[Y].$$

**Proof.** $\mathbb{E}[aX + bY] = \sum_\omega (aX(\omega) + bY(\omega))\Pr[\omega] = a\sum_\omega X(\omega)\Pr[\omega] + b\sum_\omega Y(\omega)\Pr[\omega] = a\mathbb{E}[X] + b\mathbb{E}[Y]$.

Linearity holds **regardless of whether $X$ and $Y$ are independent**. This is the single most useful fact in discrete probability.

**Example — expected number of heads in $n$ flips.** Let $X = X_1 + X_2 + \cdots + X_n$ where $X_i = 1$ if flip $i$ is heads, $0$ otherwise. $\mathbb{E}[X_i] = p$ (probability of heads). By linearity: $\mathbb{E}[X] = np$. No need to compute the full PMF of $X$.

## Indicator random variables

The **indicator** of event $A$ is $\mathbf{1}_A(\omega) = 1$ if $\omega \in A$, $0$ otherwise.

Key fact: $\mathbb{E}[\mathbf{1}_A] = \Pr[A]$.

Indicators decompose complex random variables into sums of simple ones, making linearity of expectation the standard proof technique.

**Example — expected number of fixed points of a random permutation.** A **fixed point** of permutation $\sigma$ is an index $i$ with $\sigma(i) = i$. Let $X_i = \mathbf{1}[\sigma(i) = i]$. Then $\mathbb{E}[X_i] = 1/n$ (by symmetry, each element is fixed with probability $1/n$). Total fixed points $X = \sum_{i=1}^n X_i$, so

$$\mathbb{E}[X] = \sum_{i=1}^n \frac{1}{n} = 1.$$

A uniformly random permutation of $n$ elements has expected $1$ fixed point regardless of $n$.

**Example — expected number of collisions in a hash table.** $n$ keys hashed uniformly into $m$ buckets. Let $X_{ij} = \mathbf{1}[\text{keys } i \text{ and } j \text{ collide}]$. $\Pr[X_{ij} = 1] = 1/m$. Number of colliding pairs $= \sum_{i < j} X_{ij}$, so

$$\mathbb{E}[\text{collisions}] = \binom{n}{2} \cdot \frac{1}{m} = \frac{n(n-1)}{2m}.$$

## Variance

Expectation captures the centre; **variance** captures the spread:

$$\text{Var}[X] = \mathbb{E}\!\left[(X - \mathbb{E}[X])^2\right] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2.$$

The second form (computing formula) is usually easier. The **standard deviation** is $\sigma_X = \sqrt{\text{Var}[X]}$.

**Variance of a sum of independent variables:**

$$\text{Var}[X + Y] = \text{Var}[X] + \text{Var}[Y] \quad \text{(when $X$ and $Y$ are independent).}$$

Variance does not have the unconditional linearity that expectation has — independence is required.

## Common distributions

### Bernoulli($p$)

Single trial: success with probability $p$, failure with probability $1-p$.

$$\Pr[X = 1] = p, \quad \Pr[X = 0] = 1-p.$$
$$\mathbb{E}[X] = p, \qquad \text{Var}[X] = p(1-p).$$

### Binomial($n$, $p$)

Number of successes in $n$ independent Bernoulli($p$) trials.

$$\Pr[X = k] = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \ldots, n.$$
$$\mathbb{E}[X] = np, \qquad \text{Var}[X] = np(1-p).$$

**Proof of expectation via indicators.** $X = \sum_{i=1}^n X_i$, $X_i \sim \text{Bernoulli}(p)$ independent, so $\mathbb{E}[X] = np$ by linearity.

![[binomial_pmf.png]]

### Geometric($p$)

Number of trials until the first success (including the success), each trial independent with success probability $p$.

$$\Pr[X = k] = (1-p)^{k-1} p, \quad k = 1, 2, 3, \ldots$$
$$\mathbb{E}[X] = \frac{1}{p}, \qquad \text{Var}[X] = \frac{1-p}{p^2}.$$

**Proof of expectation.** $\mathbb{E}[X] = \sum_{k=1}^\infty k(1-p)^{k-1}p$. Let $q = 1-p$. Then $\sum_{k=1}^\infty k q^{k-1} = \frac{d}{dq}\sum_{k=0}^\infty q^k = \frac{d}{dq}\frac{1}{1-q} = \frac{1}{(1-q)^2}$. So $\mathbb{E}[X] = p \cdot \frac{1}{p^2} = \frac{1}{p}$.

The geometric distribution has the **memoryless property**: $\Pr[X > s + t \mid X > s] = \Pr[X > t]$. Past failures give no information about future trials.

**CS application.** Expected number of hash probes until an empty slot (open addressing), number of random restarts until a randomised algorithm succeeds, coupon collector problem.

### Negative binomial and Poisson (brief)

The **negative binomial** generalises the geometric: number of trials until $r$ successes. The **Poisson($\lambda$)** distribution ($\Pr[X=k] = e^{-\lambda}\lambda^k/k!$, $\mathbb{E}[X] = \lambda$) approximates the binomial when $n$ is large and $p$ is small with $np = \lambda$ fixed. It models rare-event counts: packet arrivals, server requests, mutations.

## Expectation of a function

For $g : \mathbb{R} \to \mathbb{R}$:

$$\mathbb{E}[g(X)] = \sum_k g(k)\, p_X(k).$$

In particular $\mathbb{E}[X^2] = \sum_k k^2 p_X(k)$, used in the computing formula for variance.

## Conditional expectation

$$\mathbb{E}[X \mid A] = \sum_k k\, \Pr[X = k \mid A].$$

**Law of total expectation.** If $B_1, \ldots, B_r$ partition $\Omega$:

$$\mathbb{E}[X] = \sum_{i=1}^r \mathbb{E}[X \mid B_i]\,\Pr[B_i].$$

This is used in analysing algorithms with branching behaviour, e.g. quicksort expected runtime: condition on the rank of the pivot, sum over all possible pivots.

## See also

- [[Probability]]
- [[Counting]]
- [[Concentration & Random Walks]]
- [[Index]]
