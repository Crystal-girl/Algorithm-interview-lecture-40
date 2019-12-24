"""
leetcode 206
reverse List
"""

def reverse_list(self, head):
    cur, prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev
