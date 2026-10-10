class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0

        visited = set()

        def dfs(r,c):

            if min(r,c) < 0 or r >= ROWS or c >= COLS or (r,c) in visited or grid[r][c] == "0":
                return

            visited.add((r,c))
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

            return

           
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == "1":
                    count += 1
                  
                    dfs(r,c)

        return count

























        

           

            
            

        