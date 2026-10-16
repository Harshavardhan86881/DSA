# Coding problem template

Copy this file into `week-0X-<theme>/problems/<difficulty>/<problem-name>.md` and fill every section.
Delete the guidance notes in angle brackets. The order of sections is mandatory: a learner must be
able to read the statement and hints without ever seeing the solution early.

---

# `<Problem name>`

| | |
| --- | --- |
| **Difficulty** | `easy` / `intermediate` |
| **Topics** | `<comma-separated topic tags>` |
| **Target time** | `<20–30>` minutes |
| **Solution file** | `<relative link to the .py solution>` |

## 1. Problem statement

`<Original wording, written here. Do not copy the editorial text of an existing problem. Refer to a
well-known problem by name only as "related problem".>`

## 2. Constraints

- `1 ≤ n ≤ 10^5`
- `<value range>`
- `<input guarantees: sorted? unique? always a solution?>`

## 3. Examples

**Example 1**

```text
Input:  <input>
Output: <output>
Explanation: <one or two sentences, only if it is not obvious>
```

**Example 2**

```text
Input:  <input>
Output: <output>
```

**Example 3 — edge case**

```text
Input:  <empty or single-element input>
Output: <output>
```

## 4. Hints (read only after 10 minutes of thinking)

<details>
<summary>Hint 1 — orientation</summary>

`<Point at the brute force or the input size. Example: "n is 10^5, so O(n^2) will be too slow.">`

</details>

<details>
<summary>Hint 2 — technique</summary>

`<Name the technique or data structure, without coding it.>`

</details>

<details>
<summary>Hint 3 — structure</summary>

`<Sketch the loop structure or the invariant, still without full code.>`

</details>

## 5. Brute-force approach

`<The simplest correct idea, with its complexity. State why it is correct and why it may be too
slow.>`

```python
# brute force, with the complexity in a comment
```

## 6. Optimised approach

`<Explain what the brute force repeats, and which data structure or observation removes the
repetition. State the invariant in one sentence.>`

```python
# optimised solution, type hints and a docstring
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `<...>` | `<...>` | `<...>` |

## 8. Dry run

Input: `<input>` — trace by hand. Track every variable that changes.

| Step | `i` | `<other variable>` | Decision / result | Note |
| --- | --- | --- | --- | --- |
| 0 | — | | initial state | |
| 1 | | | | |

## 9. Complexity analysis

| Approach | Time | Space | Reasoning |
| --- | --- | --- | --- |
| Brute force | | | |
| Optimised | | | |

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| Empty | | | |
| Single element | | | |
| All equal | | | |
| Negatives / zero | | | |
| Maximum size | | | |

```python
# tests for this problem (pytest style, standard library only)
```

## 11. Follow-up questions

1. `<How would the answer change if the input were sorted? / streamed? / much larger?>`
2. `<Can the space be reduced? What would it cost in time?>`

## 12. Related problems

- `<repository problem or technique, as a relative link>`
- `<external practice reference by name, with the tag used to find it>`
