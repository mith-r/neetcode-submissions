class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        cache = {}
        def dfs(i):

            if i == len(nums):
                return
            
            if i in cache:
                return cache[i]

            LIS = 1

            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + dfs(j))

            cache[i] = LIS
            return LIS
        
        return max(dfs(i) for i in range(len(nums)))
            