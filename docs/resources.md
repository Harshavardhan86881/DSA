# Free learning resources

Selected free resources for this course. Every URL below was checked on **2026-10-16** using an
HTTP page fetch from this repository's development environment (see "How these links were
verified" at the end). Nothing here is paid content.

## Suggested order of use

| # | Resource | Use it for | When |
| --- | --- | --- | --- |
| 1 | [Python Tutorial — Data Structures](https://docs.python.org/3/tutorial/datastructures.html) | Lists, list methods, comprehensions, dicts, sets, tuples | Week 1, Day 3–5 |
| 2 | [collections module docs](https://docs.python.org/3/library/collections.html) | `Counter`, `defaultdict`, `deque` details | Week 1, Day 5 |
| 3 | [Problem Solving with Algorithms and Data Structures (Runestone)](https://runestone.academy/ns/books/published/pythonds/index.html) | A second explanation of analysis, lists and dict performance | Week 1, after Day 2 |
| 4 | [VisuAlgo](https://visualgo.net/en) | Animating array, sorting and hash-table operations | Week 1, Day 3–5 |
| 5 | [Python Tutor](https://pythontutor.com/) | Seeing what your own code does step by step | any day you are stuck |
| 6 | [Python wiki — TimeComplexity](https://wiki.python.org/moin/TimeComplexity) + [Big-O Cheat Sheet](https://www.bigocheatsheet.com/) | The reference tables behind [complexity-cheatsheet.md](complexity-cheatsheet.md) | Week 1, Day 2 |
| 7 | [NeetCode roadmap](https://neetcode.io/roadmap) | Choosing which pattern to practise next, free problem lists | Day 6 and Weeks 2–7 |
| 8 | [LeetCode problem set](https://leetcode.com/problemset/) | Extra problems filtered by tag (Array, String, Hash Table, Prefix Sum) | after the week's own problems |
| 9 | [Exercism — Python track](https://exercism.org/tracks/python) | Free mentored Python exercises with feedback | throughout |
| 10 | [MIT OCW 6.006 Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) | Lectures and notes for deeper analysis and later weeks | Week 4 onwards, selectively |
| 11 | [cp-algorithms](https://cp-algorithms.com/) | Precise reference articles for specific algorithms | Weeks 5–6 |
| 12 | [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | Reading alternative Python implementations | Weeks 3–6 |

---

## 1. Python language reference (official)

### Python Tutorial, Chapter 5 — Data Structures

- **URL:** <https://docs.python.org/3/tutorial/datastructures.html>
- **Topic:** Lists and list methods, list comprehensions, `del`, tuples and sequences, sets,
  dictionaries, looping techniques.
- **Recommended section:** 5.1 "More on Lists" through 5.5 "Dictionaries" — read the subsections on
  stack/queue use of lists and on comprehensions.
- **Why it is useful:** the fastest way to confirm the exact behaviour and complexity of list and
  dict operations before using them in a problem solution. The section also explains why lists are
  poor queues, which is exactly the `pop(0)` mistake beginners make.
- **Order:** first resource of Week 1, used alongside Day 3 (arrays), Day 4 (strings) and Day 5
  (hashing).

### Python `collections` module documentation

- **URL:** <https://docs.python.org/3/library/collections.html>
- **Topic:** `Counter`, `defaultdict`, `deque`, `namedtuple`.
- **Recommended section:** the summary table at the top, then the `Counter` and `defaultdict` class
  sections; the `deque` section is needed in Week 3.
- **Why it is useful:** `Counter` and `defaultdict` remove a lot of manual counting code, and their
  documented behaviour explains what happens on missing keys — a frequent source of bugs.
- **Order:** read after Day 5's lesson, then rewrite two of your counting solutions using
  `Counter` and compare readability.

### Sorting Techniques (official HOWTO)

- **URL:** <https://docs.python.org/3/howto/sorting.html>
- **Topic:** `sorted()` and `list.sort()`, the `key` parameter, multi-key sorting, stability.
- **Recommended section:** "Sorting Basics" and "Key Functions".
- **Why it is useful:** sorting is allowed in many Week 1 problems; using `key=` correctly avoids
  hand-written comparison loops.
- **Order:** read before Day 6, when sorting is compared with frequency counting.

## 2. Complexity and analysis

### Python wiki — Time & Space Complexity ("TimeComplexity")

- **URL:** <https://wiki.python.org/moin/TimeComplexity>
- **Topic:** Average vs amortised worst-case complexity of `list`, `deque`, `set` and `dict`
  operations.
- **Recommended section:** the `list`, `set` and `dict` tables.
- **Why it is useful:** it is the canonical reference used by interviewers when they ask "what is
  the complexity of `x in set`?".
- **Note:** the wiki is in archival/maintenance mode and the page may move in future. If it fails to
  load, use the Big-O Cheat Sheet or the newer official documentation page for time complexity that
  recent Python documentation versions include.
- **Order:** Week 1, Day 2, then keep the tab open during every problem you solve.

### Big-O Cheat Sheet

- **URL:** <https://www.bigocheatsheet.com/>
- **Topic:** Growth-rate chart plus time/space complexity tables for data structures and sorting
  algorithms.
- **Recommended section:** "Big-O Complexity Chart" and "Common Data Structure Operations".
- **Why it is useful:** one page that answers "how do these arrays/lists compare as n grows".
- **Order:** Week 1, Day 2 as a visual companion to the lesson.

### pythoncomplexity.com — Python Time & Space Complexity reference

- **URL:** <https://pythoncomplexity.com/>
- **Topic:** Per-operation complexity for builtins and standard-library modules, across Python
  versions and implementations, with sources cited.
- **Recommended section:** "Builtins" (list, dict, set, str) and "Standard Library" (`heapq`,
  `bisect`).
- **Why it is useful:** a more granular and more actively maintained cross-reference than the wiki
  page, useful when you need the complexity of an operation the wiki does not list.
- **Caveat:** it is a community project (its own introduction says the content has been reviewed
  with AI assistance), so treat it as a secondary source and prefer the official documentation when
  the two disagree.
- **Order:** Week 1, Day 2, and afterwards whenever a complexity question is unclear.

### MIT OpenCourseWare 6.006 — Introduction to Algorithms (Spring 2020)

- **URL:** <https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/>
- **Topic:** University-level algorithm analysis, data structures, sorting, hashing, graphs,
  dynamic programming.
- **Recommended section:** lecture notes and problem sets for the "Introduction and Analysis"
  lectures (start of the course); return for graphs and DP in Weeks 5–6.
- **Why it is useful:** the reference-quality treatment of *why* the analysis rules in the
  cheatsheet are true, with free lecture videos and problem sets.
- **Order:** optional from Week 1 Day 2 onward; most valuable in Weeks 4–6. Do not try to watch all
  lectures during Week 1.

## 3. Visualisation and debugging practice

### VisuAlgo

- **URL:** <https://visualgo.net/en>
- **Topic:** Animated data structures and algorithms, including Array, Sorting, Hash Table,
  Linked List, Graph traversal.
- **Recommended section:** "Array" first, then "Sorting" and "Hash Table" (each page also has a
  Training mode with generated questions).
- **Why it is useful:** array shifts (`insert` in the middle, `pop(0)`) become obvious visually,
  which makes the complexity table believable instead of memorised.
- **Order:** Week 1, Day 3 (arrays) and Day 5 (hash table).

### Python Tutor

- **URL:** <https://pythontutor.com/>
- **Topic:** Step-by-step visualisation of Python execution: variables, objects, references, and
  call stack.
- **Recommended section:** "Start Visualizing" and paste your own function; enable "render all
  objects inline".
- **Why it is useful:** the fastest way to see why a list operation or a loop bound is wrong, and to
  build a correct mental model of list references (very relevant to Week 1 mistake patterns).
- **Order:** use whenever a bug survives 10 minutes of manual tracing.

## 4. Problem practice (free)

### NeetCode roadmap

- **URL:** <https://neetcode.io/roadmap>
- **Topic:** Free, topic-ordered roadmaps of interview problems (Arrays & Hashing, Two Pointers,
  Sliding Window, Stack, Trees, Graphs, DP…).
- **Recommended section:** the "Arrays & Hashing" group during Week 1; do not jump ahead before the
  Week 1 checklist passes.
- **Why it is useful:** the order matches this course's week structure, so it is easy to find
  exactly the next practice category without browsing thousands of problems.
- **Note:** the site has paid tiers for some features; the roadmap and problem lists are usable free.
- **Order:** Week 1, Day 6 for extra practice; every week afterwards.

### LeetCode problem set

- **URL:** <https://leetcode.com/problemset/>
- **Topic:** The largest public problem collection, filterable by tag (Array, String, Hash Table,
  Counting, Prefix Sum) and difficulty.
- **Recommended section:** filter by the Week 1 tags and difficulty `Easy`, then try `Medium` for
  the same tags in Week 1 Day 6.
- **Why it is useful:** the standard practice ground used in interviews; problem statements are
  short and the sample tests are included. Free to use; a few features (for example some company
  question lists) are subscriber-only.
- **Order:** after finishing the repository's own problems for a topic — never instead of them.

### Exercism — Python track

- **URL:** <https://exercism.org/tracks/python>
- **Topic:** Small Python exercises with automated tests and optional human mentoring.
- **Recommended section:** the "Easy"/"Medium" difficulty exercises that involve lists, strings and
  dictionaries.
- **Why it is useful:** free, structured practice with feedback on code style; useful when the
  interviewer-style problems feel too large on a low-energy day.
- **Order:** throughout the course, as light-day practice.

## 5. Deeper references for later weeks

### cp-algorithms — Algorithms for Competitive Programming

- **URL:** <https://cp-algorithms.com/>
- **Topic:** Precise, proof-oriented articles for specific algorithms and algorithms-and-data-
  structures techniques.
- **Recommended section:** later weeks only (graph traversal, suffix/prefix techniques, dynamic
  programming introductions). For Week 1, the "Prefix function" style articles are *not* needed;
  prefix sums are covered in Day 6 of this course.
- **Why it is useful:** when a lesson's simplified explanation is not enough and you want the formal
  version with complexity proofs.
- **Order:** Weeks 5–6, referenced on demand.

### TheAlgorithms/Python (GitHub)

- **URL:** <https://github.com/TheAlgorithms/Python>
- **Topic:** Community collection of algorithm implementations in Python, organised by category.
- **Recommended section:** `data_structures/` (arrays, linked lists, hashes) and `searches/`.
- **Why it is useful:** reading two or three alternative implementations of an algorithm trains you
  to recognise the parts that must stay the same. Code quality varies, so read critically.
- **Order:** Weeks 3–6, after you have implemented the structure yourself at least once.

---

## Resources deliberately not included

- **Paid courses and books.** They may be worth it later, but this plan is built on free material.
- **YouTube "solve 500 problems" playlists.** Watching solutions is passive; the goal here is
  writing code yourself.
- **AI-generated solution dumps.** Unverified and often subtly wrong; the course rules in
  [../CONTRIBUTING.md](../CONTRIBUTING.md) require every explanation to be checked by a human before
  it is committed.

## How these links were verified

Each URL above was fetched on 2026-10-16 and returned a live page matching the description
(for example, the Python docs page returned the "Data Structures" chapter, the MIT page returned the
6.006 course page). The links are therefore considered verified as of that date.

Two things to re-check manually over time:

1. **Site redesigns.** The Python wiki page is archived; if it is ever removed, use the Big-O Cheat
   Sheet and pythoncomplexity.com instead. The exact section links inside third-party sites
   (Runestone, VisuAlgo, NeetCode) can change after redesigns even though the home pages stay valid.
2. **Content staying free.** If a listed site later paywalls the recommended content, replace it
   with an equivalent free resource rather than paying, and update this file.

## Related documents

- [course-overview.md](course-overview.md) — where each resource fits in the 7-week scope.
- [complexity-cheatsheet.md](complexity-cheatsheet.md) — the summary tables distilled from the
  complexity references above.
- [../CONTRIBUTING.md](../CONTRIBUTING.md) — the rule that new links must be verified before commit.
