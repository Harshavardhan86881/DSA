import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from find_peak_element import find_peak_element

def test_basic():
    idx = find_peak_element([1, 2, 3, 1])
    assert idx == 2

def test_single():
    assert find_peak_element([1]) == 0

def test_two():
    idx = find_peak_element([1, 2])
    assert idx in (0, 1)
