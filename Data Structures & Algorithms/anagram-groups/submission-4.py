class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dictionary = {}

        for i in strs:
            sort = ''.join(sorted(i))
            if sort not in dictionary:
                dictionary[sort] = []
            dictionary[sort].append(i)

        res = []
        for key,val in dictionary.items():
            res.append(val)

        return res



        