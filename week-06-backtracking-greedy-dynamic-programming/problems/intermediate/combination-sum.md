# Combination Sum

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | backtracking, pruning |
| **Target time** | 25 minutes |
| **Solution file** | [combination-sum.py](combination-sum.py) |

## 1. Problem statement

Given an array of positive integers `candidates` and a target integer, return all unique combinations of candidates that sum to target. The same candidate may be used unlimited times. Combinations are compared as multisets; order within a combination does not matter.

Function contract: `combination_sum(candidates: list[int], target: int) -> list[list[int]]`.

## 2. Constraints

- `1 <= len(candidates) <= 30`
- `1 <= candidates[i] <= 200`
- `1 <= target <= 500`
- Candidates may contain duplicates; duplicate candidates may lead to duplicate combinations unless deduplicated.

## 3. Examples

Input: `candidates = [2,3,6,7], target = 7`
Output: `[[2,2,3],[7]]`.

Input: `candidates = [2], target = 1`
Output: `[]`.

## 4. Hints

<details><summary>Hint 1</summary>
Use backtracking with a start index to avoid duplicate orderings.
</details>

<details><summary>Hint 2</summary>
Pass `i`, not `i + 1`, when reusing a candidate.
</details>

<details><summary>Hint 3</summary>
Prune when remaining becomes negative.
</details>

## 5. Brute-force approach

Generate all sequences of candidates and keep those summing to target. This creates duplicate orderings and exponential blowup.

## 6. Optimised approach

Sort if needed, then backtrack by choosing candidates from `start` onward. Reuse is allowed by recursing with the same index. Prune negative remainders.

Important code lines:

- `if remaining == 0`: record a copy.
- `if remaining < 0`: prune.
- `for i in range(start, len(candidates))`: avoid duplicate orderings.
- `backtrack(i, ...)`: allow reuse.
- `path.pop()`: undo.

## 7. Complexity analysis

- Worst case: exponential in target and candidate size.
- Pruning improves practical runtime but does not guarantee a better worst-case asymptotic bound.

## 8. Edge cases and tests

- Target 0 returns `[[]]` under this implementation.
- No solution returns `[]`.
- Candidate larger than target.
- Duplicate candidates.

## 9. Common mistakes

- Passing `i + 1` and accidentally disallowing reuse.
- Forgetting to copy path.
- Pruning a valid branch.

## 10. Follow-up questions

1. How would you handle each candidate used at most once?
2. How would you remove duplicate combinations from duplicate candidates?
3. How would you count solutions without storing them?

## 11. Related problems

- `../../exercises/starter-code/combination_sum.py` — starter code.
- `../../exercises/solutions/combination_sum.py` — solution.
- `../../exercises/test-cases/test_combination_sum.py` — tests.
- `../../lessons/backtracking/backtracking.md` — lesson.
