# Koko Eating Bananas

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | binary search on answer, arrays |
| **Target time** | 25 minutes |
| **Solution file** | [koko-eating-bananas.py](koko-eating-bananas.py) |

## 1. Problem statement

Koko loves bananas. There are `n` piles of bananas; pile `i` has `piles[i]` bananas. The
guards will return in `h` hours. Koko can choose her eating speed `k` (bananas per hour). Each
hour she picks one pile and eats `k` bananas from it; if the pile has fewer than `k`, she eats
all of them and does not eat from another pile that hour. Find the minimum integer `k` such
that she can eat all bananas within `h` hours.

## 2. Constraints

- `1 ≤ piles.length ≤ 10^4`
- `piles.length ≤ h ≤ 10^9`
- `1 ≤ piles[i] ≤ 10^9`

## 3. Examples

**Example 1**

```text
Input:  piles = [3, 6, 7, 11], h = 8
Output: 4
```

**Example 2**

```text
Input:  piles = [30, 11, 23, 4, 20], h = 5
Output: 30
```

**Example 3 — edge case**

```text
Input:  piles = [30, 11, 23, 4, 20], h = 6
Output: 23
```

## 4. Hints

<details><summary>Hint 1 — orientation</summary>
The answer is a speed between 1 and max(piles). Checking a speed is O(n).
</details>
<details><summary>Hint 2 — technique</summary>
Binary search on the speed. Feasible(k) = total hours at speed k ≤ h.
</details>
<details><summary>Hint 3 — structure</summary>

```python
def feasible(k):
    hours = sum((p + k - 1) // k for p in piles)
    return hours <= h
```
</details>

## 5. Brute-force approach

Try every speed from 1 to max(piles). O(max_pile * n) time.

```python
def koko_brute(piles, h):
    for k in range(1, max(piles) + 1):
        hours = sum((p + k - 1) // k for p in piles)
        if hours <= h:
            return k
```

## 6. Optimised approach

Binary search on answer. Feasible(k) is monotonic: larger k → fewer hours.

```python
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
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `feasible(k)` | Hours at speed k ≤ h | Decision function |
| `(p + k - 1) // k` | Ceil division | Hours per pile |
| `left, right = 1, max(piles)` | Bounds | 1 ≤ answer ≤ max pile |
| `if feasible(mid)` | Candidate works? | Try smaller if yes |
| `answer = mid; right = mid - 1` | Record and shrink | Find first feasible |
| `else: left = mid + 1` | Need larger speed | Not feasible |

## 8. Dry run

Input: piles = [3, 6, 7, 11], h = 8. Answer = 4.

| Step | `left` | `right` | `mid` | `feasible(mid)` | Action |
| --- | --- | --- | --- | --- | --- |
| 0 | 1 | 11 | 6 | 1+1+2+2=6 ≤ 8 → True | answer=6, right=5 |
| 1 | 1 | 5 | 3 | 1+2+3+4=10 > 8 → False | left=4 |
| 2 | 4 | 5 | 4 | 1+2+2+3=8 ≤ 8 → True | answer=4, right=3 |
| 3 | 4 | 3 | — | — | loop ends; answer=4 |

## 9. Complexity analysis

| Approach | Time | Space | Reasoning |
| --- | --- | --- | --- |
| Brute force | O(n * max_pile) | O(1) | Try every speed |
| Optimised | O(n log max_pile) | O(1) | log steps * O(n) check |

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| h equals number of piles | `[3,6,7,11]`, h=4 | `11` | Must eat one pile per hour |
| h very large | `[3,6,7,11]`, h=100 | `1` | Speed 1 suffices |
| Single pile | `[5]`, h=1 | `5` | One pile, one hour |
| All equal | `[4,4,4]`, h=3 | `4` | Simple case |

```python
def test_basic():
    assert min_eating_speed([3, 6, 7, 11], 8) == 4

def test_large_h():
    assert min_eating_speed([3, 6, 7, 11], 100) == 1
```

## 11. Follow-up questions

1. What if Koko must eat from the largest pile first? (Feasibility changes; may not be monotonic.)
2. What if there is a maximum speed limit? (Adjust upper bound.)
3. How would you handle fractional speeds? (Problem requires integers.)

## 12. Related problems

- `../../exercises/starter-code/koko_eating_bananas.py` — starter code.
- `../../lessons/binary-search-on-answer/binary-search-on-answer.md` — the full lesson.
