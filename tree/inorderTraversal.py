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


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


if __name__ == '__main__':
    a, b, c, d, e, f, g = [TreeNode(x) for x in [1, 2, 3, 4, 5, 6, 7]]
    a.left, a.right = b, c
    b.left, b.right = d, e
    c.left, c.right = f, g
    path = inOrder(a)
    for i in path:
        print(i)