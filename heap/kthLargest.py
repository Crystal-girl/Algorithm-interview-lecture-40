"""
leetcode 703
Kth Largest Element in a Stream
"""

import heapq

def __init__(self, k, nums):
    self.heap = nums
    self.k = k
    heapq.heapify(self.heap)
    while len(self.heap) > k:
        heapq.heappop(self.heap)

def add(self, val):
    if len(self.heap) < self.k:
        heapq.heappush(self.heap, val)
    elif val > self.heap[0]:
        heapq.heappushpop(self.heap, val)
    return self.heap[0]
