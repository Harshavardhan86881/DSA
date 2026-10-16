# Two Sum II - Input Array Is Sorted

| | |
| --- | --- |
| **Difficulty** | easy |
| **Topics** | two pointers, sorted array |
| **Target time** | 20 minutes |
| **Solution file** | [two-sum-ii-input-array-is-sorted.py](two-sum-ii-input-array-is-sorted.py) |

## 1. Problem statement

Given a 1-indexed sorted array `numbers` and a `target`, return the indices (0-based) of
two numbers that add up to `target`. There is exactly one solution and you may not use the
same element twice.

## 2. Constraints

- `2 ≤ n ≤ 3 * 10^4`
- `-1000 ≤ numbers[i] ≤ 1000`
- `numbers` is sorted in non-decreasing order.
- Exactly one solution exists.

## 3. Examples

**Example 1**

```text
Input:  numbers = [2, 7, 11, 15], target = 9
Output: [0, 1]
```

**Example 2**

```text
Input:  numbers = [2, 3, 4], target = 6
Output: [1, 2]
```

**Example 3 — edge case**

```text
Input:  numbers = [-1, 0], target = -1
Output: [0, 1]
```

## 4. Hints

<details><summary>Hint 1 — orientation</summary>
The array is sorted, so two pointers can solve it in O(n) with O(1) space.
</details>
<details><summary>Hint 2 — technique</summary>
Start at both ends. Move left up if the sum is too small, right down if too large.
</details>
<details><summary>Hint 3 — structure</summary>

```python
left, right = 0, len(numbers) - 1
while left < right:
    s = numbers[left] + numbers[right]
    if s == target: return [left, right]
    if s < target: left += 1
    else: right -= 1
```
</details>

## 5. Brute-force approach

Check every pair. O(n²) time, O(1) space.

```python
def two_sum_ii_brute(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]
```

## 6. Optimised approach

Opposite-direction two pointers. Invariant: all pairs with left index < i or right index > j
have been ruled out.

```python
def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left, right]
        if s < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `left, right = 0, len(numbers) - 1` | Widest pair | Sorted array |
| `s = numbers[left] + numbers[right]` | Current sum | Compared with target |
| `if s == target` | Found it | Return 0-based indices |
| `if s < target: left += 1` | Sum too small | Increase smaller side |
| `else: right -= 1` | Sum too large | Decrease larger side |

## 8. Dry run

Input: `numbers = [2, 7, 11, 15]`, target = 9.

| Step | `left` | `right` | `s` | Decision |
| --- | --- | --- | --- | --- |
| 0 | 0 | 3 | 17 | too large → right-- |
| 1 | 0 | 2 | 13 | too large → right-- |
| 2 | 0 | 1 | 9 | match → [1, 2] |

## 9. Complexity analysis

| Approach | Time | Space | Reasoning |
| --- | --- | --- | --- |
| Brute force | O(n²) | O(1) | Nested loops |
| Optimised | O(n) | O(1) | Each pointer moves at most n steps |

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| Minimum input | `[1, 2]`, target 3 | `[1, 2]` | Smallest valid |
| Negatives | `[-1, 0]`, target -1 | `[1, 2]` | Negative numbers |
| Duplicates | `[1, 1, 2]`, target 2 | `[1, 2]` | Duplicate values |
| Large values | within constraints | valid indices | No overflow in Python |

```python
def test_basic():
    assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2]

def test_negatives():
    assert two_sum_sorted([-1, 0], -1) == [1, 2]
```

## 11. Follow-up questions

1. What if the array is not sorted? (Sort first O(n log n), or use a hash map.)
2. What if there are multiple valid pairs? (Return all or the first.)
3. What if you need 0-based indices? (Return [left, right].)

## 12. Related problems

- `../../exercises/starter-code/two_sum_sorted.py` — starter code.
- `../../lessons/two-pointers/two-pointers.md` — monotonicity argument.
