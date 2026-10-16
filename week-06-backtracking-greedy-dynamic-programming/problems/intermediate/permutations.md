# Permutations

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | backtracking |
| **Target time** | 25 minutes |
| **Solution file** | [permutations.py](permutations.py) |

## 1. Problem statement

Given an array `nums`, return all permutations of its positions. You may return them in any order. If values repeat, this position-based version may return duplicate value-arrangements; the unique-permutation follow-up asks you to remove those duplicates.

Function contract: `permute(nums: list[int]) -> list[list[int]]`.

## 2. Constraints

- `0 <= len(nums) <= 6`
- `-10 <= nums[i] <= 10`
- Values may repeat; this implementation treats positions separately, so duplicate values can produce duplicate value-arrangements.

## 3. Examples

Input: `nums = [1,2,3]`
Output: `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`.

Input: `nums = [1]`
Output: `[[1]]`.

## 4. Hints

<details><summary>Hint 1</summary>
At each level, choose an unused element.
</details>

<details><summary>Hint 2</summary>
Use a boolean `used` array.
</details>

<details><summary>Hint 3</summary>
When the path length equals `len(nums)`, record a copy.
</details>

## 5. Brute-force approach

Generate all sequences of length n from n elements without tracking used elements. This creates invalid repeated elements and exponential blowup.

## 6. Optimised approach

Backtrack with a `used` array. At each level, try every unused index, mark it used, recurse, then undo.

Important code lines:

- `if len(path) == len(nums)`: base case.
- `if used[i]: continue`: skip used elements.
- `used[i] = True` and `used[i] = False`: choose and undo.
- `path[:]`: snapshot.

## 7. Complexity analysis

- Time: O(n * n!).
- Auxiliary space: O(n), excluding output.

## 8. Edge cases and tests

- Single element.
- Empty input returns `[[]]`, representing the single permutation of zero elements.
- Duplicate values may produce duplicate value-arrangements because indices, not values, are marked as used.

## 9. Common mistakes

- Forgetting to unmark `used`.
- Storing a mutable path.
- Reusing an element.

## 10. Follow-up questions

1. How would you handle duplicate values uniquely?
2. How would you generate permutations iteratively?
3. What is the complexity for n = 10?

## 11. Related problems

- `../../exercises/starter-code/permutations.py` — starter code.
- `../../exercises/solutions/permutations.py` — solution.
- `../../exercises/test-cases/test_permutations.py` — tests.
- `../../lessons/backtracking/backtracking.md` — lesson.
