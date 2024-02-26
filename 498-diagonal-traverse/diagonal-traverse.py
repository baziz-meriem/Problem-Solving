class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        cols = len(mat[0])
        rows = len(mat)
        inter_list = [deque() for _ in range(cols+rows-1)]
        
        for row in range(rows):
            for col in range(cols):
                if (row+col) %2 ==0:
                    inter_list[row+col].appendleft(mat[row][col])
                else :
                    inter_list[row+col].append(mat[row][col])
        
        flattened_list = [element for q in inter_list for element in q]
        return flattened_list