"""Solution for 'Reverse an Array'. O(n) time, O(1) extra space."""


def reverse_in_place(nums: list[int]) -> None:
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    reverse_in_place(data)
    print(data)
