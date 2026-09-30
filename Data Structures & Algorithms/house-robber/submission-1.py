class Solution:
    def rob(self, nums: List[int]) -> int:

        #for each one the question is rob or skip

        #gonna iterate through, calling it dfs starting at 0
        def dfs(i,cache):

            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = max(nums[i] + dfs(i+2,cache),dfs(i+1,cache))
            return cache[i]
            
        return dfs(0,{})
  
        