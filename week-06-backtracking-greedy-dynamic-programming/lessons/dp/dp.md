# Dynamic Programming

| | |
| --- | --- |
| **Week** | 6 — Backtracking, greedy, dynamic programming |
| **Topic** | Dynamic programming |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Recursion |
| **Deliverable** | `exercises/starter-code/coin_change.py` attempted |

## 1. Learning objectives

After this lesson you can:

1. Start from a brute-force recursive definition.
2. Identify repeated subproblems.
3. Define exactly what each state means.
4. Write a recurrence in words and mathematics.
5. Establish base cases.
6. Determine dependencies between states.
7. Implement memoization.
8. Convert to tabulation.
9. Optimize space after understanding the recurrence.
10. Derive time and space complexity from state count and work per state.

## 2. Prerequisites check

1. Can you write a recursive function?
2. Can you explain what a cache is?
3. Can you fill a list in a loop?

## 3. Why this matters

Dynamic programming appears in interviews as soon as recursion is understood. The key skill is defining the state before writing code.

## 4. Build intuition

DP stores answers to subproblems so they are not recomputed. If a recursive solution calls the same smaller problem many times, DP can remove the duplication.

Mental model: DP is recursion with memory, or a table filled in dependency order.

## 5. Repeatable DP process

1. Start with brute-force recursion.
2. Identify repeated subproblems.
3. Define exactly what each state means.
4. Write the recurrence in words and mathematics.
5. Establish base cases.
6. Determine dependencies between states.
7. Implement memoization.
8. Convert to tabulation.
9. Optimize space only after the full recurrence is understood.
10. Derive time and space complexity from state count and work per state.

## 6. Climbing Stairs

Problem: count ways to climb `n` stairs using 1 or 2 steps.

Brute force: `climb(n) = climb(n-1) + climb(n-2)`.

State: `dp[i]` = number of ways to reach stair `i`.

Recurrence: `dp[i] = dp[i-1] + dp[i-2]`.

Base cases: `dp[0] = 1` (one way to stand at ground), `dp[1] = 1`.

Contract: `n >= 0`. `climb_stairs(0) = 1` by the empty-path convention; negative input is invalid.

Memoization (validate the public input before entering the cached helper):

```python
from functools import lru_cache

def climb_stairs_memo(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    @lru_cache(None)
    def ways(i):
        if i <= 1:
            return 1
        return ways(i - 1) + ways(i - 2)

    return ways(n)
```

Tabulation:

```python
def climb_stairs(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    prev2, prev1 = 1, 1
    for _ in range(2, n + 1):
        cur = prev1 + prev2
        prev2, prev1 = prev1, cur
    return prev1
```

Dry run for n = 4: values are 1, 1, 2, 3, 5.

Complexity: O(n) time, O(1) space after optimization.

## 7. House Robber

Problem: choose a subset of houses to maximize money without robbing adjacent houses.

State: `dp[i]` = maximum money using houses `0..i`.

Recurrence: `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`.

- Skip house i: `dp[i-1]`.
- Rob house i: `dp[i-2] + nums[i]`.

Base cases: empty list gives 0; one house gives `nums[0]`.

```python
def rob(nums):
    prev2, prev1 = 0, 0
    for num in nums:
        cur = max(prev1, prev2 + num)
        prev2, prev1 = prev1, cur
    return prev1
```

Dry run for `[1, 2, 3, 1]`:

| i | num | prev2 | prev1 | cur |
| --- | --- | --- | --- | --- |
| 0 | 1 | 0 | 0 | 1 |
| 1 | 2 | 0 | 1 | 2 |
| 2 | 3 | 1 | 2 | 4 |
| 3 | 1 | 2 | 4 | 4 |

Result: 4.

Complexity: O(n) time, O(1) space.

## 8. Coin Change

Problem: minimum number of coins to make `amount`, with unlimited use of each denomination.

State: `dp[a]` = minimum coins needed for amount `a`.

Recurrence: `dp[a] = min(dp[a - coin] + 1)` over coins with `coin <= a`.

Base case: `dp[0] = 0`.

Impossible amounts remain a sentinel value.

```python
def coin_change(coins, amount):
    if amount < 0:
        raise ValueError("amount must be non-negative")
    if any(coin <= 0 for coin in coins):
        raise ValueError("coins must be positive")
    INF = amount + 1
    dp = [INF] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                dp[a] = min(dp[a], dp[a - coin] + 1)
    return dp[amount] if dp[amount] != INF else -1
```

Dry run for coins `[1,2,5]`, amount 11: answer 3 (5+5+1).

Greedy largest-coin-first can fail for arbitrary coin systems, for example coins `[1,3,4]`, amount 6: greedy gives 4+1+1 = 3 coins, optimal is 3+3 = 2 coins.

Complexity: O(amount * len(coins)) time, O(amount) space.

## 9. Longest Increasing Subsequence

Problem: length of the longest strictly increasing subsequence.

State: `dp[i]` = length of the longest increasing subsequence ending at index `i`.

Recurrence: `dp[i] = max(dp[j] + 1)` for `j < i` with `nums[j] < nums[i]`; otherwise 1.

```python
def length_of_lis(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

Dry run for `[10,9,2,5,3,7,101,18]`: answer 4, for example `2,3,7,101`.

Duplicates: equal values do not extend a strictly increasing subsequence because the condition is `<`.

Complexity: O(n^2) time, O(n) space. An O(n log n) optimization exists using binary search, but the implementation above is O(n^2).

## 10. Memoization versus tabulation

Same recurrence, different execution:

- Memoization is top-down: recurse and cache. It computes only reachable states and is often easier to derive.
- Tabulation is bottom-up: fill a table in dependency order. It avoids recursion depth and can be space-optimized.

Trade-offs:

| Aspect | Memoization | Tabulation |
| --- | --- | --- |
| Direction | Top-down | Bottom-up |
| States computed | Reachable states | All states |
| Recursion depth | Yes | No |
| Space optimization | Harder | Easier |
| Common bug | Missing cache key | Wrong fill order |

Caching works only when the state captures all information relevant to the answer.

## 11. Common mistakes

| Mistake | Symptom | Fix |
| --- | --- | --- |
| Vague state definition | wrong recurrence | write state meaning in words |
| Wrong base case | off-by-one or wrong small input | test n=0, n=1 |
| Wrong fill order | uses uninitialized values | follow dependencies |
| Forgetting impossible case | returns large sentinel | return -1 when unreachable |
| Claiming O(n log n) for O(n^2) LIS | wrong complexity | state actual complexity |

## 12. Debugging checklist

1. Write state meaning before coding.
2. Test base cases.
3. Print DP table for small input.
4. Verify recurrence on a 3-4 element example.
5. Check impossible cases.

## 13. Practice

### Guided exercise 1

Derive climbing stairs recurrence.

### Guided exercise 2

Trace house robber table.

### Independent exercise 1

Implement coin change.

### Independent exercise 2

Implement LIS.

### Debugging exercise

Fix:

```python
def bad_climb(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return bad_climb(n-1) + bad_climb(n-2)
```

### Prediction exercise

What is `dp[0]` for coin change? Answer: 0.

## 14. Active-recall questions

1. What is a DP state?
2. What is a recurrence?
3. What is memoization?
4. What is tabulation?
5. How do you derive complexity?

Answers:

1. A subproblem answer.
2. How a state depends on smaller states.
3. Top-down caching.
4. Bottom-up table filling.
5. States times transition cost.

## 15. Interview questions

**Q:** How do you define a DP state?
**A:** State what `dp[i]` means in words before writing code.

**Q:** Memoization vs tabulation?
**A:** Top-down with recursion vs bottom-up with a table.

Follow-up: When can you optimize space? When dependencies use only a constant number of previous states.

## 16. Spaced-repetition checklist

- Day 1: Write climbing stairs.
- Day 3: Write coin change.
- Day 7: Explain memo vs tabulation.
- Day 14: Derive LIS recurrence.

## 17. Explain aloud

"Dynamic programming stores subproblem answers. I define the state, write the recurrence, set base cases, then choose memoization or tabulation."
