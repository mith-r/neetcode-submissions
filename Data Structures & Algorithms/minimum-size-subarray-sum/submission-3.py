class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        L = 0
        size = 0
        result = float('inf')

        for R in range(len(nums)):
            size += nums[R]
        
            while size >= target:
                
                result = min(R-L+1,result)
                size -= nums[L]
                L += 1
                
                
        
        return result if result != float('inf') else 0
