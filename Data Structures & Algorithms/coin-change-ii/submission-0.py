class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        def dfs(i,currSum, cache):

            if i == len(coins) or currSum > amount:
                return 0

            if currSum == amount:
                return 1

            if ((i,currSum)) in cache:
                return cache[(i,currSum)]
            
            cache[(i,currSum)] = dfs(i,currSum+coins[i], cache) + dfs(i+1,currSum,cache)
            return cache[(i,currSum)]
        
        return dfs(0,0,{})
        