# Remove Duplicates from Sorted Array

| | |
| --- | --- |
| **Difficulty** | easy |
| **Topics** | two pointers, in-place, arrays |
| **Target time** | 20 minutes |
| **Solution file** | [remove-duplicates-from-sorted-array.py](remove-duplicates-from-sorted-array.py) |

## 1. Problem statement

Given a sorted array `nums`, remove the duplicates **in place** so that each unique element
appears only once. The relative order is preserved. Return `k`, the number of unique elements.
The first `k` elements of `nums` should hold the result.

## 2. Constraints

- `0 ≤ n ≤ 3 * 10^4`
- `-100 ≤ nums[i] ≤ 100`
- `nums` is sorted in non-decreasing order.

## 3. Examples

**Example 1**

```text
Input:  [1, 1, 2]
Output: 2, nums = [1, 2, _]
```

**Example 2**

```text
Input:  [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
```

**Example 3 — edge case**

```text
Input:  []
Output: 0
```

## 4. Hints

<details><summary>Hint 1 — orientation</summary>
The array is sorted, so duplicates are adjacent. You can compact in one pass.
</details>
<details><summary>Hint 2 — technique</summary>
Use a write pointer. Only write when the current value differs from the last kept value.
</details>
<details><summary>Hint 3 — structure</summary>

```python
write = 1
for read in range(1, len(nums)):
    if nums[read] != nums[write - 1]:
        nums[write] = nums[read]
        write += 1
return write
```
</details>

## 5. Brute-force approach

Build a new list of unique values, then copy back. O(n) time and O(n) space.

```python
def remove_duplicates_brute(nums):
    unique = []
    for v in nums:
        if not unique or v != unique[-1]:
            unique.append(v)
    for i in range(len(unique)):
        nums[i] = unique[i]
    return len(unique)
```

## 6. Optimised approach

Same-direction read/write pointers. Invariant: `nums[0..write-1]` holds the unique values in
order.

```python
def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `if not nums` | Handle empty | Avoid indexing |
| `write = 1` | First element kept | write is next free slot |
| `for read in range(1, len(nums))` | Scan from index 1 | read visits each element once |
| `if nums[read] != nums[write - 1]` | New value? | Compare with last kept |
| `nums[write] = nums[read]` | Keep it | Write into next free slot |
| `write += 1` | Advance write | Next kept goes after |
| `return write` | New length | Trailing slots are stale |

## 8. Dry run

Input: `[1, 1, 2]`

| Step | `read` | `nums[read]` | `nums[write-1]` | Action | `write` |
| --- | --- | --- | --- | --- | --- |
| 0 | — | — | — | init | 1 |
| 1 | 1 | 1 | 1 | equal, skip | 1 |
| 2 | 2 | 2 | 1 | keep → nums[1]=2 | 2 |

## 9. Complexity analysis

| Approach | Time | Space | Reasoning |
| --- | --- | --- | --- |
| Brute force | O(n) | O(n) | New list of uniques |
| Optimised | O(n) | O(1) | read and write each advance at most n |

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| Empty | `[]` | `0` | No elements |
| Single | `[5]` | `1` | One unique |
| All equal | `[4, 4, 4]` | `1` | All collapse to one |
| Already unique | `[1, 2, 3]` | `3` | No writes needed |
| Negatives | `[-1, -1, 0]` | `2` | Sign does not matter |

```python
def test_basic():
    data = [1, 1, 2]
    assert remove_duplicates(data) == 2
    assert data[:2] == [1, 2]

def test_empty():
    assert remove_duplicates([]) == 0
```

## 11. Follow-up questions

1. What if the array is not sorted? (Use a set; O(n) space.)
2. What if you must keep at most two duplicates? (Change the comparison to `nums[write-2]`.)
3. What if you need to remove a specific value instead of duplicates?

## 12. Related problems

- `../../exercises/starter-code/remove_duplicates.py` — starter code.
- `../../lessons/two-pointers/two-pointers.md` — read/write invariant.
