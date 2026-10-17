"""Solution: Two Sum. O(n) time, O(n) space."""


def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for i, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], i]
        seen[value] = i
    raise ValueError("no solution found")


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
