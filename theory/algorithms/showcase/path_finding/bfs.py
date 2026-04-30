from __future__ import annotations

from collections import deque
from collections.abc import Hashable, Iterable, Mapping


Node = Hashable
Graph = Mapping[Node, Iterable[Node]]


def bfs(graph: Graph, start: Node) -> list[Node]:
    if start not in graph:
        return [start]

    order: list[Node] = []
    queue: deque[Node] = deque([start])
    visited = {start}

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

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
    print(bfs(graph, "A"))


if __name__ == "__main__":
    main()
