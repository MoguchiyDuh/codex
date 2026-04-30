from __future__ import annotations

from collections.abc import Hashable, Mapping
from math import inf

Node = Hashable
WeightedGraph = Mapping[Node, Mapping[Node, float]]


def bellman_ford(
    graph: WeightedGraph, start: Node
) -> tuple[dict[Node, float], dict[Node, Node | None]]:
    distances = {node: inf for node in graph}
    parents: dict[Node, Node | None] = {node: None for node in graph}
    distances[start] = 0.0

    nodes = list(graph.keys())
    for _ in range(len(nodes) - 1):
        for u in nodes:
            for v, weight in graph.get(u, {}).items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    parents[v] = u

    # Check for negative weight cycles
    for u in nodes:
        for v, weight in graph.get(u, {}).items():
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative weight cycle")

    return distances, parents


if __name__ == "__main__":
    graph = {
        "A": {"B": -1, "C": 4},
        "B": {"C": 3, "D": 2, "E": 2},
        "C": {},
        "D": {"B": 1, "C": 5},
        "E": {"D": -3},
    }
    print(bellman_ford(graph, "A"))
