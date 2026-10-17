"""Solution: Topological Sort. O(V + E) time, O(V + E) space."""


from collections import deque


def topological_sort(num_nodes, edges):
    graph = {i: [] for i in range(num_nodes)}
    indegree = [0] * num_nodes
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    queue = deque([i for i in range(num_nodes) if indegree[i] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    if len(order) != num_nodes:
        return None
    return order

if __name__ == "__main__":
    print(topological_sort(4, [(0,1),(0,2),(1,3),(2,3)]))
