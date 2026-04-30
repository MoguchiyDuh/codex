from __future__ import annotations

import heapq
from collections.abc import Hashable, Mapping
from math import inf


Node = Hashable
WeightedGraph = Mapping[Node, Mapping[Node, float]]


def dijkstra(
    graph: WeightedGraph, start: Node
) -> tuple[dict[Node, float], dict[Node, Node | None]]:
    distances = {node: inf for node in graph}
    parents: dict[Node, Node | None] = {node: None for node in graph}
    distances[start] = 0.0

    heap: list[tuple[float, Node]] = [(0.0, start)]
    while heap:
        current_distance, node = heapq.heappop(heap)
        if current_distance > distances[node]:
            continue

        for neighbor, weight in graph.get(node, {}).items():
            if weight < 0:
                raise ValueError("dijkstra requires non-negative edge weights")
            new_distance = current_distance + weight
            if new_distance < distances.get(neighbor, inf):
                distances[neighbor] = new_distance
                parents[neighbor] = node
                heapq.heappush(heap, (new_distance, neighbor))

    return distances, parents


def shortest_path(graph: WeightedGraph, start: Node, goal: Node) -> list[Node]:
    distances, parents = dijkstra(graph, start)
    if distances.get(goal, inf) == inf:
        return []
    return _reconstruct_path(parents, goal)


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
        "A": {"B": 4, "C": 1},
        "B": {"D": 1},
        "C": {"B": 2, "D": 5},
        "D": {},
    }
    print(dijkstra(graph, "A"))


if __name__ == "__main__":
    main()
