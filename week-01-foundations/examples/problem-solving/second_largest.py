"""Find the second-largest distinct value in one pass.

Run: python3 second_largest.py
"""


def second_largest(nums: list[int]) -> int | None:
    """Return the second-largest distinct value, or None. O(n) time, O(1) space."""
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


def main() -> None:
    print(second_largest([3, 1, 4, 4, 2]))  # 3
    print(second_largest([5, 5, 5]))         # None
    print(second_largest([]))                # None
    print(second_largest([9]))               # None
    print(second_largest([-1, -3, -2]))      # -2


if __name__ == "__main__":
    main()
