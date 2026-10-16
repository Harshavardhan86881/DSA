"""Solution: Subsets. O(n * 2^n) time, O(n) auxiliary space.

Position-based subsets: duplicate input values may produce duplicate subsets.
"""


def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


if __name__ == "__main__":
    print(subsets([1, 2, 3]))
