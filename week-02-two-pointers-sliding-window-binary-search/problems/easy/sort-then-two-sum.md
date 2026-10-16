# Sort Then Two Sum

| | |
| --- | --- |
| **Difficulty** | easy |
| **Topics** | sorting, two pointers |
| **Target time** | 20 minutes |
| **Solution file** | [sort-then-two-sum.py](sort-then-two-sum.py) |

## 1. Problem statement

Given an array of integers and a target, determine whether there exist two distinct elements
that sum to the target. Return `True` or `False`. (Indices are not required.)

## 2. Constraints

- `0 ≤ n ≤ 10^4`
- `-10^4 ≤ nums[i], target ≤ 10^4`

## 3. Examples

**Example 1**

```text
Input:  nums = [3, 2, 4], target = 6
Output: True
```

**Example 2**

```text
Input:  nums = [3, 2, 4], target = 10
Output: False
```

**Example 3 — edge case**

```text
Input:  nums = [], target = 0
Output: False
```

## 4. Hints

<details><summary>Hint 1</summary>
Sort first, then use two pointers.
</details>
<details><summary>Hint 2</summary>
If the sum is too small, move left up; if too large, move right down.
</details>

## 5. Brute-force approach

Check every pair. O(n²) time, O(1) space.

## 6. Optimised approach

Sort, then two pointers. O(n log n) time, O(n) space (sorted copy).

```python
def has_pair_sum(nums: list[int], target: int) -> bool:
    s = sorted(nums)
    left, right = 0, len(s) - 1
    while left < right:
        total = s[left] + s[right]
        if total == target:
            return True
        if total < target:
            left += 1
        else:
            right -= 1
    return False
```

## 7. Complexity analysis

| Approach | Time | Space |
| --- | --- | --- |
| Brute force | O(n²) | O(1) |
| Optimised | O(n log n) | O(n) |

## 8. Edge cases and tests

| Case | Input | Expected |
| --- | --- | --- |
| Empty | `[]`, 0 | `False` |
| Single | `[5]`, 5 | `False` |
| Duplicate values | `[2, 2, 3]`, 4 | `True` |
| Negatives | `[-1, 2, 0]`, 1 | `True` |

```python
def test_basic():
    assert has_pair_sum([3, 2, 4], 6) is True

def test_false():
    assert has_pair_sum([3, 2, 4], 10) is False
```

## 9. Follow-up questions

1. What if you need the indices? (Sort pairs with original indices.)
2. When would hashing be better? (O(n) time, O(n) space, no sorting.)
3. What if the array is already sorted? (Skip sorting; O(n) total.)

## 10. Related problems

- `../../exercises/starter-code/sort_then_two_sum.py` — starter code.
- `../../lessons/sorting-patterns/sorting-as-a-pattern.md` — the full lesson.
