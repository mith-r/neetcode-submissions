class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
            
        numset = set(nums)
        visited = set()

        length = 1
        total = 1

        for i in nums:
            if i not in visited:
                total = 1
                if i - 1 not in numset:
                    visited.add(i)
                    while i + 1 in numset:
                        total += 1
                        i += 1
                length = max(length,total)
        
        return length




        