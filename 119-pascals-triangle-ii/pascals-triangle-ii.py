class Solution:
    def __init__(self):
        self.memo = {}

    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex in self.memo:
            return self.memo[rowIndex]
        elif rowIndex == 0:
            return [1]
        else:
            previous_content = self.getRow(rowIndex-1)
            row_content = [ x+y for x,y in zip([0]+previous_content,previous_content+[0])]
            return row_content