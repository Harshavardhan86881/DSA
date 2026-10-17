"""Solution: Count Connected Components. O(V + E) time, O(V + E) space."""


def count_components(n, edges):
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = set()

    def dfs(node):
        stack = [node]
        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            visited.add(cur)
            for neighbor in graph[cur]:
                if neighbor not in visited:
                    stack.append(neighbor)

    count = 0
    for i in range(n):
        if i not in visited:
            count += 1
            dfs(i)
    return count

if __name__ == "__main__":
    print(count_components(5, [[0,1],[1,2],[3,4]]))
