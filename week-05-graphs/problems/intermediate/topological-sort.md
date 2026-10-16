# Topological Sort

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | graphs |
| **Target time** | 25 minutes |
| **Solution file** | [topological-sort.py](topological-sort.py) |

## 1. Problem statement

Return a topological ordering of a DAG.

## 2. Constraints

Reasonable graph sizes.

## 3. Examples

```text
See solution file.
```

## 4. Hints

<details><summary>Hint 1</summary>
Use adjacency list and visited set.
</details>

## 5. Optimised approach

```python
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
```

## 6. Complexity analysis

See solution docstring.

## 7. Edge cases and tests

See `../../exercises/test-cases/`.

## 8. Follow-up questions

1. How to handle disconnected graphs?
2. What if graph is large?
3. How to reconstruct path?

## 9. Related problems

- `../../exercises/starter-code/topological_sort.py` — starter code.
