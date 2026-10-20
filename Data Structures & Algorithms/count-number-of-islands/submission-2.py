class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        num = 0

        def dfs(i,j,grid):
            
            if i < 0:
                return
            if i >= len(grid):
                return
            
            if j < 0:
                return

            if j >= len(grid[0]):
                return
            if grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            
            dfs(i+1,j,grid)
            dfs(i-1,j,grid)
            dfs(i,j+1,grid)
            dfs(i,j-1,grid)
            
            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num += 1
                    dfs(i,j,grid)
        
        return num
