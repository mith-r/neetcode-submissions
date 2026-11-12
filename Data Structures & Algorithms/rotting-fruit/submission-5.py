class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        remaining = 0

        for row in grid:
            for column in row:
                if column == 1:
                    remaining += 1

        queue = deque()
        graph = {}

        last_row,last_col = -1,-1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
        
        while len(queue) > 0:
            print(len(queue))

            row,col = queue.popleft()

            for nr, nc in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]:
                
                if nr == len(grid) or nc == len(grid[0]):
                    continue
                
                if nr < 0 or nc < 0:
                    continue
                
                if grid[nr][nc] == 1:
                    remaining -= 1
                    queue.append((nr,nc))
                    grid[nr][nc] = 2
                    graph[(nr,nc)] = (row,col)

                    last_row,last_col = nr,nc
        
        #now calculating distance
        #return early if remaining not high enough

        if remaining > 0:
            return -1

        #now calculate length

        distance = 0

        while (last_row,last_col) in graph:
            (last_row,last_col) = graph[last_row,last_col] 
            distance += 1

        return distance
        