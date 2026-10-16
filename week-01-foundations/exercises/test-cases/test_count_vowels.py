import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from count_vowels import count_vowels

def test_basic():
    assert count_vowels("Hello World") == 3

def test_empty():
    assert count_vowels("") == 0

def test_case():
    assert count_vowels("AEIOUaeiou") == 10

def test_no_vowels():
    assert count_vowels("bcdfg") == 0
