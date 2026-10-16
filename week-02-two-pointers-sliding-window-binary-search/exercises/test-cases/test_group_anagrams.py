import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from group_anagrams import group_anagrams

def test_basic():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted([sorted(g) for g in result]) == sorted([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])

def test_empty_str():
    assert group_anagrams([""]) == [[""]]

def test_single():
    assert group_anagrams(["a"]) == [["a"]]
