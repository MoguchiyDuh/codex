from __future__ import annotations

import heapq
from collections.abc import Callable, Hashable, Mapping
from math import inf


Node = Hashable
WeightedGraph = Mapping[Node, Mapping[Node, float]]
Heuristic = Callable[[Node, Node], float]


def a_star(
    graph: WeightedGraph, start: Node, goal: Node, heuristic: Heuristic
) -> list[Node]:
    open_heap: list[tuple[float, float, Node]] = [(heuristic(start, goal), 0.0, start)]
    g_score: dict[Node, float] = {start: 0.0}
    parents: dict[Node, Node | None] = {start: None}

    while open_heap:
        _, current_cost, node = heapq.heappop(open_heap)
        if current_cost > g_score.get(node, inf):
            continue
        if node == goal:
            return _reconstruct_path(parents, goal)

        for neighbor, weight in graph.get(node, {}).items():
            if weight < 0:
                raise ValueError("A* requires non-negative edge weights")
            tentative_cost = current_cost + weight
            if tentative_cost < g_score.get(neighbor, inf):
                g_score[neighbor] = tentative_cost
                parents[neighbor] = node
                f_score = tentative_cost + heuristic(neighbor, goal)
                heapq.heappush(open_heap, (f_score, tentative_cost, neighbor))

    return []


def _reconstruct_path(parents: Mapping[Node, Node | None], goal: Node) -> list[Node]:
    path: list[Node] = []
    current: Node | None = goal
    while current is not None:
        path.append(current)
        current = parents.get(current)
    path.reverse()
    return path


def main() -> None:
    graph = {
        "A": {"B": 1, "C": 4},
        "B": {"C": 2, "D": 5},
        "C": {"D": 1},
        "D": {},
    }
    heuristic = {
        "A": 3,
        "B": 2,
        "C": 1,
        "D": 0,
    }
    print(a_star(graph, "A", "D", lambda node, goal: heuristic[node]))


if __name__ == "__main__":
    main()
