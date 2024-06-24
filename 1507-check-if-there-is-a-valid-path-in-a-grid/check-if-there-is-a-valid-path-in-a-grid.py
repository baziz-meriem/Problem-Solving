class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        step = {(0, 1):{1, 3, 5}, (0, -1):{1, 4, 6}, (1, 0):{2, 5, 6}, (-1, 0):{2, 3, 4}}
        direct = {1:[(0,-1), (0,1)], 2:[(-1,0), (1,0)], 3:[(0,-1), (1,0)], 4:[(0,1), (1,0)], 5:[(0,-1), (-1,0)], 6:[(0,1), (-1,0)]}
        n, m = len(grid), len(grid[0])
        stack = [(0, 0)]
        while stack:
            x, y = stack.pop()
            for i, j in direct.get(grid[x][y], []):
                ii, jj = x+i, y+j
                if 0 <= ii < n and 0 <= jj < m and grid[ii][jj] in step[(i, j)]:
                    stack.append((ii, jj))
            grid[x][y] = 0  
        return not grid[n-1][m-1] 