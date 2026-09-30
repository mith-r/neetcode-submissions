class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        #stores the maxArea that we will return
        maxArea = 0
        visited = set()

        #stores the tuples that have been visited and the currMax

        def dfs(grid,r,c):
            #base case if there is nowhere to go, return 0
            if min(r,c) < 0 or r == len(grid) or c == len(grid[0]) or (r,c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r, c))

            return 1 + dfs(grid,r,c+1) + dfs(grid,r,c-1) + dfs(grid,r+1,c) + dfs(grid,r-1,c)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited and grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(grid, r, c))
        
        return maxArea



