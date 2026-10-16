"""Solution: array stats in one pass. O(n) time, O(1) space."""


def array_stats(nums: list[int]) -> tuple[int, int, int] | None:
    if not nums:
        return None
    best_min = best_max = total = nums[0]
    for value in nums[1:]:
        if value < best_min:
            best_min = value
        if value > best_max:
            best_max = value
        total += value
    return best_min, best_max, total


if __name__ == "__main__":
    print(array_stats([3, 1, 4, 1, 5]))  # (1, 5, 14)
