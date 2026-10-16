"""Solution: Climbing Stairs. O(n) time, O(1) space."""


def climb_stairs(n):
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        cur = prev1 + prev2
        prev2, prev1 = prev1, cur
    return prev1
