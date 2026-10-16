# Mistake notebook template

A mistake notebook is the highest-value document in this repository. Reading a solution once
teaches you that problem; writing down *why your own code failed* prevents the same class of bug
from returning in an interview.

Copy this file to `week-0X-<theme>/progress/mistake-notebook.md` and keep one file per week, or keep
a single running copy in your own notes.

## How to use it

1. Add an entry when a bug costs you **more than 10 minutes**, or when a test fails in a way you did
   not predict.
2. Fill every field. "Careless mistake" is not an acceptable cause.
3. Write the fix as a rule you can apply to other problems ("check the empty list before indexing",
   not "fixed the bug").
4. Read the whole notebook during Sunday revision, and re-solve the problems in the "re-solve date"
   column.
5. When you make the same class of mistake three times, add it to your personal pre-submit checklist.

## Entry format

```markdown
### <date> — <problem name> (<topic>)

- **What I wanted the code to do:** <one sentence>
- **What it actually did:** <observed behaviour, including the exact error message>
- **Smallest input that showed the bug:** <e.g. [2, 2]>
- **Root cause:** <the real reason, e.g. "I compared values before inserting, so the first occurrence was never stored">
- **Fix:** <the change made>
- **Rule to remember:** <generalised prevention rule>
- **Re-solve date:** <YYYY-MM-DD, 3 or 7 days later>
- **Re-solved correctly?** yes / no
```

## Worked example entry

### 2026-10-16 — Contains Duplicate (hashing)

- **What I wanted the code to do:** return `True` if any value appears at least twice.
- **What it actually did:** returned `False` for `[2, 2]`.
- **Smallest input that showed the bug:** `[2, 2]`.
- **Root cause:** I wrote `if value in seen: return False` instead of `return True`, and I checked
  membership before adding the current value, so a pair of adjacent duplicates could not be detected.
- **Fix:** check `if value in seen: return True`, then `seen.add(value)`.
- **Rule to remember:** in "seen before" patterns, the check and the insert order defines the
  meaning; state the invariant in a comment before coding.
- **Re-solve date:** 2026-10-19
- **Re-solved correctly?** yes

## Quick index

| Date | Problem | Topic | Root cause (short) | Re-solve date | Re-solved OK |
| --- | --- | --- | --- | --- | --- |
| 2026-10-16 | Contains Duplicate | hashing | reversed boolean in the seen check | 2026-10-19 | yes |
| | | | | | |

## Repeated-mistake watchlist

| Class of mistake | Times seen | My pre-submit check |
| --- | --- | --- |
| Empty / single-element input not handled | `<n>` | Run the function with `[]` and `[x]` before submitting |
| Off-by-one in loop bounds | `<n>` | Write the loop bounds in a comment and re-read them |
| `pop(0)` or `insert(0, x)` inside a loop | `<n>` | Ask "does this shift the whole list?" |
| Building strings with `+=` in a loop | `<n>` | Collect parts and join once |
| Wrong boolean returned from a "seen before" check | `<n>` | State the invariant above the loop |
| Complexity claimed but not counted from the loops | `<n>` | Count loops explicitly before answering |
