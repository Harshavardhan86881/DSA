# Backtracking

| | |
| --- | --- |
| **Week** | 6 — Backtracking, greedy, dynamic programming |
| **Topic** | Backtracking |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Week 4 recursion |
| **Deliverable** | `exercises/starter-code/subsets.py` attempted |

## 1. Learning objectives

After this lesson you can:

1. Explain search-space exploration in simple English.
2. Identify the decision at each recursion level.
3. Use the choose, explore, undo pattern.
4. Distinguish a decision tree from the Python call stack.
5. Generate subsets, permutations, and combinations.
6. Handle duplicates safely.
7. Explain why `path.copy()` or `path[:]` is needed.
8. State time and space complexity including output cost.

## 2. Prerequisites check

1. Can you trace a recursive function on a small input?
2. Can you explain what a base case does?
3. Can you append and pop from a Python list?

## 3. Why this matters

Backtracking solves problems where you must explore combinations of choices: subsets, permutations, combinations, N-Queens, Sudoku, and word search. Interviewers often ask you to explain not just the code, but why an undo step is necessary.

## 4. Build intuition

Backtracking is depth-first search over a tree of choices. At each node you make one choice, recurse, then undo that choice so the next sibling choice starts from a clean state.

Mental model: imagine trying outfits. You put on a shirt, try all pants with it, then take the shirt off before trying the next shirt.

## 5. Search space and decisions

A search space is the set of all possible answers. A decision is one small choice at one recursion level, such as "include element 2 next" or "place queen in column 3."

The recursion level usually represents a position, index, or partial answer. The loop at that level tries every legal next choice.

## 6. Choose, explore, undo

```python
def backtrack(state):
    if base_case(state):
        record(state)
        return
    for choice in choices(state):
        choose(choice)      # mutate state
        backtrack(state)    # explore
        undo(choice)        # restore state
```

The undo step is not optional when state is mutable. Without it, later branches see changes made by earlier branches.

## 7. Decision tree vs call stack

The decision tree is the conceptual tree of all choices. The Python call stack is the runtime mechanism that remembers where to return. One call stack frame corresponds to one node in the decision tree, but the call stack also stores local variables and the loop position.

## 8. Subsets

Subsets of n distinct elements produce 2^n subsets. Each element has two choices: include or exclude.

```python
def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path[:])          # record current subset
        for i in range(start, len(nums)):
            path.append(nums[i])         # choose
            backtrack(i + 1, path)       # explore
            path.pop()                   # undo

    backtrack(0, [])
    return result
```

Line-by-line explanation:

- `result.append(path[:])`: record a copy, because `path` will change later.
- `for i in range(start, len(nums))`: try each element from `start` onward.
- `path.append(nums[i])`: choose the element.
- `backtrack(i + 1, path)`: explore subsets that include it; `i + 1` prevents reusing the same position.
- `path.pop()`: undo so the next iteration starts clean.

Dry run for `nums = [1, 2]`:

| Step | start | path before | choice | recursive call | path after undo | result added |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0 | [] | record | - | [] | [] |
| 2 | 0 | [] | 1 | backtrack(1, [1]) | [] | [] |
| 3 | 1 | [1] | record | - | [1] | [1] |
| 4 | 1 | [1] | 2 | backtrack(2, [1,2]) | [1] | [1] |
| 5 | 2 | [1,2] | record | - | [1,2] | [1,2] |
| 6 | 1 | [1] | done | return | [1] | [1,2] |
| 7 | 0 | [] | 2 | backtrack(2, [2]) | [] | [1,2] |
| 8 | 2 | [2] | record | - | [2] | [2] |

Final result: `[[], [1], [1,2], [2]]`.

## 9. Why copy the path

`result.append(path)` would store a reference to the same mutable list. Every later `append` and `pop` would change all stored results. `path[:]` or `path.copy()` creates a snapshot at recording time.

## 10. Permutations

Permutations of n distinct elements produce n! arrangements. Each level chooses an unused element.

```python
def permute(nums):
    result = []

    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False

    backtrack([], [False] * len(nums))
    return result
```

For n = 3, there are 3! = 6 permutations. For n = 10, there are 3,628,800 permutations, so output size dominates runtime.

## 11. Combinations

Combinations choose k items from n without regard to order. The same start-index idea as subsets avoids duplicate orderings.

```python
def combine(n, k):
    result = []

    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])
    return result
```

## 12. Duplicate handling

If input values can repeat, the position-based algorithms above may produce duplicate results. To produce unique value-based results, sort first and skip equal choices at the same level:

```python
def subsets_with_duplicates(nums):
    nums.sort()
    result = []

    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result
```

The condition `i > start` is important: it allows the first equal value at a level but skips later equal values, preventing duplicate branches.

## 13. Backtracking vs brute force vs recursion

- Brute force generates all possibilities without structure or pruning.
- Ordinary recursion solves a problem by reducing it; it may not explore multiple choices.
- Backtracking is structured DFS over choices with undo. It can include pruning.

## 14. Pruning preview

Pruning rejects a partial candidate before exploring all descendants. Example: in combination sum, if `remaining < 0`, stop. Pruning can make practical runtime much smaller, but it does not guarantee a better worst-case asymptotic bound.

## 15. Complexity

| Problem | Number of results | Time | Auxiliary space |
| --- | --- | --- | --- |
| Subsets | 2^n | O(n 2^n) | O(n) |
| Permutations | n! | O(n n!) | O(n) |
| Combinations | C(n,k) | O(k C(n,k)) | O(k) |

Time includes the cost of copying each result. Auxiliary space excludes the output list.

## 16. Common mistakes

| Mistake | Symptom | Fix |
| --- | --- | --- |
| Storing `path` instead of `path[:]` | all results look identical | copy before storing |
| Forgetting `path.pop()` | wrong or extra elements | undo every choose |
| Reusing the same index | duplicate or invalid results | pass `i` or `i + 1` |
| Skipping duplicates incorrectly | missing valid results | use `i > start` condition |
| No pruning on large input | timeout | add safe rejection |

## 17. Debugging checklist

1. Print `path` at the start of `backtrack`.
2. Check that every `append` has a matching `pop`.
3. Verify the base case records a copy.
4. Test with `[]`, one element, and duplicate values.
5. Count results and compare with 2^n or n!.

## 18. Practice

### Guided exercise 1

Trace subsets on `[1, 2, 3]` by hand.

### Guided exercise 2

Add duplicate handling to subsets.

### Independent exercise 1

Implement permutations.

### Independent exercise 2

Implement combination sum with reuse.

### Debugging exercise

Fix:

```python
def bad_subsets(nums):
    result = []
    path = []
    def backtrack(start):
        result.append(path)
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1)
    backtrack(0)
    return result
```

### Prediction exercise

How many subsets does a 4-element set have? Answer: 16.

## 19. Active-recall questions

1. What are the three backtracking steps?
2. Why copy path?
3. Why undo?
4. How many subsets for n elements?
5. How many permutations for n elements?

Answers:

1. Choose, explore, undo.
2. To avoid storing a mutable reference.
3. To restore state for the next choice.
4. 2^n.
5. n!.

## 20. Interview questions

**Q:** Why does backtracking need an undo step?
**A:** Because state is mutated in place; undo restores it for sibling choices.

**Q:** How do you avoid duplicate permutations with duplicates?
**A:** Sort and skip equal unused values at the same level.

Follow-up: What is the complexity of generating all permutations? O(n n!).

## 21. Spaced-repetition checklist

- Day 1: Write subsets from memory.
- Day 3: Write permutations from memory.
- Day 7: Explain duplicate handling.
- Day 14: Solve combination sum with pruning.

## 22. Explain aloud

"Backtracking explores choices depth-first. At each level I choose, recurse, then undo so the next choice starts clean. I copy the path when recording a result."
