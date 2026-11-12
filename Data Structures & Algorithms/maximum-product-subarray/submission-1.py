class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # any i can either continue the subarray or start a new one.
        # track both the max and min product ending at i, because a
        # negative number turns the smallest product into the largest.

        dp = [0] * len(nums)   # max product ending at i
        mn = [0] * len(nums)   # min product ending at i
        dp[0] = mn[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] * dp[i-1], nums[i] * mn[i-1])
            mn[i] = min(nums[i], nums[i] * dp[i-1], nums[i] * mn[i-1])

        return max(dp)