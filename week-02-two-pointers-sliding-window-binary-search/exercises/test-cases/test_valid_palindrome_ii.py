import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from valid_palindrome_ii import valid_palindrome_ii

def test_basic():
    assert valid_palindrome_ii("aba") is True

def test_delete_one():
    assert valid_palindrome_ii("abca") is True

def test_false():
    assert valid_palindrome_ii("abc") is False

def test_empty():
    assert valid_palindrome_ii("") is True
