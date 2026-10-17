"""Solution for 'Maximum Subarray'. O(n) time, O(1) space."""


def max_subarray(nums: list[int]) -> int:
    if not nums:
        return 0
    best = running = nums[0]
    for value in nums[1:]:
        running = max(value, running + value)
        best = max(best, running)
    return best


if __name__ == "__main__":
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
