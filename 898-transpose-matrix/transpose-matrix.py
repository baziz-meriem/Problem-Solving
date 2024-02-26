class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        transpose = [[0]*rows for _ in range(cols)]

        for row in range(cols):
            for col in range(rows):
                    transpose[row][col] = matrix[col][row]
        return transpose
