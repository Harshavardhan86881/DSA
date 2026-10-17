import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from has_path import has_path

def test_true():
    graph = {0:[1],1:[2],2:[]}
    assert has_path(graph,0,2) is True

def test_false():
    graph = {0:[1],1:[],2:[]}
    assert has_path(graph,0,2) is False

def test_same():
    assert has_path({0:[]},0,0) is True
