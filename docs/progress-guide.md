# Progress guide

How progress is measured in this course, what to write in the trackers, and how the readiness gates
work. This keeps the course honest: "I watched a video" is not progress; "I solved it unaided and can
explain it" is.

## 1. The three levels of tracking

| Level | File | What it records | Update frequency |
| --- | --- | --- | --- |
| Course level | [../progress-tracking/overall-progress.md](../progress-tracking/overall-progress.md) | Week status, gate results, current focus, next actions | End of every week (and Sunday planning block) |
| Problem level | [../progress-tracking/problem-tracker.csv](../progress-tracking/problem-tracker.csv) | One row per solved problem: topic, difficulty, tries, time, hints used, re-solve date | After every problem |
| Week level | each week's `progress/` folder | Daily study log, completion checklist, problem log for that week | Daily |

Everything else (mistake notebook, flashcards) supports these three.

## 2. Logging a problem properly

Every attempt gets one row, even unsuccessful ones. Column meanings:

| Column | Meaning | Why it matters |
| --- | --- | --- |
| `date` | Day you solved it (YYYY-MM-DD) | Shows study consistency |
| `week` | Course week (1–7) | Groups progress by topic area |
| `topic` | Short topic tag, e.g. `hashing`, `prefix-sums` | Reveals weak topics |
| `problem` | Problem name as used in the repository | Traceability |
| `source` | `week-01-foundations/problems/easy` or an external site name | Traceability |
| `difficulty` | `easy` / `intermediate` / `hard` | Difficulty mix across time |
| `solved_unaided` | `yes` / `no` | The key quality signal |
| `attempts` | Number of submissions before correctness | Detects guessing |
| `time_minutes` | Total time from reading to passing | Interview-speed tracking |
| `hints_used` | `none` / `hint1` / `hint2` / `solution` | Detects over-reliance on solutions |
| `re_solve_date` | Date of the spaced re-solve (R1/R3) | Drives the revision schedule |
| `notes` | One line about the bug or insight | Feeds the mistake notebook |

Rules:

- If `solved_unaided = no`, that problem returns to the practice queue within 3 days.
- If `time_minutes` is more than double the target time for that difficulty, repeat the problem
  once more after 3 days to build speed.

## 3. Readiness gates

A week is not "done" because the files were read. The gate questions are listed in
[course-overview.md](course-overview.md) section 5 and expanded verbally in
[learning-method.md](learning-method.md) section 9. The pattern for every week:

1. Attempt every exercise before reading its solution.
2. Solve every problem in that week's own `problems/` folders unaided at least once.
3. Re-solve the weakest problems once more from scratch.
4. Pass the week's cumulative assessment at the level defined by that week's rubric.
5. Explain three solutions aloud in English.

Only then move on. Moving on early is the main reason learners plateau at the same difficulty.

## 4. Grading your own work

Self-grading is part of the routine. Assessments are scored on four dimensions, weighted equally:

| Dimension | What is checked |
| --- | --- |
| Correctness | Passes sample tests and the edge-case matrix (empty, single, duplicates, negatives) |
| Complexity | A correct time and space statement, matching the implemented code |
| Code quality | Clear names, no dead code, docstring on reusable functions, simple control flow |
| Explanation | Spoken three-part answer: idea, correctness and complexity, small walkthrough |

Bands used by every week's rubric:

- **Pass with confidence:** all four dimensions solid; at most one small slip.
- **Pass:** correctness solid; complexity or explanation needs polish.
- **Not yet:** correctness or complexity is wrong, or the explanation cannot be produced without
  notes. Re-study the topic and retake the assessment after the next revision round.

The full per-week rubric lives with that week's assessment material (for Week 1:
`week-01-foundations/assessments/`), once it is generated.

## 5. Weekly review ritual (30–60 minutes, Sunday)

1. Fill the week's tracking rows and mark the week's status in overall-progress.md.
2. Answer: which topic had the most `solved_unaided = no` rows? That topic gets two extra
   problems next week.
3. Read every new mistake-notebook entry and write the one-line lesson learned for each.
4. Check the spaced-repetition calendar: which topics are due for R3/R4 review next week?
5. Write the next week's focus: 1 topic to strengthen, 1 habit to improve (for example: "state the
   plan before coding", "always test the empty case first").

## 6. Falling behind: the recovery plan

Life happens; the plan below prevents a missed week from becoming a lost course.

| Situation | Action |
| --- | --- |
| Missed 1–2 days | Keep the week's order, shrink the problem block; do not skip Sunday revision |
| Missed 3+ days | Freeze new topics; spend the next learning day only on the week's flashcards and mistake notebook |
| A week's gate fails twice | Repeat the week with the same material, solving different problems from the same topics |
| Two weeks feel too hard | Go back one week and re-solve its hardest 3 problems, then continue |
| Consistently short on time | Cut to 2.5 hours a day: 30 min concepts, 60 min implementation, 60 min problems; keep the recall block |

Slower is not failure. Skipping revision is.

## 7. Habit and motivation notes

- Track a streak of **days with real practice** (code written, problems solved), not days with
  files opened.
- Publicly visible progress helps: the CSV and checklist in this repository are meant to be
  committed, so the commit history itself becomes evidence.
- Prefer 4 focused hours over 8 distracted ones. The blocks in
  [learning-method.md](learning-method.md) include the breaks for this reason.
- When motivation drops, do a 25-minute timer on the easiest exercise in the current topic; a
  finished small task restores momentum better than a plan.

## 8. Related documents

- [learning-method.md](learning-method.md) — the daily and Sunday routines these trackers support.
- [course-overview.md](course-overview.md) — weekly deliverables used by the gates.
- [../progress-tracking/overall-progress.md](../progress-tracking/overall-progress.md) — course-level tracker.
- [../progress-tracking/problem-tracker.csv](../progress-tracking/problem-tracker.csv) — problem log.
- [../templates/mistake-notebook-template.md](../templates/mistake-notebook-template.md) — where bugs are recorded.
