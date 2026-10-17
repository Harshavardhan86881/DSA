"""Solution: Find First and Last Position. O(log n) time, O(1) space."""


def first_and_last(nums: list[int], target: int) -> list[int]:
    def first() -> int:
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

    def last() -> int:
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

    if not nums:
        return [-1, -1]
    f = first()
    if f == -1:
        return [-1, -1]
    return [f, last()]


if __name__ == "__main__":
    print(first_and_last([5, 7, 7, 8, 8, 10], 8))  # [3, 4]
