class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        arr = s.split(" ")
        
        for i in range(len(arr)):
            if i + 1 == len(arr):
                res += arr[i][::-1]
            else:
                res += arr[i][::-1] + " "
        
        return res