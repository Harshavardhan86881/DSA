# Search Insert Position

| | |
| --- | --- |
| **Difficulty** | easy |
| **Topics** | binary search, lower bound |
| **Target time** | 20 minutes |
| **Solution file** | [search-insert-position.py](search-insert-position.py) |

## 1. Problem statement

Given a sorted array of distinct integers `nums` and a `target`, return the index where
`target` should be inserted to keep the array sorted. If `target` is already present, return
its index.

## 2. Constraints

- `1 ≤ n ≤ 10^4`
- `-10^4 ≤ nums[i], target ≤ 10^4`
- `nums` is sorted in ascending order with distinct values.

## 3. Examples

**Example 1**

```text
Input:  nums = [1, 3, 5, 6], target = 5
Output: 2
```

**Example 2**

```text
Input:  nums = [1, 3, 5, 6], target = 2
Output: 1
```

**Example 3 — edge case**

```text
Input:  nums = [1, 3, 5, 6], target = 7
Output: 4
```

## 4. Hints

<details><summary>Hint 1 — orientation</summary>
This is exactly the lower bound: the first index where nums[i] >= target.
</details>
<details><summary>Hint 2 — technique</summary>
Use a half-open interval [left, right) and narrow it.
</details>
<details><summary>Hint 3 — structure</summary>

```python
left, right = 0, len(nums)
while left < right:
    mid = left + (right - left) // 2
    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid
return left
```
</details>

## 5. Brute-force approach

Linear scan. O(n) time, O(1) space.

```python
def search_insert_brute(nums, target):
    for i, v in enumerate(nums):
        if v >= target:
            return i
    return len(nums)
```

## 6. Optimised approach

Lower bound via half-open binary search.

```python
def search_insert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `left, right = 0, len(nums)` | Half-open interval | right is exclusive |
| `while left < right` | Loop while non-empty | Empty interval means done |
| `mid = left + (right - left) // 2` | Safe midpoint | Avoids overflow |
| `if nums[mid] < target: left = mid + 1` | Target to the right | Discard mid and left part |
| `else: right = mid` | Target at or left of mid | Keep mid as candidate |
| `return left` | Insertion position | left == right == answer |

## 8. Dry run

Input: `nums = [1, 3, 5, 6]`, target = 2.

| Step | `left` | `right` | `mid` | `nums[mid]` | Action |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 4 | 2 | 5 | 5 >= 2 → right = 2 |
| 1 | 0 | 2 | 1 | 3 | 3 >= 2 → right = 1 |
| 2 | 0 | 1 | 0 | 1 | 1 < 2 → left = 1 |
| 3 | 1 | 1 | — | — | loop ends; return 1 |

## 9. Complexity analysis

| Approach | Time | Space | Reasoning |
| --- | --- | --- | --- |
| Brute force | O(n) | O(1) | Linear scan |
| Optimised | O(log n) | O(1) | Interval halves each step |

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| Target present | `[1,3,5,6]`, 5 | `2` | Return existing index |
| Target before all | `[1,3,5,6]`, 0 | `0` | Insert at front |
| Target after all | `[1,3,5,6]`, 7 | `4` | Insert at end |
| Single element | `[1]`, 0 | `0` | Small input |
| Empty | `[]`, 5 | `0` | Insert into empty |

```python
def test_basic():
    assert search_insert([1, 3, 5, 6], 5) == 2

def test_insert():
    assert search_insert([1, 3, 5, 6], 2) == 1
```

## 11. Follow-up questions

1. How does this differ from standard binary search?
2. What if the array has duplicates? (Lower bound still works.)
3. How would you implement upper bound?

## 12. Related problems

- `../../exercises/starter-code/search_insert_position.py` — starter code.
- `../../lessons/binary-search/binary-search.md` — lower/upper bound.
