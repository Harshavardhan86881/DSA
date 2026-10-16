"""Solution for 'Valid Palindrome II'. O(n) time, O(1) space."""


def valid_palindrome_ii(s: str) -> bool:
    def is_pal(l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_pal(left + 1, right) or is_pal(left, right - 1)
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print(valid_palindrome_ii("aba"))  # True
