class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        #lower bound
        lower = math.ceil(sum(piles)/h)
        print(lower)

        #upper bound for speed
        upper = max(piles)
        print(upper)
        
        #binary search by trying middle. If succeeds, upper is reduced, if fails lower is increased
        res = upper
        while lower < upper:

            center = lower + (upper-lower)//2
            print(center)
            total = 0

            for i in piles:
                total += math.ceil(i/center)
            
            #total time is greater, means, too slow, so increase rate
            if total > h:
                lower = center + 1
            
            if total <= h:
                res = min(res,center)
                upper = center
        
        return res

        