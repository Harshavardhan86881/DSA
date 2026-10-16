# Week 6 Answer Key and Scoring Notes

Use this after attempting the assessment. Compare reasoning and edge cases, not just final output.

## Part A — Coding

### 1. Subsets
Use backtracking. Record `path[:]` at each node, loop from a `start` index, recurse with `i + 1`, then undo with `path.pop()`. There are `2^n` subsets; generating and copying them takes `O(n * 2^n)` time and `O(n)` auxiliary recursion/path space, excluding output.

### 2. Coin Change
Let `dp[a]` be the minimum number of coins needed to form amount `a`. Set `dp[0] = 0`; initialize other states to an unreachable sentinel. For each amount, try every denomination no greater than that amount: `dp[a] = min(dp[a], dp[a - coin] + 1)`. Return `-1` if the target state remains unreachable. Validate that the amount is non-negative and every denomination is positive. Time: `O(A * C)`; space: `O(A)`, where `A` is the amount and `C` is the number of denominations.

### 3. House Robber
Maintain the best total for the prefix before the previous house and the best total through the previous house. For each value `x`, compute `current = max(previous, before_previous + x)`, then shift the two variables. Empty input returns `0`. Time: `O(n)`; auxiliary space: `O(1)`.

### 4. Activity Selection
Sort intervals by increasing finish time. Accept an interval when `start >= last_end`, then update `last_end`. This is optimal by the exchange-argument intuition: replacing the first chosen activity with the earliest-finishing activity cannot leave less time for the remaining activities. Time: `O(n log n)` with sorting.

## Part B — Concepts

1. **DP state:** a precise sentence defining what `dp[i]` represents, including the prefix/index/amount it covers.
2. **Greedy counterexample:** denominations `[1, 3, 4]`, amount `6`. Largest-first chooses `4 + 1 + 1` (3 coins), while `3 + 3` uses 2.
3. **Choose/explore/undo:** make one legal choice, recursively explore its consequences, then restore mutable state so sibling branches start from the correct state.
4. **Memoization vs tabulation:** memoization is top-down recursion with cached states; tabulation fills states bottom-up in dependency order.

## Common partial-credit deductions

- Missing `path[:]` or `pop()` in subsets.
- No impossible-target handling in coin change.
- Robbing adjacent houses or failing on an empty list.
- Sorting activities by start time rather than finish time.
- Giving a greedy claim without a valid counterexample or proof intuition.
- Naming a DP state without defining exactly what it means.
