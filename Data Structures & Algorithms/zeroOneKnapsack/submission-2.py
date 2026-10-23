class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        n = len(profit)
        v = [[0 for i in range(capacity + 1)] for i in range(n + 1)]

        for item in range(n):
            for c in range(1,capacity+1,1):
                v[item+1][c] = max(v[item][c]
                ,(profit[item] + v[item][c-weight[item]]) if weight[item] <= c else 0)

        
        return v[n][capacity]
