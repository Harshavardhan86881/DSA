# Binary Search on Answer

| | |
| --- | --- |
| **Week** | 2 — Two pointers, sliding window, binary search, sorting patterns |
| **Topic** | Binary search on answer |
| **Estimated time** | Concepts 45 min + implementation 40 min |
| **Prerequisites** | Day 3 binary search |
| **Deliverable** | `exercises/starter-code/koko_eating_bananas.py` attempted and tested |

## 1. Learning objectives

After this lesson you can:

1. Explain the difference between searching an array and searching an answer space.
2. Define a feasibility (decision) function.
3. Identify a monotonic predicate and its direction.
4. Derive lower and upper bounds mathematically.
5. Solve Koko Eating Bananas and Capacity To Ship Packages.
6. State complexity as O(log(range) * cost_of_feasible).

## 2. Prerequisites check

1. Can you implement standard binary search? (If no, review Day 3.)
2. Can you state a loop invariant? (If no, review Day 3.)
3. Have you completed Week 1 complexity? (If no, review Week 1 Day 2.)

## 3. Why this matters

Many problems ask for the minimum or maximum value satisfying a condition, where checking a
candidate is easy but searching all candidates is expensive. Binary search on answer turns an
O(n * range) search into O(n * log range). Classic examples: Koko eating bananas, capacity to
ship packages, split array largest sum. The key skill is deriving the feasibility function and
proving monotonicity.

## 4. Concept explanation

### 4.1 Searching an answer space

Instead of searching an array index, we search a range of possible **answers** (e.g., eating
speed from 1 to max pile). Each candidate answer is tested by a **feasibility function**
`feasible(x)` that returns True if x works.

### 4.2 Monotonic predicate

Binary search on answer requires monotonicity:

- Pattern A (find first feasible): `F F F T T T`. As x increases, feasibility flips from False
  to True and stays True. We search for the first True.
- Pattern B (find last feasible): `T T T F F F`. As x increases, feasibility flips from True
  to False. We search for the last True.

If the predicate is not monotonic, binary search is invalid.

> **Mental model:** the feasibility function is a sorted array of True/False; binary search finds
> the transition point.

### 4.3 Feasibility function

A function `feasible(x)` that returns True if candidate x satisfies the problem's constraint.
It must be:

- Precise: exact condition from the problem.
- Monotonic: once True, stays True (or vice versa).
- Efficient: usually O(n).

### 4.4 Deriving bounds

- **Lower bound:** the smallest value that could possibly be feasible. Often 1 or max(element).
- **Upper bound:** a value that is definitely feasible. Often sum of all elements or max * n.

The bounds must contain the answer. Prove: lower ≤ answer ≤ upper.

### 4.5 Template (find first feasible, Pattern A)

```python
left, right = lo, hi
answer = hi
while left <= right:
    mid = left + (right - left) // 2
    if feasible(mid):
        answer = mid
        right = mid - 1   # try smaller
    else:
        left = mid + 1    # need larger
return answer
```

### 4.6 Template (find last feasible, Pattern B)

```python
left, right = lo, hi
answer = lo
while left <= right:
    mid = left + (right - left) // 2
    if feasible(mid):
        answer = mid
        left = mid + 1    # try larger
    else:
        right = mid - 1   # need smaller
return answer
```

## 5. Worked examples (simple → difficult)

### Example 1 — Koko Eating Bananas (simple)

Koko has piles of bananas. She eats at speed `k` bananas/hour. Each hour she picks one pile and
eats `k` from it. Find the minimum `k` to finish within `h` hours.

Feasibility: `feasible(k)` = total hours needed at speed k ≤ h. Hours for a pile = ceil(pile/k).
Monotonic: larger k → fewer hours → once feasible, stays feasible (Pattern A).

Bounds: lo = 1, hi = max(piles).

```python
import math

def min_eating_speed(piles: list[int], h: int) -> int:
    def feasible(k: int) -> bool:
        hours = sum((p + k - 1) // k for p in piles)
        return hours <= h

    left, right = 1, max(piles)
    answer = right
    while left <= right:
        mid = left + (right - left) // 2
        if feasible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


if __name__ == "__main__":
    print(min_eating_speed([3, 6, 7, 11], 8))  # 4
```

### Example 2 — Capacity To Ship Packages (moderate)

Find the minimum ship capacity to ship all packages within `days` days. Packages must be shipped
in order.

Feasibility: `feasible(cap)` = number of days needed with capacity cap ≤ days. Greedy: fill each
day until adding the next package exceeds cap.

Bounds: lo = max(weights) (must fit largest package), hi = sum(weights) (one day).

```python
def ship_within_days(weights: list[int], days: int) -> int:
    def feasible(cap: int) -> bool:
        needed = 1
        current = 0
        for w in weights:
            if current + w > cap:
                needed += 1
                current = w
            else:
                current += w
        return needed <= days

    left, right = max(weights), sum(weights)
    answer = right
    while left <= right:
        mid = left + (right - left) // 2
        if feasible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


if __name__ == "__main__":
    print(ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))  # 15
```

### Example 3 — Split Array Largest Sum (harder)

Split an array into `m` contiguous subarrays to minimise the largest subarray sum.

Feasibility: `feasible(limit)` = number of subarrays needed with max sum ≤ limit ≤ m.

Bounds: lo = max(nums), hi = sum(nums).

```python
def split_array(nums: list[int], m: int) -> int:
    def feasible(limit: int) -> bool:
        count = 1
        current = 0
        for n in nums:
            if current + n > limit:
                count += 1
                current = n
            else:
                current += n
        return count <= m

    left, right = max(nums), sum(nums)
    answer = right
    while left <= right:
        mid = left + (right - left) // 2
        if feasible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


if __name__ == "__main__":
    print(split_array([7, 2, 5, 10, 8], 2))  # 18
```

## 6. Dry-run table

Trace Koko on piles = [3, 6, 7, 11], h = 8. Answer = 4.

| Step | `left` | `right` | `mid` | `feasible(mid)` | Action |
| --- | --- | --- | --- | --- | --- |
| 0 | 1 | 11 | 6 | hours = 1+1+2+2=6 ≤ 8 → True | answer=6, right=5 |
| 1 | 1 | 5 | 3 | hours = 1+2+3+4=10 > 8 → False | left=4 |
| 2 | 4 | 5 | 4 | hours = 1+2+2+3=8 ≤ 8 → True | answer=4, right=3 |
| 3 | 4 | 3 | — | — | loop ends; answer=4 |

## 7. Complexity

For each problem: O(n * log(range)) time, O(1) auxiliary space, where range = hi - lo + 1
and n is the input size (for the feasibility check).

- Koko: O(n log max_pile).
- Ship: O(n log sum).
- Split: O(n log sum).

## 8. Common mistakes

| Mistake | Symptom | Fix |
| --- | --- | --- |
| Non-monotonic feasibility | Wrong answer | Verify the predicate direction |
| Bounds too small | Misses the answer | Prove lo ≤ answer ≤ hi |
| Bounds too large | Extra iterations (still correct) | Tighten hi |
| Treating feasible as O(1) | Underestimated complexity | Count the loop inside feasible |
| Off-by-one in template | Wrong boundary | Use the proven template |
| Forgetting impossible input | Crash or wrong answer | Handle per contract |

## 9. Practice exercises

Do these before reading the hints. Files live in `exercises/starter-code/`.

1. **Koko eating bananas** → `exercises/starter-code/koko_eating_bananas.py`
2. **Capacity to ship packages** → `exercises/starter-code/capacity_to_ship.py`
3. **Split array largest sum** → `exercises/starter-code/split_array_largest_sum.py`

## 10. Hints

<details><summary>Hint 1 — for exercise 1</summary>
Feasible(speed) = total hours at that speed ≤ h. Bounds: 1 to max(piles).
</details>
<details><summary>Hint 2 — for exercise 2</summary>
Feasible(cap) = days needed with that capacity ≤ days. Bounds: max(weights) to sum(weights).
</details>
<details><summary>Hint 3 — for exercise 3</summary>
Feasible(limit) = number of subarrays with max sum ≤ limit ≤ m. Bounds: max(nums) to sum(nums).
</details>

## 11. Solutions

- `exercises/solutions/koko_eating_bananas.py`
- `exercises/solutions/capacity_to_ship.py`
- `exercises/solutions/split_array_largest_sum.py`

Do not open these until you have attempted the starter code for at least 25 minutes.

## 12. Interview applications

- **Question form:** "Find the minimum speed to finish eating all bananas within h hours."
- **Expected answer shape:** "I binary search on the speed. The feasibility function computes
  total hours at a given speed. Since larger speed means fewer hours, the predicate is
  monotonic. Bounds are 1 and max pile. Each check is O(n), so total is O(n log max)."
- **Follow-up:** "How do you know the bounds are correct?" (Answer: prove lo ≤ answer ≤ hi.)

## 13. Review questions

Answer without looking at the lesson. If you cannot, make a flashcard.

1. What is a feasibility function?
2. What are the two monotonic patterns?
3. How do you derive bounds?
4. State the template for first feasible.
5. State the complexity and justify.

## 14. Related lessons

- `../binary-search/binary-search.md` — the foundation.
- `../../week-01-foundations/lessons/arrays/arrays-and-lists.md` — list operations.
- `../../docs/problem-solving-framework.md` — the routine to reuse.
