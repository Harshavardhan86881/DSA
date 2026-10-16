"""Solution: running sum of a 1D array. O(n) time, O(n) space (output)."""


def running_sum(nums: list[int]) -> list[int]:
    output: list[int] = []
    total = 0
    for value in nums:
        total += value
        output.append(total)
    return output


if __name__ == "__main__":
    print(running_sum([1, 2, 3, 4]))  # [1, 3, 6, 10]
