class Solution:
    def sortColors(self, nums: List[int]) -> None:
        buckets = {0:0,1:0,2:0}

        for i in nums:
            buckets[i] = buckets[i] + 1

        i = 0

        for key,value in buckets.items():
            for item in range(value):
                nums[i] = key
                i += 1

        return nums
        



        """
        Do not return anything, modify nums in-place instead.
        """
        