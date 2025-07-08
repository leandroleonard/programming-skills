from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

                
s = Solution()

print(s.searchInsert([1,3,5,6], 5)) # 2
print(s.searchInsert([1,3,5,6], 2)) # 1
print(s.searchInsert([1,3,5,6], 7)) # 4
print(s.searchInsert([1,3,5,6], 0)) # 0