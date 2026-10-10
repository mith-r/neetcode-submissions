class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        path = set()


        def backTrack(r,c,i):
            #base case
            if i == len(word):
                return True

            #if not a valid combo return false
            if (min(r,c)) < 0 or r>= ROWS or c >= COLS or word[i] != board[r][c] or (r,c) in path:
                return False
            
            path.add((r,c))

            #see if you can continue to any of the 4. If any one of the 4 is valid thats enough
            res = backTrack(r+1,c,i+1) or backTrack(r-1,c,i+1) or backTrack(r,c+1,i+1) or backTrack(r,c-1, i+1)

            path.remove((r,c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if backTrack(r,c,0):
                    return True
        
        return False
        


            

