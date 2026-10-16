# Majority Element

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | arrays, hashing, counting |
| **Target time** | 25 minutes |
| **Solution file** | [majority-element.py](majority-element.py) |

## 1. Problem statement

Given a list of integers, return the element that appears **more than** `n / 2` times, where `n`
is the length of the list. If no such element exists, return `None`.

## 2. Constraints

- `0 ≤ n ≤ 10^5`
- `-10^9 ≤ nums[i] ≤ 10^9`

## 3. Examples

**Example 1**

```text
Input:  [3, 2, 3]
Output: 3
```

**Example 2**

```text
Input:  [2, 2, 1, 1, 1, 2, 2]
Output: 2
```

**Example 3 — edge case**

```text
Input:  [1, 2, 3]
Output: None
```

## 4. Hints

<details><summary>Hint 1 — orientation</summary>
n can be 10^5. A brute force that calls count for each candidate is O(n^2).
</details>
<details><summary>Hint 2 — technique</summary>
Count every value in one pass with a dict, then check the threshold.
</details>
<details><summary>Hint 3 — structure</summary>

```python
counts = {}
for value in nums:
    counts[value] = counts.get(value, 0) + 1
for value, count in counts.items():
    if count > len(nums) // 2:
        return value
return None
```
</details>

## 5. Brute-force approach

For each distinct candidate, count its occurrences with `nums.count`. O(n^2) time, O(1) space.

```python
def majority_brute(nums):
    for candidate in nums:
        if nums.count(candidate) > len(nums) // 2:
            return candidate
    return None
```

## 6. Optimised approach

Count all values in one pass, then scan the distinct values. Invariant: after the first pass,
`counts` holds the exact frequency of every value.

```python
def majority_element(nums: list[int]) -> int | None:
    if not nums:
        return None
    counts: dict[int, int] = {}
    for value in nums:
        counts[value] = counts.get(value, 0) + 1
    for value, count in counts.items():
        if count > len(nums) // 2:
            return value
    return None
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `if not nums` | Handle empty input | Avoids indexing an empty list |
| `counts[value] = ...` | Increment count | One pass over the input |
| `for value, count in counts.items()` | Scan distinct values | At most n distinct values |
| `if count > len(nums) // 2` | Majority threshold | More than half |
| `return value` | Found majority | Only one value can exceed n/2 |
| `return None` | No majority | Threshold never met |

## 8. Dry run

Input: `[3, 2, 3]`

| Step | `value` | `counts` after |
| --- | --- | --- |
| 1 | 3 | {3: 1} |
| 2 | 2 | {3: 1, 2: 1} |
| 3 | 3 | {3: 2, 2: 1} |

Then scan: 3 has count 2 > 1 (3//2), so return 3.

## 9. Complexity analysis

| Approach | Time | Space | Reasoning |
| --- | --- | --- | --- |
| Brute force | O(n^2) | O(1) | `count` scans per candidate |
| Optimised | O(n) | O(n) | One pass to count, one pass over distinct values |

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| Empty | `[]` | `None` | No majority |
| Single | `[5]` | `5` | The single element is the majority |
| No majority | `[1, 2, 3]` | `None` | Threshold never met |
| All equal | `[4, 4, 4]` | `4` | Trivial majority |
| Negatives | `[-1, -1, 2]` | `-1` | Sign does not matter |

```python
def test_basic():
    assert majority_element([3, 2, 3]) == 3

def test_none():
    assert majority_element([1, 2, 3]) is None
```

## 11. Follow-up questions

1. Can you solve it in O(n) time and O(1) space? (Boyer-Moore voting algorithm.)
2. What if the threshold is n/3 instead of n/2? (Generalise to two candidates.)
3. What if you need all elements appearing more than n/3 times?

## 12. Related problems

- `../../exercises/starter-code/majority_element.py` — starter code.
- `../../lessons/hashing/hashing-dictionaries-sets.md` — frequency counting pattern.
