class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        L = 0
        length = 0
        result = 0
        num0 = 0

        for R in range(len(nums)):
           
            length += 1
            if nums[R] == 0:
                num0 += 1
            while num0 > k:

                if nums[L] == 0:
                    num0 -= 1
                L += 1
                length -= 1
            
            result = max(length,result)

        return result
        