# Day 4 — Binary Search on Answer

| | |
| --- | --- |
| **Week** | 2 — Two pointers, sliding window, binary search, sorting patterns |
| **Theme** | Binary search on answer |
| **Estimated time** | 4 hours (45 + 35 + 40 + 75 + 20 + 25) |
| **Prerequisites** | Day 3 binary search |
| **Deliverable** | `exercises/starter-code/koko_eating_bananas.py` and `capacity_to_ship.py` attempted |

## 1. Day objectives

By the end of today you can:

1. Explain the difference between searching an array and searching an answer space.
2. Define a feasibility (decision) function.
3. Identify a monotonic predicate and its direction.
4. Derive lower and upper bounds mathematically.
5. Solve Koko Eating Bananas and Capacity To Ship Packages.
6. State complexity as O(log(range) * cost_of_feasible).

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Concept learning (45 min) | Read `lessons/binary-search-on-answer/binary-search-on-answer.md` sections 1–6. |
| Worked examples (35 min) | Trace the two worked examples in the lesson. |
| Guided implementation (40 min) | Run `examples/binary-search-on-answer/koko.py` and `ship.py`; modify inputs. |
| Independent problem solving (75 min) | Solve `koko-eating-bananas`, `capacity-to-ship-packages-within-d-days`, `split-array-largest-sum`. |
| Testing and debugging (20 min) | Test boundary speeds/capacities and impossible cases. |
| Active recall and explanation (25 min) | Answer review questions; explain one solution aloud. |

## 3. Concepts to learn

- Candidate answer and answer space.
- Feasibility function.
- Monotonic predicates: FFFTTT and TTTFFF.
- Deriving bounds.
- Template selection.
- Complexity of feasibility checks.

## 4. Guided implementation

1. Run `examples/binary-search-on-answer/koko.py`. Predict the answer.
2. Run `examples/binary-search-on-answer/ship.py`. Trace the feasibility check.
3. Write a non-monotonic predicate and observe failure.
4. Re-type the template from memory.

## 5. Problems for today

1. `problems/intermediate/koko-eating-bananas.md` — 25 min.
2. `problems/intermediate/capacity-to-ship-packages-within-d-days.md` — 25 min.
3. `problems/intermediate/split-array-largest-sum.md` — 25 min.

## 6. Practice exercises (starter code)

- `exercises/starter-code/koko_eating_bananas.py`
- `exercises/starter-code/capacity_to_ship.py`
- `exercises/starter-code/split_array_largest_sum.py`

## 7. Active recall checklist

- [ ] Define a feasibility function.
- [ ] Identify monotonic direction.
- [ ] Derive bounds for Koko and Ship.
- [ ] Write the template from memory.
- [ ] State complexity.

## 8. Common mistakes today

- Non-monotonic feasibility.
- Wrong bounds (too small/large).
- Off-by-one in template.
- Forgetting to handle impossible input.
- Treating feasibility as O(1) when it is O(n).

## 9. Exit criteria for Day 4

- [ ] All three problems solved unaided at least once.
- [ ] Monotonicity explained aloud.
- [ ] Tests include boundary and impossible cases.
- [ ] Complexity stated for every solution.
