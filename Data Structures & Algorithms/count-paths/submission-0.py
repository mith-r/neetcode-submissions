class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0]* n for i in range(m)]
        def memoization(m,n,r,c,cache):
            if r ==m:
                return 0
            
            if c == n:
                return 0

            if cache[r][c] > 0 :
                return cache[r][c]
            
            if r == m-1 and c == n-1:
                return 1
            
    
            
            #there are two options: down and right

            cache[r][c] = memoization(m,n,r+1,c,cache) + memoization(m,n,r,c+1,cache)

            return cache[r][c]
    
        return memoization(m,n,0,0,cache)