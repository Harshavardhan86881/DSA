"""Solution: Character Frequency. O(n) time, O(k) space."""


def char_frequency(s: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    return counts


if __name__ == "__main__":
    print(char_frequency("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
