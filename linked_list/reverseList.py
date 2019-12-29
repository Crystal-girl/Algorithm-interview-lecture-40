"""
leetcode 206
reverse List
"""

class ListNode:
    def __int__(self, x):
        self.val = x
        self.next = None

def reverseList(self, head: ListNode) -> ListNode:
    cur, prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev
