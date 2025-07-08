class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left, right = 0, len(needle)
        while right <= len(haystack):
            if haystack[left:right] == needle:
                return left
            left += 1
            right += 1  
        return - 1