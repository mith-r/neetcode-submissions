class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        island = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == "1":

                    queue = deque()
                    queue.append((row,col))
                    grid[row][col] = "0"

                    island += 1

                    while len(queue) > 0:
                        cr,cc = queue.popleft()

                        for nr,nc in [(cr+1,cc),(cr-1,cc),(cr,cc+1),(cr,cc-1)]:

                            if min(nr,nc) < 0:
                                continue
                            
                            if nr >= len(grid):
                                continue

                            if nc >= len(grid[0]):
                                continue

                            if grid[nr][nc] == "1":

                                grid[nr][nc] = "0"

                                queue.append((nr,nc))


        return island
                    


        