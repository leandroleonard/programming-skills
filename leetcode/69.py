class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        
        left, right = 1, x // 2
        
        while left <= right:
            middle = (left + right) // 2
            
            if middle * middle == x:
                return middle
            
            if middle * middle > x:
                right = middle - 1
            if middle * middle < x:
                left = middle + 1
            
        return right

s = Solution()
print(s.mySqrt(2147395599))
