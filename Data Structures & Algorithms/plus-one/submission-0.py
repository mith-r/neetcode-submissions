class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1
        res = []
        index = -1

        for i in range(len(digits)-1,-1,-1):
            if carry > 0:
                res.append((digits[i]+carry) % 10)
                carry = (digits[i]+carry) // 10
                print(carry)
            
            else:
                res.append(digits[i])

        if carry > 0:
            res.append(carry)
        
        return list(reversed(res))




        
        