# Day 5 — Sorting as a Problem-Solving Pattern

| | |
| --- | --- |
| **Week** | 2 — Two pointers, sliding window, binary search, sorting patterns |
| **Theme** | Sorting as a pattern |
| **Estimated time** | 4 hours (45 + 35 + 40 + 75 + 20 + 25) |
| **Prerequisites** | Week 1; Week 2 Days 1–4 |
| **Deliverable** | `exercises/starter-code/sort_then_two_sum.py` and `group_anagrams.py` attempted |

## 1. Day objectives

By the end of today you can:

1. Explain why sorting can simplify a problem.
2. Use `sorted()` vs `.sort()` correctly.
3. Sort with `key`, `reverse`, tuples, and custom keys.
4. Detect duplicates after sorting.
5. Solve Two Sum II via sorting + two pointers.
6. State the O(n log n) + O(n) complexity.

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Concept learning (45 min) | Read `lessons/sorting-patterns/sorting-as-a-pattern.md`. |
| Worked examples (35 min) | Trace the four worked examples. |
| Guided implementation (40 min) | Run `examples/sorting-patterns/*.py`; modify inputs. |
| Independent problem solving (75 min) | Solve `sort-then-two-sum`, `group-anagrams`, `merge-intervals`. |
| Testing and debugging (20 min) | Test empty, single, duplicates, already sorted. |
| Active recall and explanation (25 min) | Answer review questions; explain one solution aloud. |

## 3. Concepts to learn

- Sorting as preprocessing.
- Stable sort and stability.
- Custom keys and tuples.
- Sorting enables two pointers, grouping, intervals.
- Complexity: O(n log n) sort + O(n) scan.
- Preserving original order with indices.

## 4. Guided implementation

1. Run `examples/sorting-patterns/sort_basics.py`.
2. Run `examples/sorting-patterns/sort_then_two_pointers.py`.
3. Break stability and observe.
4. Re-type the merge intervals solution from memory.

## 5. Problems for today

1. `problems/easy/sort-then-two-sum.md` — 20 min.
2. `problems/intermediate/group-anagrams.md` — 25 min.
3. `problems/intermediate/merge-intervals.md` — 30 min.

## 6. Practice exercises (starter code)

- `exercises/starter-code/sort_then_two_sum.py`
- `exercises/starter-code/group_anagrams.py`
- `exercises/starter-code/merge_intervals.py`

## 7. Active recall checklist

- [ ] Explain stable sort.
- [ ] State when sorting helps.
- [ ] Write a custom key sort.
- [ ] State complexity of sort + scan.
- [ ] Explain index preservation.

## 8. Common mistakes today

- Sorting when not needed (O(n log n) waste).
- Mutating input unexpectedly.
- Unstable sort assumptions.
- Forgetting O(n log n) dominates.

## 9. Exit criteria for Day 5

- [ ] All three problems solved unaided.
- [ ] Sorting pattern explained aloud.
- [ ] Tests include empty, single, duplicates.
- [ ] Complexity stated.
