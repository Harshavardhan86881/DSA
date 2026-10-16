# Search in Rotated Sorted Array

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | binary search, arrays |
| **Target time** | 25 minutes |
| **Solution file** | [search-in-rotated-sorted-array.py](search-in-rotated-sorted-array.py) |

## 1. Problem statement

Given a rotated sorted array `nums` and a target, return its index, or -1 if not present.
The array was originally sorted ascending and then rotated at some pivot.

## 2. Constraints

- `1 ≤ nums.length ≤ 5000`
- `-10^4 ≤ nums[i], target ≤ 10^4`
- All values are distinct.

## 3. Examples

**Example 1**

```text
Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4
```

**Example 2**

```text
Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1
```

**Example 3 — edge case**

```text
Input:  nums = [1], target = 1
Output: 0
```

## 4. Hints

<details><summary>Hint 1</summary>
At least one half of the array is always sorted.
</details>
<details><summary>Hint 2</summary>
Check whether target lies in the sorted half; otherwise search the other half.
</details>

## 5. Brute-force approach

Linear scan. O(n) time.

## 6. Optimised approach

Modified binary search. O(log n) time, O(1) space.

```python
def search_rotated(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
```

## 7. Complexity analysis

| Approach | Time | Space |
| --- | --- | --- |
| Brute force | O(n) | O(1) |
| Optimised | O(log n) | O(1) |

## 8. Edge cases and tests

| Case | Input | Expected |
| --- | --- | --- |
| No rotation | `[1, 2, 3, 4], 3` | `2` |
| Single | `[1], 1` | `0` |
| Not found | `[4, 5, 6, 7, 0, 1, 2], 3` | `-1` |

```python
def test_basic():
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4

def test_no_rotation():
    assert search_rotated([1, 2, 3, 4], 3) == 2
```

## 9. Follow-up questions

1. How would you handle duplicates?
2. Can you find the rotation pivot first?
3. What changes if values are not distinct?

## 10. Related problems

- `../../exercises/starter-code/search_rotated_sorted_array.py` — starter code.
- `../../lessons/binary-search/binary-search.md` — binary search lesson.
