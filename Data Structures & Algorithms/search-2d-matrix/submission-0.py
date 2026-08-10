class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for column in matrix:
            if self.binarySearch(column, target):
                return True
        
        return False
            
    
    def binarySearch(self, column: List[int], target: int) -> bool:
        middle = len(column) // 2

        if column[middle] == target:
            return True
        elif len(column) == 1:
            return False
        elif target > column[middle]:
            return self.binarySearch(column[middle:], target)
        elif target < column[middle]:
            return self.binarySearch(column[:middle], target)
        