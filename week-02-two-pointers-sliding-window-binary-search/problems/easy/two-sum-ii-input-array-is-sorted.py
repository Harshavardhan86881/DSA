"""Solution for 'Two Sum II'. O(n) time, O(1) space."""


def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left, right]
        if s < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]


if __name__ == "__main__":
    print(two_sum_sorted([2, 7, 11, 15], 9))  # [1, 2]
