class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1:
            return -1
        
        queue = deque()
        queue.append((0,0))

        visited = set()
        visited.add((0,0))
        length = 1

        if 0 == len(grid)-1 and 0 == len(grid[0])-1:
            return length

        while len(queue) > 0:
            print(queue)
            length+=1 
            
            for i in range(len(queue)):
                r,c = queue.popleft()

                for nr in range(r-1,r+2):
                    for nc in range(c-1,c+2):
                        print(f"{nr,nc}")

                        if nr == len(grid) - 1 and nc==len(grid[0]) - 1:
                            if grid[nr][nc] == 0:
                                return length

                        if min(nr,nc) < 0:
                            print("here")
                            continue
                        
                        if nr == len(grid) or nc == len(grid[0]):
                            continue
                        
                        if (nr,nc) in visited:
                            continue
                        
                        if grid[nr][nc] == 1:
                            continue
                        
                        visited.add((nr,nc))
                        queue.append((nr,nc))
        return -1

                    

                    

        

        