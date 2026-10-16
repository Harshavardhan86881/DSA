# DSA Roadmap — a 7-week Python DSA course

A self-paced, interview-oriented Data Structures and Algorithms course in Python.
The course is organised week by week: each week has its own folder with study plans,
lessons, runnable examples, exercises, problems, revision material and assessments.

**Current status:** the full 7-week structure and the shared documentation are in place.
Week 1 lesson content has **not** been generated yet — it is the next task.
Weeks 2–7 are scoped and reserved but intentionally empty.

## Who this course is for

| Aspect | Assumption |
| --- | --- |
| Python level | Intermediate — comfortable with functions, lists, dicts and loops |
| DSA level | Beginner to intermediate |
| Goal | Become a software developer and pass coding interviews |
| Time per day | ~4 hours |
| Weekly rhythm | 6 learning days + Sunday revision |
| Budget | Free resources only |
| Known difficulties | Writing logic independently, retaining concepts, debugging, and explaining solutions in English |

Every file is therefore written in simple English, with step-by-step reasoning,
dry-run tables, and hints separated from solutions so the logic is attempted first.

## How to use this repository

1. Read [docs/course-overview.md](docs/course-overview.md) to see the whole 7-week scope.
2. Read [docs/learning-method.md](docs/learning-method.md) and set up your daily 4-hour block.
3. Open the week you are on (start with [week-01-foundations/README.md](week-01-foundations/README.md)).
4. Follow that week's `curriculum/` day plans. Each day has its own file.
5. Write code yourself in `exercises/starter-code/` before opening `exercises/solutions/`.
6. Log every solved problem in [progress-tracking/problem-tracker.csv](progress-tracking/problem-tracker.csv).
7. Use Sunday for revision and the cumulative assessment of that week.
8. Finish a week only when its readiness checklist passes.

Keep a mistake notebook from day 1 — the template is at
[templates/mistake-notebook-template.md](templates/mistake-notebook-template.md).

## The 7-week roadmap

| Week | Folder | Focus | Status |
| --- | --- | --- | --- |
| 1 | [week-01-foundations](week-01-foundations/README.md) | Problem solving, Big-O, arrays, strings, hashing, prefix sums | Structure ready, content pending |
| 2 | [week-02-two-pointers-sliding-window-binary-search](week-02-two-pointers-sliding-window-binary-search/README.md) | Two pointers, sliding window, binary search, sorting patterns | Scoped, lessons not generated |
| 3 | [week-03-linked-lists-stacks-queues](week-03-linked-lists-stacks-queues/README.md) | Linked lists, stacks, queues and their applications | Scoped, lessons not generated |
| 4 | [week-04-recursion-trees-heaps](week-04-recursion-trees-heaps/README.md) | Recursion, trees, binary search trees, heaps | Scoped, lessons not generated |
| 5 | [week-05-graphs](week-05-graphs/README.md) | Graph representation, BFS, DFS, basic graph problems | Scoped, lessons not generated |
| 6 | [week-06-backtracking-greedy-dynamic-programming](week-06-backtracking-greedy-dynamic-programming/README.md) | Backtracking, greedy, dynamic programming fundamentals | Scoped, lessons not generated |
| 7 | [week-07-revision-mock-interviews](week-07-revision-mock-interviews/README.md) | Revision, mixed practice, mock interviews, final assessment | Scoped, lessons not generated |

## What lives where

| Path | Purpose |
| --- | --- |
| [docs/](docs/course-overview.md) | Shared course documentation: scope, method, framework, complexity cheatsheet, resources, progress guide |
| [templates/](templates/lesson-template.md) | Reusable templates so every lesson and problem has the same shape |
| `week-0X-…/curriculum/` | Day-by-day study plans (4-hour blocks); Week 1 day files are pending |
| `week-0X-…/lessons/` | Written lessons per topic |
| `week-0X-…/examples/` | Small runnable scripts that support a lesson |
| `week-0X-…/exercises/` | Starter code, test cases and separate solutions |
| `week-0X-…/problems/` | Full coding problems: statement, hints, solution, complexity |
| `week-0X-…/interview-prep/` | Interview questions, spoken answers, mock interviews |
| `week-0X-…/revision/` | Flashcards and active-recall material |
| `week-0X-…/assessments/` | Quizzes, weekly assessment, answer key, rubric |
| [progress-tracking/](progress-tracking/overall-progress.md) | Course-level progress and the problem log |
| [projects/](projects/README.md) | Larger practice projects built from the patterns learned |
| [scripts/](scripts/check_links.py) | Validation tools (internal links, repository structure) |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to add lessons, problems and content safely |

## Daily rhythm (every learning day)

| Block | Time | Activity |
| --- | --- | --- |
| Concepts | 45 min | Read the lesson, annotate, write questions |
| Guided implementation | 45 min | Re-type and modify the lesson examples without looking |
| Problem solving | 90 min | Solve the day's problems; try hints before solutions |
| Active recall | 30 min | Flashcards, error log, explain one solution out loud in English |

Sunday replaces the four blocks with mistake review, re-solving, retention testing and a
cumulative assessment. Details: [docs/learning-method.md](docs/learning-method.md).

## Requirements

- Python 3.11 or newer (developed and validated on 3.11).
- No third-party packages. Everything uses the Python standard library.

No dependency file is needed at this stage; if a week later requires tooling, it will be added
deliberately rather than by default.

## Validating the repository

```bash
python3 scripts/check_structure.py   # required folders/files for all 7 weeks
python3 scripts/check_links.py       # every relative Markdown link resolves
```

Both scripts are standard-library only and exit with a non-zero status on failure, so they can
run locally or in CI ([.github/workflows/validate.yml](.github/workflows/validate.yml)).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the content rules: one topic per lesson, hints before
solutions, original explanations, verified links only, and no duplicate documents.

## Next steps

1. Approve this structure.
2. Generate the complete Week 1 content (lessons, examples, exercises, problems, interview
   preparation, revision, assessments) into the folders already reserved for it.
3. Repeat the same pattern for Weeks 2–7, one week at a time.
