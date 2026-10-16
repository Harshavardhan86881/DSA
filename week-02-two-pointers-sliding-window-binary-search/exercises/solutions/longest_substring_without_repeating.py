"""Solution: Longest Substring Without Repeating Characters. O(n) time, O(k) space."""


def longest_unique_substring(s: str) -> int:
    seen: set[str] = set()
    left = 0
    best = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        if right - left + 1 > best:
            best = right - left + 1
    return best


if __name__ == "__main__":
    print(longest_unique_substring("abcabcbb"))  # 3
