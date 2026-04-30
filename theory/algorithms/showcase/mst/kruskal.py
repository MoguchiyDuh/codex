from __future__ import annotations

from collections.abc import Hashable, Mapping


Node = Hashable
WeightedGraph = Mapping[Node, Mapping[Node, float]]
Edge = tuple[Node, Node, float]


def kruskal(graph: WeightedGraph) -> tuple[list[Edge], float]:
    parent: dict[Node, Node] = {node: node for node in graph}
    rank: dict[Node, int] = {node: 0 for node in graph}
    mst: list[Edge] = []
    total_weight = 0.0

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            parent.setdefault(neighbor, neighbor)
            rank.setdefault(neighbor, 0)

    for u, v, weight in sorted(_edges(graph), key=lambda edge: edge[2]):
        if _find(parent, u) == _find(parent, v):
            continue
        _union(parent, rank, u, v)
        mst.append((u, v, weight))
        total_weight += weight

    return mst, total_weight


def _edges(graph: WeightedGraph) -> list[Edge]:
    seen: set[frozenset[Node]] = set()
    edges: list[Edge] = []
    for u, neighbors in graph.items():
        for v, weight in neighbors.items():
            key = frozenset((u, v))
            if key in seen:
                continue
            seen.add(key)
            edges.append((u, v, weight))
    return edges


def _find(parent: dict[Node, Node], node: Node) -> Node:
    if parent[node] != node:
        parent[node] = _find(parent, parent[node])
    return parent[node]


def _union(parent: dict[Node, Node], rank: dict[Node, int], u: Node, v: Node) -> None:
    root_u = _find(parent, u)
    root_v = _find(parent, v)
    if root_u == root_v:
        return
    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    else:
        parent[root_v] = root_u
        rank[root_u] += 1


def main() -> None:
    graph = {
        "A": {"B": 1, "C": 3},
        "B": {"A": 1, "C": 2, "D": 4},
        "C": {"A": 3, "B": 2, "D": 5},
        "D": {"B": 4, "C": 5},
    }
    print(kruskal(graph))


if __name__ == "__main__":
    main()
