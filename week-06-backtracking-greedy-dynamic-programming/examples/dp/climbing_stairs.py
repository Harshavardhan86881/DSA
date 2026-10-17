"""Runnable example: climbing stairs with tabulation and space optimization.

Lesson: ../../lessons/dp/dp.md
Complexity: O(n) time, O(1) space.
"""


def climb_stairs(n):
    """Return the number of ways to climb n stairs using 1 or 2 steps."""
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
    for n in range(8):
        print(n, climb_stairs(n))
