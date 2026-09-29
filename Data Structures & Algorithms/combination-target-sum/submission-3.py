class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, remain):

            #if its at the right amount, might as well add right

            if remain == 0:
                res.append(subset.copy())
                return
            
            #if too much that sucks gotta return
            if remain < 0 or i >= len(nums):
                return
            
            #the version where you do add
            subset.append(nums[i])

            #since you are adding gottar emove numbs
            dfs(i, remain-nums[i])

            #version not adding, so dont need to subtract
            subset.pop()
            dfs(i+1,remain)
        
        dfs(0, target)
        return res
            

        