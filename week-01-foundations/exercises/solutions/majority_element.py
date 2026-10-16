"""Solution: Majority Element. O(n) time, O(n) space."""


def majority_element(nums: list[int]) -> int | None:
    if not nums:
        return None
    counts: dict[int, int] = {}
    for value in nums:
        counts[value] = counts.get(value, 0) + 1
    for value, count in counts.items():
        if count > len(nums) // 2:
            return value
    return None


if __name__ == "__main__":
    print(majority_element([3, 2, 3]))  # 3
