"""Runnable example: check balanced brackets with a stack."""


def is_valid(s: str) -> bool:
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack


if __name__ == "__main__":
    for s in ["()", "()[]{}", "(]", "([)]", "{[]}"]:
        print(s, "->", is_valid(s))
