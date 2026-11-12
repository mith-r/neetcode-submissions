class Solution:
    def countSubstrings(self, s: str) -> int:
        
        #can think of this as two dimensional DP
        #dp[i][j] is substring starting at i ending at j (inclusive)

        n = len(s)

        dp = [[False]*n for _ in range(n)]
        numTrue = 0


        #j is the ending character
        for j in range(n):
            #i is the starting index
            for i in range(j+1):
                #outsides are equal and either length is below 3 or interior is
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    numTrue += 1
        
        return numTrue
