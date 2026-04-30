from __future__ import annotations

from collections.abc import Hashable, Mapping
from math import inf

Node = Hashable
WeightedGraph = Mapping[Node, Mapping[Node, float]]


def floyd_warshall(graph: WeightedGraph) -> dict[Node, dict[Node, float]]:
    nodes = list(graph.keys())
    dist = {u: {v: inf for v in nodes} for u in nodes}

    for u in nodes:
        dist[u][u] = 0.0
        for v, weight in graph.get(u, {}).items():
            dist[u][v] = weight

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


if __name__ == "__main__":
    graph = {
        "A": {"C": -2},
        "B": {"A": 4, "C": 3},
        "C": {"D": 2},
        "D": {"B": -1},
    }
    print(floyd_warshall(graph))
