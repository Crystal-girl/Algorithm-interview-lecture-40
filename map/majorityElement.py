"""
leetcode 169
Majority Element
"""
from typing import List


def majorityElement(self, nums: List[int]) -> int:
    dic = {}
    for num in nums:
        if num not in dic:
            dic.update({num: 1})
        else:
            dic.update({num: dic[num]+1})
    return max(dic.keys(), key=(lambda x: dic[x]))
