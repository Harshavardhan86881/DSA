# Day 3 — Binary Search

| | |
| --- | --- |
| **Week** | 2 — Two pointers, sliding window, binary search, sorting patterns |
| **Theme** | Binary search |
| **Estimated time** | 4 hours (45 + 35 + 40 + 75 + 20 + 25) |
| **Prerequisites** | Week 1; Week 2 Days 1–2 |
| **Deliverable** | `exercises/starter-code/binary_search.py` and `first_last_occurrence.py` attempted |

## 1. Day objectives

By the end of today you can:

1. Explain why binary search requires an ordered search space.
2. Implement standard binary search with correct bounds and termination.
3. Implement first/last occurrence, lower/upper bound, and insertion position.
4. Prove the loop invariant and correctness.
5. State O(log n) time and O(1) space.
6. Debug an off-by-one error.

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Concept learning (45 min) | Read `lessons/binary-search/binary-search.md` sections 1–6. |
| Worked examples (35 min) | Trace the five worked examples in the lesson. |
| Guided implementation (40 min) | Run `examples/binary-search/standard_binary_search.py` and `bounds.py`; modify inputs. |
| Independent problem solving (75 min) | Solve `binary-search`, `search-insert-position`, `first-and-last-position`. |
| Testing and debugging (20 min) | Test empty, single, duplicates, not found. |
| Active recall and explanation (25 min) | Answer review questions; explain one solution aloud. |

## 3. Concepts to learn

- Linear vs binary search.
- Inclusive vs half-open intervals.
- Midpoint formula and overflow safety.
- Loop invariants and termination.
- Variations: first/last occurrence, lower/upper bound, insertion position.
- Counting occurrences via boundaries.
- Recursive vs iterative complexity.

## 4. Guided implementation

1. Run `examples/binary-search/standard_binary_search.py`. Predict each step.
2. Run `examples/binary-search/bounds.py`. Compare lower/upper bounds.
3. Introduce an off-by-one bug and debug it.
4. Re-type the standard search from memory.

## 5. Problems for today

1. `problems/easy/binary-search.md` — 20 min.
2. `problems/easy/search-insert-position.md` — 20 min.
3. `problems/intermediate/find-first-and-last-position.md` — 30 min.

## 6. Practice exercises (starter code)

- `exercises/starter-code/binary_search.py`
- `exercises/starter-code/search_insert_position.py`
- `exercises/starter-code/first_last_occurrence.py`

## 7. Active recall checklist

- [ ] State the loop invariant for standard binary search.
- [ ] Write the inclusive-interval loop from memory.
- [ ] Explain lower vs upper bound.
- [ ] State complexity and justify.
- [ ] Debug an off-by-one error.

## 8. Common mistakes today

- Using `left <= right` vs `left < right` inconsistently.
- Midpoint overflow (not in Python, but conceptually).
- Infinite loops from wrong boundary update.
- Returning the wrong index for duplicates.
- Off-by-one in insertion position.

## 9. Exit criteria for Day 3

- [ ] All three problems solved unaided at least once.
- [ ] Invariants explained aloud.
- [ ] Tests include empty, single, duplicates, not found.
- [ ] Complexity stated for every solution.
