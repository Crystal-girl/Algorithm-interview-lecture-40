"""
leetcode 225
Queue implementation Stack
"""
import collections

def __init__(self):
    self.stack = collections.deque

def push(self, x):
    self.stack.append(x)
    for _ in range(len(self.stack) - 1):
        self.stack.append(self.stack.popleft())

def pop(self):
    return self.stack.popleft()

def top(self):
    return self.stack[0]

def empty(self):
    return not self.stack
