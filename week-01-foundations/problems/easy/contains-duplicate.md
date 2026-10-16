# Contains Duplicate

| | |
| --- | --- |
| **Difficulty** | easy |
| **Topics** | arrays, sets, hashing |
| **Target time** | 15 minutes |
| **Solution file** | [contains-duplicate.py](contains-duplicate.py) |

## 1. Problem statement

Given a list of integers, return `True` if any value appears at least twice, and `False`
otherwise.

## 2. Constraints

- `0 ≤ n ≤ 10^5`
- `-10^9 ≤ nums[i] ≤ 10^9`

## 3. Examples

**Example 1**

```text
Input:  [1, 2, 3, 1]
Output: True
```

**Example 2**

```text
Input:  [1, 2, 3, 4]
Output: False
```

**Example 3 — edge case**

```text
Input:  []
Output: False
```

## 4. Hints

<details><summary>Hint 1 — orientation</summary>
n can be 10^5, so O(n^2) is too slow. You need O(1) membership.
</details>
<details><summary>Hint 2 — technique</summary>
A set remembers values you have seen.
</details>
<details><summary>Hint 3 — structure</summary>

```python
seen = set()
for value in nums:
    if value in seen:
        return True
    seen.add(value)
return False
```
</details>

## 5. Brute-force approach

Compare every pair. O(n^2) time, O(1) space.

```python
def contains_duplicate_brute(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
```

## 6. Optimised approach

Single pass with a set. Invariant: `seen` contains all values from indices before the current one.

```python
def contains_duplicate(nums: list[int]) -> bool:
    seen: set[int] = set()
    for value in nums:
        if value in seen:
            return True
        seen.add(value)
    return False
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `seen = set()` | Empty set | O(1) average membership |
| `if value in seen` | Seen before? | Early return on first duplicate |
| `seen.add(value)` | Record value | Future duplicates caught here |
| `return False` | No duplicate | All values distinct |

## 8. Dry run

Input: `[1, 2, 3, 1]`

| Step | `value` | `seen` before | `value in seen`? | Action |
| --- | --- | --- | --- | --- |
| 1 | 1 | {} | False | add → {1} |
| 2 | 2 | {1} | False | add → {1, 2} |
| 3 | 3 | {1, 2} | False | add → {1, 2, 3} |
| 4 | 1 | {1, 2, 3} | True | return True |

## 9. Complexity analysis

| Approach | Time | Space | Reasoning |
| --- | --- | --- | --- |
| Brute force | O(n^2) | O(1) | Nested loops |
| Optimised | O(n) average | O(n) | One pass; set stores up to n values |

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| Empty | `[]` | `False` | No duplicates possible |
| Single | `[7]` | `False` | One element |
| All equal | `[4, 4, 4]` | `True` | Immediate duplicate |
| All distinct | `[1, 2, 3]` | `False` | No duplicate |
| Negatives | `[-1, -1]` | `True` | Sign does not matter |

```python
def test_basic():
    assert contains_duplicate([1, 2, 3, 1]) is True

def test_distinct():
    assert contains_duplicate([1, 2, 3]) is False
```

## 11. Follow-up questions

1. What if you cannot use extra space? (Sort first, O(n log n) time, O(1) space.)
2. What if values are bounded and the array is mutable? (Sign-flipping trick, O(n) time, O(1) space.)
3. What if you need the index of the duplicate?

## 12. Related problems

- `../../exercises/starter-code/contains_duplicate.py` — starter code.
- `../../lessons/hashing/hashing-dictionaries-sets.md` — duplicate detection pattern.
