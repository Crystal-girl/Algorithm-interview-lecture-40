"""
leetcode 141
linked list has Cycle
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(self, head: ListNode) -> bool:
    fast = slow = head
    while fast and slow and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
