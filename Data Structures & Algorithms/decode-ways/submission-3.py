class Solution:
    def numDecodings(self, s: str) -> int:

        #message is max length 2. Can look in group of 2 (ie i and i + 1)
        #dp is ways to decode ending at i + 1

        #starting with 0
        dp = [0] * (len(s)+1)
        dp[0] = 1
   

        #any valid number must start with non zero. If it is 1 or 2, can extend one more digit (as long as second digit is less than 1)

        for i in range(1,len(s)+1):
            count = 0
            if s[i-1] != '0':
                count += dp[i-1]
            
            if i >= 2 and int(s[i-2:i]) in range(10,27):
                count += dp[i-2]
            
            dp[i] = count
        
        return dp[len(s)]





        