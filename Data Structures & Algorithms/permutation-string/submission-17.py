class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        check = Counter(s1)
        

        curr = Counter(s2[:len(s1)])

        for i in range(len(s1),len(s2),1):

            print(curr)
            if check == curr:
                return True
            
            if s2[i] not in curr:
                curr[s2[i]] = 0
            curr[s2[i]] += 1

            curr[s2[i-len(s1)]] -= 1

            if curr[s2[i-len(s1)]] == 0:
                del curr[(s2[i-len(s1)])]
        
        return check == curr




        