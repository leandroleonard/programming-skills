from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        res = []

        for i in nums2:
            if counts[i] > 0:
                res.append(i)
                counts[i] -= 1
        return res
        
        
        
s = Solution()         
print(s.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
print(s.intersect(nums1=[4,9,5], nums2=[9,4,9,8,4]))
print(s.intersect(nums1=[3,1,2], nums2=[1,1]))
        