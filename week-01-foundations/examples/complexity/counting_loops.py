"""Match each snippet to its complexity class by counting loops.

Run: python3 counting_loops.py
"""


def snippet_a(n: int) -> int:
    # One loop over n -> O(n)
    total = 0
    for i in range(n):
        total += i
    return total


def snippet_b(n: int) -> int:
    # Loop inside a loop, both over n -> O(n^2)
    total = 0
    for i in range(n):
        for j in range(n):
            total += 1
    return total


def snippet_c(n: int) -> int:
    # Halving range each time -> O(log n)
    steps = 0
    size = n
    while size > 1:
        size //= 2
        steps += 1
    return steps


def snippet_d(n: int) -> int:
    # Outer loop over n, inner loop fixed 26 -> O(n)
    total = 0
    for i in range(n):
        for _ in range(26):
            total += 1
    return total


def main() -> None:
    n = 1000
    print("a (O(n))      :", snippet_a(n))
    print("b (O(n^2))    :", snippet_b(100))
    print("c (O(log n))  :", snippet_c(n))
    print("d (O(n))      :", snippet_d(n))


if __name__ == "__main__":
    main()
