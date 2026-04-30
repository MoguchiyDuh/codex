---
tags:
  - algorithms
  - greedy
status: complete
---

# Greedy Algorithms

> Build a solution one piece at a time, each step choosing the option that looks best locally — and never reconsidering.

## When greedy works

A greedy algorithm is correct when the problem exhibits two properties:

| Property | Meaning |
|---|---|
| **Greedy-choice property** | A globally optimal solution can be assembled by making locally optimal choices |
| **Optimal substructure** | After committing to the greedy choice, the remaining problem has the same form, and its optimal solution combined with the greedy choice gives an optimal whole |

Optimal substructure alone is shared with [[Dynamic Programming]] — what distinguishes greedy is the *greedy-choice property*: you don't need to enumerate all options; one is provably right.

When greedy applies, you skip the DP table entirely and run in $\Theta(n)$ or $\Theta(n \log n)$ instead of $\Theta(n^2)$ or worse.

## Proving greedy correctness

Two standard techniques.

### Exchange argument

Assume an optimal solution that does *not* make the greedy choice. Show that swapping in the greedy choice produces a solution at least as good. Conclude: there exists an optimal solution making the greedy choice. Recurse on the remaining problem.

### Greedy stays ahead

Compare the greedy solution to any optimal solution step by step. Show greedy is at least as good after each step. Conclude: greedy's final answer matches the optimal's.

Both reduce to induction. The hard part is identifying the right invariant — what "ahead" means for the problem.

## Activity selection

Given $n$ activities with start times $s_i$ and finish times $f_i$, select the maximum number of non-overlapping activities.

**Greedy choice.** Sort by finish time; repeatedly pick the activity that finishes earliest and is compatible with the previously chosen one.

```pseudo
activity_select(activities):
    sort activities by finish time
    selected = [activities[1]]
    last_finish = activities[1].f
    for i = 2 to n:
        if activities[i].s ≥ last_finish:
            selected.append(activities[i])
            last_finish = activities[i].f
    return selected
```

**Code:** `theory/algorithms/showcase/activity_selection.py`

| Property | Value |
|---|---|
| Time | $\Theta(n \log n)$ for sort, $\Theta(n)$ scan |
| Optimal | yes |

**Why it works.** Among compatible activities, the one finishing earliest leaves the most room for future activities. Exchange argument: any optimal solution either contains this activity or can be modified to contain it (replacing its first activity with the earliest-finishing one yields a solution with the same count).

![[activity_selection.png]]

## Huffman coding

Build a prefix-free binary code minimising the expected encoded length, given character frequencies.

**Greedy choice.** Repeatedly merge the two least-frequent characters (or sub-trees) into a new node whose frequency is their sum. Continue until one tree remains.

```pseudo
huffman(C):
    Q = min-priority queue of C, keyed by frequency
    for i = 1 to |C| - 1:
        a = extract_min(Q)
        b = extract_min(Q)
        z = new node with freq = a.freq + b.freq, children {a, b}
        insert(Q, z)
    return extract_min(Q)
```

| Property | Value |
|---|---|
| Time | $\Theta(n \log n)$ |
| Optimal | yes (proven via exchange argument) |
| Application | data compression (DEFLATE, JPEG, MP3 entropy coding) |

The proof: in an optimal tree, the two characters with smallest frequencies are siblings at the deepest level. Merging them and recursing on the smaller alphabet preserves optimality.

## Fractional knapsack

$n$ items, weight $w_i$, value $v_i$, capacity $W$. Each item is divisible — take any fraction.

**Greedy choice.** Sort by value-per-weight $v_i / w_i$ descending. Take whole items until you can't fit one; take a fraction of the next to fill the remainder.

| Property | Value |
|---|---|
| Time | $\Theta(n \log n)$ |
| Optimal | yes |

The 0/1 knapsack (items are indivisible) does *not* admit greedy — that's where DP earns its keep.

## Where greedy is provably correct

| Problem | Greedy choice | Where proven |
|---|---|---|
| Activity selection | earliest finish | exchange argument |
| Fractional knapsack | best value/weight | exchange argument |
| Huffman codes | merge two smallest frequencies | exchange argument |
| [[Minimum Spanning Tree\|MST]] (Kruskal, Prim) | lightest edge crossing the cut | cut property |
| [[Shortest Path\|Dijkstra]] (non-negative weights) | unvisited vertex with smallest tentative distance | invariant proof |
| Job scheduling on a single machine to minimize lateness | earliest-deadline-first | exchange argument |

## Where greedy fails

| Problem | Greedy that doesn't work | Reason |
|---|---|---|
| 0/1 knapsack | best value/weight first | granularity of choice |
| Coin change (arbitrary denominations) | largest coin first | optimal may need a smaller coin earlier |
| Graph coloring (minimum colors) | smallest unused color | depends on vertex order |
| Travelling salesman (optimal) | nearest unvisited city | local choices compound poorly |
| Longest path in a DAG | longest first edge | future paths constrained |

In all of these, DP, branch-and-bound, or approximation is the right tool.

The cautionary classic: coin change with denominations $\{1, 3, 4\}$ for amount $6$. Greedy picks $4 + 1 + 1 = 3$ coins; optimal is $3 + 3 = 2$ coins. With $\{1, 5, 10, 25\}$ (US system) greedy *is* optimal — but you have to prove it for the specific denominations.

## Greedy vs DP

| | Greedy | DP |
|---|---|---|
| Choices per step | one (locally best) | all, pick best |
| Subproblem reuse | no | yes |
| Time | typically $\Theta(n)$ or $\Theta(n \log n)$ | typically $\Theta(n^2)$+ |
| Correctness | requires greedy-choice property — proof is non-trivial | requires only optimal substructure |
| When unsure | use DP | use greedy *only after* proving correctness |

The danger of greedy: it always *runs*, but might silently produce a suboptimal answer. Always verify the greedy-choice property before deploying one.

## See also

- [[Dynamic Programming]]
- [[Minimum Spanning Tree]]
- [[Shortest Path]]
- [[Backtracking]]
- [[Index]]
