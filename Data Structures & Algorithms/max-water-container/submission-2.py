class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_water = 0
        L=0
        R = len(heights) - 1

        while L != R:
            curr_water = (R-L) * min(heights[L],heights[R])

            max_water = max(curr_water,max_water)

            if heights[R] < heights[L]:
                R -= 1
            else:
                L += 1
        
        return(max_water)
