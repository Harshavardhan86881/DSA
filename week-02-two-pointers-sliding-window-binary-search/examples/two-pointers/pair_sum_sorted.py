"""Pair sum in a sorted array using two pointers.

Run: python3 pair_sum_sorted.py
"""


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


def main() -> None:
    print(two_sum_sorted([1, 2, 3, 4, 6], 6))   # [1, 3]
    print(two_sum_sorted([1, 2, 3, 4, 6], 10))  # [3, 4]
    print(two_sum_sorted([1, 2, 3, 4, 6], 100)) # [-1, -1]
    print(two_sum_sorted([], 5))                 # [-1, -1]


if __name__ == "__main__":
    main()
