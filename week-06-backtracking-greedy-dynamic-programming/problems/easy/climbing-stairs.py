"""Solution: Climbing Stairs. O(n) time, O(1) space.

Input contract: n is a non-negative integer.
"""


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


if __name__ == "__main__":
    print(climb_stairs(5))
