"""
leetcode 15
Three Sum
"""
from typing import List

"""
simple solution
T: O(N^3)
S: O(1)
result: time out
"""
def threeSum(self, nums: List[int]) -> List[List[int]]:
    if not nums:
        return []
    res = []
    for i in range(len(nums) - 2):
        for j in range(i, len(nums) - 1):
            for k in range(j, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0 and sorted(nums[i], nums[j], nums[k]) not in res:
                    res.append(sorted(nums[i], nums[j], nums[k]))
    return res


"""
better solution
T: O(N^2)
S: O(N)
"""
def threeSum(self, nums: List[int]) -> List[List[int]]:
    if not nums or len(nums) < 3:
        return []
    res = set()
    nums.sort()
    for i, a in enumerate(nums[:-2]):
        if i >= 1 and a == nums[i-1]:
            continue
        s = set()
        for b in nums[i+1:]:
            if b not in s:
                s.add(-a-b)
            else:
                res.add((a, -a-b, b))
    return map(list, res)


"""
better better solution
T: O(N^2)
S: O(1)
"""
def threeSum(self, nums: List[int]) -> List[List[int]]:
    if not nums and len(nums) < 3:
        return []
    nums.sort()
    res = []
    for i, a in enumerate(nums[:-2]):
        if i >= 1 and a == nums[i-1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l+1] == nums[l]:
                    l += 1
                while l < r and nums[r-1] == nums[r]:
                    r -= 1
                l += 1
                r -= 1
    return map(list, res)
