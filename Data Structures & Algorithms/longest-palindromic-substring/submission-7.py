class Solution:
    def longestPalindrome(self, s: str) -> str:

        #Gonna do this the two pointer method

        longest_string = ""

        #for odd ones
        for center in range(len(s)):
            string = s[center]
            i = center-1
            j = center+1

            while i >= 0 and j < len(s) and s[i] == s[j]:
                string = s[i] + string + s[j]
                i -= 1
                j += 1

            if len(string) > len(longest_string):
                longest_string = string
        
        #for even ones
        for center in range(len(s)):
            string = ""
            i = center
            j = center+1

            while i >= 0 and j < len(s) and s[i] == s[j]:
                string = s[i] + string + s[j]
                i -= 1
                j += 1

            if len(string) > len(longest_string):
                longest_string = string
        
        
        return longest_string

        