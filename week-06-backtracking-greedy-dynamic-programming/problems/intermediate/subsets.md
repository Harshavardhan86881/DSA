# Subsets

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | backtracking |
| **Target time** | 20 minutes |
| **Solution file** | [subsets.py](subsets.py) |

## 1. Problem statement

Return all subsets of an array.

## 2. Constraints

Reasonable input sizes.

## 3. Examples

See solution file.

## 4. Hints

<details><summary>Hint 1</summary>
Use recursion/DP as appropriate.
</details>

## 5. Optimised approach

```python
"""Solution: Subsets. O(n * 2^n) time, O(n) space (excluding output)."""


def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result
```

## 6. Complexity analysis

See solution docstring.

## 7. Edge cases and tests

See `../../exercises/test-cases/`.

## 8. Follow-up questions

1. Can you reduce space?
2. What is the time complexity?
3. How to handle duplicates?

## 9. Related problems

- `../../exercises/starter-code/subsets.py` — starter code.
