class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        cache = obstacleGrid.copy()

        for i in range(len(cache)):
            for j in range(len(cache[0])):
                if cache[i][j] == 1:
                    cache[i][j] = -1

        columnSize = len(cache[0])
        rowSize = len(cache)

        if cache[rowSize-1][ columnSize-1] == -1:
            return 0

        def memoization(r,c,cache):
            
            if r == rowSize or c == columnSize:
                return 0

            if cache[r][c] > 0:
                return cache[r][c]

            if r == rowSize-1 and c == columnSize-1:
                return 1
            
            if cache[r][c] == -1:
                return 0

            cache[r][c] = memoization(r+1,c,cache) + memoization(r,c+1,cache)

            return cache[r][c]

        return memoization(0,0,cache)
            

        