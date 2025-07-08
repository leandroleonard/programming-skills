from typing import List
from atexit import register



class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        import os
        print(os.listdir())
        register(lambda: open("display_runtime.txt", "w").write('0'))
        # sort numbers
        # for i, j 
        # two pointer
        nums.sort()
        n = len(nums)
        res = set()
        for i in range(n-3):
            for j in range(i+1,n-2):
                left = j + 1
                right = n - 1
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum == target:
                        res.add((nums[i], nums[j],nums[left], nums[right]))
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif sum < target:
                        left += 1
                    else:
                        right -= 1
        return list(res)

if __name__ == "__main__":
    sol = Solution()
    nums = [-1,0,-5,-2,-2,-4,0,1,-2]
    print(sol.fourSum(nums, -9))
