"""Runnable example: recursive and iterative DFS."""


def dfs_recursive(graph, start):
    visited = set()
    result = []

    def visit(node):
        if node in visited:
            return
        visited.add(node)
        result.append(node)
        for neighbor in graph.get(node, []):
            visit(neighbor)

    visit(start)
    return result


def dfs_iterative(graph, start):
    visited = set()
    result = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        result.append(node)
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append(neighbor)
    return result


if __name__ == "__main__":
    graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
    print("recursive:", dfs_recursive(graph, 0))
    print("iterative:", dfs_iterative(graph, 0))
