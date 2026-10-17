"""Lower bound, upper bound, and insertion position.

Run: python3 bounds.py
"""


def lower_bound(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def upper_bound(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


def main() -> None:
    nums = [1, 2, 2, 2, 3]
    lo = lower_bound(nums, 2)
    hi = upper_bound(nums, 2)
    print("lower:", lo, "upper:", hi, "count:", hi - lo)
    print("insert 2.5:", lower_bound(nums, 2))  # same as lower_bound
    print("insert 0:", lower_bound(nums, 0))
    print("insert 4:", lower_bound(nums, 4))


if __name__ == "__main__":
    main()
