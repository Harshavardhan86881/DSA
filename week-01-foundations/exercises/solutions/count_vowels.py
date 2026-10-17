"""Solution: count vowels. O(n) time, O(1) space."""


def count_vowels(s: str) -> int:
    vowels = set("aeiouAEIOU")
    total = 0
    for ch in s:
        if ch in vowels:
            total += 1
    return total


if __name__ == "__main__":
    print(count_vowels("Hello World"))  # 3
