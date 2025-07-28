from typing import List
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = {}
        for word in strs:
            c = tuple(sorted(Counter(word).items()))
            if c not in counter:
                counter[c] = [word]
            else:
                counter[c].append(word)
        return list(counter.values())
    
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))