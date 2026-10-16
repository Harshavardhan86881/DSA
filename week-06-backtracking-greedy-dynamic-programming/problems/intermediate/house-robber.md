# House Robber

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | DP |
| **Target time** | 20 minutes |
| **Solution file** | [house-robber.py](house-robber.py) |

## 1. Problem statement

Max money without robbing adjacent houses.

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
"""Solution: House Robber. O(n) time, O(1) space."""


def rob(nums):
    prev2, prev1 = 0, 0
    for num in nums:
        cur = max(prev1, prev2 + num)
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

- `../../exercises/starter-code/house_robber.py` — starter code.
