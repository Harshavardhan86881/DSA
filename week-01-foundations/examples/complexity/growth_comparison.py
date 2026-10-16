"""Compare growth rates by counting operations for increasing n.

Run: python3 growth_comparison.py
"""

import time


def work_constant(n: int) -> int:
    return n * 0 + 1  # O(1)


def work_linear(n: int) -> int:
    total = 0
    for i in range(n):
        total += i
    return total  # O(n)


def work_quadratic(n: int) -> int:
    total = 0
    for i in range(n):
        for j in range(n):
            total += 1
    return total  # O(n^2)


def main() -> None:
    for n in (10, 100, 1000):
        t0 = time.perf_counter()
        work_constant(n)
        c = time.perf_counter() - t0
        t0 = time.perf_counter()
        work_linear(n)
        lin = time.perf_counter() - t0
        t0 = time.perf_counter()
        work_quadratic(n)
        quad = time.perf_counter() - t0
        print(f"n={n:>5}  constant={c:.6f}s  linear={lin:.6f}s  quadratic={quad:.6f}s")


if __name__ == "__main__":
    main()
