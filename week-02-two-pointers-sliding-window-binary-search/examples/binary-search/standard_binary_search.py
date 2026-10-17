"""Standard binary search plus first/last occurrence.

Run: python3 standard_binary_search.py
"""


def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def first_occurrence(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            result = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


def last_occurrence(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            result = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


def main() -> None:
    nums = [1, 2, 2, 2, 3]
    print("search 2:", binary_search(nums, 2))
    print("first 2:", first_occurrence(nums, 2))
    print("last 2:", last_occurrence(nums, 2))
    print("search 5:", binary_search(nums, 5))


if __name__ == "__main__":
    main()
