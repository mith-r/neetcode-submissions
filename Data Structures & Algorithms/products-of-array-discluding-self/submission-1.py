class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        pre = 1
        suffix = []
        suff = 1

        res = []

        for i in nums:
            prefix.append(pre)
            pre = pre * i
        
        rev = reversed(nums)

        for i in rev:
            suffix.append(suff)
            suff = suff*i
        
        suffix = list(reversed(suffix))

       
        
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])

       
        

        return res