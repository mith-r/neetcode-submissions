class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        num_set = set(nums)

        final = 1
        curr = 1

        for i in num_set:
            if i-1 not in num_set:
                while i+1 in num_set:
                    curr += 1
                    i = i + 1
            else:
                if final < curr:
                    final = curr
                curr = 1
        
        return max(final, curr)
        