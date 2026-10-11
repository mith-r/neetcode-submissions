class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        #both have to add up to half of the solution

        half = sum(nums)/2

        #somewhere need to say, this is the one we are adding, so take it from second
        def dfs(i,currSum,nums,cache):

            if currSum == half:
                return True

            if i == len(nums):
                return False

            if (i,currSum) in cache:
                return cache[(i,currSum)]
            
            cache[(i,currSum)] = dfs(i+1,currSum,nums,cache) or dfs(i+1,currSum + nums[i],nums,cache)

            return cache[(i,currSum)]
        
        return dfs(0,0,nums,{})
            
 
            
            

          


       
            

            

        