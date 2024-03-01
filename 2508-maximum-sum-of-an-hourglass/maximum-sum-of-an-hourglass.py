class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:

        def calculate_sum(grid,start_row,start_col):
            sum_hourglass = grid[start_row][start_col] + grid[start_row+1][start_col+1] + grid[start_row+2][start_col+2] \
            + grid[start_row+2][start_col] + grid[start_row+2][start_col+1] +grid[start_row][start_col+1]  +grid[start_row][start_col+2]  
            return sum_hourglass
        
        def start_indexes(grid):
            indexes_list=[]
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if row+2 < len(grid) and col+2 < len(grid[0]):
                        indexes_list.append((row,col))
            return indexes_list

        indexes_list = start_indexes(grid)
        max_sum = 0
        for row,col in indexes_list:
            current_sum = calculate_sum(grid,row,col)
            if max_sum < current_sum:
               max_sum = current_sum

        return max_sum
        