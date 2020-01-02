"""
leetcode 18
Four Sum
"""
from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    if not nums or len(nums) < 4:
        return []
    nums.sort()
    res = set()
    for i in range(len(nums)-3):
        if i >= 1 and nums[i] == nums[i-1]:
            continue
        if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
            break
        if nums[i] + nums[len(nums)-3] + nums[len(nums)-2] + nums[len(nums)-1] < target:
            continue
        for j in range(i+1, len(nums)-2):
            if j-1 > i and nums[j] == nums[j-1]:
                continue
            if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                break
            if nums[i] + nums[j] + nums[len(nums)-2] + nums[len(nums)-1] < target:
                continue
            s = set()
            for k in range(j+1, len(nums)):
                if nums[k] not in s:
                    s.add(target-nums[i]-nums[j]-nums[k])
                else:
                    res.add((nums[i], nums[j], nums[k], target-nums[i]-nums[j]-nums[k]))
    return map(list, res)
