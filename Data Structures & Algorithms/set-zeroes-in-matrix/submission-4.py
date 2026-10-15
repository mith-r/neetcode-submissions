class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                
                if matrix[row][col] == 0:
                    for change_col in range(len(matrix[row])):
                        if matrix[row][change_col] != 0:
                            matrix[row][change_col] = "0"
                    
                    for change_row in range(len(matrix)):
                        if matrix[change_row][col] != 0:
                            matrix[change_row][col] = "0"
          
    

      