class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        
        for idx, ch in enumerate(s):
            if not counter.get(ch):
                counter[ch] = [idx, 1]
            else:
                counter[ch][1] += 1
        
        for ch, val in counter.items():
            if val[1] == 1:
                return val[0]
            
        return -1
            
        
            

S = Solution()
print(S.firstUniqChar('leetcode'))
