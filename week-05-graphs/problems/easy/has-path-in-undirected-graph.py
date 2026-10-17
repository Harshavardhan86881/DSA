"""Solution: Has Path. O(V + E) time, O(V) space."""


def has_path(graph, src, dst):
    visited = set()

    def dfs(node):
        if node == dst:
            return True
        if node in visited:
            return False
        visited.add(node)
        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True
        return False

    return dfs(src)

if __name__ == "__main__":
    graph = {0:[1],1:[2],2:[]}
    print(has_path(graph,0,2))
