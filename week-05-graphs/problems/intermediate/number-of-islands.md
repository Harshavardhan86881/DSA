# Number of Islands

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | graphs, DFS/BFS |
| **Target time** | 25 minutes |
| **Solution file** | [number-of-islands.py](number-of-islands.py) |

## 1. Problem statement

Count islands in a grid.

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
"""Solution: Number of Islands. O(m*n) time, O(m*n) space."""


def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)
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

- `../../exercises/starter-code/number_of_islands.py` — starter code.
