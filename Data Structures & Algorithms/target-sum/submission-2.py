class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def dfs(i,currSum,cache):
        
            if i == len(nums):

                if currSum == target:

                    return 1
            
                return 0
            
            if ((i,currSum)) in cache:
                return cache[(i,currSum)]
            
            cache[(i,currSum)] = dfs(i+1,currSum+nums[i], cache) + dfs(i+1,currSum-nums[i], cache)
            return cache[(i,currSum)]
        
        return dfs(0,0,{})


        