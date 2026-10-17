# Week 6 Interview Questions

## Backtracking

**Q:** Why does backtracking need an undo step?
**A:** State is mutated in place; undo restores it for sibling choices.

**Q:** How many subsets does an n-element set have?
**A:** 2^n.

**Q:** How many permutations?
**A:** n!.

**Q:** How do you avoid duplicate permutations with duplicates?
**A:** Sort and skip equal unused values at the same level.

## Greedy

**Q:** How do you prove a greedy algorithm?
**A:** Show greedy-choice property and optimal substructure, often with an exchange argument.

**Q:** Why sort by finish time in activity selection?
**A:** The earliest-finishing activity leaves the most room.

**Q:** Give a greedy counterexample.
**A:** Coins [1,3,4], amount 6: greedy gives 3 coins, optimal gives 2.

## Dynamic programming

**Q:** How do you define a DP state?
**A:** State what `dp[i]` means in words before coding.

**Q:** Memoization vs tabulation?
**A:** Top-down with recursion vs bottom-up with a table.

**Q:** How do you derive complexity?
**A:** Number of states times work per state.

**Q:** Why is dp[0] = 0 for coin change?
**A:** Zero amount needs zero coins.

## Spoken answer exercise

Explain in 60 seconds: "Backtracking chooses, explores, and undoes. Greedy picks a local optimum and needs proof. DP stores subproblem answers and derives complexity from states and transitions."
