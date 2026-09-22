class Solution:
    def decodeString(self, s: str) -> str:

        while "[" in s:
            firstB = s.rfind("[")
            numEnd = firstB
            numStart = firstB-1

            while s[numStart-1].isnumeric():
                numStart-=1

            multiple = s[numStart:numEnd]

            firstSlice = s[:numStart]

            
            lastB=s.find("]",firstB)
            lastSlice = ""
            if lastB != len(s)-1:
                lastSlice = s[lastB+1:]
            
            midSlice = s[firstB+1:lastB]
            copy = ""
            for i in range(int(multiple)):
                copy += midSlice

            s = firstSlice + copy + lastSlice
            
        return(s)
            


        