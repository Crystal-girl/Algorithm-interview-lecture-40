"""
leetcode 98
Valid Binary Search Tree
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
solution 1
T: O(N)
S: O(N)
"""
def isValidBST(self, root: TreeNode) -> bool:
    self.prev = None

    def helper(node: TreeNode) -> bool:
        if node is None:
            return True
        if not helper(node.left):
            return False
        if self.prev and self.prev.val >= node.val:
            return False
        self.prev = node
        return helper(node.right)

    return helper(root)


"""
solution 2
T: O(N)
S: O(N)
"""
def isValidBST(self, root: TreeNode) -> bool:

    def helper(node: TreeNode, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
        val = node.val
        if val <= lower or val >= upper:
            return False
        if not helper(node.left, lower, val):
            return False
        if not helper(node.right, val, upper):
            return False
        return True

    return helper(root)