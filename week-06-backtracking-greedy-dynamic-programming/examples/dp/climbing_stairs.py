"""Runnable example: climbing stairs DP."""


def climb_stairs(n):
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        cur = prev1 + prev2
        prev2, prev1 = prev1, cur
    return prev1


if __name__ == "__main__":
    print(climb_stairs(5))
