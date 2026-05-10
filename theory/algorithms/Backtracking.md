---
tags:
  - algorithms
  - backtracking
  - search
status: complete
---

# Backtracking

> Systematic exhaustive search through a tree of partial solutions, pruning branches that cannot lead to a valid solution.

## The pattern

Backtracking explores choices recursively. At each step:

1. **Choose** an option for the next decision.
2. **Recurse** to extend the partial solution.
3. **Undo** the choice if recursion fails or we want all solutions.

The search space is a tree of partial solutions; pruning removes subtrees provably unable to contain a solution.

```pseudo
backtrack(state):
    if is_solution(state):
        record(state)
        return
    for choice in candidates(state):
        if is_valid(state, choice):
            apply(state, choice)
            backtrack(state)
            undo(state, choice)
```

Without pruning this is just brute-force enumeration. The art is in the `is_valid` check — recognising dead ends as early as possible.

## N-queens

Place $n$ non-attacking queens on an $n \times n$ board.

**State.** A partial placement giving each queen its column, with row $i$ holding the queen for column $i$ (or none).

**Choices.** For column $i$, try each of $n$ rows.

**Validity.** The new queen attacks no previously placed queen — same row, same diagonal, same anti-diagonal.

```pseudo
solve_n_queens(n):
    place(0, [], n)

place(col, queens, n):
    if col == n:
        record(queens)
        return
    for row = 0 to n - 1:
        if is_valid(queens, row, col):
            place(col + 1, queens + [row], n)
```

**Code:** `theory/algorithms/showcase/n_queens.py`

| Property      | Value                                                 |
| ------------- | ----------------------------------------------------- |
| Worst case    | $\Theta(n!)$ — but pruning collapses much of the tree |
| Practical $n$ | up to ~30 with bitmask-based pruning                  |

![[n_queens_tree.png]]

The picture: the recursion tree branches $n$ ways at each level, but most branches are killed before reaching depth $n$ because partial placements quickly conflict.

## Subset sum / target sum

Find a subset of $\{a_1, \dots, a_n\}$ summing to a target $T$.

```pseudo
subset_sum(i, current_sum, target, n):
    if current_sum == target: return True
    if i == n or current_sum > target: return False
    # include a[i]
    if subset_sum(i+1, current_sum + a[i], target, n): return True
    # exclude a[i]
    return subset_sum(i+1, current_sum, target, n)
```

Worst case $\Theta(2^n)$. Pruning: stop as soon as `current_sum > target` (assuming non-negative inputs). Pre-sorting in descending order pushes pruning earlier.

## Permutations and combinations

Enumerate all permutations of $\{1, \dots, n\}$:

```pseudo
permute(remaining, current):
    if remaining is empty:
        record(current)
        return
    for x in remaining:
        permute(remaining \ {x}, current + [x])
```

For combinations, replace `for x in remaining` with `for x in remaining where x > last(current)` to enforce monotonic order.

These are the canonical recursion-tree traversals — used as scaffolding inside more complex backtracking algorithms.

## Sudoku

Fill a $9 \times 9$ grid such that every row, column, and $3 \times 3$ box contains $\{1, \dots, 9\}$.

**State.** Current grid with some cells empty.

**Heuristic.** Always fill the most-constrained empty cell next — the one with fewest legal candidates. This is the **most-restricted-variable** heuristic, dramatically reducing the search tree compared to scanning left-to-right.

```pseudo
solve_sudoku(grid):
    cell = find_empty_with_fewest_options(grid)
    if cell is None: return True              # solved
    for d in legal_digits(grid, cell):
        grid[cell] = d
        if solve_sudoku(grid): return True
        grid[cell] = empty
    return False
```

Most $9 \times 9$ puzzles solve in milliseconds with this heuristic; without it, exhaustive enumeration takes seconds to minutes.

## Pruning techniques

| Technique                  | Idea                                                                                                           |
| -------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Constraint propagation** | apply the choice's consequences (e.g. eliminate impossible candidates) before recursing                        |
| **Bounding**               | track the best solution found so far; cut branches whose best-case completion can't beat it (branch and bound) |
| **Symmetry breaking**      | if two branches differ only by a symmetry, explore one                                                         |
| **Variable ordering**      | choose the next decision wisely — most-constrained-variable, most-promising, etc.                              |
| **Value ordering**         | within a chosen variable, try the most-promising value first                                                   |

These are not optional polish — they often turn an intractable search into a fast one.

## Backtracking vs DP

|             | Backtracking                                       | DP                                        |
| ----------- | -------------------------------------------------- | ----------------------------------------- |
| Subproblems | distinct paths through the search tree             | reused across many parents                |
| Caching     | no — state is unique per path                      | yes — table or memo                       |
| Goal        | find a solution / all solutions / best solution    | optimise an objective                     |
| Typical use | constraint satisfaction, combinatorial enumeration | optimisation with overlapping subproblems |

When the same subproblem appears on many paths — knapsack, LCS, edit distance — use DP. When each path through the tree carries unique state — N-queens, Sudoku — backtracking is correct.

## Branch and bound

Backtracking applied to optimisation. Maintain the best solution found so far as a _bound_; prune any partial solution whose best-case extension cannot beat the bound.

Used for hard optimisation problems (TSP, integer programming, knapsack with tight constants). Combines well with linear-programming relaxations to compute strong bounds at each node.

## When to reach for backtracking

| Situation                                     | Yes / no                              |
| --------------------------------------------- | ------------------------------------- |
| Constraint satisfaction (SAT-like)            | yes                                   |
| Exhaustive enumeration with structure         | yes                                   |
| Game-tree search (chess, Go)                  | yes — usually with alpha-beta pruning |
| NP-hard combinatorial problems with small $n$ | yes                                   |
| Subproblems repeat substantially              | no — use DP                           |
| Greedy is provably correct                    | no — use greedy                       |

## See also

- [[Recursion]]
- [[Dynamic Programming]]
- [[Greedy Algorithms]]
- [[NP-Completeness]]
- [[Index]]
