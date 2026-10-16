"""Runnable example: BFS shortest path in unweighted graph."""


from collections import deque


def bfs_shortest_path(graph, start, target):
    if start == target:
        return [start]
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        node, path = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor == target:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None


if __name__ == "__main__":
    graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
    print(bfs_shortest_path(graph, 0, 3))
