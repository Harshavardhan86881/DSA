"""Runnable example: DFS traversal."""


def dfs(graph, start):
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


if __name__ == "__main__":
    graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
    print(dfs(graph, 0))
