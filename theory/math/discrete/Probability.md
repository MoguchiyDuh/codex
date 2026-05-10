---
tags: [math, discrete, probability]
status: complete
---

# Probability

> Probability is counting under uncertainty — a rigorous framework for reasoning about random outcomes.

## Sample spaces and events

A **probability space** has two components:

- A **sample space** $\Omega$: the set of all possible outcomes of an experiment. Must be exhaustive and mutually exclusive.
- A **probability function** $\Pr : 2^\Omega \to [0, 1]$ assigning probabilities to **events** (subsets of $\Omega$).

For a **discrete** (finite or countably infinite) sample space, the probability function is determined by assigning a weight $\Pr[\omega] \geq 0$ to each outcome $\omega \in \Omega$ such that $\sum_{\omega \in \Omega} \Pr[\omega] = 1$. The probability of an event $E \subseteq \Omega$ is then

$$\Pr[E] = \sum_{\omega \in E} \Pr[\omega].$$

For **uniform** sample spaces every outcome has equal weight $\Pr[\omega] = 1/|\Omega|$, so $\Pr[E] = |E| / |\Omega|$ — probability reduces to counting.

**Example.** Roll a fair six-sided die. $\Omega = \{1,2,3,4,5,6\}$, each with probability $1/6$. Event "even": $E = \{2,4,6\}$, $\Pr[E] = 3/6 = 1/2$.

## Axioms of probability

The Kolmogorov axioms characterise any valid probability function:

| Axiom                | Statement                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------ |
| Non-negativity       | $\Pr[E] \geq 0$ for all events $E$                                                               |
| Normalisation        | $\Pr[\Omega] = 1$                                                                                |
| Countable additivity | If $E_1, E_2, \ldots$ are pairwise disjoint, $\Pr\!\left[\bigcup_i E_i\right] = \sum_i \Pr[E_i]$ |

Everything else — complement rule, inclusion-exclusion for events, union bound — follows from these three.

### Derived rules

| Rule                | Formula                                           | Proof                                                                                         |
| ------------------- | ------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Complement          | $\Pr[\overline{E}] = 1 - \Pr[E]$                  | $\Pr[E] + \Pr[\overline{E}] = \Pr[\Omega] = 1$                                                |
| Monotonicity        | $A \subseteq B \implies \Pr[A] \leq \Pr[B]$       | $B = A \cup (B \setminus A)$, disjoint, so $\Pr[B] = \Pr[A] + \Pr[B \setminus A] \geq \Pr[A]$ |
| Union bound         | $\Pr[A \cup B] \leq \Pr[A] + \Pr[B]$              | inclusion-exclusion minus a non-negative term                                                 |
| Inclusion-exclusion | $\Pr[A \cup B] = \Pr[A] + \Pr[B] - \Pr[A \cap B]$ | from countable additivity + split of $A \cup B$                                               |

The **union bound** is especially useful in CS: when you have many bad events and want to show their union is unlikely, bound the probability of each and sum. This technique appears in randomised algorithm analysis and cryptographic security proofs.

## The four-step method

6.042J's systematic approach to any discrete probability problem:

1. **Define the sample space** — list all possible outcomes precisely.
2. **Define the event** — which outcomes satisfy the condition of interest?
3. **Assign probabilities** — uniform or weighted, justified by the model.
4. **Compute** — use counting, complement, or conditional probability.

**Example — two dice.** What is the probability that two fair dice sum to 7?

1. $\Omega = \{(i,j) \mid 1 \leq i,j \leq 6\}$, $|\Omega| = 36$.
2. $E = \{(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)\}$, $|E| = 6$.
3. Uniform: each outcome has probability $1/36$.
4. $\Pr[E] = 6/36 = 1/6$.

## Conditional probability

The **conditional probability** of $A$ given $B$ (with $\Pr[B] > 0$):

$$\Pr[A \mid B] = \frac{\Pr[A \cap B]}{\Pr[B]}.$$

Intuitively: restrict the sample space to $B$ and renormalise. Conditioning is the core operation of probabilistic inference.

**Example.** A family has two children. Given that at least one is a girl, what is the probability both are girls?

$\Omega = \{GG, GB, BG, BB\}$ uniformly. $B = \{GG, GB, BG\}$ (at least one girl), $A = \{GG\}$ (both girls).

$$\Pr[A \mid B] = \frac{\Pr[GG]}{3/4} = \frac{1/4}{3/4} = \frac{1}{3}.$$

### Law of total probability

If $B_1, B_2, \ldots, B_k$ partition $\Omega$ (disjoint, union is $\Omega$), then for any event $A$:

$$\Pr[A] = \sum_{i=1}^{k} \Pr[A \mid B_i]\,\Pr[B_i].$$

**Proof.** $A = \bigcup_i (A \cap B_i)$, disjoint union, so $\Pr[A] = \sum_i \Pr[A \cap B_i] = \sum_i \Pr[A \mid B_i]\Pr[B_i]$.

### Bayes' theorem

$$\Pr[B \mid A] = \frac{\Pr[A \mid B]\,\Pr[B]}{\Pr[A]}.$$

**Proof.** $\Pr[A \cap B] = \Pr[A \mid B]\Pr[B] = \Pr[B \mid A]\Pr[A]$. Divide both sides by $\Pr[A]$.

Combining with the law of total probability over a partition $\{B, \overline{B}\}$:

$$\Pr[B \mid A] = \frac{\Pr[A \mid B]\,\Pr[B]}{\Pr[A \mid B]\,\Pr[B] + \Pr[A \mid \overline{B}]\,\Pr[\overline{B}]}.$$

**Medical test example.** A disease affects 1% of the population. A test is 99% sensitive (detects the disease when present) and 99% specific (negative when absent). Given a positive test, what is the probability of having the disease?

$\Pr[D] = 0.01$, $\Pr[+ \mid D] = 0.99$, $\Pr[+ \mid \overline{D}] = 0.01$.

$$\Pr[D \mid +] = \frac{0.99 \cdot 0.01}{0.99 \cdot 0.01 + 0.01 \cdot 0.99} = \frac{0.0099}{0.0099 + 0.0099} = \frac{1}{2}.$$

Despite a 99% accurate test, a positive result is only 50% likely to indicate disease when prevalence is low. This **base-rate fallacy** is why rare-event detection (fraud, malware) always has a false-positive problem.

![[bayes_tree.png]]

## Independence

Events $A$ and $B$ are **independent** if

$$\Pr[A \cap B] = \Pr[A]\,\Pr[B].$$

Equivalently (when $\Pr[B] > 0$): $\Pr[A \mid B] = \Pr[A]$ — knowing $B$ occurred gives no information about $A$.

Events $A_1, A_2, \ldots, A_n$ are **mutually independent** if for every subset $S \subseteq \{1,\ldots,n\}$:

$$\Pr\!\left[\bigcap_{i \in S} A_i\right] = \prod_{i \in S} \Pr[A_i].$$

Pairwise independence (every pair is independent) does not imply mutual independence — a common trap.

**Example.** Flip two fair coins. Let $A$ = "first coin heads", $B$ = "second coin heads", $C$ = "both coins the same". Then $A$ and $B$ are independent, $A$ and $C$ are independent, $B$ and $C$ are independent — but $\Pr[A \cap B \cap C] = 1/4 \neq \Pr[A]\Pr[B]\Pr[C] = 1/8$. Not mutually independent.

**CS application.** Hash function analysis assumes keys hash independently — mutual independence justifies the birthday-bound collision probability $\approx n^2/(2m)$ for $n$ keys and $m$ buckets. Analysing randomised algorithms (quicksort, skip lists, bloom filters) relies heavily on independence assumptions.

## Birthday paradox

How many people must be in a room before the probability that two share a birthday exceeds $1/2$?

Model: $n$ people, $365$ days, birthdays uniform and independent.

$$\Pr[\text{all distinct}] = 1 \cdot \frac{364}{365} \cdot \frac{363}{365} \cdots \frac{365-n+1}{365} = \frac{365!/(365-n)!}{365^n}.$$

For $n = 23$: $\Pr[\text{all distinct}] \approx 0.493$, so $\Pr[\text{collision}] \approx 0.507 > 1/2$.

The approximate threshold: $\Pr[\text{collision}] \gtrsim 1/2$ when $n \gtrsim \sqrt{2 \cdot 365 \cdot \ln 2} \approx 22.5$.

**General form.** For a universe of size $N$, collisions appear after roughly $\sqrt{N}$ samples. This is the birthday bound: in a hash table of size $N$, expect the first collision after $\Theta(\sqrt{N})$ insertions.

**CS application.** Birthday attacks on cryptographic hash functions — if a hash output is $b$ bits long, an attacker needs roughly $2^{b/2}$ hash evaluations to find a collision. This is why SHA-256 ($b=256$) provides only 128-bit collision resistance.

## Monty Hall problem

Three doors; one hides a car, two hide goats. You pick door 1. The host (who knows) opens a goat door (say door 3). Should you switch to door 2?

Four-step:

1. $\Omega$: (car location, host opens) — 6 outcomes. Car behind 1, 2, or 3; host opens one of the other goat doors.
2. Event: win by switching.
3. Probabilities: car equally likely behind each door ($1/3$ each); host opens uniformly among valid goat doors.
4. Compute: $\Pr[\text{win by switching}] = \Pr[\text{car behind 2 or 3}] = 2/3$.

Switching wins with probability $2/3$; staying wins with probability $1/3$.

The intuition: switching loses only if your initial pick was correct (probability $1/3$), so switching wins with probability $2/3$.

## Video references

- ![Lecture 18: Probability Introduction](https://www.youtube.com/watch?v=SmFwFdESMHI)
- ![Lecture 19: Conditional Probability](https://www.youtube.com/watch?v=E6FbvM-FGZ8)
- ![Lecture 20: Independence](https://www.youtube.com/watch?v=l1BCv3qqW4A)

## See also

- [[Counting]]
- [[Random Variables]]
- [[Functions]]
- [[Index]]
