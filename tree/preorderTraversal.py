"""
recursion Traversal
T: O(N)
S: O(N)
"""
def preOrder(self, root: 'TreeNode'):
    if root:
        self.traversal_path.append(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)


"""
non-recursion Traversal
T: O(N)
S: O(N)
"""
def preOrder(self, root: 'TreeNode'):
    stack = []
    while root or stack:
        stack.append(root)
        self.traversal_path.append(root.val)
        root = root.left
        while not root and stack:
            root = stack.pop()
            root = root.right

