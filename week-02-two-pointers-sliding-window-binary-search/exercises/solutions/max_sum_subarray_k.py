"""Solution: Maximum Sum Subarray of Size K. O(n) time, O(1) space."""


def max_sum_subarray_k(nums: list[int], k: int) -> int:
    if not nums or k <= 0 or k > len(nums):
        return 0
    window_sum = sum(nums[:k])
    best = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        if window_sum > best:
            best = window_sum
    return best


if __name__ == "__main__":
    print(max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3))  # 9
