# Coin Change

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | DP |
| **Target time** | 25 minutes |
| **Solution file** | [coin-change.py](coin-change.py) |

## 1. Problem statement

Minimum coins to make amount.

## 2. Constraints

Reasonable input sizes.

## 3. Examples

```text
See solution file.
```

## 4. Hints

<details><summary>Hint 1</summary>
Use recursion/DP as appropriate.
</details>

## 5. Optimised approach

```python
"""Solution: Coin Change. O(amount * len(coins)) time, O(amount) space."""


def coin_change(coins, amount):
    INF = amount + 1
    dp = [INF] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                dp[a] = min(dp[a], dp[a - coin] + 1)
    return dp[amount] if dp[amount] != INF else -1
```

## 6. Complexity analysis

See solution docstring.

## 7. Edge cases and tests

See `../../exercises/test-cases/`.

## 8. Follow-up questions

1. Can you reduce space?
2. What is the time complexity?
3. How to handle duplicates?

## 9. Related problems

- `../../exercises/starter-code/coin_change.py` — starter code.
