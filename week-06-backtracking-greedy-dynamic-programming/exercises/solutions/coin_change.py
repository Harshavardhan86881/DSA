"""Solution: Coin Change. O(amount * len(coins)) time, O(amount) space.

Minimum coins for amount using unlimited coins. Returns -1 if impossible.
"""


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


if __name__ == "__main__":
    print(coin_change([1, 2, 5], 11))
