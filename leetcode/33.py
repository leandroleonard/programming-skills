from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # find the minimum index, it will split the array in 2 parts
        left, right = 0, n - 1
        
        while left < right:
            middle = (left + right) // 2
            if nums[middle]  > nums[right]:
                left = middle + 1
            else:
                right = middle
        
        m = left
                
        if m == 0:
            left, right = 0, n - 1
        elif target >= nums[0] and target <= nums[m - 1]: 
            left, right = 0, m - 1
        else:
            left, right = m, n - 1
            
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
                
        
        return -1
    
s = Solution()
# print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
# print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
# print(s.search([1], 0))
print(s.search([3, 1], 3))