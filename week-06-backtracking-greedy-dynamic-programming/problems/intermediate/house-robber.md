# House Robber

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | dynamic programming |
| **Target time** | 20 minutes |
| **Solution file** | [house-robber.py](house-robber.py) |

## 1. Problem statement

You are a robber planning to rob houses along a street. Adjacent houses have connected security systems, so you cannot rob two adjacent houses. Given an array of money in each house, return the maximum amount you can rob.

Function contract: `rob(nums: list[int]) -> int`.

## 2. Constraints

- `0 <= len(nums) <= 100`
- `0 <= nums[i] <= 400`

## 3. Examples

Input: `nums = [1,2,3,1]`
Output: `4`
Explanation: rob house 0 and house 2.

Input: `nums = [2,7,9,3,1]`
Output: `12`.

Input: `nums = []`
Output: `0`.

## 4. Hints

<details><summary>Hint 1</summary>
At each house, choose between robbing it or skipping it.
</details>

<details><summary>Hint 2</summary>
If you rob it, add its value to the best result two houses back.
</details>

## 5. Brute-force approach

Try all subsets of houses and reject adjacent pairs. This is exponential.

## 6. Optimised approach

Use DP with state `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`. Optimize space to two variables.

Important code lines:

- `cur = max(prev1, prev2 + num)`: take or skip.
- `prev2, prev1 = prev1, cur`: shift state.

## 7. Complexity analysis

- Time: O(n).
- Auxiliary space: O(1).

## 8. Edge cases and tests

- Empty list.
- Single house.
- Two adjacent houses.
- All zeros.

## 9. Common mistakes

- Forgetting to skip adjacent houses.
- Wrong initialization for empty input.
- Using O(n) space when O(1) is enough.

## 10. Follow-up questions

1. How would you reconstruct the robbed houses?
2. What changes if houses are in a circle?
3. How does the state change for House Robber II?

## 11. Related problems

- `../../exercises/starter-code/house_robber.py` — starter code.
- `../../exercises/solutions/house_robber.py` — solution.
- `../../exercises/test-cases/test_house_robber.py` — tests.
- `../../lessons/dp/dp.md` — lesson.
