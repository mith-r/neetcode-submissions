# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        small = 1
        big = 9999999999999999999
        

        while guess(n) != 0:
            if guess(n) == 1:
                small = n
                print(f'small:{small}')
            elif guess(n) == -1:
                big = n
                print(f'big: {big}')
            middle = (small + big) // 2
            n = middle
        
        return n

        
