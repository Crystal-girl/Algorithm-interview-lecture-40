"""
recursion Traversal
T: O(N)
S: O(N)
"""
def inOrder(self, root: 'TreeNode'):
    if root:
        self.inOrder(root.left)
        self.traversal_path.append(root.val)
        self.inOrder(root.right)


"""
non-recursion Traversal
T: O(N)
S: O(N)
"""
def inOrder(self, root: 'TreeNode'):
    stack = []
    while root or stack:
        stack.append(root)
        root = root.left
        while not root and stack:
            root = stack.pop()
            self.traversal_path.append(root.val)
            root = root.right
