"""
leetcode 1
Two Sum
"""
from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    set1 = set()
    for i, item in enumerate(nums):
        if target - item in set1:
            return [nums.index(target - item), i]
        set1.add(item)
    return []
