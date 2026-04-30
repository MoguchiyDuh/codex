from __future__ import annotations

from collections.abc import Hashable, Iterable, Mapping


Node = Hashable
Graph = Mapping[Node, Iterable[Node]]


def dfs(graph: Graph, start: Node) -> list[Node]:
    order: list[Node] = []
    visited: set[Node] = set()

    def visit(node: Node) -> None:
        if node in visited:
            return
        visited.add(node)
        order.append(node)
        for neighbor in graph.get(node, []):
            visit(neighbor)

    visit(start)
    return order


def main() -> None:
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }
    print(dfs(graph, "A"))


if __name__ == "__main__":
    main()
