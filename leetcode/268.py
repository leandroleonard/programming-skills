from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            if nums[0] == 0:
                return 1
            else:
                return nums[0] - 1
        
        expectedSum = ((n + 1) * n) // 2
        
        return expectedSum - sum(nums)