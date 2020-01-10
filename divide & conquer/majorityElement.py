"""
leetcode 169
Majority Element
"""
from typing import List


def majorityElement(self, nums: List[int]) -> int:
    def helper(low, high):
        if low == high:
            return nums[low]
        mid = (high - low) // 2 + low
        left = helper(low, mid)
        right = helper(mid+1, high)
        if left == right:
            return left
        left_count = sum(1 for i in range(low, high+1) if nums[i] == left)
        right_count = sum(1 for i in range(low, high+1) if nums[i] == right)
        return left if left_count > right_count else right
    return helper(0, len(nums)-1)