class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        def dfs(i,currSum, cache):

            if i == len(coins) or currSum > amount:
                return float('inf')
            
            if currSum == amount:
                return 0
            
            
            if ((i,currSum)) in cache:
                return cache[(i,currSum)]
            
            cache[(i,currSum)] = min(1+dfs(i,currSum+coins[i], cache),dfs(i+1,currSum, cache))

            return cache[(i,currSum)]

        res = dfs(0,0,{})
        return res if res != float('inf') else -1


            
            


        