# Problem-Solving Foundations

| | |
| --- | --- |
| **Week** | 1 — Foundations |
| **Topic** | Problem solving |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Python functions, loops, lists; reading a traceback |
| **Deliverable** | `exercises/starter-code/reverse_array.py` and `second_largest.py` attempted and tested |

## 1. Learning objectives

After this lesson you can:

1. Extract input, output, constraints, guarantees and ambiguities from a statement.
2. Restate a problem in one or two sentences in your own words.
3. Hand-trace a small example and mark the step that repeats.
4. Write a brute-force solution first, then an optimised one, and explain the difference.
5. Test with the edge-case matrix: empty, single, duplicates, negatives, maximum size.
6. State time and space complexity for a solution you wrote.
7. Explain a solution aloud in the three-part shape: idea, correctness + complexity, walkthrough.

## 2. Prerequisites check

Answer these before starting; if any answer is "no", read the linked lesson first.

1. Can you write a Python function that takes a list and returns a value? (If no, review functions.)
2. Can you read a traceback and find the failing line? (If no, run a broken script and practise.)
3. Do you know what `len()`, indexing and `append` do? (If no, review Python lists.)

## 3. Why this matters

Every interview and every real task starts as a paragraph of English, not as code. The skill being
trained here is turning that paragraph into a plan you can type. Interviewers score the reasoning
shown in steps 1–4 of the routine, not only the final code. A correct but unexplained solution
scores lower than a slightly slower solution that is clearly reasoned. The same routine also
prevents the most common failure mode in this course: staring at an empty file for 40 minutes.

## 4. Concept explanation

### 4.1 The seven-step routine

Use the same seven steps for every problem until they become automatic.

| Step | Name | What you do |
| --- | --- | --- |
| 1 | Understand | Extract input, output, constraints, guarantees, ambiguities |
| 2 | Restate | Write the problem in one or two sentences in your own words |
| 3 | Hand-trace | Solve the smallest non-trivial example on paper |
| 4 | Plan | Write brute force, then the optimisation, in plain English |
| 5 | Code small | Write 5–10 lines, run, repeat |
| 6 | Test | Run the full edge-case matrix |
| 7 | Analyse | State complexity and explain aloud |

Steps 1–4 are spoken aloud in an interview. They are where most of the credit is earned.

> **Mental model:** coding is the last 20% of the work; understanding and planning are the first 80%.

### 4.2 Step 1 — Understand the question

Extract five things before writing anything:

1. **Input:** type, maximum size, can it be empty, can it contain duplicates?
2. **Output:** exact type, and what "no answer" looks like (`-1`, `[]`, `None`, raising an error).
3. **Constraints:** the size limit is the biggest hint about the required complexity.
4. **Guarantees:** is the input sorted? Can numbers be negative? Is there always exactly one answer?
5. **Ambiguity:** write down every question you would ask an interviewer.

The constraint-to-complexity link is worth memorising early:

| Input size (n) | Complexity expected to pass |
| --- | --- |
| n ≤ 10 | O(n!), O(2ⁿ) |
| n ≤ 20 | O(2ⁿ) with pruning |
| n ≤ 500 | O(n³) |
| n ≤ 5,000 | O(n²) |
| n ≤ 10⁶ | O(n log n) or O(n) |

If your plan is slower than the table allows, the plan is wrong, not the input.

### 4.3 Step 2 — Restate the problem

Write one or two sentences. Format:

> "Given a list of `n` integers, I must return ___ if ___ exists, otherwise ___."

If you cannot write this sentence, you do not understand the problem yet — go back to Step 1.
Restating also catches wrong assumptions early, which is much cheaper than catching them after coding.

### 4.4 Step 3 — Work a small example by hand

Take the smallest non-trivial input (usually 4–6 elements, never 20) and solve it slowly on paper:

- write the input in a row;
- write what you are looking for;
- mark which elements you compare, and in what order;
- note any step that **repeats across elements** — that repeated step is the loop.

Example of the note you are looking for: *"for every element I check whether `target - element`
was seen before"* — that sentence is already the algorithm.

### 4.5 Step 4 — Plan before coding

Write the plan as comments in the file, then code underneath the comments. Requirements:

- **Brute force first.** State the simplest correct approach even if it is slow.
- **Then optimise.** Say what is being repeated and which data structure removes the repetition.
  Example: "the inner loop searches again for the complement, so store complements in a dict".
- **Name the data structures and the loop bounds** explicitly, including inclusive/exclusive ends.
- **Predict complexity** of the plan before writing it, so you notice a slow plan early.

A plan is acceptable when you can read it aloud and someone else could type it into code.

### 4.6 Step 5 — Code in small steps and run often

- Write 5–10 lines, then run.
- Use meaningful names (`seen`, `best`, `prefix_sum`) instead of `x`, `y`, `temp2`.
- Handle the empty-input case at the top so the rest of the function can assume data exists.
- Keep a `main` block or a scratch call at the bottom so you can run the file instantly.
- If you feel stuck for more than 10 minutes, print the state and continue from Step 3, not from
  random edits.

### 4.7 Step 6 — Test with the edge-case matrix

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

### 4.8 Step 7 — Analyse complexity and explain out loud

- Count the loops and how each one scales with n; multiply nested loops that depend on n.
- State space: count extra containers created, not the input itself.
- Then answer this three-part question aloud in English:

  1. "The idea is ___."
  2. "It is correct because ___, and it runs in O(___), using O(___) extra space."
  3. "On this input, the variables look like this: ___."

## 5. Worked examples (simple → difficult)

### Example 1 — Reverse an array in place (simple)

```python
# Reverse a list of integers in place, without using a second list.
def reverse_in_place(nums: list[int]) -> None:
    left, right = 0, len(nums) - 1          # two pointers at both ends
    while left < right:                     # stop when they meet or cross
        nums[left], nums[right] = nums[right], nums[left]  # swap
        left += 1
        right -= 1


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    reverse_in_place(data)
    print(data)  # [5, 4, 3, 2, 1]
```

**Line-by-line explanation**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `left, right = 0, len(nums) - 1` | Pointers start at first and last index | Two pointers moving toward each other cover every pair once |
| `while left < right` | Loop while there is a pair to swap | `<` avoids swapping the middle element with itself |
| `nums[left], nums[right] = ...` | Swap the two values | Tuple assignment swaps without a temporary variable |
| `left += 1; right -= 1` | Move pointers inward | Shrinks the unprocessed middle |

### Example 2 — Find the second-largest distinct value (moderate)

```python
# Return the second-largest DISTINCT value, or None if it does not exist.
def second_largest(nums: list[int]) -> int | None:
    if len(nums) < 2:                       # not enough elements
        return None
    largest = second = None
    for value in nums:
        if largest is None or value > largest:
            second = largest                # old largest becomes second
            largest = value
        elif value != largest and (second is None or value > second):
            second = value
    return second


if __name__ == "__main__":
    print(second_largest([3, 1, 4, 4, 2]))  # 3
    print(second_largest([5, 5, 5]))         # None
```

**Line-by-line explanation**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `if len(nums) < 2` | Early exit | A second-largest distinct value needs at least 2 elements |
| `largest = second = None` | Track two best values seen so far | One pass is enough if we keep both |
| `if largest is None or value > largest` | New maximum found | The old maximum is now the second best |
| `elif value != largest and ...` | Candidate for second best | Must differ from largest to be "distinct" |
| `return second` | Result after the full scan | `None` means no distinct second value exists |

### Example 3 — Brute force then optimised duplicate check (harder)

```python
# Brute force: O(n^2) time, O(1) space.
def has_duplicate_brute(nums: list[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


# Optimised: O(n) time average, O(n) space.
def has_duplicate_fast(nums: list[int]) -> bool:
    seen: set[int] = set()
    for value in nums:
        if value in seen:                   # O(1) average
            return True
        seen.add(value)
    return False


if __name__ == "__main__":
    print(has_duplicate_brute([1, 2, 3, 1]))  # True
    print(has_duplicate_fast([1, 2, 3, 1]))   # True
    print(has_duplicate_fast([]))             # False
```

**Line-by-line explanation (optimised version)**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `seen: set[int] = set()` | Empty set of values met so far | Set gives O(1) average membership |
| `for value in nums` | One pass over the input | Single pass keeps time linear |
| `if value in seen` | Have we met this value before? | Early return on first duplicate |
| `seen.add(value)` | Record the value | Future duplicates will be caught here |

## 6. Dry-run table

Trace the hardest example by hand on this input: `[3, 1, 3]` for `has_duplicate_fast`.

| Step | Line executed | Variables after the step | Comment |
| --- | --- | --- | --- |
| 1 | `seen = set()` | `seen = {}` | Empty set |
| 2 | `value = 3` | `seen = {}` | First element |
| 3 | `if 3 in seen` | `seen = {}` | False, not seen before |
| 4 | `seen.add(3)` | `seen = {3}` | Record 3 |
| 5 | `value = 1` | `seen = {3}` | Second element |
| 6 | `if 1 in seen` | `seen = {3}` | False |
| 7 | `seen.add(1)` | `seen = {3, 1}` | Record 1 |
| 8 | `value = 3` | `seen = {3, 1}` | Third element |
| 9 | `if 3 in seen` | `seen = {3, 1}` | True → return True |

## 7. Complexity

| Version | Time | Space | Notes |
| --- | --- | --- | --- |
| Brute force duplicate check | O(n²) | O(1) | Nested loops; no extra container |
| Optimised duplicate check | O(n) average | O(n) | Set stores up to n values |
| Reverse in place | O(n) | O(1) | One pass, two pointers |
| Second largest (single pass) | O(n) | O(1) | Tracks two values |

## 8. Common mistakes

| Mistake | Symptom | Fix |
| --- | --- | --- |
| Coding before hand-tracing | Wrong algorithm, long debugging | Always do Step 3 first |
| Forgetting empty input | `IndexError` on `nums[0]` | Handle `len(nums) == 0` at the top |
| Using `x in list` inside a loop | Works but O(n²) | Use a set for membership |
| Counting input as extra space | Over-reported space | Count only containers you create |
| Testing only the given example | Missed empty/single cases | Run the full edge-case matrix |
| Planning only the optimised version | Cannot explain why it works | Always state brute force first |

## 9. Practice exercises

Do these before reading the hints. Files live in `exercises/starter-code/`.

1. **Reverse an array** — reverse a list in place and return it → `exercises/starter-code/reverse_array.py`
2. **Second-largest distinct element** — return the second-largest distinct value or `None` → `exercises/starter-code/second_largest.py`
3. **Find min and max** — return `(min, max)` in one pass without `min()`/`max()` → `exercises/starter-code/find_min_max.py`

## 10. Hints

<details>
<summary>Hint 1 — for exercise 1 (reverse an array)</summary>

Use two indices, one at the start and one at the end, and swap until they meet. Predict the
middle index for an odd-length list before coding.

</details>

<details>
<summary>Hint 2 — for exercise 2 (second largest)</summary>

You only need to remember two values while scanning: the largest and the second largest. Decide
what happens when the current value equals the largest.

</details>

<details>
<summary>Hint 3 — for exercise 3 (min and max)</summary>

Start both `best_min` and `best_max` from the first element, then update each independently in one
loop. This avoids a second pass.

</details>

## 11. Solutions

- `exercises/solutions/reverse_array.py`
- `exercises/solutions/second_largest.py`
- `exercises/solutions/find_min_max.py`

Do not open these until you have attempted the starter code for at least 25 minutes.

## 12. Interview applications

- **Question form:** "Given an array of integers, find the second largest distinct value."
- **Expected answer shape:** "I scan once while tracking the largest and second-largest values seen.
  It is correct because every value is compared against both trackers, and it runs in O(n) time
  and O(1) space. On `[3, 1, 4, 4, 2]` the trackers end at 4 and 3."
- **Follow-up the interviewer may ask:** "What changes if the array is streamed and you cannot
  store it?" (Answer: the same single-pass trackers still work, O(1) space.)

## 13. Review questions

Answer without looking at the lesson. If you cannot, make a flashcard.

1. List the seven steps in order.
2. What is the constraint-to-complexity link for n = 10⁶?
3. Why is brute force stated before the optimised version?
4. Name three categories from the edge-case matrix.
5. What are the three parts of the spoken answer?

## 14. Related lessons

- `../complexity/big-o-complexity.md` — how to state the complexity you claim here.
- `../../docs/problem-solving-framework.md` — the full reference for the seven-step routine.
- `../../docs/complexity-cheatsheet.md` — Python operation costs used in Step 7.
