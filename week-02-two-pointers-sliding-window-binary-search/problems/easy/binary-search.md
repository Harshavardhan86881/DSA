# Binary Search

| | |
| --- | --- |
| **Difficulty** | easy |
| **Topics** | binary search, arrays |
| **Target time** | 20 minutes |
| **Solution file** | [binary-search.py](binary-search.py) |

## 1. Problem statement

Given a sorted array of integers `nums` and a `target`, return the index of `target` if it is
in `nums`, otherwise return `-1`. You must write an algorithm with `O(log n)` runtime.

## 2. Constraints

- `1 ≤ n ≤ 10^4`
- `-10^4 ≤ nums[i], target ≤ 10^4`
- `nums` is sorted in ascending order.

## 3. Examples

**Example 1**

```text
Input:  nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
```

**Example 2**

```text
Input:  nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
```

**Example 3 — edge case**

```text
Input:  nums = [5], target = 5
Output: 0
```

## 4. Hints

<details><summary>Hint 1 — orientation</summary>
The array is sorted, so you can discard half of the remaining elements each step.
</details>
<details><summary>Hint 2 — technique</summary>
Maintain an inclusive interval [left, right]. Compute the midpoint and compare.
</details>
<details><summary>Hint 3 — structure</summary>

```python
left, right = 0, len(nums) - 1
while left <= right:
    mid = left + (right - left) // 2
    if nums[mid] == target: return mid
    if nums[mid] < target: left = mid + 1
    else: right = mid - 1
return -1
```
</details>

## 5. Brute-force approach

Linear scan. O(n) time, O(1) space. Correct but does not meet the O(log n) requirement.

```python
def binary_search_brute(nums, target):
    for i, v in enumerate(nums):
        if v == target:
            return i
    return -1
```

## 6. Optimised approach

Standard binary search with inclusive bounds.

```python
def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `left, right = 0, len(nums) - 1` | Full inclusive interval | Both ends are candidates |
| `while left <= right` | Loop while non-empty | Empty interval means not found |
| `mid = left + (right - left) // 2` | Safe midpoint | Avoids overflow |
| `if nums[mid] == target: return mid` | Found | Any matching index is fine |
| `if nums[mid] < target: left = mid + 1` | Target to the right | Discard mid and left part |
| `else: right = mid - 1` | Target to the left | Discard mid and right part |
| `return -1` | Not found | Interval exhausted |

## 8. Dry run

Input: `nums = [-1, 0, 3, 5, 9, 12]`, target = 9.

| Step | `left` | `right` | `mid` | `nums[mid]` | Action |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 5 | 2 | 3 | 3 < 9 → left = 3 |
| 1 | 3 | 5 | 4 | 9 | match → return 4 |

## 9. Complexity analysis

| Approach | Time | Space | Reasoning |
| --- | --- | --- | --- |
| Brute force | O(n) | O(1) | Linear scan |
| Optimised | O(log n) | O(1) | Interval halves each step |

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| Empty | `[]`, target 5 | `-1` | No elements |
| Single present | `[5]`, target 5 | `0` | One element |
| Single absent | `[5]`, target 3 | `-1` | One element |
| First element | `[-1,0,3]`, target -1 | `0` | Left boundary |
| Last element | `[-1,0,3]`, target 3 | `2` | Right boundary |
| Duplicates | `[2,2,2]`, target 2 | `1` (any) | Any matching index |

```python
def test_basic():
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4

def test_not_found():
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
```

## 11. Follow-up questions

1. How would you find the first occurrence instead of any?
2. What if the array is not sorted? (Sort first, O(n log n).)
3. How does the recursive version differ in space?

## 12. Related problems

- `../../exercises/starter-code/binary_search.py` — starter code.
- `../../lessons/binary-search/binary-search.md` — the full lesson.
