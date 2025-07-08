class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        result = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            left, right = i + 1, n - 1 
            while left < right:                
                total = nums[i] + nums[left] + nums[right]
                
                if total == target:
                    return total
                
                if min(abs(target - total), abs(target - result)) == abs(target - total):
                    result = total
                    
                if total < target:
                    left += 1
                else:
                    right -= 1
        
        return result
    
a = [-1,2,1,-4]
b = [0, 0, 0]
c = [1,1,1,0]
d = [4,0,5,-5,3,3,0,-4,-5]


s = Solution()

print(s.threeSumClosest(a, 1))
print(s.threeSumClosest(b, 0))
print(s.threeSumClosest(c, 100))
print(s.threeSumClosest(d, -2))
        
        