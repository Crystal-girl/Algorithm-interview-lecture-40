"""
recursion Traversal
T: O(N)
S: O(N)
"""
def postOrder(self, root: 'TreeNode'):
    if root:
        self.postOrder(root.left)
        self.postOrder(root.right)
        self.traversal_path(root.val)


"""
non-recursion Traversal
T: O(N)
S: O(N)
"""
def postOrder(root: 'TreeNode'):
    stack = []
    traversal_path = []
    stack.append(root)
    while stack:
        root = stack.pop()
        traversal_path.append(root.val)
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)
    return traversal_path[::-1]

