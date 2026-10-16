import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from longest_substring_without_repeating import longest_unique_substring

def test_basic():
    assert longest_unique_substring("abcabcbb") == 3

def test_all_same():
    assert longest_unique_substring("bbbbb") == 1

def test_empty():
    assert longest_unique_substring("") == 0

def test_all_distinct():
    assert longest_unique_substring("abcd") == 4
