class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        distances = [[-1 for i in range(len(grid[0]))] for i in range(len(grid))]
        
        queue = deque()
        minute = 0

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 2:
                    queue.append((row,column))
                    distances[row][column] = minute
                if grid[row][column] == 0:
                    distances[row][column] = 0

        while len(queue) > 0:
            minute += 1
            for i in range(len(queue)):
                r,c = queue.popleft()

                for r_new, c_new in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                    if 0 <= r_new < len(grid) and 0<=c_new< len(grid[0]):
                        if grid[r_new][c_new] == 1:
                            queue.append((r_new,c_new))
                            grid[r_new][c_new] = 2
                            distances[r_new][c_new] = minute

        maxN = 0
        print(distances)
        for i in distances:
            for j in i:
                if j > maxN:
                    maxN = j
                if j == -1:
                    return -1
        
        return maxN

            

        