from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
       return [self.findLeft(nums, target, len(nums)), self.findRight(nums, target, len(nums))]
   
    def findLeft(self, nums: List[int], target: int, n) -> int:
        left, right = 0, n-1
        res = -1 
        
        while left <= right:
            m = (left + right) // 2
            if nums[m] < target:
                left = m + 1
            else:
                if target == nums[m]:
                    res = m
                right = m - 1
            
        return res
   
    def findRight(self, nums: List[int], target: int, n) -> int:
        left, right = 0, n-1
        res = -1 
        
        while left <= right:
            m = (left + right) // 2
            if nums[m] > target:
                right = m - 1
            else:
                if target == nums[m]:
                    res = m
                left = m + 1
            
        return res
    
print(Solution().searchRange([5, 7, 8, 8, 10], 7))
                
                
                
            