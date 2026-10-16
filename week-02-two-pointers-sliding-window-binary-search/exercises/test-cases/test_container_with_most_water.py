import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from container_with_most_water import max_area

def test_basic():
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

def test_two():
    assert max_area([1, 1]) == 1

def test_empty():
    assert max_area([]) == 0

def test_increasing():
    assert max_area([1, 2, 3]) == 2
