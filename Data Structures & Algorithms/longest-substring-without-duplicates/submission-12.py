class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        L = 0
        seen = set()

        for R in range(len(s)):

            while s[R] in seen:
                seen.remove(s[L])
                L+=1
            
            seen.add(s[R])

            res = max(len(seen),res)
        
        return res

        