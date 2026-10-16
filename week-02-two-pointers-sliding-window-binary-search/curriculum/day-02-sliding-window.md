# Day 2 — Sliding Window

| | |
| --- | --- |
| **Week** | 2 — Two pointers, sliding window, binary search, sorting patterns |
| **Theme** | Sliding window |
| **Estimated time** | 4 hours (45 + 35 + 40 + 75 + 20 + 25) |
| **Prerequisites** | Day 1 two pointers; arrays and hashing |
| **Deliverable** | `exercises/starter-code/max_sum_subarray_k.py` and `longest_substring_without_repeating.py` attempted |

## 1. Day objectives

By the end of today you can:

1. Recognise a fixed-size window and maintain a running aggregate in O(n).
2. Recognise a variable-size window and shrink while a condition is violated.
3. Solve Maximum Sum Subarray of Size K and Longest Substring Without Repeating Characters.
4. State the invariant of each window.
5. Handle edge cases: empty input, window larger than input, all equal.
6. Explain why sliding window is O(n) despite nested loops.

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Concept learning (45 min) | Read `lessons/sliding-window/sliding-window.md` sections 1–6. |
| Worked examples (35 min) | Trace the window state tables in the lesson. |
| Guided implementation (40 min) | Run `examples/sliding-window/fixed_window.py` and `variable_window.py`; modify inputs. |
| Independent problem solving (75 min) | Solve `maximum-sum-subarray-of-size-k`, `longest-substring-without-repeating-characters`, `minimum-size-subarray-sum`. |
| Testing and debugging (20 min) | Test empty, k larger than n, all equal, negatives. |
| Active recall and explanation (25 min) | Answer review questions; explain one solution aloud. |

## 3. Concepts to learn

- Fixed-size window: add entering, remove leaving, keep running aggregate.
- Variable-size window: grow right, shrink left while condition violated.
- Window invariant and why each element enters/leaves at most once.
- Hash map / set for window state.
- Complexity O(n) despite two pointers.

## 4. Guided implementation

1. Run `examples/sliding-window/fixed_window.py`. Predict the running sum.
2. Run `examples/sliding-window/variable_window.py`. Trace the set state.
3. Break the fixed window on k > n and fix.
4. Compare variable window with the brute-force O(n²) version.

## 5. Problems for today

1. `problems/easy/maximum-sum-subarray-of-size-k.md` — 20 min.
2. `problems/intermediate/longest-substring-without-repeating-characters.md` — 30 min.
3. `problems/intermediate/minimum-size-subarray-sum.md` — 25 min.

## 6. Practice exercises (starter code)

- `exercises/starter-code/max_sum_subarray_k.py`
- `exercises/starter-code/longest_substring_without_repeating.py`
- `exercises/starter-code/minimum_size_subarray_sum.py`

## 7. Active recall checklist

- [ ] State the fixed-window update rule.
- [ ] State the variable-window shrink condition.
- [ ] Explain why sliding window is O(n).
- [ ] Write both loops from memory.
- [ ] State complexity for all three problems.

## 8. Common mistakes today

- Recomputing the window sum from scratch each step (O(nk)).
- Forgetting to remove the leaving element.
- Off-by-one in window bounds.
- Shrinking the window even when the condition already holds.

## 9. Exit criteria for Day 2

- [ ] All three problems solved unaided at least once.
- [ ] Window invariants explained aloud.
- [ ] Tests include empty, k > n, all equal, negatives.
- [ ] Complexity stated for every solution.
