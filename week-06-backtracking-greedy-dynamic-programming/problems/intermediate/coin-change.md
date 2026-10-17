# Coin Change

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | dynamic programming |
| **Target time** | 25 minutes |
| **Solution file** | [coin-change.py](coin-change.py) |

## 1. Problem statement

Given coin denominations and an amount, return the minimum number of coins needed to make that amount. You may use each coin unlimited times. Return `-1` if impossible.

Function contract: `coin_change(coins: list[int], amount: int) -> int`.

## 2. Constraints

- `1 <= len(coins) <= 12`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10^4`
- Coins may contain duplicates.

## 3. Examples

Input: `coins = [1,2,5], amount = 11`
Output: `3`
Explanation: 5 + 5 + 1.

Input: `coins = [2], amount = 3`
Output: `-1`.

Input: `coins = [1,2,5], amount = 0`
Output: `0`.

## 4. Hints

<details><summary>Hint 1</summary>
Define dp[a] as the minimum coins for amount a.
</details>

<details><summary>Hint 2</summary>
dp[a] = min(dp[a - coin] + 1) over coins <= a.
</details>

## 5. Brute-force approach

Try all combinations of coins recursively. This explodes because the same amount is recomputed many times.

## 6. Optimised approach

Use bottom-up DP. Initialize `dp[0] = 0` and all other amounts to a sentinel. For each amount, try every coin.

Important code lines:

- `dp = [INF] * (amount + 1)`: sentinel for impossible.
- `dp[0] = 0`: base case.
- `dp[a] = min(dp[a], dp[a - coin] + 1)`: recurrence.
- `return ... if dp[amount] != INF else -1`: impossible case.

## 7. Complexity analysis

- Time: O(amount * len(coins)).
- Space: O(amount).

## 8. Edge cases and tests

- Amount 0 returns 0.
- Impossible amount returns -1.
- Duplicate denominations.
- Greedy largest-coin-first can fail for arbitrary systems.

## 9. Common mistakes

- Forgetting `dp[0] = 0`.
- Using a sentinel that is too small.
- Assuming greedy works for all coin systems.

## 10. Follow-up questions

1. How would you reconstruct the chosen coins?
2. Why can greedy fail?
3. What changes if each coin can be used once?

## 11. Related problems

- `../../exercises/starter-code/coin_change.py` — starter code.
- `../../exercises/solutions/coin_change.py` — solution.
- `../../exercises/test-cases/test_coin_change.py` — tests.
- `../../lessons/dp/dp.md` — lesson.
