import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from valid_palindrome import is_valid_palindrome

def test_basic():
    assert is_valid_palindrome("A man, a plan, a canal: Panama") is True

def test_not_palindrome():
    assert is_valid_palindrome("race a car") is False

def test_empty():
    assert is_valid_palindrome("") is True

def test_single():
    assert is_valid_palindrome("a") is True

def test_mixed_case():
    assert is_valid_palindrome("RaceCar") is True
