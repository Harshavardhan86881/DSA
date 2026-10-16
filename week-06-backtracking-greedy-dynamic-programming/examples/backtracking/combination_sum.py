"""Runnable example: combination sum with reuse and pruning.

Lesson: ../../lessons/backtracking/backtracking.md
Complexity: exponential worst case; pruning improves practical runtime.
"""


def combination_sum(candidates, target):
    """Return combinations that sum to target; each candidate may be reused."""
    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:  # prune: no positive candidate can fix this
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])
            path.pop()

    backtrack(0, [], target)
    return result


if __name__ == "__main__":
    print(combination_sum([2, 3, 6, 7], 7))
