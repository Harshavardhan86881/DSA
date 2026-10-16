"""Solution: Valid Anagram. O(n) time, O(k) space."""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts: dict[str, int] = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in t:
        if counts.get(ch, 0) == 0:
            return False
        counts[ch] -= 1
    return True


if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))  # True
