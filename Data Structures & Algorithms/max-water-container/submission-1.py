class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i = 0
        maxArea = 0
        for j in range(len(heights)-1,-1,-1):

            while heights[i] < heights[j]:
                maxArea = max((j-i) * min(heights[j],heights[i]),maxArea)
                i += 1

            maxArea = max((j-i) * min(heights[j],heights[i]),maxArea)

        return maxArea
        