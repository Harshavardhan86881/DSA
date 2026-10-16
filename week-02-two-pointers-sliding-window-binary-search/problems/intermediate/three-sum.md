# 3Sum

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | sorting, two pointers |
| **Target time** | 30 minutes |
| **Solution file** | [three-sum.py](three-sum.py) |

## 1. Problem statement

Given an integer array `nums`, return all unique triplets `[a, b, c]` such that
`a + b + c == 0`.

## 2. Constraints

- `3 ≤ nums.length ≤ 3000`
- `-10^5 ≤ nums[i] ≤ 10^5`

## 3. Examples

**Example 1**

```text
Input:  [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
```

**Example 2**

```text
Input:  [0, 1, 1]
Output: []
```

**Example 3 — edge case**

```text
Input:  [0, 0, 0]
Output: [[0, 0, 0]]
```

## 4. Hints

<details><summary>Hint 1</summary>
Sort first, then fix one element and use two pointers for the rest.
</details>
<details><summary>Hint 2</summary>
Skip duplicate values to avoid duplicate triplets.
</details>

## 5. Brute-force approach

Three nested loops. O(n³) time.

## 6. Optimised approach

Sort + two pointers. O(n²) time, O(1) extra space (excluding output).

```python
def three_sum(nums: list[int]) -> list[list[int]]:
    nums_sorted = sorted(nums)
    result = []
    n = len(nums_sorted)
    for i in range(n):
        if i > 0 and nums_sorted[i] == nums_sorted[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums_sorted[i] + nums_sorted[left] + nums_sorted[right]
            if total == 0:
                result.append([nums_sorted[i], nums_sorted[left], nums_sorted[right]])
                left += 1
                right -= 1
                while left < right and nums_sorted[left] == nums_sorted[left - 1]:
                    left += 1
                while left < right and nums_sorted[right] == nums_sorted[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result
```

## 7. Complexity analysis

| Approach | Time | Space |
| --- | --- | --- |
| Brute force | O(n³) | O(1) |
| Optimised | O(n²) | O(1) extra |

## 8. Edge cases and tests

| Case | Input | Expected |
| --- | --- | --- |
| Basic | `[-1, 0, 1, 2, -1, -4]` | `[[-1,-1,2],[-1,0,1]]` |
| Empty | `[]` | `[]` |
| All zeros | `[0, 0, 0]` | `[[0,0,0]]` |

```python
def test_basic():
    result = three_sum([-1, 0, 1, 2, -1, -4])
    assert sorted([sorted(t) for t in result]) == sorted([[-1, -1, 2], [-1, 0, 1]])
```

## 9. Follow-up questions

1. How would you solve 4Sum?
2. Why sort first?
3. How do you avoid duplicates without a set?

## 10. Related problems

- `../../exercises/starter-code/three_sum.py` — starter code.
- `../../lessons/two-pointers/two-pointers.md` — two pointers lesson.
