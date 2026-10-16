# Minimum Size Subarray Sum

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | sliding window, variable size, arrays |
| **Target time** | 25 minutes |
| **Solution file** | [minimum-size-subarray-sum.py](minimum-size-subarray-sum.py) |

## 1. Problem statement

Given an array of positive integers `nums` and a positive integer `target`, return the
minimal length of a contiguous subarray whose sum is greater than or equal to `target`.
If there is no such subarray, return `0`.

## 2. Constraints

- `1 ≤ target ≤ 10^9`
- `1 ≤ n ≤ 10^5`
- `1 ≤ nums[i] ≤ 10^4` (all positive)

## 3. Examples

**Example 1**

```text
Input:  target = 7, nums = [2, 3, 1, 2, 4, 3]
Output: 2
Explanation: subarray [4, 3] has sum 7 and length 2.
```

**Example 2**

```text
Input:  target = 4, nums = [1, 4, 4]
Output: 1
```

**Example 3 — edge case**

```text
Input:  target = 100, nums = [1, 2, 3]
Output: 0
```

## 4. Hints

<details><summary>Hint 1 — orientation</summary>
All numbers are positive, so growing the window increases the sum and shrinking decreases it. This monotonicity enables a sliding window.
</details>
<details><summary>Hint 2 — technique</summary>
Grow right until the sum reaches target, then shrink left as much as possible while still reaching target.
</details>
<details><summary>Hint 3 — structure</summary>

```python
left = 0
running = 0
best = inf
for right in range(len(nums)):
    running += nums[right]
    while running >= target:
        best = min(best, right - left + 1)
        running -= nums[left]
        left += 1
```
</details>

## 5. Brute-force approach

Check every subarray. O(n²) time, O(1) space.

```python
def min_len_brute(target, nums):
    best = float("inf")
    for i in range(len(nums)):
        running = 0
        for j in range(i, len(nums)):
            running += nums[j]
            if running >= target:
                best = min(best, j - i + 1)
                break
    return 0 if best == float("inf") else best
```

## 6. Optimised approach

Variable-size sliding window. Invariant: when the inner loop exits, `running < target` (or left > right).

```python
def min_subarray_len(target: int, nums: list[int]) -> int:
    left = 0
    running = 0
    best = float("inf")
    for right in range(len(nums)):
        running += nums[right]
        while running >= target:
            if right - left + 1 < best:
                best = right - left + 1
            running -= nums[left]
            left += 1
    return 0 if best == float("inf") else int(best)
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `left = 0` | Left edge | Shrinks when possible |
| `running = 0` | Window sum | Grows/shrinks with edges |
| `best = inf` | Best length so far | Updated on valid windows |
| `running += nums[right]` | Grow window | Add entering element |
| `while running >= target` | Condition met | Try to shrink |
| `best = min(best, right - left + 1)` | Update best | Record valid window length |
| `running -= nums[left]; left += 1` | Shrink | Remove leaving element |
| `return 0 if best == inf else int(best)` | No valid window | Handle impossible case |

## 8. Dry run

Input: target = 7, nums = [2, 3, 1, 2, 4, 3].

| Step | `right` | `nums[right]` | `running` | `left` | `best` | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 2 | 2 | 0 | inf | grow |
| 1 | 1 | 3 | 5 | 0 | inf | grow |
| 2 | 2 | 1 | 6 | 0 | inf | grow |
| 3 | 3 | 2 | 8 | 0 | 4 | shrink: 8>=7, best=4, remove 2, left=1, running=6 |
| 4 | 4 | 4 | 10 | 1 | 2 | shrink: best=2, ... |
| 5 | 5 | 3 | ... | ... | 2 | final best 2 |

## 9. Complexity analysis

| Approach | Time | Space | Reasoning |
| --- | --- | --- | --- |
| Brute force | O(n²) | O(1) | Nested loops |
| Optimised | O(n) | O(1) | Both pointers advance at most n |

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| No valid window | target=100, [1,2,3] | `0` | Sum never reaches target |
| Single element enough | target=4, [1,4,4] | `1` | One element suffices |
| Whole array | target=10, [1,2,3,4] | `4` | Need all elements |
| Large target | target=15, [1,2,3,4,5] | `5` | All elements |

```python
def test_basic():
    assert min_subarray_len(7, [2, 3, 1, 2, 4, 3]) == 2

def test_none():
    assert min_subarray_len(100, [1, 2, 3]) == 0
```

## 11. Follow-up questions

1. What if numbers can be negative? (Sliding window no longer works; use prefix sums + binary search.)
2. What if you need the subarray itself? (Track left/right indices.)
3. What if target is very large? (Use 64-bit integers; Python handles automatically.)

## 12. Related problems

- `../../exercises/starter-code/minimum_size_subarray_sum.py` — starter code.
- `../../lessons/sliding-window/sliding-window.md` — variable window pattern.
