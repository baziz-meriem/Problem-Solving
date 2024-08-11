class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def dfs(x: int, y: int):
            # Boundary conditions and checking if the cell is water
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '0':
                return
            
            # Mark the cell as visited
            grid[x][y] = '0'
            
            # Visit all adjacent cells (up, down, left, right)
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    # Found an island, initiate DFS to mark the whole island
                    dfs(i, j)
                    num_islands += 1
        
        return num_islands
