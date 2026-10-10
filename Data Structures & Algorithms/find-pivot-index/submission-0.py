class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = 0
        suffix = sum(nums)
        last = 0

        for i in range(len(nums)):
            suffix = suffix - nums[i]
            prefix += last

            last = nums[i]

            if prefix == suffix:
                return i
        
        return -1