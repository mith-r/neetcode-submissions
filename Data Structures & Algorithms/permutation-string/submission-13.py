class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        check = Counter(s1)
        
        for R in range(len(s1),len(s2)+1,1):
            if Counter(s2[R-len(s1):R]) == check:
                return True

           

        return False


