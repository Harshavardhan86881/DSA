# Longest Increasing Subsequence

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | dynamic programming |
| **Target time** | 25 minutes |
| **Solution file** | [longest-increasing-subsequence.py](longest-increasing-subsequence.py) |

## 1. Problem statement

Given an integer array `nums`, return the length of the longest strictly increasing subsequence. A subsequence keeps relative order but need not be contiguous.

Function contract: `length_of_lis(nums: list[int]) -> int`.

## 2. Constraints

- `0 <= len(nums) <= 2500`
- `-10^4 <= nums[i] <= 10^4`

## 3. Examples

Input: `nums = [10,9,2,5,3,7,101,18]`
Output: `4`
Explanation: one LIS is `[2,3,7,101]`.

Input: `nums = [0,1,0,3,2,3]`
Output: `4`.

Input: `nums = []`
Output: `0`.

## 4. Hints

<details><summary>Hint 1</summary>
Let dp[i] be the best increasing subsequence ending at index i.
</details>

<details><summary>Hint 2</summary>
For each i, check all j < i where nums[j] < nums[i].
</details>

## 5. Brute-force approach

Try all subsequences recursively. This is exponential.

## 6. Optimised approach

Use O(n^2) DP. `dp[i] = max(dp[j] + 1)` for `j < i` with `nums[j] < nums[i]`, else 1. Return `max(dp)`.

Important code lines:

- `dp = [1] * len(nums)`: each element alone has length 1.
- `if nums[j] < nums[i]`: strict increase.
- `dp[i] = max(dp[i], dp[j] + 1)`: transition.
- `return max(dp)`: best ending position.

## 7. Complexity analysis

- Time: O(n^2).
- Space: O(n).

An O(n log n) optimization exists, but this implementation is O(n^2).

## 8. Edge cases and tests

- Empty input.
- Single element.
- Strictly decreasing input.
- Duplicates.
- All equal values.

## 9. Common mistakes

- Using `<=` instead of `<`.
- Forgetting empty input.
- Claiming O(n log n) for the quadratic version.

## 10. Follow-up questions

1. How does the O(n log n) version work?
2. What changes for non-decreasing subsequence?
3. How would you reconstruct one LIS?

## 11. Related problems

- `../../exercises/starter-code/longest_increasing_subsequence.py` — starter code.
- `../../exercises/solutions/longest_increasing_subsequence.py` — solution.
- `../../exercises/test-cases/test_longest_increasing_subsequence.py` — tests.
- `../../lessons/dp/dp.md` — lesson.
