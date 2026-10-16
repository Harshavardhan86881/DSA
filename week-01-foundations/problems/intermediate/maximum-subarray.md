# Maximum Subarray

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | arrays, prefix sums, running sum |
| **Target time** | 25 minutes |
| **Solution file** | [maximum-subarray.py](maximum-subarray.py) |

## 1. Problem statement

Given a list of integers (which may contain negatives), find the maximum sum of any contiguous
subarray. Return 0 for an empty list.

## 2. Constraints

- `0 ≤ n ≤ 10^5`
- `-10^4 ≤ nums[i] ≤ 10^4`

## 3. Examples

**Example 1**

```text
Input:  [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: subarray [4, -1, 2, 1] has sum 6.
```

**Example 2**

```text
Input:  [1]
Output: 1
```

**Example 3 — edge case**

```text
Input:  [-1, -2, -3]
Output: -1
```

## 4. Hints

<details><summary>Hint 1 — orientation</summary>
n can be 10^5, so O(n^2) is too slow. You need one pass.
</details>
<details><summary>Hint 2 — technique</summary>
Keep a running sum. If it goes negative, reset it to the current element, because a negative prefix cannot help.
</details>
<details><summary>Hint 3 — structure</summary>

```python
best = running = nums[0]
for value in nums[1:]:
    running = max(value, running + value)
    best = max(best, running)
return best
```
</details>

## 5. Brute-force approach

Try every subarray and take the maximum sum. O(n^2) time, O(1) space.

```python
def max_subarray_brute(nums):
    best = 0 if not nums else nums[0]
    for i in range(len(nums)):
        running = 0
        for j in range(i, len(nums)):
            running += nums[j]
            if running > best:
                best = running
    return best
```

## 6. Optimised approach

Single pass tracking the best sum ending at the current position. Invariant: after processing
index `i`, `running` is the maximum sum of a subarray ending at `i` (or just `nums[i]` if
extending would be worse), and `best` is the maximum over all endings so far.

```python
def max_subarray(nums: list[int]) -> int:
    if not nums:
        return 0
    best = running = nums[0]
    for value in nums[1:]:
        running = max(value, running + value)
        best = max(best, running)
    return best
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `if not nums` | Handle empty input | Return 0 |
| `best = running = nums[0]` | Seed both trackers | First element is the only candidate |
| `running = max(value, running + value)` | Reset or extend | Negative running sum cannot help |
| `best = max(best, running)` | Update global best | Tracks the maximum seen |
| `return best` | Result | Works for all-negative input |

## 8. Dry run

Input: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`

| Step | `value` | `running` | `best` | Note |
| --- | --- | --- | --- | --- |
| 0 | -2 | -2 | -2 | seed |
| 1 | 1 | 1 | 1 | reset: 1 > -2+1 |
| 2 | -3 | -2 | 1 | max(-3, 1-3=-2) = -2 |
| 3 | 4 | 4 | 4 | reset: 4 > -2+4=2 |
| 4 | -1 | 3 | 4 | extend |
| 5 | 2 | 5 | 5 | extend |
| 6 | 1 | 6 | 6 | extend, new best |
| 7 | -5 | 1 | 6 | extend |
| 8 | 4 | 5 | 6 | extend |

## 9. Complexity analysis

| Approach | Time | Space | Reasoning |
| --- | --- | --- | --- |
| Brute force | O(n^2) | O(1) | Nested loops over subarrays |
| Optimised | O(n) | O(1) | Single pass, two variables |

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| Empty | `[]` | `0` | No subarray |
| Single | `[5]` | `5` | One element |
| All negative | `[-1, -2, -3]` | `-1` | Must return the largest (least negative) |
| All positive | `[1, 2, 3]` | `6` | Whole array |
| Mixed | `[-2, 1, -3, 4, -1, 2, 1, -5, 4]` | `6` | Standard case |

```python
def test_basic():
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_negative():
    assert max_subarray([-1, -2, -3]) == -1
```

## 11. Follow-up questions

1. What if you must return the subarray itself, not just the sum? (Track start/end indices.)
2. What if the array is circular? (Handle wrap-around separately.)
3. What if you can delete at most one element? (Track two running sums.)

## 12. Related problems

- `../../exercises/starter-code/maximum_subarray.py` — starter code.
- `../../lessons/prefix-sums/prefix-sums-and-range-queries.md` — running sum pattern.
