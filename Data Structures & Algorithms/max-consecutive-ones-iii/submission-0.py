class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        L = 0
        total = 0
        result = 0

        num0 = 0

        for R in range(len(nums)):
            total += 1
            if nums[R] == 0:
                num0 += 1
            while num0 > k:
                total-=1
                if nums[L] == 0 and num0 > 0:
                    num0 -= 1
                L+=1
            result = max(total,result)

        return result
        