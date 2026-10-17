"""Runnable example: greedy largest-coin-first can fail.

Lesson: ../../lessons/greedy/greedy.md
"""


def greedy_coin_change(coins, amount):
    coins = sorted(coins, reverse=True)
    count = 0
    remaining = amount
    for coin in coins:
        while remaining >= coin:
            remaining -= coin
            count += 1
    return count if remaining == 0 else None


if __name__ == "__main__":
    coins = [1, 3, 4]
    amount = 6
    print("greedy coins:", greedy_coin_change(coins, amount))
    print("optimal coins: 2 (3 + 3)")
