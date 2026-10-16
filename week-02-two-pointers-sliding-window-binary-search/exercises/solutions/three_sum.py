"""Solution: 3Sum. O(n^2) time, O(1) extra space (excluding output)."""


def three_sum(nums: list[int]) -> list[list[int]]:
    nums_sorted = sorted(nums)
    result: list[list[int]] = []
    n = len(nums_sorted)
    for i in range(n):
        if i > 0 and nums_sorted[i] == nums_sorted[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums_sorted[i] + nums_sorted[left] + nums_sorted[right]
            if total == 0:
                result.append([nums_sorted[i], nums_sorted[left], nums_sorted[right]])
                left += 1
                right -= 1
                while left < right and nums_sorted[left] == nums_sorted[left - 1]:
                    left += 1
                while left < right and nums_sorted[right] == nums_sorted[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result


if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))
