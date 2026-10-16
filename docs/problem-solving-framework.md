# Problem-solving framework

A fixed, seven-step routine used for **every** problem in this course. It exists because the main
difficulty being solved here is not "knowing algorithms" but "being able to start, plan and finish
logic independently".

Use the same seven steps every single time until they become automatic.

## The seven steps at a glance

| Step | Name | Time in practice | Time in a 40-minute interview |
| --- | --- | --- | --- |
| 1 | Understand the question | 5 min | 3 min |
| 2 | Restate it in your own words | 2 min | 2 min |
| 3 | Work a small example by hand | 5 min | 5 min |
| 4 | Plan before coding (plain English / pseudocode) | 8 min | 5 min |
| 5 | Code in small steps and run often | 20–40 min | 15 min |
| 6 | Test with the full edge-case matrix | 10 min | 8 min |
| 7 | Analyse complexity and explain out loud | 5 min | 2 min |

In interviews, steps 1–4 are spoken aloud. Interviewers score the reasoning, not only the final code.

## Step 1 — Understand the question

Extract five things before writing anything:

1. **Input:** what type is it, how big can it be, can it be empty, can it contain duplicates?
2. **Output:** exact type and what "no answer" looks like (`-1`, `[]`, `None`, raising an error?).
3. **Constraints:** the size limit is the biggest hint about the required complexity.
4. **Guarantees:** is the input sorted? Can numbers be negative? Is there always exactly one answer?
5. **Ambiguity:** write down every question you would ask an interviewer.

The constraint-to-complexity link is worth memorising early:

| Input size (n) | Complexity that is expected to pass |
| --- | --- |
| n ≤ 10 | O(n!), O(2ⁿ) |
| n ≤ 20 | O(2ⁿ) with pruning |
| n ≤ 500 | O(n³) |
| n ≤ 5,000 | O(n²) |
| n ≤ 10⁶ | O(n log n) or O(n) |

If your plan is slower than the table allows, the plan is wrong, not the input.

## Step 2 — Restate the problem in your own words

Write one or two sentences. Format:

> "Given a list of `n` integers, I must return ___ if ___ exists, otherwise ___."

If you cannot write this sentence, you do not understand the problem yet — go back to Step 1.
Restating also catches wrong assumptions early, which is much cheaper than catching them after
coding.

## Step 3 — Work a small example by hand

Take the smallest non-trivial input (usually 4–6 elements, never 20) and solve it slowly on paper:

- write the input in a row;
- write what you are looking for;
- mark which elements you compare, and in what order;
- note any step that **repeats across elements** — that repeated step is the loop.

Example of the note you are looking for: *"for every element I check whether `target - element`
was seen before"* — that sentence is already the algorithm.

## Step 4 — Plan before coding

Write the plan as comments in the file, then code underneath the comments. Requirements:

- **Brute force first.** State the simplest correct approach even if it is slow.
- **Then optimise.** Say what is being repeated and which data structure removes the repetition.
  Example: "the inner loop searches again for the complement, so store complements in a dict".
- **Name the data structures and the loop bounds** explicitly, including inclusive/exclusive ends.
- **Predict complexity** of the plan before writing it, so you notice a slow plan early.

A plan is acceptable when you can read it aloud and someone else could type it into code.

## Step 5 — Code in small steps and run often

- Write 5–10 lines, then run.
- Use meaningful names (`seen`, `best`, `prefix_sum`) instead of `x`, `y`, `temp2`.
- Handle the empty-input case at the top so the rest of the function can assume data exists.
- Keep a `main` block or a scratch call at the bottom so you can run the file instantly.
- If you feel stuck for more than 10 minutes, print the state and continue from Step 3, not from
  random edits.

## Step 6 — Test with the edge-case matrix

Run these categories for every array or string problem:

| Category | Example | What it catches |
| --- | --- | --- |
| Empty input | `[]`, `""` | Index errors, division by zero |
| Single element | `[7]` | Loop bounds, "no pair" logic |
| Two elements | `[1, 5]` | Off-by-one in adjacent comparisons |
| All equal | `[4, 4, 4]` | Duplicate-handling bugs |
| All distinct | `[1, 2, 3]` | Hash-collision assumptions |
| Negatives and zero | `[-3, 0, 2]` | Sums/prefix logic that assumed positives |
| Already sorted / reverse sorted | `[1,2,3]`, `[3,2,1]` | Comparison bugs hidden by random data |
| Maximum size | n = 10⁵–10⁶ | Performance and recursion limits |

Also test the **sample input from the statement** and compare against the expected output.

## Step 7 — Analyse complexity and explain out loud

- Count the loops and how each one scales with n; multiply nested loops that depend on n.
- State space: count extra containers created, not the input itself.
- Then answer this three-part question aloud in English:

  1. "The idea is ___."
  2. "It is correct because ___, and it runs in O(___), using O(___) extra space."
  3. "On this input, the variables look like this: ___."

## Worked demonstration (compact)

Problem: return `True` if any value appears twice in a list of integers.

1. **Understand:** input list of ints, n up to 10⁵, may be empty; output is a boolean.
2. **Restate:** "I must report whether any value is repeated."
3. **Hand example:** `[3, 1, 3]` → compare 3 with 1, then 3 with 3 → duplicate found.
4. **Plan:**
   - Brute force: for every i, compare with every j > i → O(n²). Correct but too slow for 10⁵.
   - Optimised: keep a set of values already seen; if the current value is in the set, return
     `True`; otherwise add it. O(n) time, O(n) space.
5. **Code** the optimised version with a `main` block and run it.
6. **Test:** `[]` → False; `[7]` → False; `[4,4]` → True; `[1,2,3]` → False; 10⁵ distinct values
   finishes instantly.
7. **Explain:** "I store the values I have already met in a set. Membership test in a set is O(1)
   on average, so one pass finds a repeat in O(n) time and O(n) extra space."

## Common process mistakes

- Starting to code before Step 3, then debugging the wrong algorithm for 40 minutes.
- Planning only the optimised solution and never stating the brute force, which hides the reason
  the optimisation works.
- Testing only the given example; the given example never contains the empty case.
- Skipping the complexity sentence, then being unable to answer "how does this scale?".
- Editing code randomly when stuck instead of returning to the hand-traced example.

## Related documents

- [learning-method.md](learning-method.md) — the daily routine that uses this framework.
- [complexity-cheatsheet.md](complexity-cheatsheet.md) — the reference used in Step 7.
- [../templates/coding-problem-template.md](../templates/coding-problem-template.md) — the file
  shape every problem in this course follows.
