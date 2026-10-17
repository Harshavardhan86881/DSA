import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from valid_anagram import is_anagram

def test_basic():
    assert is_anagram("anagram", "nagaram") is True

def test_not_anagram():
    assert is_anagram("rat", "car") is False

def test_empty():
    assert is_anagram("", "") is True

def test_different_lengths():
    assert is_anagram("a", "ab") is False

def test_repeats():
    assert is_anagram("aabb", "bbaa") is True
