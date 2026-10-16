"""Solution for 'Sort Then Two Sum'. O(n log n) time, O(n) space."""


def has_pair_sum(nums: list[int], target: int) -> bool:
    s = sorted(nums)
    left, right = 0, len(s) - 1
    while left < right:
        total = s[left] + s[right]
        if total == target:
            return True
        if total < target:
            left += 1
        else:
            right -= 1
    return False


if __name__ == "__main__":
    print(has_pair_sum([3, 2, 4], 6))  # True
