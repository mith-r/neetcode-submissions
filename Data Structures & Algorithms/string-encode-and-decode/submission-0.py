class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""

        for i in strs:
            string += (str(len(i)))
            string += "#"
            string += i
        
        print(string)
        return string


    def decode(self, s: str) -> List[str]:

        res = []

        i = 0

        while i < len(s):

            length = ""

            while s[i] != "#":
                length += s[i]
                i += 1

            i += 1
            print(length)

            word = ""
            for j in range(int(length)):
                word += s[i]
                i += 1
            print(word)
            res.append(word)
        
        return res

