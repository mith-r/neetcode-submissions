class Solution:
    def compress(self, chars: List[str]) -> int:
        
        i = 0
        j = 0

        insert = 0

        while j < len(chars):

            if j+1 == len(chars) or chars[i] != chars[j+1]:

                total = j-i+1

                chars[insert] = chars[i]
                insert += 1

                if total != 1:
                    for x in str(total):
                        chars[insert] = x
                        insert += 1
                
                i = j + 1
                        
            j += 1

        return insert