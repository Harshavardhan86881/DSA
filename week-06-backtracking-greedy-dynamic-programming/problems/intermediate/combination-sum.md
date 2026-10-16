# Combination Sum

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | backtracking |
| **Target time** | 25 minutes |
| **Solution file** | [combination-sum.py](combination-sum.py) |

## 1. Problem statement

Find combinations summing to target.

## 2. Constraints

Reasonable input sizes.

## 3. Examples

```text
See solution file.
```

## 4. Hints

<details><summary>Hint 1</summary>
Use recursion/DP as appropriate.
</details>

## 5. Optimised approach

```python
"""Solution: Combination Sum. O(n^(target/min)) time."""


def combination_sum(candidates, target):
    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])
            path.pop()

    backtrack(0, [], target)
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

- `../../exercises/starter-code/combination_sum.py` — starter code.
