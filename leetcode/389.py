class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in range(len(t)):
            if i == len(s): 
                return sorted(t)[i]
            if sorted(t)[i] not in sorted(s)[i]:
                return sorted(t)[i]