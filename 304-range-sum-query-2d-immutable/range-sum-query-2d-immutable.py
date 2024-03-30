class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows,cols = len(matrix),len(matrix[0])
        self.matrix_pref_sum = [[0]*(cols+1 )for _ in range(rows+1)]
        self.matrix = matrix

        for row in range(rows):
            for col in range(cols):
                self.matrix_pref_sum[row+1][col+1] = self.matrix[row][col] + self.matrix_pref_sum[row][col+1] \
                + self.matrix_pref_sum[row+1][col]- self.matrix_pref_sum[row][col]

        #print('matrix pref sum is : ',self.matrix_pref_sum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sumRegion = self.matrix_pref_sum[row2 + 1][col2 + 1] - self.matrix_pref_sum[row1][col2 + 1] - \
                    self.matrix_pref_sum[row2 + 1][col1] + self.matrix_pref_sum[row1][col1]
        return sumRegion



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)