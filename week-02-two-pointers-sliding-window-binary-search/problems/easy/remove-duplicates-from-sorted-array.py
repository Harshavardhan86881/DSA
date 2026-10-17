"""Solution for 'Remove Duplicates from Sorted Array'. O(n) time, O(1) space."""


def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write


if __name__ == "__main__":
    data = [1, 1, 2, 2, 3]
    k = remove_duplicates(data)
    print(k, data[:k])  # 3 [1, 2, 3]
