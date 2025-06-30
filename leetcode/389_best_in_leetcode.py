class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x=s+t
        res=ord(x[0])
        for i in range(1,len(x)):
            res^=ord(x[i])
        return chr(res)