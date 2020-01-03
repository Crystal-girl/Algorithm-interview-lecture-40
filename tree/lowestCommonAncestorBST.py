"""
leetcode 235
Lowest Common Ancestor for BST
"""

def lowestCommonAncestorBST(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if p.val > root.val and q.val > root.val:
        return self.lowestCommonAncestorBST(root.right, p, q)
    if p.val < root.val and q.val < root.val:
        return self.lowestCommonAncestorBST(root.left, p, q)
    return root
