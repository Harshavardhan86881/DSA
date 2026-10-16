# Contributing to the DSA roadmap

This repository is a personal learning course, but it is also a content project that gets improved
over time (by the learner, or by a supervised AI workflow). These rules keep it consistent, honest
and easy to navigate.

## 1. Ground rules

1. **One topic per file.** If a file needs "and" in its title, it is probably two files.
2. **No duplicated explanations.** Link to the single place where a concept is explained instead of
   re-explaining it in each week.
3. **Original explanations and original code.** Do not copy editorial text from problem sites,
   other repositories or paid books. Problem *names* and *constraints* may be referred to, but the
   explanation, dry runs and Python code must be written here.
4. **No secrets, ever.** No API keys, tokens, cookies, personal data, or local machine paths.
   `.env` files are ignored by `.gitignore`; keep it that way.
5. **No placeholders in committed content.** Every committed lesson section must contain real
   explanation. Reserved folders stay empty (with a `.gitkeep`) until their content is written, and
   unfinished marker words are rejected by `scripts/check_structure.py`.
6. **Verified links only.** Every external URL must be checked and marked as verified (with a date)
   or explicitly marked for manual verification. Never invent a URL.
7. **No generated artefacts.** Do not commit caches, virtual environments, build output, notebooks
   with outputs, or datasets. `.gitignore` covers the common cases.

## 2. Repository layout conventions

| Path | Convention |
| --- | --- |
| `docs/` | Shared, cross-week documentation. Plain lower-case filenames with hyphens. |
| `templates/` | Reusable skeletons. Templates must never contain real solutions. |
| `week-0X-<theme>/README.md` | Budget (objectives, day plan, deliverables, exit criteria) for that week |
| `week-0X-<theme>/curriculum/` | Day-by-day study plans, one file per day |
| `week-0X-<theme>/lessons/<topic>/` | The written lesson for one topic, in one file per topic |
| `week-0X-<theme>/examples/` | Small runnable `.py` scripts referenced by the lessons |
| `week-0X-<theme>/exercises/starter-code/` | Open-and-solve files with incomplete functions |
| `week-0X-<theme>/exercises/solutions/` | Complete solutions, separate from starter code |
| `week-0X-<theme>/exercises/test-cases/` | Input/expected-output fixtures or test data files |
| `week-0X-<theme>/problems/easy/`, `.../intermediate/` | Full problems, one file per problem |
| `week-0X-<theme>/assessments/`, `revision/`, `interview-prep/` | Week-specific assessment and recall material |
| `progress-tracking/` | Course-level trackers only; per-week logs live in that week's `progress/` |

Naming: lower-case, hyphen-separated, `.md` for content, `.py` for code, `.csv` only for genuine
tabular logs.

## 3. Adding a lesson

1. Copy [templates/lesson-template.md](templates/lesson-template.md) into the right
   `lessons/<topic>/` folder.
2. Fill in every section. The template order is mandatory: objectives → prerequisites →
   explanation → examples → dry runs → complexity → common mistakes → practice → hints → solutions →
   interview applications → review questions.
3. Keep hints and solutions in separate, clearly labelled sections. A learner must be able to read
   the file top-to-bottom without seeing a solution too early.
4. Every code block must be either runnable as written or explicitly marked as pseudocode.
5. Run `python3 scripts/check_links.py` and `python3 scripts/check_structure.py` before committing.

## 4. Adding a coding problem

Copy [templates/coding-problem-template.md](templates/coding-problem-template.md). A finished problem
contains, in this order: statement, constraints, examples, hints (graded), brute-force approach,
optimised approach, annotated Python solution, dry-run table, complexity analysis, edge cases, tests
and related problems. If the problem is also placed in the repository's own problem collection,
its solution file stays in the same folder as the statement for easy browsing.

## 5. Supervised AI-assisted content workflow

AI can draft content quickly, but every AI-drafted change is treated as an unverified draft:

1. Generate the draft using a supported assistant interface, and check it against the human-readable
   sources listed in [docs/resources.md](docs/resources.md).
2. Check every code sample by running it: `python3 -m pytest` and `python3 -m compileall .`.
3. Re-verify every external link; mark unverifiable ones instead of guessing.
4. Re-state technical claims in your own words; delete anything you cannot confirm.
5. Only then commit, with a message that says what was added and what was verified.

Never commit generated content that has not been executed or read.

## 6. Commit and branch conventions

- Small, single-purpose commits with imperative messages, for example:
  `Add Week 1 Day 2 lesson on time complexity`.
- Content changes and structural changes go in separate commits.
- Never force-push to `main`, and never rewrite published history.
- Keep the branch you work on and the files you touch consistent: a Week 3 commit should not
  re-format Week 1.

## 7. Definition of done for any content commit

- [ ] The file follows its template and contains no placeholders.
- [ ] All Python in it runs (or is clearly labelled pseudocode).
- [ ] All internal links resolve (`scripts/check_links.py` passes).
- [ ] All external links are verified or marked for manual verification.
- [ ] The relevant README's status table is updated if a week's state changed.
- [ ] `git status` shows only intended files.

## 8. Related documents

- [README.md](README.md) — what the course contains and how to use it.
- [docs/course-overview.md](docs/course-overview.md) — the 7-week scope.
- [docs/resources.md](docs/resources.md) — verified free resources.
- [templates/lesson-template.md](templates/lesson-template.md),
  [templates/coding-problem-template.md](templates/coding-problem-template.md) — content shapes.
