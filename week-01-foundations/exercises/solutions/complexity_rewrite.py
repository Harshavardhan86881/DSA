"""Solution: complexity rewrites with stated complexities."""


def reverse_in_place(nums: list[int]) -> None:
    # O(n) time, O(1) extra space: two pointers, in-place swaps.
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def reverse_new_list(nums: list[int]) -> list[int]:
    # O(n) time, O(n) extra space: builds a new list.
    result: list[int] = []
    for i in range(len(nums) - 1, -1, -1):
        result.append(nums[i])
    return result


def second_largest(nums: list[int]) -> int | None:
    # O(n) time, O(1) extra space: single pass, two trackers.
    if len(nums) < 2:
        return None
    largest: int | None = None
    second: int | None = None
    for value in nums:
        if largest is None or value > largest:
            second = largest
            largest = value
        elif value != largest and (second is None or value > second):
            second = value
    return second


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    reverse_in_place(data)
    print(data)
    print(reverse_new_list([1, 2, 3, 4, 5]))
    print(second_largest([3, 1, 4, 4, 2]))
