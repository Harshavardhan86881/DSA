# Graphs

| | |
| --- | --- |
| **Week** | 5 — Graphs |
| **Topic** | Graphs |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Week 4 |
| **Deliverable** | `number_of_islands.py` attempted |

## 1. Learning objectives

1. Represent graphs with adjacency list/matrix.
2. Implement BFS and DFS.
3. Count connected components.
4. Detect cycles and topological sort.
5. Compute shortest unweighted paths.

## 2. Concept explanation

Graph: nodes and edges. Directed/undirected, weighted/unweighted. Adjacency list is O(V+E) space and preferred for sparse graphs. Adjacency matrix is O(V^2).

BFS uses a queue and finds shortest paths in unweighted graphs. DFS explores deeply. Topological sort orders a DAG.

## 3. Worked examples

### BFS
```python
from collections import deque
def bfs(graph, start):
    visited = {start}
    q = deque([start])
    while q:
        node = q.popleft()
        for nb in graph.get(node, []):
            if nb not in visited:
                visited.add(nb)
                q.append(nb)
    return visited
```

### Topological sort (Kahn)
```python
from collections import deque
def topo(num_nodes, edges):
    graph = {i: [] for i in range(num_nodes)}
    indeg = [0]*num_nodes
    for u,v in edges:
        graph[u].append(v)
        indeg[v]+=1
    q = deque([i for i in range(num_nodes) if indeg[i]==0])
    order=[]
    while q:
        n=q.popleft()
        order.append(n)
        for nb in graph[n]:
            indeg[nb]-=1
            if indeg[nb]==0:
                q.append(nb)
    return order if len(order)==num_nodes else None
```

## 4. Dry run

Graph 0->1,0->2,1->3,2->3:
- BFS from 0: 0,1,2,3.
- Topo: 0,1,2,3.

## 5. Complexity

| Algorithm | Time | Space |
| --- | --- | --- |
| BFS/DFS | O(V+E) | O(V) |
| Topological sort | O(V+E) | O(V+E) |
| Matrix traversal | O(V^2) | O(V^2) |

## 6. Common mistakes

- Marking visited on pop instead of push.
- Recursion depth on deep graphs.
- Forgetting disconnected components.
- Topological sort on cyclic graph.

## 7. Practice

1. Number of islands.
2. Has path.
3. Course schedule.
