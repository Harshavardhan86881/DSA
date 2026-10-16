"""Solution: Contains Duplicate. O(n) time average, O(n) space."""


def contains_duplicate(nums: list[int]) -> bool:
    seen: set[int] = set()
    for value in nums:
        if value in seen:
            return True
        seen.add(value)
    return False


if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))  # True
