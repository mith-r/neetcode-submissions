class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = set()
        maxcount = 0
        count = 0
        i = 0
        left = 0
        while i < len(s):
            if s[i] in temp:
                if maxcount < count:
                    maxcount = count
                temp.remove(s[left])
                left+=1
                count = count - 1
                continue
            temp.add(s[i])
            count += 1
            i += 1
        
        
        return max(maxcount, count)
            
                
                
                
        