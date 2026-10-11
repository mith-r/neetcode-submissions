class Solution:
    def rob(self, nums: List[int]) -> int:

        nums1 = nums[1:]
        nums2 = nums[:-1]

        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        def dfs(i,cache,numss):

            if i >= len(numss):
                return 0

            if i in cache:
                return cache[i]
            
            cache[i] = max(numss[i]+dfs(i+2, cache,numss), dfs(i+1,cache,numss))

            return cache[i]
        
        return max(dfs(0,{},nums1), dfs(0,{},nums2))