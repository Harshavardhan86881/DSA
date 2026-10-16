import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from max_depth_binary_tree import TreeNode, max_depth

def test_basic():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(root) == 3

def test_empty():
    assert max_depth(None) == 0

def test_single():
    assert max_depth(TreeNode(1)) == 1
