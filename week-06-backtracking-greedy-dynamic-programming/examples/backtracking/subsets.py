"""Runnable example: generate all subsets with choose, explore, undo.

Lesson: ../../lessons/backtracking/backtracking.md
Complexity: O(n * 2^n) time, O(n) auxiliary space.
"""


def subsets(nums):
    """Return all subsets of nums (position-based; duplicates may repeat)."""
    result = []

    def backtrack(start, path):
        result.append(path[:])  # snapshot; path will change later
        for i in range(start, len(nums)):
            path.append(nums[i])   # choose
            backtrack(i + 1, path)  # explore
            path.pop()              # undo

    backtrack(0, [])
    return result


if __name__ == "__main__":
    print(subsets([1, 2, 3]))
    print("count:", len(subsets([1, 2, 3, 4])), "expected:", 2 ** 4)
