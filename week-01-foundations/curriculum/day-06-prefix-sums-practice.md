# Day 6 — Prefix Sums and Mixed Practice

| | |
| --- | --- |
| **Week** | 1 — Foundations |
| **Theme** | Prefix sums |
| **Estimated time** | 4 hours (45 + 45 + 90 + 30) |
| **Prerequisites** | Days 1–5; arrays and hashing |
| **Deliverable** | `exercises/starter-code/prefix_sum.py` and `range_sum_query.py` attempted |

## 1. Day objectives

By the end of today you can:

1. Build a prefix-sum array in O(n).
2. Answer a range sum in O(1) per query.
3. Compare brute force (O(n) per query) with prefix sums (O(1) per query).
4. Solve Prefix Sum Construction, Range Sum Query – Immutable and Maximum Subarray.
5. State the time/space trade-off of precomputing.

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Concepts (45 min) | Read `lessons/prefix-sums/prefix-sums-and-range-queries.md` sections 1–7. |
| Guided implementation (45 min) | Run `examples/prefix-sums/prefix_sum_demo.py` and `examples/prefix-sums/range_sum.py`; modify inputs. |
| Problem solving (90 min) | Solve `problems/easy/prefix-sum-construction.md`, `problems/intermediate/range-sum-query-immutable.md`, `problems/intermediate/maximum-subarray.md`. |
| Active recall (30 min) | Prefix-sum flashcards; explain one solution aloud. |

## 3. Concepts to learn

- Prefix sum definition: `P[i] = nums[0] + ... + nums[i-1]` (or inclusive variant).
- Building in one pass.
- Range sum formula: `sum(i..j) = P[j+1] - P[i]`.
- Precompute once, answer many queries.
- Maximum subarray: running sum, reset when negative (Kadane-style).
- Trade-off: O(n) precompute + O(1) query versus O(n) per query.

## 4. Guided implementation

1. Run `examples/prefix-sums/prefix_sum_demo.py`. Predict prefix values before running.
2. Run `examples/prefix-sums/range_sum.py`. Test empty ranges and single elements.
3. Re-type the Maximum Subarray brute force and optimised versions from memory.
4. Compare timings on a large array with many queries.

## 5. Problems for today

1. `problems/easy/prefix-sum-construction.md` — target time 15 minutes.
2. `problems/intermediate/range-sum-query-immutable.md` — target time 20 minutes.
3. `problems/intermediate/maximum-subarray.md` — target time 25 minutes.

## 6. Practice exercises (starter code)

- `exercises/starter-code/prefix_sum.py`
- `exercises/starter-code/range_sum_query.py`
- `exercises/starter-code/maximum_subarray.py`

## 7. Active recall checklist

- [ ] Write the prefix-sum build loop from memory.
- [ ] State the range-sum formula.
- [ ] Explain the Maximum Subarray reset rule.
- [ ] State the precompute/query trade-off.

## 8. Common mistakes today

- Off-by-one in the prefix-sum indices.
- Forgetting that prefix sums need O(n) extra space.
- Resetting the running sum at the wrong time in Maximum Subarray.
- Counting the input as extra space.

## 9. Exit criteria for Day 6

- [ ] All three problems solved unaided at least once.
- [ ] Prefix-sum flashcards answered in under 2 seconds.
- [ ] Tests include empty, single, negatives, all negative.
- [ ] Complexity stated for every solution.
