# Week 6 Assessment

**Time limit:** 90 minutes  
**Total:** 100 points  
**Passing target:** 70 points  
**Rules:** Attempt without viewing solutions. You may use Python's standard library. Explain your state/choice and complexity in comments or a short written note.

## Part A — Coding (72 points)

1. **Subsets (18 points, 20 minutes)**  
   Implement `subsets(nums)`. Include the empty subset, avoid reusing an index, and explain why you copy the current path.

2. **Coin Change (22 points, 25 minutes)**  
   Implement minimum-coin DP with unlimited coins. Return `0` for amount `0`, `-1` when impossible, and reject non-positive coin denominations. Explain the state, transition, and complexity.

3. **House Robber (16 points, 20 minutes)**  
   Return the maximum amount without selecting adjacent elements. Handle an empty list and explain the two rolling variables.

4. **Activity Selection (16 points, 15 minutes)**  
   Return the maximum number of non-overlapping intervals. Treat intervals as half-open: an activity may start exactly when the previous one ends.

## Part B — Concepts (28 points, 10 minutes)

1. Define a DP state for one problem from this week (7 points).
2. Give a concrete counterexample showing why largest-coin-first greedy can fail (7 points).
3. Explain the choose/explore/undo pattern and why the undo step matters (7 points).
4. Compare memoization and tabulation (7 points).

## Scoring rubric

For each coding problem, award points for:
- Correct algorithm and output (50% of that problem's points).
- Edge cases and input contract (20%).
- Clear state/choice or recurrence reasoning (20%).
- Correct time and space complexity (10%).

For concepts, award full credit only when the answer is accurate and includes a relevant example or explanation. Partial credit is allowed for correct reasoning with a minor implementation or wording mistake.

## Review after scoring

- **90–100:** Strong; solve a new variation without notes.
- **70–89:** Pass; revisit missed edge cases and redo one problem from memory.
- **Below 70:** Review the corresponding lesson, then retry the assessment after a day. Do not memorize the answer key.
