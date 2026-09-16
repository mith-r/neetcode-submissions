class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        asNum = {}
        res = []
        for chars in strs:
            alph = ''.join(sorted(chars))
            if alph not in asNum:
                asNum[alph] = []
            asNum[alph].append(chars)
        
        for val in asNum.values():
            res.append(val)
        
        return res

        