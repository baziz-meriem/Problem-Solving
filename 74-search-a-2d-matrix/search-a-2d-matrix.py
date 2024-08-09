class Solution:
    def searchMatrix(self,matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        # Flatten the matrix into a 1D sorted array
        m, n = len(matrix), len(matrix[0])
        
        # Binary search on the 1D array
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // n][mid % n]
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
