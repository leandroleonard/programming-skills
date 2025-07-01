class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0

        while l < r:
            m = min(height[l], height[r])
            ans = max(ans, (m*(r-l)))
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        return ans