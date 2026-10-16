"""Solution for 'Find the Second-Largest Distinct Element'. O(n) time, O(1) space."""


def second_largest(nums: list[int]) -> int | None:
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
    print(second_largest([3, 1, 4, 4, 2]))  # 3
