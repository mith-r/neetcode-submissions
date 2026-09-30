class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #the maximum profit we have had so far
        maxP = 0

        #the day we buy
        buy = prices[0]

        #iterating through sell days
        for sell in prices:
            print(sell)
            if sell < buy:
                print(f"Sell is less, so buy at {sell} instead of {buy}")
                buy = sell

            if sell-buy > maxP:
                print(f"New maxP of {sell-buy}, with sell at {sell} and buy at {buy}")
                maxP = sell-buy

        return maxP