"""Tests for running_sum solution."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from running_sum import running_sum


def test_basic():
    assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]


def test_empty():
    assert running_sum([]) == []


def test_single():
    assert running_sum([5]) == [5]


def test_negatives():
    assert running_sum([-1, 2, -3]) == [-1, 1, -2]
