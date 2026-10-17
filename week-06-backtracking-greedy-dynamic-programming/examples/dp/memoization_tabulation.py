"""Runnable example: memoization and tabulation for the same recurrence.

Lesson: ../../lessons/dp/dp.md
"""


def climb_memo(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n <= 1:
        return 1
    cache[n] = climb_memo(n - 1, cache) + climb_memo(n - 2, cache)
    return cache[n]


def climb_tabulation(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == "__main__":
    print("memo:", climb_memo(10))
    print("table:", climb_tabulation(10))
