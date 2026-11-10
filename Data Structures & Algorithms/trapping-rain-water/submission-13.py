class Solution:
    def trap(self, height: List[int]) -> int:

        #brute force would be to find the wall heights for each item every time, which would be O(n^2). However we can precalculate the wall heights


        #this is for the max height on the left side
        left_max = [0] * len(height)
        left_max[0] = height[0]

        for i in range(len(left_max)-1):
            left_max[i+1] = max(left_max[i],height[i+1])

        #this is for the max height on the right side (iterating down)

        right_max = [0] * len(height)
        right_max[-1] = height[-1]

        for i in range(len(left_max)-1,0,-1):
            right_max[i-1] = max(right_max[i], height[i-1])
        
        #now to calculate total, simply go through each and add the min of each side - height at that place

        total = 0

        for i in range(len(height)):
            total += min(left_max[i],right_max[i]) - height[i]
        
        return total

        