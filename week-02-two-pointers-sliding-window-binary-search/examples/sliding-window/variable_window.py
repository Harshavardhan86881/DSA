"""Variable-size sliding window: longest substring without repeating chars.

Run: python3 variable_window.py
"""


def longest_unique_substring(s: str) -> int:
    seen: set[str] = set()
    left = 0
    best = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        best = max(best, right - left + 1)
    return best


def main() -> None:
    print(longest_unique_substring("abcabcbb"))  # 3
    print(longest_unique_substring("bbbbb"))     # 1
    print(longest_unique_substring(""))          # 0


if __name__ == "__main__":
    main()
