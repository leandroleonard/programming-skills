class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        items = {}

        for i in range(len(nums)):
            if nums[i] in items and abs(i - items[nums[i]]) <= k:
                return True
            items[nums[i]] = i
            if i >= k:
                del items[nums[i - k]]
        return False