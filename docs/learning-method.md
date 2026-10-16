# Learning method

This document explains *how* to study in this course: the daily four-hour block, the four
learning principles, the revision schedule, and the Sunday routine. Following it matters more
than finishing fast.

## 1. Four principles behind every exercise

| Principle | What it means here | Why it matters for this learner |
| --- | --- | --- |
| Active recall | Close the lesson and reproduce the idea from memory; answer flashcards without notes | Fixes "I understand when I read it, but I forget it later" |
| Spaced repetition | Revisit each topic after 1, 3, 7 and 14 days | Moves knowledge into long-term memory with minimum total time |
| Deliberate practice | Work at the edge of ability: solve problems that are slightly too hard, with hints available | Builds independent logic instead of copying |
| Explanation | Say each solution out loud in English, in a fixed three-part shape | Interview performance is a speaking skill, not only a coding skill |

Copying a solution teaches almost nothing. The rule of this course is: **write it, break it,
fix it, explain it.**

## 2. The daily four-hour block (learning days)

| Block | Time | What to do | What not to do |
| --- | --- | --- | --- |
| Concepts | 45 min | Read the day's lesson. Annotate in your own words. Write questions you cannot answer yet. | Do not copy the code yet. Do not aim to finish the whole lesson. |
| Guided implementation | 45 min | Re-type the lesson's examples from memory, then modify them (change input, break an edge case, change the goal). Compare with the lesson afterwards. | Do not paste code. Do not skip the modification step. |
| Problem solving | 90 min | Solve the day's problems with a timer: 25 minutes per problem before hints, 15 more before the solution. Log every attempt. | Do not open the solution at minute 5. Do not solve problems without writing tests. |
| Active recall | 30 min | Flashcards, mistake notebook, and one spoken explanation of the day's best solution. | Do not re-read lessons passively. Do not leave the spoke drill for later. |

Practical notes:

- Take a 5–10 minute break between blocks. Long uninterrupted sessions reduce recall quality.
- If a problem is unsolved after 40 minutes and hints, write the *blocker* in the mistake notebook,
  study the solution, then re-solve the same problem from a blank file on the next day.
- Keep the timer visible. Interview pressure is part of the skill being trained.

## 3. The lesson study loop

Use this loop for every lesson instead of reading it end to end:

1. **Skim** the headings and learning objectives (2 minutes).
2. **Read** the explanation once, slowly, and mark anything unclear (10–15 minutes).
3. **Close** the lesson and write the main idea in two sentences in your own words.
4. **Implement** the worked example from memory and run it; then run it on your own input.
5. **Answer** the review questions without looking. Anything you cannot answer is a flashcard
   for the next day.

## 4. The problem-solving loop

Every problem in this course follows the same seven-step routine, defined in
[problem-solving-framework.md](problem-solving-framework.md): understand, restate, example by
hand, plan, code small, test, then analyse complexity and explain. Reading that document once
and using it on every problem is the single highest-value habit in Week 1.

Minimum test set for any array or string problem before declaring it solved:

- empty input, single element;
- all elements equal (and, when relevant, all distinct);
- negative numbers and zero where the problem allows them;
- the largest input the constraints allow.

## 5. Debugging routine

When code fails, do not start changing lines at random. Follow this order:

1. **Read the error text fully.** Note the exception type, the line number and the last frame.
2. **Reproduce it in the smallest possible input.** Usually a 3-element case is enough.
3. **Print state, not conclusions.** Print the variables the code depends on at each iteration.
4. **Check boundaries first.** Off-by-one errors, empty containers and `None` values cause most
   failures in Weeks 1–3.
5. **Write the failing case as a test** before fixing it, then re-run the whole test set.
6. **State the cause in one sentence** and add it to the mistake notebook.

The mistake notebook template lives at
[../templates/mistake-notebook-template.md](../templates/mistake-notebook-template.md).

## 6. Spaced repetition schedule

Each topic is revisited four times after it is first learned. Keep the dates in the week's
`progress/` files.

| Review | When | Activity | Time |
| --- | --- | --- | --- |
| R1 | Next day | Answer the topic's flashcards, re-solve one exercise from scratch | 15 min |
| R2 | After 3 days | Explain the topic aloud in English for 3 minutes, re-solve one problem | 20 min |
| R3 | After 7 days | Mixed problem set containing this topic with others; no notes allowed | 30 min |
| R4 | After 14 days | Timed re-solve of the hardest problem from the topic, plus complexity analysis | 30 min |

If a review fails (wrong answer, blank mind, more than 2 seconds per flashcard), reset the interval
for that topic back to R1.

## 7. Sunday revision structure

Sunday is not a day off and not a day of new material. It is the day that makes the week stick.

| Block | Time | Activity |
| --- | --- | --- |
| Mistake review | 60 min | Read the week's mistake notebook entries. For each bug, re-solve the problem it came from with the fix in mind. |
| Re-solving selected problems | 75 min | Re-solve 2–3 problems chosen by weakness, from a blank file, with a timer. |
| Retention testing | 60 min | Flashcards and active-recall questions for the whole week; then explain 3 solutions out loud in English. |
| Cumulative assessment | 45 min | Complete the week's assessment, self-grade it with the rubric, and record the score. |
| Planning | 15 min | Fill in the next week's tracker, choose which topics need extra R1/R2 reviews. |

## 8. Speaking practice: the three-part answer

Interviews test explanation as much as code. Train this shape until it is automatic:

1. **Idea (one sentence):** "I will store each number's complement in a hash map while scanning once."
2. **Why it is correct and efficient (two sentences):** "Each element is checked exactly once, and
   the map lookup is O(1) on average, so the total time is O(n) instead of O(n²). Space grows with
   the number of stored elements, so it is O(n)."
3. **Walkthrough on a small case (30–60 seconds):** trace the example input, saying the state of
   the variables after each step.

Record yourself once a week. Listen for filler words and for paragraphs that start with
"basically".

## 9. Weekly review checklist

Answer these honestly at the end of each week; a "no" means the week is not finished yet.

- [ ] Can I state the week's main ideas without opening a file?
- [ ] Did I attempt every starter-code exercise before reading a solution?
- [ ] Did I solve every problem in that week's `problems/` folder at least once unaided?
- [ ] Does every bug that cost more than 10 minutes have a mistake-notebook entry?
- [ ] Can I answer the week's flashcards in under 2 seconds each?
- [ ] Can I explain three solutions aloud in English in under 3 minutes each?
- [ ] Is the week's assessment passed according to its rubric?

## 10. Related documents

- [course-overview.md](course-overview.md) — the 7-week scope.
- [problem-solving-framework.md](problem-solving-framework.md) — the 7-step problem routine.
- [complexity-cheatsheet.md](complexity-cheatsheet.md) — reference for complexity analysis.
- [resources.md](resources.md) — free resources, in suggested order.
- [progress-guide.md](progress-guide.md) — trackers, readiness and grading.
