import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from kth_smallest_in_bst import TreeNode, kth_smallest

def test_basic():
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    assert kth_smallest(root, 1) == 1
    assert kth_smallest(root, 3) == 3

def test_single():
    assert kth_smallest(TreeNode(1), 1) == 1
