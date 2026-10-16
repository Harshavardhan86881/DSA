"""Tests for find_min_max solution."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from find_min_max import find_min_max


def test_basic():
    assert find_min_max([3, 1, 4, 1, 5]) == (1, 5)


def test_empty():
    assert find_min_max([]) is None


def test_single():
    assert find_min_max([7]) == (7, 7)


def test_negatives():
    assert find_min_max([-3, 0, 2]) == (-3, 2)


def test_all_equal():
    assert find_min_max([4, 4, 4]) == (4, 4)
