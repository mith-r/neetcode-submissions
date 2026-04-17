class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for i in s:
            if not i in letters:
                letters[i] = 1
            else:
                letters[i] = letters[i] + 1

        letters2 = {}
        for j in t:
            if not j in letters2:
                letters2[j] = 1
            else:
                letters2[j] = letters2[j]+1

            

        return letters == letters2
        