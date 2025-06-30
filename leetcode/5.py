class Solution:
    def longestPalindrome(self, s: str) -> str:
        l, r = 0, 1
        res = ""
        
        while l <= len(s):
            if s[l:r][::-1] == s[l:r] and len(s[l:r]) > len(res):
                res = s[l:r]
                l = 0
                r = len(res) + 1
                continue
            r += 1
            if r > len(s):
                l += 1
                r = l + len(res)           
        return res