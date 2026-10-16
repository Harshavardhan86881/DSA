# Graphs

Graphs consist of nodes and edges. Represent with adjacency list (dict of lists) or adjacency matrix. BFS uses queue for shortest unweighted paths; DFS explores fully. Topological sort works on DAGs.

## Example BFS
```python
from collections import deque
def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```
