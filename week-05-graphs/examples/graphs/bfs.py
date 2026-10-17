"""Runnable example: BFS traversal and shortest path in an unweighted graph."""

from collections import deque


def bfs(graph, start):
    """Return all vertices reachable from start."""
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


def shortest_path(graph, start, target):
    """Return a shortest path as a list, or None if unreachable."""
    if start == target:
        return [start]
    parent = {start: None}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in parent:
                parent[neighbor] = node
                if neighbor == target:
                    path = []
                    cur = target
                    while cur is not None:
                        path.append(cur)
                        cur = parent[cur]
                    path.reverse()
                    return path
                queue.append(neighbor)
    return None


if __name__ == "__main__":
    graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
    print("BFS:", sorted(bfs(graph, 0)))
    print("Path:", shortest_path(graph, 0, 3))
