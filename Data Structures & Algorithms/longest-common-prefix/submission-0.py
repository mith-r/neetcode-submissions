class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = ""

        for i in range(len(strs[0])):
            letter = strs[0][i]

            for j in range(len(strs)):
                word = strs[j]

                if i == len(word) or word[i] != letter:
                    return prefix
            prefix += letter
        
        return prefix
        