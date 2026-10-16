"""Runnable example: generate all permutations with a used array.

Lesson: ../../lessons/backtracking/backtracking.md
Complexity: O(n * n!) time, O(n) auxiliary space.
"""


def permute(nums):
    """Return all permutations of nums."""
    result = []

    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False

    backtrack([], [False] * len(nums))
    return result


if __name__ == "__main__":
    print(permute([1, 2, 3]))
    print("count:", len(permute([1, 2, 3, 4])), "expected:", 24)
