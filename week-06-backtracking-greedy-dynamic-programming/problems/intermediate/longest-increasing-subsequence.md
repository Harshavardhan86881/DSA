# Longest Increasing Subsequence

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | DP |
| **Target time** | 25 minutes |
| **Solution file** | [longest-increasing-subsequence.py](longest-increasing-subsequence.py) |

## 1. Problem statement

Length of longest increasing subsequence.

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
"""Solution: Longest Increasing Subsequence. O(n^2) time, O(n) space."""


def length_of_lis(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
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

- `../../exercises/starter-code/longest_increasing_subsequence.py` — starter code.
