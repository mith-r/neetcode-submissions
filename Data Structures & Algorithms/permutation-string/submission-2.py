class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        i = 0
        for i in range(len(s2)-len(s1)+1):
            j = i + len(s1)

            s1 = sorted(s1);
            curr = sorted(s2[i:j])

       

            if s1 == curr:
                return True
        
        return False