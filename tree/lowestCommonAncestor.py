"""
leetcode 236
Lowest Common Ancestor
"""
from typing import List


#  requirements: not parent pointer
"""
solution 1
T: O(N)
S: O(N)
"""
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def findPath(node: 'TreeNode', findnode: 'TreeNode') -> List['TreeNode']:
        path = []
        prev = None
        while node or path:
            while node:
                path.append(node)
                if node == findnode:
                    return path
                node = node.left
            if path:
                node = path[-1]
                while not node.right or (prev and node.right == prev):
                    prev = path.pop()
                    node = path[-1]
                node = node.right
        return []

    path1 = findPath(root, p)
    path2 = findPath(root, q)
    lowestcommonnode = None
    minlen = min(len(path1), len(path2))
    for i in range(minlen):
        if path1[i] == path2[i]:
            lowestcommonnode = path1[i]
        else:
            break
    return lowestcommonnode


"""
solution 2
T: O(N)
S: O(N)
"""
# Three static flags to keep track of post-order traversal.

# Both left and right traversal pending for a node.
# Indicates the nodes children are yet to be traversed.
BOTH_PENDING = 2
# Left traversal done.
LEFT_DONE = 1
# Both left and right traversal done for a node.
# Indicates the node can be popped off the stack.
BOTH_DONE = 0
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    stack = [(root, BOTH_PENDING)]
    one_node_found = False
    lca_index = -1
    while stack:
        parent_node, flag = stack[-1]
        if flag != BOTH_DONE:
            if flag == BOTH_PENDING:
                if parent_node == p or parent_node == q:
                    if one_node_found:
                        return stack[lca_index][0]
                    else:
                        one_node_found = True
                        lca_index = len(stack) - 1
                child_node = parent_node.left
            else:
                child_node = parent_node.right
            stack.pop()
            stack.append((parent_node, flag-1))
            if child_node:
                stack.append((child_node, BOTH_PENDING))
        else:
            if one_node_found and lca_index == len(stack) - 1:
                lca_index -= 1
            stack.pop()
    return None


"""
solution 3
T: O(N)
S: O(N)
"""
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root == p or root == q:
        return root
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    if not left:
        return right
    if not right:
        return left
    return root


# requirements: has parent pointer
"""
T: O(N)
S: O(N)
"""
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    stack = [root]
    parent = {root: None}
    while p not in parent or q not in parent:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
            parent[node.left] = node
        if node.right:
            stack.append(node.right)
            parent[node.right] = node
    common_ancestor = set()
    while p:
        common_ancestor.add(p)
        p = parent[p]
    while q not in common_ancestor:
        q = parent[q]
    return q
