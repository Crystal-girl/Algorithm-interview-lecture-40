"""
leetcode 242
Valid Anagram
"""

"""
solution1: hashMap
"""
def isAnagram(self, s: str, t: str) -> bool:
    dic1, dic2 = {}, {}
    for item in s:
        dic1[item] = dic1.get(item) + 1
    for item in t:
        dic2[item] = dic2.get(item) + 1
    return dic1 == dic2


"""
solution2: hashTable
"""
def isAnagram(self, s: str, t: str) -> bool:
    tab1, tab2 = [0] * 26, [0] * 26
    for item in s:
        tab1[ord(item) - ord('a')] += 1
    for item in t:
        tab2[ord(item) - ord('a')] += 1
    return tab1 == tab2
