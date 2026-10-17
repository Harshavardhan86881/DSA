"""Solution: Longest Repeating Character Replacement. O(n) time, O(1) space (26 letters)."""


def character_replacement(s: str, k: int) -> int:
    counts: dict[str, int] = {}
    left = 0
    best = 0
    max_count = 0
    for right in range(len(s)):
        counts[s[right]] = counts.get(s[right], 0) + 1
        if counts[s[right]] > max_count:
            max_count = counts[s[right]]
        while (right - left + 1) - max_count > k:
            counts[s[left]] -= 1
            left += 1
        if right - left + 1 > best:
            best = right - left + 1
    return best


if __name__ == "__main__":
    print(character_replacement("ABAB", 2))  # 4
