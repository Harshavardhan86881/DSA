# Activity Selection

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | greedy |
| **Target time** | 20 minutes |
| **Solution file** | [activity-selection.py](activity-selection.py) |

## 1. Problem statement

Given a list of activities as `(start, end)` intervals, return the maximum number of activities that can be selected without overlapping. An activity ending at time `t` can be followed by an activity starting at time `t`.

Function contract: `max_activities(intervals: list[tuple[int, int]]) -> int`.

## 2. Constraints

- `0 <= len(intervals) <= 10^5`
- `0 <= start <= end <= 10^9`
- Intervals may be unsorted.

## 3. Examples

Input: `[(1,3),(2,4),(3,5),(0,6),(5,7),(8,9)]`
Output: `4`
Explanation: choose `(1,3)`, `(3,5)`, `(5,7)`, `(8,9)`.

Input: `[]`
Output: `0`.

## 4. Hints

<details><summary>Hint 1</summary>
Sort by finish time.
</details>

<details><summary>Hint 2</summary>
Keep the last selected finish time and accept an interval when its start is at least that time.
</details>

## 5. Brute-force approach

Try all subsets of activities and check non-overlap. This is exponential and only useful for tiny inputs.

## 6. Optimised approach

Sort by finish time. Greedily select the earliest-finishing compatible activity. Use an exchange argument to justify safety.

Important code lines:

- `sorted(intervals, key=lambda interval: interval[1])`: sort by finish time.
- `if start >= last_end`: compatibility check.
- `last_end = end`: commit to selected activity.

## 7. Complexity analysis

- Time: O(n log n).
- Auxiliary space: O(1) if sorting in place, otherwise O(n).

## 8. Edge cases and tests

- Empty input.
- One activity.
- Equal start/end times.
- Nested intervals.
- Back-to-back activities.

## 9. Common mistakes

- Sorting by start time or duration.
- Using `>` instead of `>=`.
- Assuming greedy works without a counterexample test.

## 10. Follow-up questions

1. How would you return the selected intervals, not just the count?
2. What is a greedy counterexample?
3. When is DP more appropriate?

## 11. Related problems

- `../../exercises/starter-code/activity_selection.py` — starter code.
- `../../exercises/solutions/activity_selection.py` — solution.
- `../../exercises/test-cases/test_activity_selection.py` — tests.
- `../../lessons/greedy/greedy.md` — lesson.
