---
tags: [math, discrete, state-machines, invariants]
status: complete
---

# State Machines

> A state machine models any process that changes over time — and invariants are how you prove things about it.

## Definition

A **state machine** consists of:

- A set of **states** $Q$.
- A set of **start states** $Q_0 \subseteq Q$.
- A **transition relation** $\to\; \subseteq Q \times Q$ specifying which state transitions are legal.

If $q \to r$ we say there is a transition from $q$ to $r$. A machine may be **deterministic** (each state has at most one successor) or **non-deterministic** (a state may have zero, one, or many successors).

A **execution** is a (possibly infinite) sequence of states $q_0, q_1, q_2, \ldots$ where $q_0 \in Q_0$ and $q_i \to q_{i+1}$ for all $i$. A **reachable state** is any state that appears in some execution.

![[state_machine_diagram.png]]

## Why state machines matter

State machines are not just a CS formalism — they are a mathematical proof tool. Any process with a well-defined notion of "current state" and "legal step" can be modelled this way, and then **invariant-based reasoning** applies uniformly. Examples:

| Process | States | Transitions |
|---|---|---|
| Program execution | variable valuations + program counter | assignment, branch |
| Network protocol | (sender state, receiver state, channel) | send, receive, timeout |
| Puzzle (15-puzzle, Rubik's cube) | board configuration | legal moves |
| Dining philosophers | allocation of forks | acquire, release |

## Preserved invariants

A predicate $P$ on states is a **preserved invariant** (or simply an **invariant**) if:

1. $P(q_0)$ holds for every start state $q_0 \in Q_0$.
2. For every transition $q \to r$, if $P(q)$ holds then $P(r)$ holds.

**Invariant theorem.** If $P$ is a preserved invariant, then $P(q)$ holds for every reachable state $q$.

**Proof.** By induction on the length of the execution reaching $q$. The base case is the start state (condition 1). The inductive step is a single transition (condition 2). Every reachable state is reached by a finite execution, so the claim follows.

This is the machinery of [[Induction]] applied to processes.

### Example — robot on a grid

A robot starts at $(0, 0)$ on an integer grid. Each move changes the position by $(+1, 0)$, $(-1, 0)$, $(0, +1)$, or $(0, -1)$.

**Claim.** The robot can never reach $(1, 1)$.

**Proof by invariant.** Let $P(x, y) \equiv (x + y \text{ is even})$. At the start: $0 + 0 = 0$, even. ✓

Each move changes $x + y$ by $\pm 1$, flipping parity. But $1 + 1 = 2$ is even — contradiction? Wait: $P$ says the sum is always even, and $(1,1)$ has even sum, so this invariant does not work. We need a stronger one.

Better invariant: let $Q(x, y) \equiv (x + y \text{ is even})$. This is preserved (each move flips sign of $x+y$... but the sum changes by $\pm 1$, so parity *does* flip). Start: $0+0=0$ even. After one move: $x+y = \pm 1$, odd. So after every odd step the sum is odd, after every even step the sum is even. $(1,1)$ has even sum so it's reachable only after an even number of steps — not a full block.

Correct invariant: $P(x,y) \equiv (x + y \equiv 0 \pmod{2})$. Start holds. Each step flips parity, so after an even number of steps parity is even, after an odd number odd. $(1,1)$ has $x+y=2$ which is even, reachable after $2$ steps: $(0,0) \to (1,0) \to (1,1)$. The claim is false — the robot *can* reach $(1,1)$.

This illustrates that choosing the right invariant requires care. The attempt is not wasted — it reveals structure.

**A correct claim:** the robot can never reach $(1, 0)$ starting from $(0, 0)$ using only diagonal moves $(\pm 1, \pm 1)$.

Invariant: $P(x,y) \equiv (x + y \equiv 0 \pmod{2})$. Start: $0+0=0$ ✓. Each diagonal move changes both $x$ and $y$ by $\pm 1$, so $x+y$ changes by $0$ or $\pm 2$ — parity preserved. $(1, 0)$ has $x+y = 1$, odd — not reachable.

## Derived variables

Sometimes no single state predicate is an invariant, but a function of the state — a **derived variable** — has a useful monotone property.

A derived variable $f : Q \to \mathbb{R}$ is:

- **Weakly decreasing** if $q \to r \implies f(r) \leq f(q)$.
- **Strictly decreasing** if $q \to r \implies f(r) < f(q)$.
- **Bounded below** if $f(q) \geq c$ for all reachable $q$ and some fixed $c$.

**Termination theorem.** If there exists a strictly decreasing, integer-valued, bounded-below derived variable, then every execution is finite — the machine terminates.

**Proof.** Each transition strictly decreases an integer bounded below — it can only decrease finitely many times before hitting the bound.

This is the mathematical form of a **termination argument** for programs. A loop terminates iff you can exhibit such a variable (a "loop variant" or "Lyapunov function"). Compilers and program verifiers search for exactly this.

### Example — Euclidean algorithm terminates

State: pair $(a, b)$ with $b > 0$. Transition: $(a, b) \to (b, a \bmod b)$.

Derived variable: $f(a, b) = b$.

- Strictly decreasing: $a \bmod b < b$ always, so $f$ decreases on every step.
- Bounded below: $b \geq 1$ in all non-terminal states.

Therefore the algorithm terminates.

## Partial correctness vs total correctness

For a program modelled as a state machine with designated terminal states:

| Property | Meaning |
|---|---|
| **Partial correctness** | if the machine terminates, it terminates in a correct state |
| **Termination** | the machine always reaches a terminal state |
| **Total correctness** | partial correctness + termination |

Partial correctness is proved by invariant. Termination is proved by strictly decreasing derived variable. Total correctness requires both.

**Example — division algorithm.** State: $(q, r)$ where $a = qd + r$, $r \geq 0$. Start: $(0, a)$. Transition: if $r \geq d$, move to $(q+1, r-d)$; otherwise halt.

*Invariant (partial correctness):* $a = qd + r$ and $r \geq 0$. Preserved by each transition: $(q+1)d + (r-d) = qd + r = a$, and $r - d \geq 0$ since the transition only fires when $r \geq d$.

*Termination:* derived variable $f(q,r) = r$, strictly decreasing by $d$ per step, bounded below by $0$.

At the terminal state $r < d$ and $a = qd + r$ with $r \geq 0$ — exactly the output of the division algorithm.

## See also

- [[Induction]]
- [[Logic & Proofs]]
- [[Graphs]]
- [[../../concurrency/Memory Models|Memory Models]]
- [[Index]]
