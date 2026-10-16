"""Tests for second_largest solution."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from second_largest import second_largest


def test_basic():
    assert second_largest([3, 1, 4, 4, 2]) == 3


def test_all_equal():
    assert second_largest([5, 5, 5]) is None


def test_empty():
    assert second_largest([]) is None


def test_single():
    assert second_largest([9]) is None


def test_negatives():
    assert second_largest([-1, -3, -2]) == -2


def test_two_distinct():
    assert second_largest([1, 2]) == 1
