class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        curr_set = []

        for i in s:
            if i in curr_set:
                if len(curr_set) > longest:
                    longest = len(curr_set)
                del curr_set[:curr_set.index(i)+1]
            curr_set.append(i)

        return max(longest,len(curr_set))
                
        