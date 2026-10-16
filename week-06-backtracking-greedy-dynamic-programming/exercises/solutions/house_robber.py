"""Solution: House Robber. O(n) time, O(1) space."""


def rob(nums):
    prev2, prev1 = 0, 0
    for num in nums:
        cur = max(prev1, prev2 + num)
        prev2, prev1 = prev1, cur
    return prev1
