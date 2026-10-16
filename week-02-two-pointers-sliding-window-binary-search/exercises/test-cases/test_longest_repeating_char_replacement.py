import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from longest_repeating_char_replacement import character_replacement

def test_basic():
    assert character_replacement("ABAB", 2) == 4

def test_one():
    assert character_replacement("AABABBA", 1) == 4

def test_empty():
    assert character_replacement("", 2) == 0
