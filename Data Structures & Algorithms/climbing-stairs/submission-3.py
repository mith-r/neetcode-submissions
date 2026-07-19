class Solution:
    def climbStairs(self, n: int) -> int:
        a = 2
        b = 3

        if n == a:
            return a
        
        if n == b:
            return b
        
        if n == 1:
            return 1

        while n-3> 0:
            c = a + b
            a=b
            b=c
            n -= 1

        return b