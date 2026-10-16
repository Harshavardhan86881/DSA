"""Reverse an array in place, plus a new-list variant.

Run: python3 reverse_array.py
"""


def reverse_in_place(nums: list[int]) -> None:
    """Reverse nums in place using two pointers. O(n) time, O(1) space."""
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def reverse_new(nums: list[int]) -> list[int]:
    """Return a new reversed list. O(n) time, O(n) space."""
    result: list[int] = []
    for i in range(len(nums) - 1, -1, -1):
        result.append(nums[i])
    return result


def main() -> None:
    data = [1, 2, 3, 4, 5]
    print("original:", data)
    reverse_in_place(data)
    print("in place:", data)
    print("new list:", reverse_new([1, 2, 3, 4, 5]))
    # edge cases
    empty: list[int] = []
    reverse_in_place(empty)
    print("empty in place:", empty)
    single = [7]
    reverse_in_place(single)
    print("single in place:", single)


if __name__ == "__main__":
    main()
