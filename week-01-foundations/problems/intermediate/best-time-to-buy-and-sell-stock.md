# Best Time to Buy and Sell Stock

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | arrays, single pass, running minimum |
| **Target time** | 25 minutes |
| **Solution file** | [best-time-to-buy-and-sell-stock.py](best-time-to-buy-and-sell-stock.py) |

## 1. Problem statement

You are given a list `prices` where `prices[i]` is the price of a stock on day `i`. You want to
maximise your profit by choosing a single day to buy one stock and a later day to sell it. Return
the maximum profit you can achieve. If no profit is possible, return `0`.

## 2. Constraints

- `1 ≤ n ≤ 10^5`
- `0 ≤ prices[i] ≤ 10^4`
- You must buy before you sell (one transaction).

## 3. Examples

**Example 1**

```text
Input:  [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: buy on day 2 (price 1), sell on day 5 (price 6), profit 5.
```

**Example 2**

```text
Input:  [7, 6, 4, 3, 1]
Output: 0
Explanation: prices only decrease, so no profitable transaction.
```

**Example 3 — edge case**

```text
Input:  [5]
Output: 0
```

## 4. Hints (read only after 10 minutes of thinking)

<details>
<summary>Hint 1 — orientation</summary>

n can be 10^5, so checking every buy/sell pair (O(n²)) is too slow. You need one pass.

</details>

<details>
<summary>Hint 2 — technique</summary>

Track the cheapest price seen so far. At each day, the best profit ending that day is
`price - cheapest_so_far`.

</details>

<details>
<summary>Hint 3 — structure</summary>

```python
cheapest = prices[0]
best = 0
for price in prices[1:]:
    if price < cheapest:
        cheapest = price
    else:
        best = max(best, price - cheapest)
```

</details>

## 5. Brute-force approach

Try every pair `(buy_day, sell_day)` with `buy_day < sell_day` and take the maximum difference.
Correct but O(n²) time and O(1) space. It is the natural first idea.

```python
def max_profit_brute(prices):
    best = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            best = max(best, prices[j] - prices[i])
    return best
```

## 6. Optimised approach

Single pass tracking the running minimum price and the best profit so far. The invariant: after
processing day `i`, `cheapest` is the minimum price in `prices[0..i]` and `best` is the maximum
profit achievable with a sell on or before day `i`.

```python
def max_profit(prices: list[int]) -> int:
    if not prices:
        return 0
    cheapest = prices[0]
    best = 0
    for price in prices[1:]:
        if price < cheapest:
            cheapest = price
        else:
            profit = price - cheapest
            if profit > best:
                best = profit
    return best
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `if not prices` | Handle empty input | Avoids indexing an empty list |
| `cheapest = prices[0]` | Seed the running minimum | First day is the only candidate so far |
| `best = 0` | No profit yet | Zero means "do nothing" is allowed |
| `for price in prices[1:]` | One pass over remaining days | Keeps time linear |
| `if price < cheapest` | New minimum found | Future sells compare against this |
| `profit = price - cheapest` | Profit if selling today | Buy at the cheapest so far |
| `if profit > best` | Update best profit | Keep the maximum seen |
| `return best` | Result | 0 if no profitable transaction |

## 8. Dry run

Input: `[7, 1, 5, 3, 6, 4]`

| Step | `price` | `cheapest` | `best` | Note |
| --- | --- | --- | --- | --- |
| 0 | — | 7 | 0 | initial |
| 1 | 1 | 1 | 0 | new minimum |
| 2 | 5 | 1 | 4 | profit 4 |
| 3 | 3 | 1 | 4 | profit 2, no improvement |
| 4 | 6 | 1 | 5 | profit 5, new best |
| 5 | 4 | 1 | 5 | profit 3, no improvement |

## 9. Complexity analysis

| Approach | Time | Space | Reasoning |
| --- | --- | --- | --- |
| Brute force | O(n²) | O(1) | Nested loops over pairs |
| Optimised | O(n) | O(1) | Single pass, two variables |

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| Empty | `[]` | `0` | No transaction possible |
| Single day | `[5]` | `0` | Cannot buy and sell |
| Decreasing | `[7, 6, 4, 3, 1]` | `0` | No profit possible |
| Increasing | `[1, 2, 3, 4]` | `3` | Buy first, sell last |
| One dip | `[7, 1, 5, 3, 6, 4]` | `5` | Standard case |

```python
def test_basic():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5

def test_decreasing():
    assert max_profit([7, 6, 4, 3, 1]) == 0
```

## 11. Follow-up questions

1. What if you are allowed at most two transactions? (Dynamic programming, Week 6.)
2. What if you must pay a transaction fee? (Subtract fee from each profit.)
3. What if you can buy and sell on the same day? (No change; the formula still holds.)

## 12. Related problems

- `../../exercises/starter-code/best_time_to_buy_sell_stock.py` — starter code.
- `../../lessons/arrays/arrays-and-lists.md` — single-pass tracking pattern.
