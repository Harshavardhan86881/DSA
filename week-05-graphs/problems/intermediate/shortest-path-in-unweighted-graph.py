"""Solution: Shortest Path in Unweighted Graph. O(V + E) time, O(V) space."""


from collections import deque


def shortest_path(graph, start, target):
    if start == target:
        return 0
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        node, dist = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor == target:
                return dist + 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1

if __name__ == "__main__":
    graph = {0:[1,2],1:[3],2:[3],3:[]}
    print(shortest_path(graph,0,3))
