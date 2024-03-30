class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        # Fill prefix sum matrix
        for row in range(rows):
            for col in range(cols):
                prefix[row+1][col+1] = mat[row][col] + prefix[row][col+1] + \
                                       prefix[row+1][col] - prefix[row][col]
        
        # Calculate the block sum from the prefix sum
        result = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                # Calculate bounds for the sum
                row_min = max(i - k, 0)
                col_min = max(j - k, 0)
                row_max = min(i + k, rows - 1)
                col_max = min(j + k, cols - 1)

                
                result[i][j] = prefix[row_max + 1][col_max + 1] - prefix[row_max + 1][col_min] - \
                               prefix[row_min][col_max + 1] + prefix[row_min][col_min]
        
        return result
