from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                return True
        return False