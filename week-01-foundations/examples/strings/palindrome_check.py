"""Palindrome checks: naive and two-pointer.

Run: python3 palindrome_check.py
"""


def is_palindrome_naive(s: str) -> bool:
    # O(n) time, O(n) space: builds a reversed copy.
    return s == s[::-1]


def is_palindrome_two_pointers(s: str) -> bool:
    # O(n) time, O(1) space.
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def main() -> None:
    for word in ("racecar", "hello", "", "a", "abba"):
        print(word, is_palindrome_naive(word), is_palindrome_two_pointers(word))


if __name__ == "__main__":
    main()
