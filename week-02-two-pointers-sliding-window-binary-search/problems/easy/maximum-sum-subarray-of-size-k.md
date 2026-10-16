# Maximum Sum Subarray of Size K

| | |
| --- | --- |
| **Difficulty** | easy |
| **Topics** | sliding window, fixed size |
| **Target time** | 20 minutes |
| **Solution file** | [maximum-sum-subarray-of-size-k.py](maximum-sum-subarray-of-size-k.py) |

## 1. Problem statement

Given an array of integers and an integer `k`, find the maximum sum of any contiguous
subarray of size `k`.

## 2. Constraints

- `1 ≤ n ≤ 10^5`
- `1 ≤ k ≤ n`
- `-10^4 ≤ nums[i] ≤ 10^4`

## 3. Examples

**Example 1**

```text
Input:  nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: subarray [5, 1, 3] has sum 9.
```

**Example 2**

```text
Input:  nums = [2, 3, 4, 1, 5], k = 2
Output: 7
```

**Example 3 — edge case**

```text
Input:  nums = [5], k = 1
Output: 5
```

## 4. Hints

<details><summary>Hint 1 — orientation</summary>
n can be 10^5, so recomputing each window sum is O(nk) — too slow.
</details>
<details><summary>Hint 2 — technique</summary>
Fixed-size window: update the sum by adding the entering element and subtracting the leaving one.
</details>
<details><summary>Hint 3 — structure</summary>

```python
window_sum = sum(nums[:k])
best = window_sum
for i in range(k, len(nums)):
    window_sum += nums[i] - nums[i - k]
    best = max(best, window_sum)
```
</details>

## 5. Brute-force approach

Compute the sum of each window from scratch. O(nk) time, O(1) space.

```python
def max_sum_brute(nums, k):
    best = 0
    for i in range(len(nums) - k + 1):
        best = max(best, sum(nums[i:i + k]))
    return best
```

## 6. Optimised approach

Fixed-size sliding window. Invariant: `window_sum` always equals the sum of the current window.

```python
def max_sum_subarray_k(nums: list[int], k: int) -> int:
    if not nums or k <= 0 or k > len(nums):
        return 0
    window_sum = sum(nums[:k])
    best = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        if window_sum > best:
            best = window_sum
    return best
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `if not nums or k <= 0 or k > len(nums)` | Guard | No valid window |
| `window_sum = sum(nums[:k])` | Initial window | First k elements |
| `best = window_sum` | Seed best | First window is a candidate |
| `for i in range(k, len(nums))` | Slide right edge | i is the entering index |
| `window_sum += nums[i] - nums[i - k]` | Update in O(1) | Add entering, remove leaving |
| `if window_sum > best` | Track best | Update if better |

## 8. Dry run

Input: `nums = [2, 1, 5, 1, 3, 2]`, k = 3.

| Step | Window | `window_sum` | `best` | Note |
| --- | --- | --- | --- | --- |
| 0 | [2,1,5] | 8 | 8 | initial |
| 1 | [1,5,1] | 7 | 8 | +1 -2 |
| 2 | [5,1,3] | 9 | 9 | +3 -1 |
| 3 | [1,3,2] | 6 | 9 | +2 -5 |

## 9. Complexity analysis

| Approach | Time | Space | Reasoning |
| --- | --- | --- | --- |
| Brute force | O(nk) | O(1) | Sum each window from scratch |
| Optimised | O(n) | O(1) | Each element added/removed once |

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| k equals n | `[1, 2, 3]`, k=3 | `6` | Single window |
| k = 1 | `[5]`, k=1 | `5` | Each element its own window |
| Negatives | `[-1, -2, -3]`, k=2 | `-3` | Negative values |
| All equal | `[2, 2, 2]`, k=2 | `4` | Simple case |

```python
def test_basic():
    assert max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3) == 9

def test_k_equals_n():
    assert max_sum_subarray_k([1, 2, 3], 3) == 6
```

## 11. Follow-up questions

1. What if k is not fixed but "at most k"? (Variable window.)
2. What if you need the subarray itself, not just the sum? (Track start index.)
3. What if the array is circular? (Handle wrap-around.)

## 12. Related problems

- `../../exercises/starter-code/max_sum_subarray_k.py` — starter code.
- `../../lessons/sliding-window/sliding-window.md` — fixed window pattern.
