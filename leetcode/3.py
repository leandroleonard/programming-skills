class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        res = 1
        counts = {}
        counts[s[0]] = 1
        l, r = 0, 0
        while r < len(s) - 1:
            r += 1
            if not counts.get(s[r]):
                counts[s[r]] = 1
                res = max(res, (r - l) + 1)
            else:
                while s[l] != s[r]:
                    counts[s[l]] -= 1
                    l+=1
                l += 1
        return res
    
s = Solution()

print(s.lengthOfLongestSubstring('abcabcbb'))
print(s.lengthOfLongestSubstring('bbbbb'))
print(s.lengthOfLongestSubstring('pwwkew'))
print(s.lengthOfLongestSubstring('tmmzuxt'))