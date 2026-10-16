# Climbing Stairs

| | |
| --- | --- |
| **Difficulty** | easy |
| **Topics** | DP |
| **Target time** | 15 minutes |
| **Solution file** | [climbing-stairs.py](climbing-stairs.py) |

## 1. Problem statement

Count ways to climb n stairs.

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
"""Solution: Climbing Stairs. O(n) time, O(1) space."""


def climb_stairs(n):
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        cur = prev1 + prev2
        prev2, prev1 = prev1, cur
    return prev1
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

- `../../exercises/starter-code/climbing_stairs.py` — starter code.
