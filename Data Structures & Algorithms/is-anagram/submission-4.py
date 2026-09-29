class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        check = [0] * 26

        for i in s:
            check[ord(i)-ord('a')] += 1

    
        for i in t:
            if check[ord(i)-ord('a')] <= 0:
                return False
            check[ord(i)-ord('a')] -= 1
        

        return sum(check) == 0