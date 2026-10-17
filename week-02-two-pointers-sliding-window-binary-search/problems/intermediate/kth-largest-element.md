# Kth Largest Element in an Array

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | sorting, selection |
| **Target time** | 20 minutes |
| **Solution file** | [kth-largest-element.py](kth-largest-element.py) |

## 1. Problem statement

Given an integer array `nums` and an integer `k`, return the `k`th largest element in the
array (1-indexed).

## 2. Constraints

- `1 ≤ k ≤ nums.length ≤ 10^5`
- `-10^4 ≤ nums[i] ≤ 10^4`

## 3. Examples

**Example 1**

```text
Input:  nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5
```

**Example 2**

```text
Input:  nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output: 4
```

**Example 3 — edge case**

```text
Input:  nums = [1], k = 1
Output: 1
```

## 4. Hints

<details><summary>Hint 1</summary>
Sorting descending makes the answer the element at index k-1.
</details>
<details><summary>Hint 2</summary>
For O(n) average, use quickselect; sorting is acceptable here.
</details>

## 5. Brute-force approach

Sort ascending and pick index n-k. O(n log n) time.

## 6. Optimised approach

Sort descending and return index k-1. O(n log n) time, O(n) space (new list).

```python
def find_kth_largest(nums: list[int], k: int) -> int:
    nums_sorted = sorted(nums, reverse=True)
    return nums_sorted[k - 1]
```

## 7. Complexity analysis

| Approach | Time | Space |
| --- | --- | --- |
| Sorting | O(n log n) | O(n) |
| Quickselect (avg) | O(n) | O(1) |

## 8. Edge cases and tests

| Case | Input | Expected |
| --- | --- | --- |
| Single | `[1], 1` | `1` |
| Duplicates | `[3, 3, 3], 2` | `3` |
| k = n | `[1, 2, 3], 3` | `1` |

```python
def test_basic():
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5

def test_single():
    assert find_kth_largest([1], 1) == 1
```

## 9. Follow-up questions

1. How would quickselect work?
2. What is the worst-case complexity of quickselect?
3. Can you do it with a min-heap of size k?

## 10. Related problems

- `../../exercises/starter-code/kth_largest_element.py` — starter code.
- `../../lessons/sorting-patterns/sorting-as-a-pattern.md` — sorting pattern.
