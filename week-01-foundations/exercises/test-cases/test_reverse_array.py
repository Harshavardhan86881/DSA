"""Tests for reverse_array solution."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from reverse_array import reverse_in_place


def test_basic():
    data = [1, 2, 3, 4, 5]
    reverse_in_place(data)
    assert data == [5, 4, 3, 2, 1]


def test_empty():
    data: list[int] = []
    reverse_in_place(data)
    assert data == []


def test_single():
    data = [7]
    reverse_in_place(data)
    assert data == [7]


def test_duplicates():
    data = [2, 2, 2]
    reverse_in_place(data)
    assert data == [2, 2, 2]


def test_negatives():
    data = [-3, 0, 2]
    reverse_in_place(data)
    assert data == [2, 0, -3]
