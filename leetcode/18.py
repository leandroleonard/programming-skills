class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        n = len(nums)
        ans = []
        
        for i in range(n - 3):
            j = i + 1
            while j < n - 2:
                left, right = j + 1, n - 1
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        if [nums[i], nums[j], nums[left], nums[right]] not in ans:
                            ans.append([nums[i], nums[j], nums[left], nums[right]])
                            
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
                j += 1
        return ans
    
s = Solution()

print(s.fourSum(nums=[1,0,-1,0,-2,2], target=0))
print(s.fourSum(nums=[2,2,2,2,2], target=8))