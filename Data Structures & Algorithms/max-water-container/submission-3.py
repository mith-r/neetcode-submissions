class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #brute force would be O(n^2), because we would have to compare each height with all other heights

        #however, we know we must move whichever height is lower to get max, so can use two pointer

        #initializing left and right pointers

        left = 0
        right = len(heights) - 1

        #storing max amount (starts at 0)
        amount = 0

        #move pointers until they meet

        while left < right:

            #amount is equal to the minimum surrounding wall we've chosen * distance between
            amount = max(amount,min(heights[left],heights[right]) * (right-left))

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return amount
