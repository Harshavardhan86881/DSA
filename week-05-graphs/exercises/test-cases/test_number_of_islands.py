import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from number_of_islands import num_islands

def test_basic():
    grid = [["1","1","0"],["1","0","0"],["0","0","1"]]
    assert num_islands(grid) == 2

def test_empty():
    assert num_islands([]) == 0

def test_all_water():
    assert num_islands([["0","0"],["0","0"]]) == 0
