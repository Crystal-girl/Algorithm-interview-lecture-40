"""
leetcode 1
Two Sum
"""
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    dict1 = {}
    for i, item in enumerate(nums):
        if target - item in dict1:
            return [dict1[target - item], i]
        dict1[item] = i
    return []
