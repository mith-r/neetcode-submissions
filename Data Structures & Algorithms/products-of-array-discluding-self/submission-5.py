class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        pre = 1
        suff = 1

        for i in range(len(nums)):
            prefix[i] = pre
            pre *= nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            suffix[i] = suff
            suff *= nums[i]


        res = [0] * len(nums)

        for i in range(len(res)):
            res[i] = prefix[i] * suffix[i]

        return res

        