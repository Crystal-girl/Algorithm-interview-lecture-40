"""
leetcode 232
Stack implementation Queue
"""

def __init__(self):
    self.instack = []
    self.outstack = []

def push(self, x):
    self.instack.append(x)

def pop(self):
    if not self.outstack:
        while self.instack:
            self.outstack.append(self.instack.pop())
    return self.outstack.pop()

def peek(self):
    if not self.outstack:
        while self.instack:
            self.outstack.append(self.instack.pop())
    return self.outstack[-1]

def empty(self):
    if not self.instack and not self.outstack:
        return True
    return False
