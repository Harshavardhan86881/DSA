# Permutations

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | backtracking |
| **Target time** | 25 minutes |
| **Solution file** | [permutations.py](permutations.py) |

## 1. Problem statement

Return all permutations.

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
"""Solution: Permutations. O(n * n!) time, O(n) space."""


def permute(nums):
    result = []

    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False

    backtrack([], [False] * len(nums))
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

- `../../exercises/starter-code/permutations.py` — starter code.
