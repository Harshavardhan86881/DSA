# Day 5 — Hashing (Dictionaries and Sets)

| | |
| --- | --- |
| **Week** | 1 — Foundations |
| **Theme** | Hashing |
| **Estimated time** | 4 hours (45 + 45 + 90 + 30) |
| **Prerequisites** | Days 1–4; Python dicts and sets |
| **Deliverable** | `exercises/starter-code/contains_duplicate.py` and `majority_element.py` attempted |

## 1. Day objectives

By the end of today you can:

1. Explain how a hash table gives average O(1) lookup.
2. Choose between dict and set for a given task.
3. Count frequencies in one pass with a dict.
4. Detect duplicates in one pass with a set.
5. Solve Contains Duplicate and Majority Element with stated complexity.
6. State the difference between average and worst-case hashing.

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Concepts (45 min) | Read `lessons/hashing/hashing-dictionaries-sets.md` sections 1–7. |
| Guided implementation (45 min) | Run `examples/hashing/frequency_counter.py` and `examples/hashing/duplicate_detector.py`; modify inputs. |
| Problem solving (90 min) | Solve `problems/easy/contains-duplicate.md` and `problems/intermediate/majority-element.md`. |
| Active recall (30 min) | Hashing flashcards; explain one solution aloud. |

## 3. Concepts to learn

- Hash table idea: key → hash → bucket → value.
- dict: key→value; set: keys only.
- Average O(1) lookup/insert/delete; worst case O(n) on collisions.
- Frequency counting pattern.
- Duplicate detection pattern.
- Membership testing to remove nested loops.
- Counter and defaultdict from collections.

## 4. Guided implementation

1. Run `examples/hashing/frequency_counter.py`. Predict counts before running.
2. Run `examples/hashing/duplicate_detector.py`. Break it on an empty input and fix.
3. Re-type the majority-element brute force and optimised versions from memory.
4. Compare `x in list` versus `x in set` on a large input.

## 5. Problems for today

1. `problems/easy/contains-duplicate.md` — target time 15 minutes.
2. `problems/intermediate/majority-element.md` — target time 25 minutes.

## 6. Practice exercises (starter code)

- `exercises/starter-code/contains_duplicate.py`
- `exercises/starter-code/majority_element.py`
- `exercises/starter-code/character_frequency.py`

## 7. Active recall checklist

- [ ] Explain hashing in one sentence.
- [ ] State average and worst-case complexity of dict lookup.
- [ ] Write the frequency-counting pattern from memory.
- [ ] Explain why hashing turns O(n²) into O(n).

## 8. Common mistakes today

- Assuming dict lookups are worst-case O(1).
- Using a list for membership inside a loop.
- Forgetting that keys must be hashable.
- Counting the input as extra space.

## 9. Exit criteria for Day 5

- [ ] Both problems solved unaided at least once.
- [ ] Hashing flashcards answered in under 2 seconds.
- [ ] Tests include empty, single, all equal, negatives.
- [ ] Complexity stated for every solution.
