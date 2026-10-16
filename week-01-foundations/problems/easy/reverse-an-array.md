# Reverse an Array

| | |
| --- | --- |
| **Difficulty** | easy |
| **Topics** | arrays, two pointers, in-place |
| **Target time** | 20 minutes |
| **Solution file** | [reverse-an-array.py](reverse-an-array.py) |

## 1. Problem statement

Given a list of integers, reverse the order of its elements **in place** and return nothing
(the list itself is modified). Do not allocate a second list proportional to the input size.

## 2. Constraints

- `0 ≤ n ≤ 10^5`
- `-10^4 ≤ nums[i] ≤ 10^4`
- The input may be empty.

## 3. Examples

**Example 1**

```text
Input:  [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
```

**Example 2**

```text
Input:  [1, 2]
Output: [2, 1]
```

**Example 3 — edge case**

```text
Input:  []
Output: []
```

## 4. Hints (read only after 10 minutes of thinking)

<details>
<summary>Hint 1 — orientation</summary>

n can be 10^5, so any approach that builds a second list of size n is acceptable for time but
not for the in-place requirement. Focus on swapping.

</details>

<details>
<summary>Hint 2 — technique</summary>

Two pointers: one at the start, one at the end. Swap and move them toward the middle.

</details>

<details>
<summary>Hint 3 — structure</summary>

```python
left, right = 0, len(nums) - 1
while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1
```

</details>

## 5. Brute-force approach

The simplest correct idea is to build a new list by reading the input from the end to the start.
It is correct and O(n) time, but uses O(n) extra space, so it does not satisfy the in-place
requirement. It is still worth stating because it is the first idea most people have.

```python
def reverse_brute(nums):
    result = []
    for i in range(len(nums) - 1, -1, -1):
        result.append(nums[i])
    # copy back so the original list is updated
    for i in range(len(nums)):
        nums[i] = result[i]
```

## 6. Optimised approach

Swap elements symmetrically around the centre using two pointers. The invariant: after each swap,
the elements outside `[left, right]` are already in their final positions. Stop when `left >= right`,
which also handles odd lengths (the middle element stays put).

```python
def reverse_in_place(nums: list[int]) -> None:
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `left, right = 0, len(nums) - 1` | Pointers at both ends | Covers every symmetric pair once |
| `while left < right` | Loop while a pair remains | `<` skips the middle element for odd lengths |
| `nums[left], nums[right] = ...` | Swap the two values | Tuple assignment needs no temporary variable |
| `left += 1; right -= 1` | Shrink the unprocessed middle | Moves toward the centre |

## 8. Dry run

Input: `[1, 2, 3, 4, 5]`

| Step | `left` | `right` | List after step | Note |
| --- | --- | --- | --- | --- |
| 0 | 0 | 4 | [1, 2, 3, 4, 5] | initial |
| 1 | 1 | 3 | [5, 2, 3, 4, 1] | swap 1 and 5 |
| 2 | 2 | 2 | [5, 4, 3, 2, 1] | swap 2 and 4 |
| 3 | 2 | 2 | [5, 4, 3, 2, 1] | left >= right, stop |

## 9. Complexity analysis

| Approach | Time | Space | Reasoning |
| --- | --- | --- | --- |
| Brute force (new list) | O(n) | O(n) | One pass to build, one pass to copy |
| Optimised (two pointers) | O(n) | O(1) | n/2 swaps, only two index variables |

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| Empty | `[]` | `[]` | Loop must not run; no index error |
| Single element | `[7]` | `[7]` | Middle element stays put |
| Two elements | `[1, 5]` | `[5, 1]` | One swap |
| All equal | `[4, 4, 4]` | `[4, 4, 4]` | Swapping equal values is harmless |
| Negatives | `[-3, 0, 2]` | `[2, 0, -3]` | Sign does not affect swapping |

```python
# tests (pytest style, standard library only)
def test_basic():
    data = [1, 2, 3, 4, 5]
    reverse_in_place(data)
    assert data == [5, 4, 3, 2, 1]

def test_empty():
    data = []
    reverse_in_place(data)
    assert data == []
```

## 11. Follow-up questions

1. How would you reverse only a sub-array between indices `i` and `j`?
2. Can you do it with a single pointer and arithmetic on indices?
3. What changes if the input is a string (immutable in Python)?

## 12. Related problems

- `../../exercises/starter-code/reverse_array.py` — starter code for this problem.
- `../../lessons/problem-solving/problem-solving-foundations.md` — two-pointer pattern.
