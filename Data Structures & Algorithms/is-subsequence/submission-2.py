class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        res = ""


        i = 0
        j = 0

        while i < len(s) and j < len(t):
            print((i,j))
            if s[i] == t[j]:
                res += s[i]
                i += 1  
            j+=1

        print(res)
        return res == s

        