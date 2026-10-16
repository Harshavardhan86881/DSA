"""Duplicate detection with a set.

Run: python3 duplicate_detector.py
"""


def has_duplicate(nums: list[int]) -> bool:
    seen: set[int] = set()
    for value in nums:
        if value in seen:
            return True
        seen.add(value)
    return False


def main() -> None:
    print(has_duplicate([1, 2, 3, 1]))  # True
    print(has_duplicate([1, 2, 3]))      # False
    print(has_duplicate([]))            # False


if __name__ == "__main__":
    main()
