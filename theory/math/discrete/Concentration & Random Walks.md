---
tags: [math, discrete, probability, concentration, random-walks, markov-chains]
status: complete
---

# Concentration & Random Walks

> Concentration inequalities bound how far a random variable strays from its mean — the mathematical basis for analysing randomised algorithms.

## Why concentration matters

Expectation tells you the average outcome. For algorithm analysis you also need to know: how likely is the outcome to be far from that average? A randomised algorithm with good expected runtime might still be useless if the variance is enormous. Concentration inequalities turn "unlikely to be far" into a precise quantitative statement.

## Markov's inequality

For any **non-negative** random variable $X$ and $a > 0$:

$$\Pr[X \geq a] \leq \frac{\mathbb{E}[X]}{a}.$$

**Proof.** Let $\mathbf{1}_{X \geq a}$ be the indicator of the event $X \geq a$. Then $X \geq a \cdot \mathbf{1}_{X \geq a}$ (true when $X \geq a$, and $X \geq 0$ when $X < a$). Taking expectations: $\mathbb{E}[X] \geq a \cdot \Pr[X \geq a]$. Divide by $a$.

**Example.** Average commute time is 30 minutes. Probability commute exceeds 2 hours ($= 4 \times 30$) is at most $1/4$.

Markov's is weak — it only uses non-negativity and the mean. But it is often sufficient, and it is the building block for Chebyshev's and Chernoff bounds.

**Applied form.** With $a = t \cdot \mathbb{E}[X]$:

$$\Pr[X \geq t\,\mathbb{E}[X]] \leq \frac{1}{t}.$$

## Chebyshev's inequality

For any random variable $X$ with finite mean $\mu = \mathbb{E}[X]$ and variance $\sigma^2 = \text{Var}[X]$, and any $k > 0$:

$$\Pr[|X - \mu| \geq k] \leq \frac{\sigma^2}{k^2}.$$

Equivalently, with $k = c\sigma$: $\Pr[|X - \mu| \geq c\sigma] \leq 1/c^2$.

**Proof.** Apply Markov's inequality to the non-negative variable $(X - \mu)^2$ with threshold $k^2$:

$$\Pr[(X-\mu)^2 \geq k^2] \leq \frac{\mathbb{E}[(X-\mu)^2]}{k^2} = \frac{\sigma^2}{k^2}.$$

Note $(X-\mu)^2 \geq k^2$ iff $|X - \mu| \geq k$.

**Example.** $X$ has mean $50$ and standard deviation $5$. Probability $X$ falls outside $[40, 60]$ (i.e. deviates by $\geq 10 = 2\sigma$): $\leq 1/4$.

Chebyshev's uses both the mean and the variance — it is tighter than Markov's when variance is small.

![[concentration_bounds.png]]

## Weak law of large numbers

Let $X_1, X_2, \ldots$ be independent, identically distributed (i.i.d.) random variables with mean $\mu$ and variance $\sigma^2 < \infty$. Let $\bar{X}_n = (X_1 + \cdots + X_n)/n$. Then for any $\varepsilon > 0$:

$$\Pr[|\bar{X}_n - \mu| \geq \varepsilon] \leq \frac{\sigma^2}{n\varepsilon^2} \to 0 \text{ as } n \to \infty.$$

**Proof via Chebyshev.** $\mathbb{E}[\bar{X}_n] = \mu$ (linearity). $\text{Var}[\bar{X}_n] = \sigma^2/n$ (independence: variance of sum divides by $n^2$, but the sum of $n$ equal variances gives $n\sigma^2$, divided by $n^2$ gives $\sigma^2/n$). Apply Chebyshev with $k = \varepsilon$:

$$\Pr[|\bar{X}_n - \mu| \geq \varepsilon] \leq \frac{\sigma^2/n}{\varepsilon^2} = \frac{\sigma^2}{n\varepsilon^2}.$$

**Interpretation.** The sample mean converges in probability to the true mean. This is the mathematical justification for empirical estimation: run an experiment many times, average the results — the average approaches the expected value. Every A/B test, Monte Carlo simulation, and statistical estimator rests on this.

## Chernoff bounds (sketch)

Chebyshev gives polynomial decay in the deviation. Chernoff bounds — derived by applying Markov's to $e^{tX}$ for an optimised $t > 0$ — give **exponential** decay for sums of independent bounded random variables.

For the sum $X = X_1 + \cdots + X_n$ of independent Bernoulli($p_i$) variables with $\mu = \mathbb{E}[X]$:

$$\Pr[X \geq (1+\delta)\mu] \leq \left(\frac{e^\delta}{(1+\delta)^{1+\delta}}\right)^\mu \leq e^{-\mu\delta^2/3} \quad \text{for } 0 < \delta \leq 1.$$

$$\Pr[X \leq (1-\delta)\mu] \leq e^{-\mu\delta^2/2} \quad \text{for } 0 < \delta < 1.$$

| Bound     | Decay in deviation                        | Requires                  |
| --------- | ----------------------------------------- | ------------------------- |
| Markov    | $1/t$ (linear)                            | non-negativity, mean      |
| Chebyshev | $1/k^2$ (quadratic)                       | mean, variance            |
| Chernoff  | $e^{-\Theta(\delta^2 \mu)}$ (exponential) | independence, boundedness |

**CS application.** Chernoff bounds prove that a balanced load balancer with $n$ servers and $n$ jobs achieves maximum load $O(\log n / \log \log n)$ with high probability. They also underpin the analysis of randomised data structures (skip lists, bloom filters) and randomised algorithms (randomised quicksort, hashing).

## Random walks

A **random walk** on $\mathbb{Z}$ starts at $0$. At each step, move $+1$ with probability $p$ and $-1$ with probability $1-p$.

For the **symmetric** walk ($p = 1/2$):

- Position after $n$ steps: $S_n = X_1 + \cdots + X_n$ where $X_i \in \{+1,-1\}$ uniformly.
- $\mathbb{E}[S_n] = 0$, $\text{Var}[S_n] = n$, so $\sigma_{S_n} = \sqrt{n}$.
- By Chebyshev: $\Pr[|S_n| \geq c\sqrt{n}] \leq 1/c^2$. The walk drifts $\Theta(\sqrt{n})$ from the origin.

![[random_walk_1d.png]]

### Gambler's ruin

A gambler starts with $k$ dollars and plays until reaching $N$ dollars (win) or $0$ dollars (ruin). Each round: win $1$ with probability $p$, lose $1$ with probability $1-p$.

For the **symmetric** case ($p = 1/2$), the probability of ruin starting from $k$ is:

$$\Pr[\text{ruin} \mid \text{start at } k] = 1 - \frac{k}{N}.$$

**Proof by invariant / martingale.** The position $S_n$ is a martingale (its expected future value always equals its current value). By optional stopping, $\mathbb{E}[S_T] = k$ where $T$ is the stopping time. The terminal value is $0$ (ruin) with probability $r$ and $N$ (win) with probability $1-r$. So $0 \cdot r + N \cdot (1-r) = k$, giving $r = 1 - k/N$.

**Consequence.** For $p < 1/2$ (unfavourable game), ruin is certain as $N \to \infty$. The house always wins in the long run because the asymmetric walk drifts towards $0$.

### Random walks on graphs

A **random walk on a graph** $G$ starts at some vertex and at each step moves to a uniformly random neighbour. It generalises the 1D walk to arbitrary graph topology.

Key facts for a connected non-bipartite graph $G$ on $n$ vertices:

- The walk converges to a **stationary distribution** $\pi$ where $\pi(v) = \deg(v) / (2m)$ — vertices with higher degree are visited more often.
- The **mixing time** — steps until the distribution is close to $\pi$ — depends on the graph's spectral gap (the gap between the first and second eigenvalue of the adjacency matrix). Well-connected graphs mix fast; bottlenecked graphs mix slowly.

**CS application.** Google's original PageRank algorithm is a random walk on the web graph: the stationary distribution ranks pages by how often a random surfer visits them. MCMC (Markov Chain Monte Carlo) sampling exploits mixing of random walks to sample from complex distributions.

## Markov chains

A **Markov chain** is a sequence of random variables $X_0, X_1, X_2, \ldots$ taking values in a state space $S$, satisfying the **Markov property**:

$$\Pr[X_{n+1} = s \mid X_0, X_1, \ldots, X_n] = \Pr[X_{n+1} = s \mid X_n].$$

The next state depends only on the current state, not on history. A random walk on a graph is a Markov chain.

A **transition matrix** $P$ has $P_{ij} = \Pr[X_{n+1} = j \mid X_n = i]$. Each row sums to $1$.

A **stationary distribution** $\pi$ satisfies $\pi P = \pi$ (it is a left eigenvector of $P$ with eigenvalue $1$). For irreducible, aperiodic chains, the stationary distribution is unique and the chain converges to it from any start state.

![[markov_chain_transitions.png]]

**Example — two-state chain.** States: sunny (S) and rainy (R). $P_{SS} = 0.9$, $P_{SR} = 0.1$, $P_{RS} = 0.5$, $P_{RR} = 0.5$.

Stationary distribution: solve $\pi_S = 0.9\pi_S + 0.5\pi_R$ and $\pi_S + \pi_R = 1$. From the first equation $0.1\pi_S = 0.5\pi_R$, so $\pi_S = 5\pi_R$. Normalising: $\pi_S = 5/6$, $\pi_R = 1/6$.

In the long run, $5/6$ of days are sunny regardless of the starting weather.

## Video references

- ![Can a Chess Piece Explain Markov Chains? | Infinite Series](https://youtu.be/63HHmjlh794?si=1rFWexAkLvVo2zYr)
- ![What is a Random Walk? | Infinite Series](https://youtu.be/stgYW6M5o4k?si=3twfHLJhUeyF9UWl)

## See also

- [[Random Variables]]
- [[Probability]]
- [[Graphs]]
- [[../../algorithms/Graph Basics|Graph Basics]]
- [[Index]]
