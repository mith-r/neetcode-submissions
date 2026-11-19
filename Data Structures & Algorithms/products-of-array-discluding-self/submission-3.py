class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #Can use prefix and suffix array
        #start with suffix fully filled, and before something is multiplied, remove it, then afterwards add to prefix array. 
        
        #considered just having a running total, but can't recover from 0
        # don't add 0's to prefix or suffix, but if anything other than self is 0, append 0

        #if 0 anywhere else, multiplies to 0
        #only if self is only 0, its not 0

        count0 = nums.count(0)

        if count0 > 1:
            return [0] * len(nums)

        prefix = 1
        suffix = 1

        for i in nums:
            if i != 0:
                suffix = suffix * i
        
        res = []

        if count0 == 1:
            for i in nums:
                if i != 0:
                    res.append(0)
                else:
                    res.append(suffix)

        else:
            for i in nums:
                suffix = suffix//i
                res.append(prefix*suffix)
                prefix = prefix * i
        
        return res




        


        