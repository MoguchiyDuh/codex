---
tags:
  - algorithms
status: complete
---

# Algorithms

Design techniques, complexity analysis, and the canonical algorithms every CS curriculum covers. Structured after CLRS 4e (Cormen, Leiserson, Rivest, Stein) and MIT 6.046, with implementation companions in `showcase/`.

## Foundations

- [[Complexity]] — Big-O / Θ / Ω, growth classes, best/avg/worst case
- [[Recurrence Relations]] — substitution, recursion-tree, master theorem
- [[Amortized Analysis]] — aggregate, accounting, potential method
- [[Recursion]] — base cases, call stack, tail recursion, tree recursion

## Sorting and selection

- [[Sorting]] — overview, comparison-sort lower bound, classification
- [[Merge Sort]] — divide-and-conquer, stable, $\Theta(n \log n)$ guaranteed
- [[Quick Sort]] — partition, pivot strategies, $\Theta(n \log n)$ average
- [[Heap Sort]] — in-place, $\Theta(n \log n)$ worst case
- [[Linear-Time Sorting]] — counting, radix, bucket
- [[Selection]] — quickselect, median-of-medians, order statistics

## Searching and divide-and-conquer

- [[Searching]] — linear, binary, lower-bound / upper-bound, search structures
- [[Divide and Conquer]] — paradigm, master theorem, Karatsuba, Strassen, closest pair

## Algorithm design paradigms

- [[Dynamic Programming]] — memoization, tabulation, LCS, knapsack, edit distance
- [[Greedy Algorithms]] — greedy-choice property, exchange argument, Huffman, activity selection
- [[Backtracking]] — N-queens, Sudoku, branch and bound

## Graph algorithms

- [[Graph Basics]] — BFS, DFS, edge classes, topological sort, SCC
- [[Shortest Path]] — Dijkstra, Bellman-Ford, DAG-shortest-path
- [[A Star]] — heuristic-guided shortest path
- [[All-Pairs Shortest Path]] — Floyd-Warshall, Johnson's
- [[Minimum Spanning Tree]] — Kruskal, Prim, cut property
- [[Network Flow]] — max-flow / min-cut, Ford-Fulkerson, Edmonds-Karp, Dinic's

## Theory of computation

- [[NP-Completeness]] — P, NP, reductions, Cook-Levin, classic NP-complete problems
- [[Approximation Algorithms]] — ratio, PTAS / FPTAS, vertex cover, TSP, set cover

## Code

Implementation and matplotlib visualization for each algorithm live alongside the notes:

- `showcase/sort/` — bubble, insertion, merge, quick, heap, radix
- `showcase/bfs_dfs/` — BFS, DFS
- `showcase/mst_compare/` — Kruskal, Prim
- `showcase/dijkstra.py`, `showcase/bellman_ford.py`, `showcase/a_star.py`, `showcase/floyd_warshall.py`
- `showcase/dp_memo_vs_tab.py`, `showcase/lcs_dp.py`
- `showcase/n_queens.py`, `showcase/quickselect.py`, `showcase/activity_selection.py`
- `showcase/topological_sort.py`, `showcase/max_flow.py`, `showcase/tsp_approx.py`
- `showcase/growth_rates.py`, `showcase/recursion_tree.py`, `showcase/amortized_costs.py`
- `showcase/binary_search.py`

Each file pairs the implementation with a matplotlib visualization gated by `if __name__ == "__main__":` writing into `resources/pictures/`.

## See also

- [[../data_structures/Index|Data Structures]]
- [[../math/discrete/Index|Discrete Math]]
- [[../computing/Index|Computing]]
