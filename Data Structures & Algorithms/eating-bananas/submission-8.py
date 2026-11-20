class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #binary searching trying different numbers

        #minimum eating rate is 1
        low = 1

        #max eating rate is max of piles
        high = max(piles)

        #store min eating rate
        res = high

        while low < high:

            k = low + (high-low)//2

            eaten = 0

            for i in piles:
                eaten += math.ceil(i/k)

            
            if eaten > h:
                low = k + 1
            
 

            if eaten <= h:
                res = min(res, k)
                high = k
            
        return res


            
        