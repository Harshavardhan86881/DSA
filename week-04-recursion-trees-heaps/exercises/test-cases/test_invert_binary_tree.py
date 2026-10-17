import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from invert_binary_tree import TreeNode, invert_tree

def to_list(root):
    if root is None: return []
    return [root.val] + to_list(root.left) + to_list(root.right)

def test_basic():
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    inv = invert_tree(root)
    assert to_list(inv) == [4, 7, 9, 6, 2, 3, 1]

def test_empty():
    assert invert_tree(None) is None
