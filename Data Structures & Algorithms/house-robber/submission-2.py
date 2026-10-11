class Solution:
    def rob(self, nums: List[int]) -> int:


        def memoization(i,cache):

            #this is iterative, so the max amount at end includes max amoutn for earlier houses + the optimal strategy from then
            
            #if you reach the end or past it you done so return and shit
            if i >= len(nums):
                return 0
            
            #if you know the optimal strategy from this house, return that

            if i in cache:
                return cache[i]

            #the optimal strategy is the best of the two strategies
            cache[i] = max(nums[i] + memoization(i+2,cache),memoization(i+1,cache))
            return cache[i]

        
        return memoization(0,{})

        