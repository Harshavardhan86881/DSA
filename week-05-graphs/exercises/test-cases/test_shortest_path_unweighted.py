import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from shortest_path_unweighted import shortest_path

def test_basic():
    graph = {0:[1,2],1:[3],2:[3],3:[]}
    assert shortest_path(graph,0,3) == 2

def test_same():
    assert shortest_path({0:[]},0,0) == 0

def test_none():
    assert shortest_path({0:[],1:[]},0,1) == -1
