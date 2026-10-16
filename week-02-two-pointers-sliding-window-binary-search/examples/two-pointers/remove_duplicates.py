"""Remove duplicates in place using read/write pointers.

Run: python3 remove_duplicates.py
"""


def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write


def main() -> None:
    data = [1, 1, 2, 2, 3]
    k = remove_duplicates(data)
    print(k, data[:k])  # 3 [1, 2, 3]
    empty: list[int] = []
    print(remove_duplicates(empty), empty)  # 0 []


if __name__ == "__main__":
    main()
