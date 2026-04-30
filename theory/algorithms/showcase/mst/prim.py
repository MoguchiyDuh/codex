from __future__ import annotations

import heapq
from collections.abc import Hashable, Mapping


Node = Hashable
WeightedGraph = Mapping[Node, Mapping[Node, float]]
Edge = tuple[Node, Node, float]


def prim(graph: WeightedGraph, start: Node | None = None) -> tuple[list[Edge], float]:
    if not graph:
        return [], 0.0

    root = next(iter(graph)) if start is None else start
    visited = {root}
    heap: list[tuple[float, Node, Node]] = []
    mst: list[Edge] = []
    total_weight = 0.0

    for neighbor, weight in graph.get(root, {}).items():
        heapq.heappush(heap, (weight, root, neighbor))

    while heap and len(visited) < len(graph):
        weight, u, v = heapq.heappop(heap)
        if v in visited:
            continue
        visited.add(v)
        mst.append((u, v, weight))
        total_weight += weight

        for neighbor, edge_weight in graph.get(v, {}).items():
            if neighbor not in visited:
                heapq.heappush(heap, (edge_weight, v, neighbor))

    return mst, total_weight


def main() -> None:
    graph = {
        "A": {"B": 1, "C": 3},
        "B": {"A": 1, "C": 2, "D": 4},
        "C": {"A": 3, "B": 2, "D": 5},
        "D": {"B": 4, "C": 5},
    }
    print(prim(graph, "A"))


if __name__ == "__main__":
    main()
