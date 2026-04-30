# Algorithms — Course Roadmap

Structured after two MIT courses that form the standard two-semester algorithms sequence:

- **Tiers 1–3** map to **MIT 6.006 — Introduction to Algorithms** (Fall 2011, Demaine / Devadas): foundations, sorting, searching, divide-and-conquer.
- **Tiers 4–6** map to **MIT 6.046J — Design and Analysis of Algorithms** (Spring 2015, Demaine / Devadas / Lynch): design paradigms, advanced graph algorithms, hardness.

Reference textbook for both: CLRS 4e (Cormen, Leiserson, Rivest, Stein).

Each algorithm pairs a theory note with a runnable Python implementation and matplotlib visualization in `showcase/`.

Progress is tracked by **implementation completeness**, not exams: a tier is done when every algorithm in it has both a `complete` note and a working `showcase/` script with visualization.

## Tiers

### Tier 1 — Foundations of analysis

Asymptotic notation, recurrences, amortized analysis, recursion model.

- [[Complexity]]
- [[Recurrence Relations]]
- [[Amortized Analysis]]
- [[Recursion]]

**Showcase:** `growth_rates.py`, `recursion_tree.py`, `amortized_costs.py`

### Tier 2 — Sorting and selection

Comparison-sort lower bound, classical sorts, linear-time sorts, order statistics.

- [[Sorting]]
- [[Merge Sort]]
- [[Quick Sort]]
- [[Heap Sort]]
- [[Linear-Time Sorting]]
- [[Selection]]

**Showcase:** `sort/{bubble,insertion,merge,quick,heap,radix}_sort.py` + `_viz.py` pairs, `quickselect.py`

### Tier 3 — Searching and divide-and-conquer

Linear / binary search, master theorem, Karatsuba, Strassen, closest pair.

- [[Searching]]
- [[Divide and Conquer]]

**Showcase:** `binary_search.py`

### Tier 4 — Algorithm design paradigms

Memoisation vs tabulation, greedy correctness, backtracking with pruning.

- [[Dynamic Programming]]
- [[Greedy Algorithms]]
- [[Backtracking]]

**Showcase:** `dp_memo_vs_tab.py`, `lcs_dp.py`, `activity_selection.py`, `n_queens.py`

### Tier 5 — Graph algorithms

Traversal, shortest paths, MST, network flow, heuristic search.

- [[Graph Basics]]
- [[Shortest Path]]
- [[A Star]]
- [[All-Pairs Shortest Path]]
- [[Minimum Spanning Tree]]
- [[Network Flow]]

**Showcase:** `bfs_dfs/{bfs,dfs}.py`, `topological_sort.py`, `dijkstra.py`, `bellman_ford.py`, `a_star.py`, `floyd_warshall.py`, `mst_compare/{kruskal,prism}.py`, `max_flow.py`

### Tier 6 — Theory of computation

Hardness, reductions, when exact solutions are infeasible.

- [[NP-Completeness]]
- [[Approximation Algorithms]]

**Showcase:** `tsp_approx.py`

## Completion criteria

A tier is **complete** when:

1. Every note in the tier has `status: complete`.
2. Every algorithm cited in the notes has a working `.py` in `showcase/` with both implementation and matplotlib visualization (`if __name__ == "__main__":`).
3. The visualization writes its image into `resources/pictures/` matching the wiki-embed in the note.

## Reference materials

- [MIT OCW 6.006 Introduction to Algorithms, Fall 2011](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/) — Tiers 1–3
- [MIT OCW 6.046J Design and Analysis of Algorithms, Spring 2015](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/) — Tiers 4–6
- Textbook: CLRS — *Introduction to Algorithms*, 4e — commercial, widely available

## See also

- [[Index]]
- [[../data_structures/ROADMAP|Data Structures — Course Roadmap]]
- [[../math/discrete/Index|Discrete Math]]
