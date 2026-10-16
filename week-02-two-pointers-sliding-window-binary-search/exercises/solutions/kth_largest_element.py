"""Solution: Kth Largest Element. O(n log n) time, O(1) extra space (in-place sort)."""


def find_kth_largest(nums: list[int], k: int) -> int:
    nums_sorted = sorted(nums, reverse=True)
    return nums_sorted[k - 1]


if __name__ == "__main__":
    print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # 5
