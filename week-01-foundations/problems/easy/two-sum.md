# Two Sum

| | |
| --- | --- |
| **Difficulty** | easy |
| **Topics** | arrays, hash map, complements |
| **Target time** | 25 minutes |
| **Solution file** | [two-sum.py](two-sum.py) |

## 1. Problem statement

Given a list of integers `nums` and an integer `target`, return the **indices** of the two
numbers such that they add up to `target`. You may assume that exactly one solution exists and
that you may not use the same element twice. Return the indices in any order.

## 2. Constraints

- `2 ≤ n ≤ 10^4` (this instance; the pattern scales to 10^5+)
- `-10^9 ≤ nums[i] ≤ 10^9`
- `-10^9 ≤ target ≤ 10^9`
- Exactly one valid pair exists.

## 3. Examples

**Example 1**

```text
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9.
```

**Example 2**

```text
Input:  nums = [3, 2, 4], target = 6
Output: [1, 2]
```

**Example 3 — edge case**

```text
Input:  nums = [3, 3], target = 6
Output: [0, 1]
```

## 4. Hints (read only after 10 minutes of thinking)

<details>
<summary>Hint 1 — orientation</summary>

n can be 10^4 or larger, so checking every pair (O(n²)) is too slow. You need a way to
answer "have I seen the complement?" in O(1).

</details>

<details>
<summary>Hint 2 — technique</summary>

A hash map maps a value to its index. For each element, the complement is `target - value`.

</details>

<details>
<summary>Hint 3 — structure</summary>

```python
seen = {}
for i, value in enumerate(nums):
    complement = target - value
    if complement in seen:
        return [seen[complement], i]
    seen[value] = i
```

</details>

## 5. Brute-force approach

Check every pair `(i, j)` with `i < j`. Correct and simple, but O(n²) time and O(1) space.
It is the natural first idea and shows why the hash map helps.

```python
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

## 6. Optimised approach

Single pass with a hash map of value → index. The invariant: after processing index `i`, `seen`
contains every value from indices `0..i` with its index. For the current value, if its complement
is already in `seen`, the pair is found.

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for i, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], i]
        seen[value] = i
    raise ValueError("no solution found")
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `seen = {}` | Empty value→index map | O(1) lookups later |
| `for i, value in enumerate(nums)` | One pass with index | Need the index in the answer |
| `complement = target - value` | The partner value needed | Derived from the target |
| `if complement in seen` | Have we seen the partner? | O(1) average lookup |
| `return [seen[complement], i]` | Found the pair | Indices in increasing order |
| `seen[value] = i` | Record current value | Future complements can find it |

## 8. Dry run

Input: `nums = [2, 7, 11, 15]`, `target = 9`

| Step | `i` | `value` | `complement` | `seen` after | Decision |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 2 | 7 | {2: 0} | 7 not seen |
| 1 | 1 | 7 | 2 | {2: 0, 7: 1} | 2 seen → return [0, 1] |

## 9. Complexity analysis

| Approach | Time | Space | Reasoning |
| --- | --- | --- | --- |
| Brute force | O(n²) | O(1) | Nested loops |
| Optimised | O(n) average | O(n) | One pass; map stores up to n entries |

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| Minimum input | `[1, 2]`, target 3 | `[0, 1]` | Smallest valid input |
| Duplicate values | `[3, 3]`, target 6 | `[0, 1]` | Same value used at two indices |
| Negatives | `[-1, 2, 0]`, target 1 | `[0, 1]` | Negative numbers |
| Large values | within constraints | valid indices | No overflow in Python |

```python
def test_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_duplicates():
    assert two_sum([3, 3], 6) == [0, 1]
```

## 11. Follow-up questions

1. What if the array is sorted? (Two pointers, O(n) time, O(1) space.)
2. What if there are multiple valid pairs? (Return all, or the first.)
3. What if the input is a stream and you cannot store all of it? (The same map still works
   for finding one pair, but memory grows.)

## 12. Related problems

- `../../exercises/starter-code/two_sum.py` — starter code.
- `../../lessons/arrays/arrays-and-lists.md` — list operations and traversal.
