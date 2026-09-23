class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        L = 0
        total = 0
        length = float('inf')

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                total -= nums[L]
                length = min(R-L+1,length)
                L += 1
                
            
        return 0 if length == float('inf') else length
        