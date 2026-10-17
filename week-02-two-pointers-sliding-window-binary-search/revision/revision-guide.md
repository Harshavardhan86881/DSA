# Week 2 Revision Guide

Link to lessons rather than duplicating them.

## Concise summaries

- **Two pointers:** opposite-direction on sorted data; read/write for in-place compaction.
- **Sliding window:** fixed size with running aggregate; variable size with shrink loop.
- **Binary search:** halve sorted search space; O(log n).
- **Binary search on answer:** feasibility function + monotonic predicate; O(n log range).
- **Sorting as pattern:** sort then scan/group/merge; O(n log n).

## Decision rules

- Sorted + pair/partition → two pointers.
- Contiguous subarray + condition → sliding window.
- Sorted + search value/boundary → binary search.
- Numeric answer + monotonic feasibility → binary search on answer.
- Grouping/merging/intervals → sort first.

## Invariants

- Two pointers: pairs outside the interval are ruled out.
- Sliding window: window satisfies the condition.
- Binary search: target lies in [left, right] if present.
- Binary search on answer: first feasible is the answer.

## Complexity patterns

- Two pointers: O(n) after sort.
- Sliding window: O(n).
- Binary search: O(log n).
- Binary search on answer: O(n log range).
- Sorting: O(n log n).

## Common mistakes

- Off-by-one in binary search bounds.
- Non-monotonic feasibility.
- Forgetting to remove leaving element in window.
- Sorting when hashing suffices.
- Moving the wrong pointer.

## Links

- `../lessons/two-pointers/two-pointers.md`
- `../lessons/sliding-window/sliding-window.md`
- `../lessons/binary-search/binary-search.md`
- `../lessons/binary-search-on-answer/binary-search-on-answer.md`
- `../lessons/sorting-patterns/sorting-as-a-pattern.md`
- `../lessons/pattern-selection/pattern-selection.md`
