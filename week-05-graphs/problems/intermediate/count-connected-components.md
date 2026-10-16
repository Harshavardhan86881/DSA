# Count Connected Components

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | graphs, DFS |
| **Target time** | 20 minutes |
| **Solution file** | [count-connected-components.py](count-connected-components.py) |

## 1. Problem statement

Count connected components in an undirected graph.

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

- `../../exercises/starter-code/connected_components.py` — starter code.
