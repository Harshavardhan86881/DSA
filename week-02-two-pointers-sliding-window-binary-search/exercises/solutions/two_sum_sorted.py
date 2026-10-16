"""Solution: Two Sum II (sorted input). O(n) time, O(1) space."""


def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        if s < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]


if __name__ == "__main__":
    print(two_sum_sorted([1, 2, 3, 4, 6], 6))  # [1, 3]
