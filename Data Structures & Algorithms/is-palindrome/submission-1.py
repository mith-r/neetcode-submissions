class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        R = (len(s)-1)
        for i in range(len(s)//2):

            if s[i].isalnum():

                while not s[R].isalnum():
                    R  -= 1
            

                if s[i].lower() != s[R].lower():
                    return False
            
                R-= 1

        return True
        