class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        m = min(len(word1), len(word2))
        
        for i in range(m):
            merged += word1[i]
            merged += word2[i]
            
        merged = merged + word1[m:] + word2[m:]

        return merged
        