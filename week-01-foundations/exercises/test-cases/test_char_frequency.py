import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from character_frequency import char_frequency

def test_basic():
    assert char_frequency("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}

def test_empty():
    assert char_frequency("") == {}

def test_single():
    assert char_frequency("a") == {"a": 1}
