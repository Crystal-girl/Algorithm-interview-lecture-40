"""
leetcode 24
Swap Nodes in Pairs
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(self, head: ListNode) -> ListNode:
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
    return self.next
