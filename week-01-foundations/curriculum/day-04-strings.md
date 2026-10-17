# Day 4 — Strings

| | |
| --- | --- |
| **Week** | 1 — Foundations |
| **Theme** | Strings |
| **Estimated time** | 4 hours (45 + 45 + 90 + 30) |
| **Prerequisites** | Day 3 arrays; Python strings and slicing |
| **Deliverable** | `exercises/starter-code/valid_palindrome.py` and `valid_anagram.py` attempted |

## 1. Day objectives

By the end of today you can:

1. Explain why Python strings are immutable and what that costs.
2. State the complexity of indexing, slicing, concatenation and join.
3. Build strings efficiently with a list and `"".join`.
4. Traverse and compare strings with indices and two pointers.
5. Solve Valid Palindrome and Valid Anagram with stated complexity.
6. Handle case, spaces and non-alphanumeric characters correctly.

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Concepts (45 min) | Read `lessons/strings/strings-and-immutability.md` sections 1–7. |
| Guided implementation (45 min) | Run `examples/strings/string_operations.py` and `examples/strings/palindrome_check.py`; modify inputs. |
| Problem solving (90 min) | Solve `problems/easy/valid-palindrome.md` and `problems/easy/valid-anagram.md`. |
| Active recall (30 min) | String-cost flashcards; explain one solution aloud. |

## 3. Concepts to learn

- Immutability: every "change" builds a new string.
- Indexing O(1); slicing O(k); concatenation O(len(s)+len(t)).
- The `+=` in a loop trap and the `join` fix.
- Character iteration and `enumerate`.
- Two-pointer palindrome check.
- Frequency counting for anagrams.
- Case and whitespace handling.

## 4. Guided implementation

1. Run `examples/strings/string_operations.py`. Predict costs before running.
2. Run `examples/strings/palindrome_check.py`. Re-type the two-pointer version from memory.
3. Break the naive version on a mixed-case input and fix it.
4. Compare `build_bad` and `build_good` timings on a long input.

## 5. Problems for today

1. `problems/easy/valid-palindrome.md` — target time 25 minutes.
2. `problems/easy/valid-anagram.md` — target time 20 minutes.

## 6. Practice exercises (starter code)

- `exercises/starter-code/valid_palindrome.py`
- `exercises/starter-code/valid_anagram.py`
- `exercises/starter-code/count_vowels.py`

## 7. Active recall checklist

- [ ] Why is `s = s + c` in a loop quadratic?
- [ ] State the complexity of slicing, lower(), split(), join().
- [ ] Explain the two-pointer palindrome invariant.
- [ ] State when frequency counting beats sorting for anagrams.

## 8. Common mistakes today

- Forgetting strings are immutable and "modifying" in place.
- Using `+` to build a string in a loop.
- Comparing characters without normalising case.
- Off-by-one in two-pointer loops.

## 9. Exit criteria for Day 4

- [ ] Both problems solved unaided at least once.
- [ ] String-cost flashcards answered in under 2 seconds.
- [ ] Tests include empty, single, mixed case, spaces.
- [ ] Complexity stated for every solution.
