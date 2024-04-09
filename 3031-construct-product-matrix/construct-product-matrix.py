class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        productArr = [[1 for _ in range(m)] for _ in range(n)]

        product = 1
        i = 0
        while(i < n):
            j = 0
            while(j < m):
                productArr[i][j] = product % 12345
                product = (product * grid[i][j]) % 12345
                j+=1
            i+=1
        
        product = 1
        i = n-1
        while(i >= 0):
            j = m-1
            while(j >= 0):
                productArr[i][j] = (productArr[i][j] * product) % 12345
                product = (product * grid[i][j]) % 12345
                j-=1
            i-=1
        
        return productArr