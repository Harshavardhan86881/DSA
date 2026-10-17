# Range Sum Query – Immutable

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | arrays, prefix sums, class design |
| **Target time** | 20 minutes |
| **Solution file** | [range-sum-query-immutable.py](range-sum-query-immutable.py) |

## 1. Problem statement

Design a data structure that is initialised with a list of integers and can answer
`query(i, j)` = sum of elements from index `i` to `j` inclusive, with many queries. The list
is immutable after construction.

## 2. Constraints

- `0 ≤ n ≤ 10^4` (this instance; pattern scales higher)
- `-10^5 ≤ nums[i] ≤ 10^5`
- `0 ≤ i ≤ j < n`
- Up to 10^4 queries.

## 3. Examples

**Example 1**

```text
Input:  nums = [1, 2, 3, 4], query(1, 3)
Output: 9
```

**Example 2**

```text
Input:  nums = [1, 2, 3, 4], query(0, 3)
Output: 10
```

**Example 3 — edge case**

```text
Input:  nums = [5], query(0, 0)
Output: 5
```

## 4. Hints

<details><summary>Hint 1 — orientation</summary>
With up to 10^4 queries on up to 10^4 elements, O(n) per query is 10^8 — borderline. O(1) per query is better.
</details>
<details><summary>Hint 2 — technique</summary>
Precompute a prefix-sum array in __init__; answer each query with the range formula.
</details>
<details><summary>Hint 3 — structure</summary>

```python
class RangeSumQuery:
    def __init__(self, nums):
        self.P = [0] * (len(nums) + 1)
        for i, v in enumerate(nums):
            self.P[i + 1] = self.P[i] + v
    def query(self, i, j):
        return self.P[j + 1] - self.P[i]
```
</details>

## 5. Brute-force approach

Loop from i to j for each query. O(n) per query, O(1) extra space. Simple but slow for many queries.

```python
def query_brute(self, i, j):
    return sum(self.nums[i:j + 1])
```

## 6. Optimised approach

Precompute prefix sums once. Each query is O(1).

```python
class RangeSumQuery:
    def __init__(self, nums: list[int]):
        self.P = [0] * (len(nums) + 1)
        for i, value in enumerate(nums):
            self.P[i + 1] = self.P[i] + value

    def query(self, i: int, j: int) -> int:
        return self.P[j + 1] - self.P[i]
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `self.P = [0] * (len(nums) + 1)` | Allocate prefix array | Slot 0 is empty prefix |
| `self.P[i + 1] = self.P[i] + value` | Build prefix | One pass, O(n) |
| `return self.P[j + 1] - self.P[i]` | Range sum | O(1) per query |

## 8. Dry run

Input: `nums = [1, 2, 3, 4]`, so `P = [0, 1, 3, 6, 10]`.

`query(1, 3)` = `P[4] - P[1]` = `10 - 1` = `9`.

## 9. Complexity analysis

| Approach | Precompute | Per query | Space |
| --- | --- | --- | --- |
| Brute force | O(1) | O(n) | O(n) for storing nums |
| Optimised | O(n) | O(1) | O(n) for prefix array |

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| Single element | `[5]`, query(0,0) | `5` | Smallest input |
| Full range | `[1,2,3,4]`, query(0,3) | `10` | Whole array |
| Single index | `[1,2,3,4]`, query(2,2) | `3` | One element |
| Negatives | `[-1, 2, -3]`, query(0,2) | `-2` | Negative values |

```python
def test_basic():
    rs = RangeSumQuery([1, 2, 3, 4])
    assert rs.query(1, 3) == 9

def test_single():
    rs = RangeSumQuery([5])
    assert rs.query(0, 0) == 5
```

## 11. Follow-up questions

1. What if the array can be updated? (Fenwick tree or segment tree.)
2. What if queries are on a 2D grid? (2D prefix sums.)
3. Can you reduce space by computing queries online without storing P? (No, then each query is O(n).)

## 12. Related problems

- `../../exercises/starter-code/range_sum_query.py` — starter code.
- `../../lessons/prefix-sums/prefix-sums-and-range-queries.md` — the full lesson.
