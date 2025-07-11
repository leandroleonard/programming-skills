from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        m = min(len(nums1), len(nums2))
        
        if m == len(nums1):
            for i in nums1:
                if i in nums2:
                    res.add(i)
        else:
            for i in nums2:
                if i in nums1:
                    res.add(i)
        return list(res)
                
s = Solution()         
print(s.intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]))
print(s.intersection(nums1=[4,9,5], nums2=[9,4,9,8,4]))
        