class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        res = 0
        i = 0
        while i < len(s):
            if i + 1 != len(s) and symbols.get(s[i + 1]) > symbols.get(s[i]):
                res -= symbols.get(s[i])
            else:
                res += symbols.get(s[i])
            i+=1
        return res