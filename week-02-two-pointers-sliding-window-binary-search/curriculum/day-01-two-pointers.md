# Day 1 — Two Pointers

| | |
| --- | --- |
| **Week** | 2 — Two pointers, sliding window, binary search, sorting patterns |
| **Theme** | Two pointers |
| **Estimated time** | 4 hours (45 + 35 + 40 + 75 + 20 + 25) |
| **Prerequisites** | Week 1 complete: arrays, complexity, hashing |
| **Deliverable** | `exercises/starter-code/two_sum_sorted.py` and `remove_duplicates.py` attempted |

## 1. Day objectives

By the end of today you can:

1. Explain why two pointers on a sorted array never need to move backwards.
2. Solve a pair-sum problem in O(n) instead of O(n²).
3. Implement same-direction (read/write) two pointers for in-place filtering.
4. Solve Container With Most Water with a stated invariant.
5. State time and space complexity for each variant.
6. Choose two pointers versus hashing and justify the choice.

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Concept learning (45 min) | Read `lessons/two-pointers/two-pointers.md` sections 1–6. |
| Worked examples (35 min) | Trace the pointer movements in the lesson's dry-run tables. |
| Guided implementation (40 min) | Run `examples/two-pointers/pair_sum_sorted.py` and `remove_duplicates.py`; modify inputs. |
| Independent problem solving (75 min) | Solve `two-sum-ii`, `remove-duplicates-from-sorted-array`, `container-with-most-water`. |
| Testing and debugging (20 min) | Test empty, single, all equal, already sorted/reverse. |
| Active recall and explanation (25 min) | Answer review questions; explain one solution aloud. |

## 3. Concepts to learn

- Opposite-direction two pointers on a sorted array.
- The monotonicity argument: why a pointer never moves back.
- Same-direction read/write pointers for in-place compaction.
- Container With Most Water: greedy pointer movement.
- Invariants and why they hold.
- Complexity and trade-offs versus hashing.

## 4. Guided implementation

1. Run `examples/two-pointers/pair_sum_sorted.py`. Predict pointer moves before running.
2. Run `examples/two-pointers/remove_duplicates.py`. Re-type from memory.
3. Break the bounds on an empty input and fix.
4. Compare the two-pointer pair sum with the hash-map version from Week 1.

## 5. Problems for today

1. `problems/easy/two-sum-ii-input-array-is-sorted.md` — 20 min.
2. `problems/easy/remove-duplicates-from-sorted-array.md` — 20 min.
3. `problems/intermediate/container-with-most-water.md` — 30 min.

## 6. Practice exercises (starter code)

- `exercises/starter-code/two_sum_sorted.py`
- `exercises/starter-code/remove_duplicates.py`
- `exercises/starter-code/container_with_most_water.py`

## 7. Active recall checklist

- [ ] State the monotonicity argument in one sentence.
- [ ] Write the opposite-direction loop from memory.
- [ ] Write the read/write compaction loop from memory.
- [ ] Explain why Container With Most Water moves the shorter side.
- [ ] State complexity for all three variants.

## 8. Common mistakes today

- Forgetting the array must be sorted for opposite-direction pointers.
- Using `<=` instead of `<` in the loop and double-counting.
- Moving the wrong pointer in Container With Most Water.
- Off-by-one in the read/write index.

## 9. Exit criteria for Day 1

- [ ] All three problems solved unaided at least once.
- [ ] Pointer invariants explained aloud.
- [ ] Tests include empty, single, all equal, sorted/reverse.
- [ ] Complexity stated for every solution.
