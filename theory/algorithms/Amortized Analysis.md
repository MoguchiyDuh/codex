---
tags:
  - algorithms
  - amortized
  - analysis
status: complete
---

# Amortized Analysis

> A technique for bounding the average cost per operation across a sequence, even when individual operations can be expensive.

## The motivation

Worst-case bounds can be misleading. A dynamic-array `push` is $O(n)$ when it triggers a resize, but resizes happen rarely. Reporting "push is $O(n)$" overstates real cost; reporting "amortized $O(1)$" captures that any sequence of $m$ pushes costs $\Theta(m)$ total.

Amortized analysis bounds the **total cost of any valid sequence**, then divides by sequence length. It is not average-case analysis (which assumes a random input distribution) — it is a worst-case bound on a sequence rather than on a single operation.

## Three methods

### Aggregate method

Bound the total cost $T(m)$ of any sequence of $m$ operations directly, then state amortized cost as $T(m) / m$.

**Dynamic array push.** Inserting $m$ elements into an initially empty array with doubling:

- Non-resize cost: $m$ (one write per push).
- Resize cost: $1 + 2 + 4 + \cdots + 2^{\lfloor \log_2 m \rfloor} \leq 2m$ (sum of geometric series).
- Total: $T(m) \leq 3m$, amortized $O(1)$ per push.

The series telescopes because resize size doubles each time — most pushes are cheap, the rare expensive ones are paid for by the cheap ones that came before.

![[dynamic_array_amortized.png]]

### Accounting method

Charge each operation an amortized cost that may exceed its actual cost; the surplus accumulates as **credit** stored on data-structure elements, paying for future expensive operations. The invariant is: total credit must remain non-negative.

**Dynamic array push, accounting style.** Charge $3$ per push. Actual cost is $1$ to write the new element, plus $2$ stored as credit on it. When a resize copies $k$ elements, each carries $2$ credit — exactly the cost to copy itself and one of the older elements. Credit never goes negative; amortized $O(1)$ confirmed.

**Stack with multipop.** A stack supports `push`, `pop`, `multipop(k)` (pop up to $k$ elements). `multipop` is $O(k)$ worst-case. Charge $2$ per push, $0$ per pop and per element popped by `multipop`. Each pushed element carries one credit, paying for its eventual pop. Amortized $O(1)$ per operation.

### Potential method

Define a **potential function** $\Phi$ mapping data-structure states to non-negative reals, with $\Phi(\text{initial}) = 0$. The amortized cost of operation $i$ is

$$\hat{c_i} = c_i + \Phi(D_i) - \Phi(D_{i-1})$$

Total amortized cost telescopes:

$$\sum_{i=1}^{m} \hat{c_i} = \sum c_i + \Phi(D_m) - \Phi(D_0) \geq \sum c_i$$

so the sum of amortized costs is an upper bound on the actual total. Choose $\Phi$ so that expensive operations release stored potential.

**Dynamic array push, potential style.** Let $\Phi(D) = 2 \cdot \text{size}(D) - \text{capacity}(D)$ (set to $0$ when at half capacity, grows by $2$ per non-resizing push, drops back to $0$ on a resize that doubles capacity).

- Non-resize push: $c_i = 1$, $\Delta \Phi = 2$, $\hat{c_i} = 3$.
- Resize push (was at capacity $k$, doubles to $2k$): $c_i = k + 1$, $\Delta \Phi = 2(k+1) - 2k - (k - 0) = 2 - k$… cost balances out. Detailed in CLRS Ch. 16.

All three methods produce the same amortized bound when the analysis is tight; they differ in which is easiest to apply.

## Comparison

| Method | Reasoning style | When to prefer |
|---|---|---|
| Aggregate | Direct sum over a sequence | Simple regular workloads |
| Accounting | Credit per operation, locally verified | Mixed-operation data structures |
| Potential | Algebraic, telescoping | Most general; preferred in formal proofs |

## Other classic results

| Structure | Operation | Worst-case | Amortized |
|---|---|---|---|
| Dynamic array | push | $O(n)$ | $O(1)$ |
| Binary counter | increment (count flipped bits) | $O(\log n)$ | $O(1)$ |
| Splay tree | search / insert / delete | $O(n)$ | $O(\log n)$ |
| Disjoint set with path compression + union by rank | find / union | $O(\log n)$ | $O(\alpha(n))$ |
| Fibonacci heap | decrease-key | $O(\log n)$ | $O(1)$ |

The **binary counter** is the canonical small example: incrementing a $k$-bit counter flips many bits when carries propagate, but over $n$ increments the total bit flips is $< 2n$ — amortized $O(1)$ per increment.

## What amortization does not buy you

- **Real-time guarantees.** A real-time system that must respond within a fixed deadline cannot rely on amortized $O(1)$ if a single operation is $O(n)$. Use a deamortized variant or a structure with strict worst-case bounds.
- **Cost on a single operation.** The bound is on sequences. A user who calls one operation cannot expect the amortized cost.

## See also

- [[Complexity]]
- [[../data_structures/Arrays|Arrays]]
- [[../data_structures/Disjoint Set|Disjoint Set]]
- [[Index]]
