import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from valid_parentheses import is_valid

def test_valid():
    assert is_valid("()[]{}") is True

def test_invalid():
    assert is_valid("(]") is False

def test_empty():
    assert is_valid("") is True

def test_nested():
    assert is_valid("{[()]}") is True
