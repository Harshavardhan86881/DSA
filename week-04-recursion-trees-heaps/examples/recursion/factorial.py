"""Runnable example: recursion basics."""


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    print("factorial(5) =", factorial(5))
    print("fibonacci(10) =", fibonacci(10))
