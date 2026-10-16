# Day 3 — Arrays (Python Lists)

| | |
| --- | --- |
| **Week** | 1 — Foundations |
| **Theme** | Arrays |
| **Estimated time** | 4 hours (45 + 45 + 90 + 30) |
| **Prerequisites** | Day 1 problem-solving routine; Day 2 complexity basics; Python lists |
| **Deliverable** | `exercises/starter-code/two_sum.py` and `best_time_to_buy_sell_stock.py` attempted |

## 1. Day objectives

By the end of today you can:

1. Explain how a Python list is stored and why indexing is O(1).
2. State the complexity of append, pop, insert, slicing and membership.
3. Choose in-place mutation versus building a new list, with a stated trade-off.
4. Traverse an array with indices and with direct iteration.
5. Solve Two Sum and Best Time to Buy and Sell Stock with a stated complexity.
6. Write the edge-case matrix for an array problem.

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Concepts (45 min) | Read `lessons/arrays/arrays-and-lists.md` sections 1–7. |
| Guided implementation (45 min) | Run `examples/arrays/array_operations.py` and `examples/arrays/traversal_patterns.py`; modify inputs. |
| Problem solving (90 min) | Solve `problems/easy/two-sum.md` and `problems/intermediate/best-time-to-buy-and-sell-stock.md`. |
| Active recall (30 min) | Operation-cost flashcards; explain one solution aloud. |

## 3. Concepts to learn

- Dynamic array layout: contiguous storage, capacity, resize.
- Indexing O(1); append amortised O(1); pop last O(1).
- insert/pop at arbitrary index O(n); `x in list` O(n).
- Slicing creates a copy: O(k) time and space.
- In-place versus new list: space trade-offs.
- Traversal: index-based, value-based, enumerate.
- Prefix idea for range sums (preview of Day 6).

## 4. Guided implementation

1. Run `examples/arrays/array_operations.py`. Predict each printed complexity before running.
2. Change the list size and observe which operations get slow.
3. Run `examples/arrays/traversal_patterns.py`. Re-type the enumerate version from memory.
4. Mutate a list in place, then compare with a sliced copy.

## 5. Problems for today

1. `problems/easy/two-sum.md` — target time 25 minutes.
2. `problems/intermediate/best-time-to-buy-and-sell-stock.md` — target time 25 minutes.

## 6. Practice exercises (starter code)

- `exercises/starter-code/two_sum.py`
- `exercises/starter-code/best_time_to_buy_sell_stock.py`
- `exercises/starter-code/array_stats.py`

## 7. Active recall checklist

- [ ] State the complexity of append, insert(0, x), pop(), pop(i), slicing.
- [ ] Explain why a list resize is amortised O(1).
- [ ] Name three traversal patterns.
- [ ] Give the constraint-to-complexity link for n = 10^5.

## 8. Common mistakes today

- Using `insert(0, x)` in a loop (O(n²)).
- Slicing inside a loop and claiming O(n).
- Confusing in-place mutation with returning a new list.
- Forgetting that `min`/`max`/`sum` are O(n).

## 9. Exit criteria for Day 3

- [ ] Both problems solved unaided at least once.
- [ ] Operation-cost flashcards answered in under 2 seconds.
- [ ] Tests written for empty, single, duplicates, negatives.
- [ ] Complexity stated for every solution.
