"""Solution: find min and max in one pass. O(n) time, O(1) extra space."""


def find_min_max(nums: list[int]) -> tuple[int, int] | None:
    if not nums:
        return None
    best_min = best_max = nums[0]
    for value in nums[1:]:
        if value < best_min:
            best_min = value
        if value > best_max:
            best_max = value
    return best_min, best_max


if __name__ == "__main__":
    print(find_min_max([3, 1, 4, 1, 5]))  # (1, 5)
