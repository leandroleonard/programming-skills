#  - Time complexity: O(N ^ 2)
#  - Space complexity O(1)
 
def bubble(nums):
    size = len(nums)
    for _ in nums:
        isSorted = True
        for i in range(size - 1):
            if nums[i] > nums[i + 1]:
                isSorted = False
                nums[i], nums[i+1] = nums[i+1], nums[i]
        if isSorted:
            return 
                