# Find First and Last Position of Element in Sorted Array

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | binary search, boundaries |
| **Target time** | 30 minutes |
| **Solution file** | [find-first-and-last-position.py](find-first-and-last-position.py) |

## 1. Problem statement

Given a sorted array `nums` and a `target`, return the starting and ending position of
`target`. If `target` is not found, return `[-1, -1]`. You must write an algorithm with
`O(log n)` runtime.

## 2. Constraints

- `0 ≤ n ≤ 10^5`
- `-10^9 ≤ nums[i], target ≤ 10^9`
- `nums` is sorted in non-decreasing order.

## 3. Examples

**Example 1**

```text
Input:  nums = [5, 7, 7, 8, 8, 10], target = 8
Output: [3, 4]
```

**Example 2**

```text
Input:  nums = [5, 7, 7, 8, 8, 10], target = 6
Output: [-1, -1]
```

**Example 3 — edge case**

```text
Input:  nums = [], target = 0
Output: [-1, -1]
```

## 4. Hints

<details><summary>Hint 1 — orientation</summary>
Standard binary search returns any matching index, not necessarily the first or last.
</details>
<details><summary>Hint 2 — technique</summary>
Run binary search twice: once to find the first occurrence (keep searching left), once for the last (keep searching right).
</details>
<details><summary>Hint 3 — structure</summary>

```python
def first():
    result = -1
    while left <= right:
        if nums[mid] == target:
            result = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result
```
</details>

## 5. Brute-force approach

Linear scan to find the first and last match. O(n) time, O(1) space.

```python
def first_last_brute(nums, target):
    first = last = -1
    for i, v in enumerate(nums):
        if v == target:
            if first == -1:
                first = i
            last = i
    return [first, last]
```

## 6. Optimised approach

Two binary searches: first occurrence and last occurrence.

```python
def first_and_last(nums: list[int], target: int) -> list[int]:
    def first() -> int:
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                result = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    def last() -> int:
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                result = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    if not nums:
        return [-1, -1]
    f = first()
    if f == -1:
        return [-1, -1]
    return [f, last()]
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `first()` records match and searches left | Finds leftmost | `right = mid - 1` |
| `last()` records match and searches right | Finds rightmost | `left = mid + 1` |
| `if not nums` | Handle empty | Avoid indexing |
| `if f == -1` | Not found | Skip second search |
| `return [f, last()]` | Both boundaries | First and last indices |

## 8. Dry run

Input: `nums = [5, 7, 7, 8, 8, 10]`, target = 8.

First search: finds index 3, then searches left (none), returns 3.
Last search: finds index 3, then searches right, finds 4, returns 4.
Result: `[3, 4]`.

## 9. Complexity analysis

| Approach | Time | Space | Reasoning |
| --- | --- | --- | --- |
| Brute force | O(n) | O(1) | Linear scan |
| Optimised | O(log n) | O(1) | Two binary searches |

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| Not found | `[5,7,7,8,8,10]`, 6 | `[-1,-1]` | Target absent |
| Empty | `[]`, 0 | `[-1,-1]` | No elements |
| Single present | `[1]`, 1 | `[0,0]` | One element |
| All same | `[2,2,2]`, 2 | `[0,2]` | All match |
| Single occurrence | `[1,2,3]`, 2 | `[1,1]` | One match |

```python
def test_basic():
    assert first_and_last([5, 7, 7, 8, 8, 10], 8) == [3, 4]

def test_not_found():
    assert first_and_last([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
```

## 11. Follow-up questions

1. How would you count occurrences using these boundaries?
2. What if the array is not sorted? (Sort first or use hashing.)
3. How does this relate to lower/upper bound?

## 12. Related problems

- `../../exercises/starter-code/first_last_occurrence.py` — starter code.
- `../../lessons/binary-search/binary-search.md` — boundaries.
