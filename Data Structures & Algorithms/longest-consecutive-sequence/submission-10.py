class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(nums)
        if len(nums) == 0:
            return 0
        
        long = 1
        curr = 1
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                continue
            
            if nums[i+1] == nums[i] + 1:
                curr += 1
            else:
                if long < curr:
                    long = curr
                curr = 1
        
        return max(long,curr)

        