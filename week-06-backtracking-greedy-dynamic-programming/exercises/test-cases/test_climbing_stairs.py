import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from climbing_stairs import climb_stairs

def test_basic():
    assert climb_stairs(5) == 8

def test_small():
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2

def test_zero():
    assert climb_stairs(0) == 1

def test_larger():
    assert climb_stairs(10) == 89
