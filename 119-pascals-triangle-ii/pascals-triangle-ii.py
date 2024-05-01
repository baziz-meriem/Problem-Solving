class Solution:
    def getRow(self,rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        row = [1]  # Start with the first row
        for _ in range(rowIndex):
            # Create the next row based on the previous row
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row

