"""
leetcode 169
Majority Element
"""
from typing import List

"""
    使用 摩尔(Boyer-Moore)投票法
T: O(N)
S: O(1)
"""
def majorityElement(self, nums: List[int]) -> int:
    cur_num = 0
    count = 0
    for num in nums:
        if count == 0:
            cur_num = num
            count += 1
        else:
            if cur_num == num:
                count += 1
            else:
                count -= 1
    if count > 0:
        return cur_num
