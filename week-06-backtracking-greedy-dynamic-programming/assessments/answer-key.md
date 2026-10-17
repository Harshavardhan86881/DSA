# Week 6 Answer Key

Subsets: backtracking; record path[:]; undo with pop; 2^n results.

Coin change: DP; dp[0]=0; dp[a]=min(dp[a-coin]+1); return -1 if impossible.

House robber: dp[i]=max(dp[i-1], dp[i-2]+nums[i]); O(n) time, O(1) space.

Activity selection: sort by finish time; accept if start >= last_end.

DP state: a sentence defining dp[i].

Greedy counterexample: coins [1,3,4], amount 6.

Backtracking un-choose: restore mutable state for sibling choices.

Memoization: top-down caching. Tabulation: bottom-up table filling.
