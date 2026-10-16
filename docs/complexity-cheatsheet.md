# Complexity cheatsheet

A reference for estimating time and space complexity quickly, focused on Python. Use it while
working Step 7 of the [problem-solving framework](problem-solving-framework.md), and revise it
before every interview.

## 1. How to read Big-O

- Big-O describes how the work grows when the input grows, ignoring constant factors and
  small-input behaviour.
- `O(2n + 5)` simplifies to `O(n)`. `O(n² + n)` simplifies to `O(n²)` because the slowest term wins.
- Best / average / worst case are different questions. Interviews normally mean the worst case
  ("what is the complexity of your solution?"), but hashing is stated as **average O(1)** because
  worst case is O(n) per operation.
- Amortised complexity spreads the cost of occasional expensive operations, for example list
  `append` that occasionally reallocates: amortised **O(1)**.

## 2. Growth rates: how bad is it really?

Assuming roughly 10⁷ simple operations per second:

| Complexity | n = 10 | n = 100 | n = 1,000 | n = 10⁶ | Practical meaning |
| --- | --- | --- | --- | --- | --- |
| O(1) | instant | instant | instant | instant | Index lookup, hash lookup |
| O(log n) | 3 steps | 7 | 10 | 20 | Binary search, balanced tree height |
| O(n) | 10 | 100 | 1,000 | 1,000,000 | One pass over the data |
| O(n log n) | 33 | 664 | ~10⁴ | ~2·10⁷ | Sorting; use `sorted()` |
| O(n²) | 100 | 10⁴ | 10⁶ (slow) | too slow | Nested loops over the same list |
| O(n³) | 1,000 | 10⁶ | too slow | — | Triple nested loops |
| O(2ⁿ) | 1,024 | astronomically large | — | — | Subset enumeration |
| O(n!) | 3.6M | impossible | — | — | Permutations |

Rule of thumb: **n up to ~10⁶ needs O(n) or O(n log n). n up to ~5,000 can afford O(n²).**

## 3. Python list (dynamic array)

| Operation | Complexity | Note |
| --- | --- | --- |
| `lst[i]`, `lst[i] = x` | O(1) | Direct index |
| `lst.append(x)` | O(1) amortised | Occasional resize copies elements |
| `lst.pop()` (last) | O(1) | |
| `lst.pop(i)`, `lst.insert(i, x)` | O(n) | Every element after `i` shifts |
| `lst.insert(0, x)` | O(n) | Avoid in loops |
| `x in lst`, `lst.index(x)` | O(n) | Linear scan |
| `len(lst)`, `min`, `max`, `sum` | O(1) for `len`; O(n) for the rest | |
| `lst[a:b]` (slice of length k) | O(k) time, O(k) space | Creates a copy |
| `lst.sort()`, `sorted(lst)` | O(n log n) | Timsort; stable |
| `lst.reverse()`, `reversed(lst)` | O(n) / O(1) space | |
| `lst + lst2`, `lst * k` | O(total length) | Creates a new list |
| `lst.clear()` | O(n) | |

## 4. Strings

Strings are **immutable**: any "change" builds a new string.

| Operation | Complexity | Note |
| --- | --- | --- |
| `s[i]` | O(1) | |
| `len(s)` | O(1) | |
| `s + t` | O(len(s) + len(t)) | In a loop this becomes O(n²) |
| `x in s` | O(len(s)) | Substring search |
| `s.lower()`, `s.upper()`, `s.strip()` | O(len(s)) | New string |
| `s.split(sep)`, `sep.join(parts)` | O(len(s)) | Preferred for building strings |
| `s[a:b]` | O(k) | Copy of k characters |

**Loop rule:** never build a result with `result = result + x` inside a loop. Collect parts in a
list and `"".join(parts)` once.

## 5. dict and set (hash tables)

Average case assumes a good hash function.

| Operation | Average | Worst case |
| --- | --- | --- |
| `d[key]`, `d[key] = value` | O(1) | O(n) |
| `key in d`, `key in s` | O(1) | O(n) |
| `del d[key]` | O(1) | O(n) |
| iterate a dict or set | O(n) | O(n) |
| copy a dict or set | O(n) | O(n) |
| `set` union `s | t` | O(len(s) + len(t)) | — |
| `set` intersection `s & t` | O(min(len(s), len(t))) | O(len(s)·len(t)) |
| `set` difference `s - t` | O(len(s)) | — |

Two consequences used constantly in Week 1:

- Counting with a dict is a single O(n) pass instead of O(n²) nested loops.
- Membership tests in a set turn "have I seen this?" from O(n) into O(1) on average.

## 6. Other containers worth knowing

| Container | Operation | Complexity |
| --- | --- | --- |
| `collections.deque` | `append`, `appendleft`, `pop`, `popleft` | O(1) |
| `collections.deque` | index in the middle | O(n) |
| `collections.Counter` | build from a sequence | O(n) |
| `collections.Counter` | `most_common(k)` | O(n log k) |
| `collections.defaultdict` | like `dict` | O(1) average |
| `heapq` (min-heap on a list) | `heappush`, `heappop` | O(log n) |
| `heapq` | `heapify` | O(n) |
| `bisect` on a sorted list | `bisect_left`/`insort` | O(log n) search, O(n) insert |

## 7. Counting loops correctly

| Code shape | Complexity |
| --- | --- |
| One loop over n | O(n) |
| Two independent loops over n | O(n) (they add) |
| Loop inside a loop, both over n | O(n²) (they multiply) |
| Loop that halves its range each time | O(log n) |
| Loop over n with an inner loop over n/2 | O(n²) still — constants are dropped |
| Loop over n with an inner loop that runs a fixed number of times (e.g. 26 letters) | O(n) |
| Sorting inside a loop | O(n² log n) — a red flag |

Example of dropping constants:

```python
for i in range(n):          # n iterations
    for j in range(100):    # fixed 100 iterations
        pass
# Total work: 100n → O(n), not O(n²)
```

## 8. Space complexity basics

- Count **extra** memory your algorithm allocates; the input itself is not counted.
- A hash map that stores up to n entries is O(n) space.
- Recursion costs O(depth) stack frames; the depth is usually equal to the recursion depth
  (a naive recursive Fibonacci is O(n) depth but O(2ⁿ) time).
- Slicing or copying a list of length n costs O(n) extra space — easy to forget.
- Interviewers often accept trading space for time when the trade is stated: "this is O(n) time
  instead of O(n²), at the cost of O(n) extra space."

## 9. Common mistakes

- Calling `x in list` inside a loop and still claiming O(n) overall.
- Forgetting that `s = s + c` in a loop is quadratic for long strings.
- Assuming dict lookups are worst-case O(1); they are average O(1).
- Counting the input array as extra space.
- Reporting the complexity of the code you wrote instead of the algorithm's worst case (an early
  `return` does not remove the worst case).
- Ignoring the cost of `sorted()` inside a loop.

## 10. Sources and related documents

- Python wiki, Time & Space Complexity of built-in operations:
  <https://wiki.python.org/moin/TimeComplexity> (archived reference; see
  [resources.md](resources.md) for alternatives and versions).
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/) — algorithm and data structure tables.
- [problem-solving-framework.md](problem-solving-framework.md) — where this cheatsheet is used.
- [resources.md](resources.md) — free resources for practising complexity analysis.
