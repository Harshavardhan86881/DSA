# Find Peak Element

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | binary search, arrays |
| **Target time** | 20 minutes |
| **Solution file** | [find-peak-element.py](find-peak-element.py) |

## 1. Problem statement

Given an array `nums`, find a peak element and return its index. A peak element is one that
is strictly greater than its neighbours. You may imagine `nums[-1] = nums[n] = -∞`.

## 2. Constraints

- `1 ≤ nums.length ≤ 10^5`
- `-2^31 ≤ nums[i] ≤ 2^31 - 1`
- Multiple peaks may exist; return any.

## 3. Examples

**Example 1**

```text
Input:  [1, 2, 3, 1]
Output: 2
```

**Example 2**

```text
Input:  [1, 2, 1, 3, 5, 6, 4]
Output: 1 or 5
```

**Example 3 — edge case**

```text
Input:  [1]
Output: 0
```

## 4. Hints

<details><summary>Hint 1</summary>
Compare mid with mid+1 to decide which half must contain a peak.
</details>
<details><summary>Hint 2</summary>
If nums[mid] > nums[mid+1], a peak is in the left half including mid.
</details>

## 5. Brute-force approach

Scan for an index greater than both neighbours. O(n) time.

## 6. Optimised approach

Binary search on the slope. O(log n) time, O(1) space.

```python
def find_peak_element(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left
```

## 7. Complexity analysis

| Approach | Time | Space |
| --- | --- | --- |
| Brute force | O(n) | O(1) |
| Optimised | O(log n) | O(1) |

## 8. Edge cases and tests

| Case | Input | Expected |
| --- | --- | --- |
| Single | `[1]` | `0` |
| Increasing | `[1, 2, 3]` | `2` |
| Decreasing | `[3, 2, 1]` | `0` |

```python
def test_basic():
    assert find_peak_element([1, 2, 3, 1]) == 2

def test_single():
    assert find_peak_element([1]) == 0
```

## 9. Follow-up questions

1. Why does the binary search guarantee a peak exists?
2. Can you find the global maximum instead?
3. How would you handle plateaus (equal neighbours)?

## 10. Related problems

- `../../exercises/starter-code/find_peak_element.py` — starter code.
- `../../lessons/pattern-selection/pattern-selection.md` — pattern selection.
