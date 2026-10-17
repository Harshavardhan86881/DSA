# Running Sum of 1D Array

| | |
| --- | --- |
| **Difficulty** | easy |
| **Topics** | arrays, prefix sums, cumulative sum |
| **Target time** | 15 minutes |
| **Solution file** | [running-sum-of-1d-array.py](running-sum-of-1d-array.py) |

## 1. Problem statement

Given a list of integers `nums`, return a list `output` of the same length where
`output[i] = nums[0] + nums[1] + ... + nums[i]`. The input list is not modified.

## 2. Constraints

- `1 ≤ n ≤ 10^5` (an empty list returns an empty list)
- `-10^4 ≤ nums[i] ≤ 10^4`
- Values may be negative.

## 3. Examples

**Example 1**

```text
Input:  [1, 2, 3, 4]
Output: [1, 3, 6, 10]
```

**Example 2**

```text
Input:  [1, 1, 1, 1, 1]
Output: [1, 2, 3, 4, 5]
```

**Example 3 — edge case**

```text
Input:  []
Output: []
```

## 4. Hints (read only after 10 minutes of thinking)

<details>
<summary>Hint 1 — orientation</summary>

n can be 10^5, so an O(n²) approach that recomputes each prefix sum from scratch is too slow.

</details>

<details>
<summary>Hint 2 — technique</summary>

Keep a running total. Each output element is the previous running total plus the current input.

</details>

<details>
<summary>Hint 3 — structure</summary>

```python
total = 0
for value in nums:
    total += value
    output.append(total)
```

</details>

## 5. Brute-force approach

For each index `i`, sum `nums[0..i]` from scratch. Correct but O(n²) time because the inner
sum repeats work. It is useful to state because it shows why the running total helps.

```python
def running_sum_brute(nums):
    output = []
    for i in range(len(nums)):
        s = 0
        for j in range(i + 1):
            s += nums[j]
        output.append(s)
    return output
```

## 6. Optimised approach

Maintain a running total and append it after adding each element. Each element is visited once.

```python
def running_sum(nums: list[int]) -> list[int]:
    output: list[int] = []
    total = 0
    for value in nums:
        total += value
        output.append(total)
    return output
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `output = []` | Empty result list | Will hold n prefix sums |
| `total = 0` | Running sum so far | Starts at zero for an empty prefix |
| `for value in nums` | One pass over input | Keeps time linear |
| `total += value` | Extend the prefix | Reuses previous work instead of recomputing |
| `output.append(total)` | Record current prefix | O(1) amortised append |
| `return output` | Result | Input is untouched |

## 8. Dry run

Input: `[1, 2, 3, 4]`

| Step | `value` | `total` after | `output` after |
| --- | --- | --- | --- |
| 0 | — | 0 | [] |
| 1 | 1 | 1 | [1] |
| 2 | 2 | 3 | [1, 3] |
| 3 | 3 | 6 | [1, 3, 6] |
| 4 | 4 | 10 | [1, 3, 6, 10] |

## 9. Complexity analysis

| Approach | Time | Space | Reasoning |
| --- | --- | --- | --- |
| Brute force | O(n²) | O(n) | Recomputes each prefix from scratch |
| Optimised | O(n) | O(n) | One pass; output list is the extra space |

The output list is counted as extra space because it is newly allocated; the input is not.

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| Empty | `[]` | `[]` | Loop does not run |
| Single | `[5]` | `[5]` | One prefix |
| Negatives | `[-1, 2, -3]` | `[-1, 1, -2]` | Running total can decrease |
| All ones | `[1, 1, 1, 1, 1]` | `[1, 2, 3, 4, 5]` | Simple cumulative check |

```python
def test_basic():
    assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]

def test_empty():
    assert running_sum([]) == []
```

## 11. Follow-up questions

1. How would you answer many range-sum queries on the same array? (Prefix sums, O(1) per query.)
2. Can you do it in place, overwriting the input? What is the space then?
3. What if the array is streamed and you must print prefix sums as they arrive?

## 12. Related problems

- `../../exercises/starter-code/running_sum.py` — starter code.
- `../../lessons/complexity/big-o-complexity.md` — counting the output as space.
