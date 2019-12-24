"""
leetcode 24
Swap Nodes in Pairs
"""

def swap_pairs(self, head):
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
    return self.next
