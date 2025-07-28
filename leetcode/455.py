from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        i, j, counter = 0, 0, 0
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i+=1
                j+=1
                counter +=1
            else:
                j += 1
                
        return counter
    
print(Solution().findContentChildren([1, 2], [1, 2, 3]))