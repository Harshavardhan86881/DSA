# Day 1 — Problem-Solving Foundations

| | |
| --- | --- |
| **Week** | 1 — Foundations |
| **Theme** | Problem solving |
| **Estimated time** | 4 hours (45 + 45 + 90 + 30) |
| **Prerequisites** | Python functions, loops, lists; reading a traceback |
| **Deliverable** | `exercises/starter-code/reverse_array.py`, `second_largest.py` attempted and tested |

## 1. Day objectives

By the end of today you can:

1. Turn any short problem statement into a written plan before writing code.
2. Restate a problem in one or two sentences in your own words.
3. Hand-trace a small example and mark the step that repeats (the loop).
4. Write a brute-force solution first, then explain why an optimisation works.
5. Test with the full edge-case matrix: empty, single, duplicates, negatives, maximum size.
6. State time and space complexity for a solution you wrote.

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Concepts (45 min) | Read `lessons/problem-solving/problem-solving-foundations.md` sections 1–7. Annotate in your own words. |
| Guided implementation (45 min) | Re-type `examples/problem-solving/reverse_array.py` and `second_largest.py` from memory, then change the input and re-run. |
| Problem solving (90 min) | Solve `problems/easy/reverse-an-array.md` and `problems/easy/find-the-second-largest-distinct-element.md` with a 25-minute timer each. |
| Active recall (30 min) | Flashcards for the seven steps; one spoken explanation of the second-largest solution. |

## 3. Concepts to learn

- The seven-step routine: understand, restate, hand-trace, plan, code small, test, analyse.
- Extracting input, output, constraints, guarantees and ambiguities from a statement.
- The constraint-to-complexity link (n ≤ 10 → O(n!), n ≤ 10⁶ → O(n) or O(n log n)).
- Brute force first, then optimise by removing repeated work.
- The edge-case matrix for arrays.
- The three-part spoken answer: idea, correctness + complexity, walkthrough.

## 4. Guided implementation

1. Open `examples/problem-solving/reverse_array.py`. Read it once, then close the file.
2. Re-type both functions from memory. Run the file. Fix any mistake.
3. Modify the input to `[-3, 0, 2, 2]` and predict the output before running.
4. Open `examples/problem-solving/second_largest.py`. Repeat the process.
5. Break an edge case on purpose (empty list) and watch the error. Fix it.

## 5. Problems for today

1. `problems/easy/reverse-an-array.md` — target time 20 minutes.
2. `problems/easy/find-the-second-largest-distinct-element.md` — target time 25 minutes.

For each: attempt for 25 minutes before opening hints, 15 more before the solution. Write tests.

## 6. Practice exercises (starter code)

- `exercises/starter-code/reverse_array.py`
- `exercises/starter-code/second_largest.py`
- `exercises/starter-code/find_min_max.py`

Attempt these before opening `exercises/solutions/`.

## 7. Active recall checklist

- [ ] List the seven steps in order without looking.
- [ ] State the constraint-to-complexity link for n = 10⁶.
- [ ] Explain why brute force comes before the optimised version.
- [ ] Name the six edge-case categories for arrays.
- [ ] Give the three-part spoken answer for the second-largest problem.

## 8. Common mistakes today

- Coding before hand-tracing a small example.
- Forgetting the empty-input and single-element cases.
- Counting the input array as extra space.
- Claiming O(n) while calling `x in list` inside a loop.

## 9. Exit criteria for Day 1

- [ ] Both problems solved unaided at least once.
- [ ] Tests written for empty, single, duplicates, negatives.
- [ ] Complexity stated for every solution.
- [ ] One spoken explanation recorded (or spoken aloud).
