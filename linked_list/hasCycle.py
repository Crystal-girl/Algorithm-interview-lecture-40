"""
leetcode 141
linked list has Cycle
"""

def has_cycle(self, head):
    fast = slow = head
    while fast and slow and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
