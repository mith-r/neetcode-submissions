class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        #loop through words in wordDic  t 
        #dp is if starting at letter, can have words to the end

        dp = [False] * len(s)

        for i in range(len(s)-1, -1, -1):

            for word in wordDict:
                
                if s[i:i+len(word)] == word and (i+len(word) >= len(s) or dp[i+len(word)]):
                    dp[i] = True
        
        return dp[0]
        