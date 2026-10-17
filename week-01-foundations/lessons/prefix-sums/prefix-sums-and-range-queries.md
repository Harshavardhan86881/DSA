# Prefix Sums and Range Queries

| | |
| --- | --- |
| **Week** | 1 — Foundations |
| **Topic** | Prefix sums |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Arrays; Day 2 complexity; Day 5 hashing (for comparison) |
| **Deliverable** | `exercises/starter-code/prefix_sum.py` attempted and tested |

## 1. Learning objectives

After this lesson you can:

1. Define a prefix sum and build it in O(n).
2. Answer a range sum in O(1) per query using the prefix array.
3. Compare brute force (O(n) per query) with prefix sums (O(1) per query).
4. Solve Prefix Sum Construction, Range Sum Query – Immutable and Maximum Subarray.
5. State the precompute/query trade-off.

## 2. Prerequisites check

1. Can you build a list by appending in a loop? (If no, review lists.)
2. Can you state the complexity of a single loop over n? (If no, review Day 2.)
3. Have you completed Days 1–5? (If no, read those lessons first.)

## 3. Why this matters

Many problems ask "what is the sum of elements from index i to j?" Answering each query by
looping is O(n) per query; with q queries that is O(nq). Prefix sums precompute once in O(n)
and answer each query in O(1), turning O(nq) into O(n + q). The same idea (precompute, then
query) recurs in 2D prefix sums, difference arrays and sliding windows.

## 4. Concept explanation

### 4.1 What a prefix sum is

A prefix sum array `P` where `P[i]` is the sum of `nums[0..i-1]` (exclusive convention) or
`nums[0..i]` (inclusive). This lesson uses the **exclusive** convention because the range
formula is cleanest:

```
P[0] = 0
P[i] = P[i-1] + nums[i-1]   for i >= 1
```

Then `sum(nums[i..j]) = P[j+1] - P[i]`.

> **Mental model:** P stores "how much has accumulated before position i".

### 4.2 Building in one pass

```python
P = [0] * (len(nums) + 1)
for i in range(len(nums)):
    P[i + 1] = P[i] + nums[i]
```

O(n) time and O(n) space (for P). The input is untouched.

### 4.3 Answering a range query

```python
def range_sum(P, i, j):   # sum of nums[i..j] inclusive
    return P[j + 1] - P[i]
```

O(1) time, O(1) extra space beyond P. This is the whole point of precomputing.

### 4.4 The trade-off

- Without prefix sums: O(1) space, O(n) per query → O(nq) total.
- With prefix sums: O(n) space, O(1) per query → O(n + q) total.

When q is large (many queries), prefix sums win. When q is small, the simpler loop may be
better. State the trade-off in your complexity sentence.

### 4.5 Maximum Subarray (running sum)

A related idea: scan left to right, keeping a running sum. If the running sum becomes negative,
reset it to 0, because a negative prefix can never help a future subarray. Track the maximum
running sum seen. This is O(n) time, O(1) space.

Invariant: after processing index `i`, `running` is the best sum of a subarray ending at `i`
(or 0 if all such sums are negative), and `best` is the maximum over all endings so far.

### 4.6 Off-by-one discipline

Prefix sums are index-heavy. Write the formula on paper with a 4-element example before coding.
The exclusive convention (`P[0] = 0`, `P[i] = sum of first i elements`) makes the range formula
symmetric and is the one used in this course.

## 5. Worked examples (simple → difficult)

### Example 1 — Build and query (simple)

```python
def build_prefix(nums: list[int]) -> list[int]:
    P = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        P[i + 1] = P[i] + nums[i]
    return P


def range_sum(P: list[int], i: int, j: int) -> int:
    # sum of nums[i..j] inclusive
    return P[j + 1] - P[i]


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    P = build_prefix(nums)
    print(P)                      # [0, 1, 3, 6, 10]
    print(range_sum(P, 1, 3))      # 2+3+4 = 9
    print(range_sum(P, 0, 0))      # 1
```

**Line-by-line explanation**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `P = [0] * (len(nums) + 1)` | Allocate n+1 slots | Slot 0 is the empty prefix |
| `P[i + 1] = P[i] + nums[i]` | Extend the prefix | Reuses previous work |
| `P[j + 1] - P[i]` | Range sum formula | Exclusive convention makes this clean |

### Example 2 — PrefixSum class (moderate)

```python
class PrefixSum:
    def __init__(self, nums: list[int]):
        self.P = [0] * (len(nums) + 1)
        for i, value in enumerate(nums):
            self.P[i + 1] = self.P[i] + value

    def query(self, i: int, j: int) -> int:
        # sum of nums[i..j] inclusive
        return self.P[j + 1] - self.P[i]


if __name__ == "__main__":
    ps = PrefixSum([1, 2, 3, 4])
    print(ps.query(1, 3))   # 9
    print(ps.query(0, 3))   # 10
```

**Line-by-line explanation**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `__init__` builds `self.P` | Precompute once | O(n) time and space |
| `query` uses the formula | Answer in O(1) | No loop per query |
| `self.P[j + 1] - self.P[i]` | Range sum | Exclusive convention |

### Example 3 — Maximum Subarray (harder)

```python
# Brute force: O(n^2) time, O(1) space.
def max_subarray_brute(nums: list[int]) -> int:
    best = nums[0] if nums else 0
    for i in range(len(nums)):
        running = 0
        for j in range(i, len(nums)):
            running += nums[j]
            if running > best:
                best = running
    return best

# Optimised: O(n) time, O(1) space.
def max_subarray(nums: list[int]) -> int:
    if not nums:
        return 0
    best = running = nums[0]
    for value in nums[1:]:
        running = max(value, running + value)
        best = max(best, running)
    return best


if __name__ == "__main__":
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_subarray([-1, -2, -3]))                      # -1
```

**Line-by-line explanation (optimised)**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `best = running = nums[0]` | Seed both trackers | Empty input handled separately |
| `running = max(value, running + value)` | Reset or extend | Negative running sum cannot help |
| `best = max(best, running)` | Update global best | Tracks the maximum seen |
| `return best` | Result | Works for all-negative input |

## 6. Dry-run table

Trace `build_prefix` on `[1, 2, 3, 4]`.

| Step | `i` | `nums[i]` | `P[i]` | `P[i+1]` | Note |
| --- | --- | --- | --- | --- | --- |
| 0 | — | — | — | 0 | P[0] = 0 |
| 1 | 0 | 1 | 0 | 1 | P[1] = 0 + 1 |
| 2 | 1 | 2 | 1 | 3 | P[2] = 1 + 2 |
| 3 | 2 | 3 | 3 | 6 | P[3] = 3 + 3 |
| 4 | 3 | 4 | 6 | 10 | P[4] = 6 + 4 |

Trace `max_subarray` on `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`.

| Step | `value` | `running` | `best` | Note |
| --- | --- | --- | --- | --- |
| 0 | -2 | -2 | -2 | seed |
| 1 | 1 | 1 | 1 | reset: 1 > -2+1 |
| 2 | -3 | -2 | 1 | extend: -2 < 0? reset to -3? max(-3, -2-3=-5) = -3? Wait running = max(-3, -2 + -3 = -5) = -3 |
| 3 | 4 | 4 | 4 | reset: 4 > -3+4=1 |
| 4 | -1 | 3 | 4 | extend |
| 5 | 2 | 5 | 5 | extend |
| 6 | 1 | 6 | 6 | extend, new best |
| 7 | -5 | 1 | 6 | extend |
| 8 | 4 | 5 | 6 | extend |

## 7. Complexity

| Version | Time | Space | Notes |
| --- | --- | --- | --- |
| Build prefix | O(n) | O(n) | One pass, n+1 slots |
| Range query | O(1) | O(1) | Formula only |
| Brute-force max subarray | O(n²) | O(1) | Nested loops |
| Optimised max subarray | O(n) | O(1) | Single pass, running sum |

## 8. Common mistakes

| Mistake | Symptom | Fix |
| --- | --- | --- |
| Off-by-one in prefix indices | Wrong range sums | Use exclusive convention and test on 4 elements |
| Forgetting P has n+1 slots | IndexError | Allocate `len(nums) + 1` |
| Resetting running sum too early | Wrong maximum subarray | Reset only when `running + value < value` |
| Counting input as extra space | Over-reported space | Count only new containers |
| Empty input not handled | Crash or wrong answer | Return 0 or handle at the top |

## 9. Practice exercises

Do these before reading the hints. Files live in `exercises/starter-code/`.

1. **Prefix sum construction** — build the prefix array → `exercises/starter-code/prefix_sum.py`
2. **Range sum query** — implement a class with `query(i, j)` → `exercises/starter-code/range_sum_query.py`
3. **Maximum subarray** — return the maximum subarray sum → `exercises/starter-code/maximum_subarray.py`

## 10. Hints

<details>
<summary>Hint 1 — for exercise 1 (prefix sum construction)</summary>

Allocate `n + 1` slots starting with 0. Each slot is the previous slot plus the corresponding input element.

</details>

<details>
<summary>Hint 2 — for exercise 2 (range sum query)</summary>

Store the prefix array in `__init__`. `query(i, j)` returns `P[j+1] - P[i]`.

</details>

<details>
<summary>Hint 3 — for exercise 3 (maximum subarray)</summary>

Keep a running sum. At each element, either start a new subarray at this element or extend the previous one. Track the best.

</details>

## 11. Solutions

- `exercises/solutions/prefix_sum.py`
- `exercises/solutions/range_sum_query.py`
- `exercises/solutions/maximum_subarray.py`

Do not open these until you have attempted the starter code for at least 25 minutes.

## 12. Interview applications

- **Question form:** "Given an array, answer many range-sum queries efficiently."
- **Expected answer shape:** "I precompute a prefix-sum array in O(n) time and O(n) space. Each query is then O(1) via `P[j+1] - P[i]`. On `[1, 2, 3, 4]`, the sum from index 1 to 3 is `P[4] - P[1] = 10 - 1 = 9`."
- **Follow-up the interviewer may ask:** "What if the array is updated between queries?" (Answer: a Fenwick tree or segment tree, beyond Week 1.)

## 13. Review questions

Answer without looking at the lesson. If you cannot, make a flashcard.

1. State the prefix-sum build loop.
2. What is the range-sum formula under the exclusive convention?
3. What is the precompute/query trade-off?
4. Explain the Maximum Subarray reset rule.
5. Why does prefix sum need n+1 slots?

## 14. Related lessons

- `../problem-solving/problem-solving-foundations.md` — the routine that uses this analysis.
- `../complexity/big-o-complexity.md` — precompute versus per-query costs.
- `../arrays/arrays-and-lists.md` — list operations used to build the prefix.
- `../../docs/complexity-cheatsheet.md` — the full reference.
