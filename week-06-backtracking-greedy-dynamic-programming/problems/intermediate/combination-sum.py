"""Solution: Combination Sum. Exponential worst case; pruning improves practice.

Each candidate may be reused. Candidates are assumed positive.
"""


def combination_sum(candidates, target):
    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])
            path.pop()

    backtrack(0, [], target)
    return result


if __name__ == "__main__":
    print(combination_sum([2, 3, 6, 7], 7))
