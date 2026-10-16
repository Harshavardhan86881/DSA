# Prefix Sum Construction

| | |
| --- | --- |
| **Difficulty** | easy |
| **Topics** | arrays, prefix sums |
| **Target time** | 15 minutes |
| **Solution file** | [prefix-sum-construction.py](prefix-sum-construction.py) |

## 1. Problem statement

Given a list of integers `nums`, build and return the prefix-sum array `P` using the
exclusive convention: `P[0] = 0` and `P[i + 1] = P[i] + nums[i]`. The input is not modified.

## 2. Constraints

- `0 ≤ n ≤ 10^5`
- `-10^4 ≤ nums[i] ≤ 10^4`

## 3. Examples

**Example 1**

```text
Input:  [1, 2, 3, 4]
Output: [0, 1, 3, 6, 10]
```

**Example 2**

```text
Input:  [5]
Output: [0, 5]
```

**Example 3 — edge case**

```text
Input:  []
Output: [0]
```

## 4. Hints

<details><summary>Hint 1 — orientation</summary>
The output has n + 1 elements. Allocate that many slots up front.
</details>
<details><summary>Hint 2 — technique</summary>
Each slot reuses the previous slot: P[i+1] = P[i] + nums[i].
</details>
<details><summary>Hint 3 — structure</summary>

```python
P = [0] * (len(nums) + 1)
for i in range(len(nums)):
    P[i + 1] = P[i] + nums[i]
return P
```
</details>

## 5. Brute-force approach

For each i, sum nums[0..i-1] from scratch. Correct but O(n^2). It shows why the running
prefix helps.

```python
def build_prefix_brute(nums):
    P = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        s = 0
        for j in range(i):
            s += nums[j]
        P[i] = s
    return P
```

## 6. Optimised approach

Single pass, reusing the previous prefix value.

```python
def build_prefix(nums: list[int]) -> list[int]:
    P = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        P[i + 1] = P[i] + nums[i]
    return P
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `P = [0] * (len(nums) + 1)` | Allocate n+1 slots | Slot 0 is the empty prefix |
| `for i in range(len(nums))` | One pass over input | Keeps time linear |
| `P[i + 1] = P[i] + nums[i]` | Extend prefix | Reuses previous work |
| `return P` | Result | Input untouched |

## 8. Dry run

Input: `[1, 2, 3, 4]`

| Step | `i` | `nums[i]` | `P[i]` | `P[i+1]` |
| --- | --- | --- | --- | --- |
| 0 | — | — | — | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 2 | 1 | 2 | 1 | 3 |
| 3 | 2 | 3 | 3 | 6 |
| 4 | 3 | 4 | 6 | 10 |

## 9. Complexity analysis

| Approach | Time | Space | Reasoning |
| --- | --- | --- | --- |
| Brute force | O(n^2) | O(n) | Recomputes each prefix |
| Optimised | O(n) | O(n) | One pass; n+1 slots |

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| Empty | `[]` | `[0]` | Loop does not run |
| Single | `[5]` | `[0, 5]` | One prefix |
| Negatives | `[-1, 2, -3]` | `[0, -1, 1, -2]` | Prefix can decrease |
| All zeros | `[0, 0, 0]` | `[0, 0, 0, 0]` | Zero handling |

```python
def test_basic():
    assert build_prefix([1, 2, 3, 4]) == [0, 1, 3, 6, 10]

def test_empty():
    assert build_prefix([]) == [0]
```

## 11. Follow-up questions

1. What if you want an inclusive prefix (P[i] = sum of nums[0..i])? (Adjust the formula and the query.)
2. Can you build it in place, overwriting the input? (Yes, but you lose the original.)
3. How would you extend this to 2D prefix sums?

## 12. Related problems

- `../../exercises/starter-code/prefix_sum.py` — starter code.
- `../../lessons/prefix-sums/prefix-sums-and-range-queries.md` — the full lesson.
