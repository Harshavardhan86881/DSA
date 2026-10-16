# Has Path in Undirected Graph

| | |
| --- | --- |
| **Difficulty** | easy |
| **Topics** | graphs, DFS |
| **Target time** | 15 minutes |
| **Solution file** | [has-path-in-undirected-graph.py](has-path-in-undirected-graph.py) |

## 1. Problem statement

Determine if a path exists between src and dst.

## 2. Constraints

Reasonable graph sizes.

## 3. Examples

```text
True
```

## 4. Hints

<details><summary>Hint 1</summary>
Use adjacency list and visited set.
</details>

## 5. Optimised approach

```python
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

- `../../exercises/starter-code/has_path.py` — starter code.
