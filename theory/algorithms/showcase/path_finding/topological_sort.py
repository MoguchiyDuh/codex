from __future__ import annotations
from collections import deque


def topological_sort(graph: dict[str, list[str]]) -> list[str]:
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] = in_degree.get(v, 0) + 1

    queue = deque([u for u in in_degree if in_degree[u] == 0])
    result = []

    while queue:
        u = queue.popleft()
        result.append(u)
        for v in graph.get(u, []):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(result) != len(graph):
        raise ValueError("Graph has a cycle!")
    return result


if __name__ == "__main__":
    dag = {
        "shirt": ["tie", "belt"],
        "tie": ["jacket"],
        "belt": ["jacket"],
        "watch": [],
        "undershirt": ["pants", "shoes"],
        "pants": ["belt", "shoes"],
        "shoes": [],
        "socks": ["shoes"],
        "jacket": [],
    }
    print(f"Topological Order: {topological_sort(dag)}")
