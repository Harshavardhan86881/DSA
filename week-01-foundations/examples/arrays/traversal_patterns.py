"""Three ways to traverse a list.

Run: python3 traversal_patterns.py
"""


def by_value(nums: list[int]) -> int:
    total = 0
    for value in nums:          # value only
        total += value
    return total


def by_index(nums: list[int]) -> None:
    for i in range(len(nums)):  # index, write back
        nums[i] *= 2


def by_enumerate(nums: list[int]) -> list[tuple[int, int]]:
    return [(i, v) for i, v in enumerate(nums)]


def main() -> None:
    data = [1, 2, 3, 4]
    print("by_value:", by_value(data))
    by_index(data)
    print("after by_index:", data)
    print("enumerate:", by_enumerate([10, 20, 30]))


if __name__ == "__main__":
    main()
