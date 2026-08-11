import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #assumptions:
            #sum(piles[i] // k + 1) = h
            # need to solve for k

       small = 1
       big = max(piles)
    
       answer = big

       while small <= big:
        k = small + (big-small) // 2
        totalHours = 0

        for pile in piles:
            a = math.ceil(pile/k)
            totalHours += a
        
        if totalHours <= h:
            answer = k 
            big = k-1
        else:
            small = k+1
        
       return answer
        
    



        
            
        