"""Solution for 'Minimum Size Subarray Sum'. O(n) time, O(1) space."""


def min_subarray_len(target: int, nums: list[int]) -> int:
    left = 0
    running = 0
    best = float("inf")
    for right in range(len(nums)):
        running += nums[right]
        while running >= target:
            if right - left + 1 < best:
                best = right - left + 1
            running -= nums[left]
            left += 1
    return 0 if best == float("inf") else int(best)


if __name__ == "__main__":
    print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))  # 2
