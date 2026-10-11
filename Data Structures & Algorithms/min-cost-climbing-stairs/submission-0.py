class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def dfs(i,cache):

            if i >= len(cost):
                return 0
            
            if i in cache:
                return cache[i]
            
            cache[i] = min(cost[i]+dfs(i+2,cache), cost[i]+dfs(i+1,cache))
            return cache[i]
        
        return min(dfs(0,{}),dfs(1,{}))

        