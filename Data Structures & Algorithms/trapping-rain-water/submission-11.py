class Solution:
    def trap(self, height: List[int]) -> int:

        L = 0
        total_water = 0
        blocks = 0

        for R in range(len(height)):

            if height[R] >= height[L]:
                total_water += (max(R-L-1,0) * height[L]) - blocks
                
                blocks = 0
                L = R
            else:
                blocks += height[R]
        
        R = len(height) - 1
        blocks = 0

        limit = L

        for L in range(len(height)-1,limit-1,-1):
            print(L)

            if height[L] >= height[R]:
                total_water += (max(R-L-1,0) * height[R]) - blocks
                print(f"height of {L} is greater than height of {R}")
                blocks = 0
                R = L
            else:
                blocks += height[L]


        
        return total_water






        