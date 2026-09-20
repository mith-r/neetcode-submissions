class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        if len(num_set) == 0:
            return 0

        total = 1
        long = 1

        for i in num_set:

            if i - 1 not in num_set:
                start = i
                while start+1 in num_set:
                    total += 1
                    start += 1
                if total > long:
                    long = total
                total = 1
                    
                    


        
        return max(total,long)


        