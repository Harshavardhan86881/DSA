# Greedy Algorithms

| | |
| --- | --- |
| **Week** | 6 — Backtracking, greedy, dynamic programming |
| **Topic** | Greedy algorithms |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Sorting |
| **Deliverable** | `exercises/starter-code/activity_selection.py` attempted |

## 1. Learning objectives

After this lesson you can:

1. Explain local optimal choice versus global optimum.
2. State when greedy works and why intuition is insufficient.
3. Explain greedy-choice property and optimal substructure simply.
4. Solve activity selection by sorting by finish time.
5. Compare sorting by start time, duration, and finish time.
6. Give a counterexample for a failing greedy rule.
7. Use an exchange-argument intuition.
8. Test a proposed greedy rule before implementing it.

## 2. Prerequisites check

1. Can you sort intervals by a key?
2. Can you explain what an optimal substructure is?
3. Can you construct a small counterexample?

## 3. Why this matters

Greedy algorithms are fast and simple, but they are easy to get wrong. Interviewers often ask you to justify why a greedy choice is safe or to provide a counterexample.

## 4. Build intuition

Greedy makes the best-looking choice now and never revisits it. It works only when a local best choice can be extended to a global best solution.

Mental model: picking the activity that finishes earliest leaves the most room for future activities.

## 5. Greedy-choice property and optimal substructure

- Greedy-choice property: a globally optimal solution can be built by making a locally optimal choice first.
- Optimal substructure: an optimal solution contains optimal solutions to subproblems.

Beginner version: if choosing the earliest-finishing activity never hurts the rest of the schedule, greedy is safe.

## 6. Activity selection

Problem: given intervals `[start, end)`, select the maximum number of non-overlapping activities. An activity ending at time `t` can be followed by an activity starting at time `t`.

```python
def max_activities(intervals):
    ordered = sorted(intervals, key=lambda interval: interval[1])
    count = 0
    last_end = float("-inf")
    for start, end in ordered:
        if start >= last_end:
            count += 1
            last_end = end
    return count
```

Why sort by finish time: the activity that finishes earliest leaves the maximum remaining time.

Worked comparison for intervals `[(1,4),(2,3),(3,5)]`:

| Sort key | Order | Selected | Count |
| --- | --- | --- | --- |
| finish time | (2,3),(1,4),(3,5) | (2,3),(3,5) | 2 |
| start time | (1,4),(2,3),(3,5) | (1,4) or (2,3),(3,5) | 1 or 2 |
| duration | (2,3),(1,4),(3,5) | (2,3),(3,5) | 2 |

Finish-time sorting is the only rule that guarantees the maximum in all cases.

## 7. Exchange argument intuition

Suppose an optimal solution does not include the earliest-finishing activity A. Replace its first activity with A. Since A finishes no later, the replacement cannot create an overlap. Thus an optimal solution exists that includes A. Repeat for the remaining activities.

## 8. Counterexample for a failing greedy

Coin denominations `[1, 3, 4]`, amount `6`:

- Greedy largest coin: 4 + 1 + 1 = 3 coins.
- Optimal: 3 + 3 = 2 coins.

So taking the largest coin first does not solve arbitrary coin systems optimally. Greedy works for canonical systems such as standard US coins, but not in general.

## 9. When greedy fails

Greedy can fail when a locally best choice blocks a better combination later. Use DP or backtracking when choices interact and future cost matters.

## 10. How to test a greedy rule

1. Try small examples by hand.
2. Try equal endpoints and nested intervals.
3. Try to construct a case where the rule picks a suboptimal first item.
4. If you find one, the rule is invalid.
5. If no counterexample appears, attempt an exchange argument.

## 11. Complexity and edge cases

- Time: O(n log n) due to sorting.
- Extra space: O(1) if sorting in place, otherwise O(n).
- Edge cases: empty input, one activity, equal start/end times, nested intervals, duplicate intervals.

Interval semantics: an activity ending at time `t` can be followed by an activity starting at `t`, implemented as `start >= last_end`.

## 12. Common mistakes

- Sorting by start time or duration instead of finish time.
- Using `>` instead of `>=` and dropping valid back-to-back activities.
- Assuming greedy works without a proof or counterexample test.
- Applying largest-coin-first to arbitrary coin systems.

## 13. Debugging checklist

1. Print sorted intervals.
2. Print `last_end` and selected intervals.
3. Test empty input and equal endpoints.
4. Compare with brute force on random small inputs.

## 14. Practice

### Guided exercise 1

Trace activity selection on `[(1,3),(2,4),(3,5),(0,6),(5,7),(8,9)]`.

### Guided exercise 2

Compare sort by start, duration, and finish.

### Independent exercise 1

Implement activity selection.

### Independent exercise 2

Find a greedy counterexample for coin change.

### Debugging exercise

Fix:

```python
def bad_max_activities(intervals):
    ordered = sorted(intervals)  # sorts by start, then end
    count = 0
    last_end = float("-inf")
    for start, end in ordered:
        if start > last_end:
            count += 1
            last_end = end
    return count
```

### Prediction exercise

Does greedy always find the maximum independent set in a general graph? Answer: No.

## 15. Active-recall questions

1. What does greedy optimize locally?
2. Why sort by finish time?
3. What is an exchange argument?
4. When does largest-coin-first fail?
5. What interval condition allows back-to-back activities?

Answers:

1. The immediate best choice.
2. To leave maximum remaining time.
3. Replacing an optimal first item with the greedy choice cannot worsen the result.
4. Arbitrary coin systems.
5. `start >= last_end`.

## 16. Interview questions

**Q:** How do you prove a greedy algorithm?
**A:** Show greedy-choice property and optimal substructure, often with an exchange argument.

**Q:** Give a greedy counterexample.
**A:** Coin denominations 1, 3, 4 for amount 6: greedy gives 3 coins, optimal gives 2.

Follow-up: How would you test a greedy rule quickly? Try small random cases against brute force.

## 17. Spaced-repetition checklist

- Day 1: Write activity selection.
- Day 3: Find a greedy counterexample.
- Day 7: Explain exchange argument.
- Day 14: Compare greedy and DP on coin change.

## 18. Explain aloud

"Greedy picks the locally best option and commits. For intervals, sorting by finish time leaves the most room, and an exchange argument shows this is safe."
