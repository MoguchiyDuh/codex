---
tags:
  - algorithms
  - approximation
  - np-hard
  - optimization
status: complete
---

# Approximation Algorithms

> Polynomial-time algorithms that produce solutions provably close to optimal for NP-hard optimisation problems.

## The setting

NP-hard optimisation problems (TSP, vertex cover, set cover, knapsack, ...) admit no known polynomial-time exact algorithm — and unless $\text{P} = \text{NP}$, none exists. See [[NP-Completeness]].

When exact answers are too expensive, three responses are possible:

| Response                    | Guarantee                         | Tradeoff                                   |
| --------------------------- | --------------------------------- | ------------------------------------------ |
| Exact (exponential)         | optimal                           | exponential time                           |
| **Approximation algorithm** | within a factor $\rho$ of optimal | polynomial time, mathematically guaranteed |
| Heuristic                   | none                              | polynomial time, no proof of quality       |

Approximation algorithms occupy the middle: provably close, fast, but not optimal.

## Approximation ratio

For a minimisation problem, an algorithm has approximation ratio $\rho \geq 1$ if for every input,

$$\text{ALG}(I) \leq \rho \cdot \text{OPT}(I)$$

For maximisation, $\rho \leq 1$ and $\text{ALG}(I) \geq \rho \cdot \text{OPT}(I)$. Conventionally both written as $\rho \geq 1$ with the right direction implied.

A **$\rho$-approximation algorithm** is one with proven ratio $\rho$, where $\rho$ may be a constant, a function of input size, or arbitrarily close to $1$.

## Approximation schemes

| Scheme                                                 | Guarantee                                                                                                                                     |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Constant-factor**                                    | $\rho$ is a fixed constant                                                                                                                    |
| **PTAS** (polynomial-time approximation scheme)        | for any $\varepsilon > 0$, returns a $(1 + \varepsilon)$-approximation in polynomial time in $n$ (with arbitrary dependence on $\varepsilon$) |
| **FPTAS** (fully polynomial-time approximation scheme) | PTAS with running time polynomial in both $n$ and $1/\varepsilon$                                                                             |
| **APX**                                                | the class of problems with constant-factor approximation                                                                                      |

The hierarchy: FPTAS $\subseteq$ PTAS $\subseteq$ APX. Some problems admit FPTAS (knapsack); others have PTAS but no FPTAS (Euclidean TSP); some admit constant-factor approximation but no PTAS (vertex cover, unless $\text{P} = \text{NP}$).

## Vertex cover: 2-approximation

**Problem.** Find the smallest set of vertices covering every edge.

**Algorithm.** Repeatedly pick any uncovered edge and add _both_ its endpoints to the cover.

```pseudo
vertex_cover_2approx(G):
    C = empty set
    E' = E
    while E' not empty:
        pick any edge (u, v) in E'
        C = C ∪ {u, v}
        remove all edges incident to u or v from E'
    return C
```

**Analysis.** Let $M$ be the set of edges picked. They are pairwise disjoint (sharing a vertex would mean already covered). Any vertex cover must cover each edge in $M$, so $\text{OPT} \geq |M|$. The algorithm returns $2|M|$ vertices.

$$|C| = 2|M| \leq 2 \cdot \text{OPT}$$

A 2-approximation. Despite decades of effort, no $(2 - \varepsilon)$-approximation is known for general vertex cover, and assuming the _Unique Games Conjecture_ none exists.

## TSP: metric 2-approximation

**Problem.** Given a complete weighted graph satisfying the triangle inequality, find a Hamiltonian cycle of minimum total weight.

General TSP cannot be approximated within any factor unless $\text{P} = \text{NP}$. The metric (triangle-inequality) version admits a 2-approximation via [[Minimum Spanning Tree|MST]].

**Algorithm.**

1. Build an MST $T$.
2. Walk $T$ in DFS order, listing each vertex when first visited.
3. Return that listing as a tour (closing back to start).

**Analysis.** Cost of MST $\leq$ cost of optimal tour (removing any edge of the optimal tour gives a spanning tree, which is at least as expensive as the MST). Walking the MST visits each edge twice — total walk cost $\leq 2 \cdot \text{MST} \leq 2 \cdot \text{OPT}$. The shortcut step (skipping repeated visits) only shortens by the triangle inequality.

$$\text{ALG} \leq 2 \cdot \text{OPT}$$

![[tsp_2_approx.png]]

**Christofides' algorithm** improves the bound to $3/2$ using a clever combination of MST + minimum-weight perfect matching on the odd-degree vertices. It was the best known for metric TSP from 1976 until 2020, when slight improvements broke the $3/2$ barrier.

## Set cover: $\ln n$-approximation

**Problem.** Given a universe $U$ of $n$ elements and a collection of subsets $S_1, \dots, S_m \subseteq U$, find the minimum number of subsets whose union is $U$.

**Algorithm.** Greedy — repeatedly pick the subset covering the most uncovered elements.

```pseudo
set_cover_greedy(U, S):
    C = empty list
    uncovered = U
    while uncovered not empty:
        pick the subset S_i maximising |S_i ∩ uncovered|
        C.append(S_i)
        uncovered = uncovered \ S_i
    return C
```

**Analysis.** Greedy returns a cover of size $\leq H_n \cdot \text{OPT}$, where $H_n = 1 + 1/2 + \cdots + 1/n \approx \ln n$.

The bound is tight: there are instances where greedy achieves exactly $H_n$. Moreover, no polynomial-time algorithm can approximate set cover better than $(1 - \varepsilon) \ln n$ unless $\text{P} = \text{NP}$ (Feige's theorem).

## Knapsack: FPTAS

**Problem.** $n$ items with values $v_i$ and weights $w_i$, capacity $W$. Maximise total value with weight $\leq W$.

[[Dynamic Programming|DP]] solves it in $\Theta(nW)$ — pseudo-polynomial. There's also a $\Theta(nV)$ DP where $V = \sum v_i$. The FPTAS scales values by a factor that loses at most $\varepsilon$ of OPT and runs in $\Theta(n^3 / \varepsilon)$:

1. Let $v_{\max}$ be the largest item value.
2. Scale: $v_i' = \lfloor v_i \cdot n / (\varepsilon v_{\max}) \rfloor$.
3. Run the $\Theta(n V')$ DP on scaled values.
4. Return the same item set as the optimal of the scaled instance.

The scaling loses at most $\varepsilon \cdot \text{OPT}$ value. Running time depends on $n$ and $1/\varepsilon$ polynomially — FPTAS by definition.

## Bin packing

**Problem.** Pack items of sizes $\in (0, 1]$ into the fewest unit-capacity bins.

| Algorithm                | Guarantee                                        |
| ------------------------ | ------------------------------------------------ |
| **First-Fit**            | $\leq 1.7 \cdot \text{OPT}$                      |
| **First-Fit Decreasing** | $\leq 11/9 \cdot \text{OPT} + 6/9$               |
| **Asymptotic PTAS**      | $\leq (1 + \varepsilon) \cdot \text{OPT} + O(1)$ |
| **No FPTAS**             | unless $\text{P} = \text{NP}$                    |

A standard demonstration that simple online heuristics (First-Fit) already give constant-factor guarantees.

## Inapproximability

For some problems, achieving a better ratio is provably as hard as solving NP-complete problems.

| Problem         | Best known                   | Lower bound                                      |
| --------------- | ---------------------------- | ------------------------------------------------ |
| Vertex cover    | $2$                          | $1.36$ (under UGC: $2$)                          |
| TSP (general)   | $\infty$ — no constant ratio | unbounded                                        |
| TSP (metric)    | $\approx 1.5 - 10^{-36}$     | $123/122$                                        |
| Set cover       | $\ln n$                      | $(1 - o(1)) \ln n$                               |
| MAX-3SAT        | $7/8$                        | $7/8 + \varepsilon$ (Håstad)                     |
| Maximum clique  | $n^{1 - \varepsilon}$        | hard to approximate within $n^{1 - \varepsilon}$ |
| Independent set | $n / \log^2 n$               | hard within $n^{1 - \varepsilon}$                |

Inapproximability proofs use the **PCP theorem** — characterising NP via probabilistically checkable proofs — to show that distinguishing exact from approximate solutions is itself NP-hard.

## Design techniques

| Technique                        | Idea                                                                             |
| -------------------------------- | -------------------------------------------------------------------------------- | ----------------------- |
| **Greedy**                       | local choice with a charging argument                                            | set cover, scheduling   |
| **LP relaxation + rounding**     | solve linear-programming relaxation, round to integers                           | vertex cover, set cover |
| **Primal-dual**                  | construct primal and dual feasible solutions in tandem                           | facility location       |
| **Local search**                 | start with a feasible solution, swap to improve, prove a bound on stopping point | $k$-median              |
| **Combinatorial structure**      | exploit MST, matching, or shortest paths                                         | TSP, Steiner tree       |
| **Randomisation**                | random rounding of LP, random ordering                                           | MAX-CUT, MAX-SAT        |
| **Pseudo-polynomial DP scaling** | scale and round inputs to make DP cheap                                          | knapsack FPTAS          |

## Online algorithms

A relative: **online algorithms** make decisions without knowing future input, and competitive ratio plays the role of approximation ratio. Caching, paging, scheduling all fit. Different theory but similar mindset — provably-near-optimal under uncertainty rather than under hardness.

## When to use approximation algorithms

| Situation                                              | Use                                                                           |
| ------------------------------------------------------ | ----------------------------------------------------------------------------- |
| NP-hard optimisation, large $n$, need provable quality | yes                                                                           |
| NP-hard, small $n$ (say $n < 50$)                      | branch-and-bound exact                                                        |
| Polynomial problem                                     | approximation is wasted; solve exactly                                        |
| Near-exact answers needed, instance structure unknown  | mathematical programming (ILP, SAT, LP)                                       |
| Real-time / streaming                                  | heuristics with empirical testing; approximation guarantees often impractical |

The main reason to learn approximation theory: it tells you what is _fundamentally_ possible. If a problem has no constant-factor approximation, no clever heuristic will produce reliably-good answers — that's a structural fact about the problem, not a limitation of your engineering.

## See also

- [[NP-Completeness]]
- [[Greedy Algorithms]]
- [[Dynamic Programming]]
- [[Minimum Spanning Tree]]
- [[Network Flow]]
- [[Backtracking]]
- [[Index]]
