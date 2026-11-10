class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
            
        nums_set = set(nums)

        total = 1
        
        for i in nums:

            if i-1 not in nums_set:

                num = i
                curr = 1

                while num+1 in nums_set:
                    num += 1
                    curr += 1

                total = max(curr,total)

        
        return total
        