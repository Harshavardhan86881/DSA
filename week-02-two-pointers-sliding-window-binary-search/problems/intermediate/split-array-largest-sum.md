# Split Array Largest Sum

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | binary search on answer, arrays |
| **Target time** | 25 minutes |
| **Solution file** | [split-array-largest-sum.py](split-array-largest-sum.py) |

## 1. Problem statement

Given an array `nums` of non-negative integers and an integer `m`, split `nums` into `m`
contiguous subarrays to minimise the largest sum among them. Return that minimised largest sum.

## 2. Constraints

- `1 ≤ m ≤ n ≤ 1000` (this instance; pattern scales higher)
- `0 ≤ nums[i] ≤ 10^6`

## 3. Examples

**Example 1**

```text
Input:  nums = [7, 2, 5, 10, 8], m = 2
Output: 18
Explanation: split as [7, 2, 5] and [10, 8]; largest sum 18.
```

**Example 2**

```text
Input:  nums = [1, 2, 3, 4, 5], m = 2
Output: 9
```

**Example 3 — edge case**

```text
Input:  nums = [1, 4, 4], m = 3
Output: 4
```

## 4. Hints

<details><summary>Hint 1 — orientation</summary>
The answer is between max(nums) (must fit largest element) and sum(nums) (one subarray).
</details>
<details><summary>Hint 2 — technique</summary>
Binary search on the largest sum. Feasible(limit) = number of subarrays with max sum ≤ limit ≤ m.
</details>
<details><summary>Hint 3 — structure</summary>

```python
def feasible(limit):
    count = 1
    current = 0
    for n in nums:
        if current + n > limit:
            count += 1
            current = n
        else:
            current += n
    return count <= m
```
</details>

## 5. Brute-force approach

Try every possible split with recursion/backtracking. Exponential time. Correct but too slow.

## 6. Optimised approach

Binary search on answer. Feasible(limit) is monotonic: larger limit → fewer subarrays.

```python
def split_array(nums: list[int], m: int) -> int:
    def feasible(limit: int) -> bool:
        count = 1
        current = 0
        for n in nums:
            if current + n > limit:
                count += 1
                current = n
            else:
                current += n
        return count <= m

    left, right = max(nums), sum(nums)
    answer = right
    while left <= right:
        mid = left + (right - left) // 2
        if feasible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `feasible(limit)` | Subarrays needed ≤ m | Decision function |
| `if current + n > limit` | Start new subarray | Would exceed limit |
| `left, right = max(nums), sum(nums)` | Bounds | Must fit largest; sum always works |
| `if feasible(mid)` | Candidate works? | Try smaller if yes |
| `answer = mid; right = mid - 1` | Record and shrink | Find first feasible |
| `else: left = mid + 1` | Need larger limit | Not feasible |

## 8. Dry run

Input: nums = [7, 2, 5, 10, 8], m = 2. Answer = 18.

| Step | `left` | `right` | `mid` | `feasible(mid)` | Action |
| --- | --- | --- | --- | --- | --- |
| 0 | 7 | 32 | 19 | count=2 ≤ 2 → True | answer=19, right=18 |
| 1 | 7 | 18 | 12 | count=3 > 2 → False | left=13 |
| 2 | 13 | 18 | 15 | count=3 > 2 → False | left=16 |
| 3 | 16 | 18 | 17 | count=3 > 2 → False | left=18 |
| 4 | 18 | 18 | 18 | count=2 ≤ 2 → True | answer=18, right=17 |
| 5 | 18 | 17 | — | — | loop ends; answer=18 |

## 9. Complexity analysis

| Approach | Time | Space | Reasoning |
| --- | --- | --- | --- |
| Brute force | Exponential | O(n) | Backtracking splits |
| Optimised | O(n log sum) | O(1) | log steps * O(n) check |

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| m = 1 | `[7,2,5,10,8]`, 1 | `32` | Whole array |
| m = n | `[7,2,5,10,8]`, 5 | `10` | Each element alone |
| Single element | `[5]`, 1 | `5` | Trivial |
| Zeros | `[0,0,0]`, 2 | `0` | Zero handling |

```python
def test_basic():
    assert split_array([7, 2, 5, 10, 8], 2) == 18

def test_m_equals_n():
    assert split_array([7, 2, 5, 10, 8], 5) == 10
```

## 11. Follow-up questions

1. What if you need the actual split positions? (Track them during the feasible check.)
2. What if m is larger than n? (Return max(nums).)
3. How does this relate to "painter's partition problem"?

## 12. Related problems

- `../../exercises/starter-code/split_array_largest_sum.py` — starter code.
- `../../lessons/binary-search-on-answer/binary-search-on-answer.md` — the full lesson.
