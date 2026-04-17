class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        x = 0
        max_x = 0
        for num in nums:
            if num == 1:
                x += 1
            elif num != 1:
                x = 0
            if x > max_x:
                max_x = x
        return max_x
        