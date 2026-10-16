import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from longest_increasing_subsequence import length_of_lis

def test_basic():
    assert length_of_lis([10,9,2,5,3,7,101,18]) == 4

def test_empty():
    assert length_of_lis([]) == 0

def test_single():
    assert length_of_lis([1]) == 1

def test_decreasing():
    assert length_of_lis([5,4,3,2,1]) == 1

def test_duplicates():
    assert length_of_lis([1,1,1]) == 1

def test_increasing():
    assert length_of_lis([1,2,3,4]) == 4
