"""Solution for 'Search Insert Position'. O(log n) time, O(1) space."""


def search_insert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == "__main__":
    print(search_insert([1, 3, 5, 6], 5))  # 2
