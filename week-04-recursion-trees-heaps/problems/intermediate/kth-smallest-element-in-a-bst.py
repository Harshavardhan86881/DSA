"""Solution for 'Kth Smallest Element In A Bst'.
#Kth Smallest Element in a BST. O(n) time, O(h) space."""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root, k):
    result = []

    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)

    inorder(root)
    return result[k - 1]
