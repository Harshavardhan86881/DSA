# Shortest Path in Unweighted Graph

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | graphs, BFS |
| **Target time** | 20 minutes |
| **Solution file** | [shortest-path-in-unweighted-graph.py](shortest-path-in-unweighted-graph.py) |

## 1. Problem statement

Return shortest distance between two nodes.

## 2. Constraints

Reasonable graph sizes.

## 3. Examples

```text
2
```

## 4. Hints

<details><summary>Hint 1</summary>
Use adjacency list and visited set.
</details>

## 5. Optimised approach

```python
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

- `../../exercises/starter-code/shortest_path_unweighted.py` — starter code.
