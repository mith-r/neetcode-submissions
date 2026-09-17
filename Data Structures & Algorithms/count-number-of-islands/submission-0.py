class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_components_visit = 0
    
        for row in range(len(grid)):
            for col in range(len(grid[0])):


                if grid[row][col] == "1":
                    num_components_visit += 1

                    queue = deque()
                    queue.append((row,col))
                    grid[row][col] = "2"

                    while len(queue) > 0:
                        row, col = queue.popleft()

                        for new_row, new_col in [(row-1, col), (row+1, col), (row, col+1), (row, col-1)]:
                            if 0 <= new_row <len(grid) and 0<= new_col < len(grid[0]):

                                if grid[new_row][new_col] == "1":
                                    grid[new_row][new_col] = "2"
                                    queue.append((new_row,new_col))

        return num_components_visit
                




#so goal is to find number of components
#can do this by seeing how many sets of dfs we have to run
#potentially change coordinate on screen to make sure we hit every 1? Like change to 2?