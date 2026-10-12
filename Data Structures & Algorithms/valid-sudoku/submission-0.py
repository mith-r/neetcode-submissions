class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #3 lists with 9 things in each (columns, squares, rows)
        #each with set, if any one is false, then entire thing is false

        #rows

        for row in board:
            dupe = set()

            for i in row:
                if i != '.':
                    if i in dupe:
                        return False

                dupe.add(i)
        
        #cols

        
        for col in range(9):
            dupe = set()
            for row in range(9):

                curr = board[row][col]
                if curr != '.':
                    if curr in dupe:
                        return False
                dupe.add(curr)
        

        #squares

        for row_offset in range(3):
            for col_offset in range(3):
                dupe = set()

                for row in range(3):
                    for col in range(3):
                    
                        curr = board[row+row_offset*3][col+col_offset*3]
                        if curr != '.':
                            if curr in dupe:
                                return False
                        dupe.add(curr)


        return True

                