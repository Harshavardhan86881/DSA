# Find the Second-Largest Distinct Element

| | |
| --- | --- |
| **Difficulty** | easy |
| **Topics** | arrays, single pass, tracking two values |
| **Target time** | 25 minutes |
| **Solution file** | [find-the-second-largest-distinct-element.py](find-the-second-largest-distinct-element.py) |

## 1. Problem statement

Given a list of integers, return the **second-largest distinct value**. If there is no such value
(fewer than two distinct values), return `None`. Do not sort the list.

## 2. Constraints

- `0 ≤ n ≤ 10^5`
- `-10^4 ≤ nums[i] ≤ 10^4`
- The input may contain duplicates.

## 3. Examples

**Example 1**

```text
Input:  [3, 1, 4, 4, 2]
Output: 3
Explanation: distinct values are {1, 2, 3, 4}; second largest is 3.
```

**Example 2**

```text
Input:  [5, 5, 5]
Output: None
```

**Example 3 — edge case**

```text
Input:  []
Output: None
```

## 4. Hints (read only after 10 minutes of thinking)

<details>
<summary>Hint 1 — orientation</summary>

n can be 10^5, so sorting (O(n log n)) works but the intended solution is O(n). Think single pass.

</details>

<details>
<summary>Hint 2 — technique</summary>

Track two values while scanning: the largest and the second largest seen so far.

</details>

<details>
<summary>Hint 3 — structure</summary>

When a new largest appears, the old largest becomes the candidate for second. When a value is
between the two trackers, it updates second. Skip values equal to the largest.

</details>

## 5. Brute-force approach

Sort a copy of the list and scan from the end for the first value smaller than the maximum.
Correct and simple, but O(n log n) time and O(n) space for the copy. It also mutates nothing
if you copy first.

```python
def second_largest_brute(nums):
    if len(set(nums)) < 2:
        return None
    distinct = sorted(set(nums))
    return distinct[-2]
```

## 6. Optimised approach

Single pass with two trackers. The invariant: after processing each element, `largest` and
`second` hold the largest and second-largest distinct values seen so far (or `None`).

```python
def second_largest(nums: list[int]) -> int | None:
    if len(nums) < 2:
        return None
    largest = second = None
    for value in nums:
        if largest is None or value > largest:
            second = largest
            largest = value
        elif value != largest and (second is None or value > second):
            second = value
    return second
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `if len(nums) < 2` | Early exit | Need at least two elements for a second value |
| `largest = second = None` | Two trackers | One pass is enough if we keep both |
| `if largest is None or value > largest` | New maximum | Old maximum becomes second best |
| `elif value != largest and ...` | Candidate for second | Must differ from largest to be distinct |
| `return second` | Result after full scan | `None` means no distinct second value |

## 8. Dry run

Input: `[3, 1, 4, 4, 2]`

| Step | `value` | `largest` | `second` | Note |
| --- | --- | --- | --- | --- |
| 0 | — | None | None | initial |
| 1 | 3 | 3 | None | first element becomes largest |
| 2 | 1 | 3 | 1 | 1 is below largest, above second (None) |
| 3 | 4 | 4 | 3 | new largest; old largest (3) becomes second |
| 4 | 4 | 4 | 3 | equal to largest, skipped |
| 5 | 2 | 4 | 3 | 2 is below largest and below second (3) |

## 9. Complexity analysis

| Approach | Time | Space | Reasoning |
| --- | --- | --- | --- |
| Brute force (sort distinct) | O(n log n) | O(n) | Sorting dominates |
| Optimised (two trackers) | O(n) | O(1) | Single pass, two variables |

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| Empty | `[]` | `None` | No elements |
| Single | `[9]` | `None` | No second value |
| All equal | `[5, 5, 5]` | `None` | No distinct second value |
| Negatives | `[-1, -3, -2]` | `-2` | Sign does not affect ordering |
| Two distinct | `[1, 2]` | `1` | Smallest possible meaningful input |

```python
def test_basic():
    assert second_largest([3, 1, 4, 4, 2]) == 3

def test_all_equal():
    assert second_largest([5, 5, 5]) is None
```

## 11. Follow-up questions

1. What if the input is a stream and you cannot store it? (The same trackers still work.)
2. How would you generalise to the k-th largest distinct value?
3. What changes if duplicates should count (second largest, not second-largest distinct)?

## 12. Related problems

- `../../exercises/starter-code/second_largest.py` — starter code.
- `../../lessons/problem-solving/problem-solving-foundations.md` — single-pass tracking.
