class Solution:
    def rob(self, nums: List[int]) -> int:

        #gonna try bottom up approach
        #dp is max money possible ending at index i

        dp = [0] * len(nums)


        for i in range(len(nums)):

            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(nums[i],dp[i-1])
            else:
            
                dp[i] = max(nums[i]+dp[i-2],dp[i-1])
        
        return dp[len(nums)-1]
        