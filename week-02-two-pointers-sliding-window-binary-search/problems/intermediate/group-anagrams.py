"""Solution for 'Group Anagrams'. O(n k log k) time, O(n k) space."""


def group_anagrams(words: list[str]) -> list[list[str]]:
    from collections import defaultdict
    groups: dict[str, list[str]] = defaultdict(list)
    for w in words:
        key = "".join(sorted(w))
        groups[key].append(w)
    return list(groups.values())


if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
