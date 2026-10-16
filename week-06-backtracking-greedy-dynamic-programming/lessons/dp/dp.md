# Dynamic Programming

| | |
| --- | --- |
| **Week** | 6 |
| **Topic** | Dynamic programming |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Recursion |
| **Deliverable** | `coin_change.py` attempted |

## 1. Learning objectives

1. Identify overlapping subproblems.
2. Define state, transition, base case.
3. Implement memoisation and tabulation.
4. State complexity as states × transition.

## 2. Concept explanation

DP stores results of subproblems. Top-down memoisation caches recursion. Bottom-up tabulation fills a table in dependency order.

## 3. Worked example

```python
def climb_stairs(n):
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n+1):
        cur = prev1 + prev2
        prev2, prev1 = prev1, cur
    return prev1
```

## 4. Dry run

n=4: 1,2,3,5.

## 5. Complexity

| Problem | Time | Space |
| --- | --- | --- |
| Climbing stairs | O(n) | O(1) |
| Coin change | O(amount * coins) | O(amount) |
| LIS O(n^2) | O(n^2) | O(n) |

## 6. Common mistakes

- Wrong base cases.
- Wrong fill order.
- Forgetting impossible case (-1).
- Counting states incorrectly.

## 7. Practice

1. Climbing stairs.
2. House robber.
3. Coin change.
4. LIS.
