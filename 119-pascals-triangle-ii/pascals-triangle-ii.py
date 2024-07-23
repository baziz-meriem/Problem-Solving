class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowList =[]
        
        if rowIndex==0:
            rowList.append(1)
            return rowList
        elif rowIndex==1:
            rowList.extend([1,1])
            return rowList
        
        else:
            myList = self.getRow(rowIndex-1)
            rowList.append(1)
            for idx in range(1,rowIndex):
                rowList.append(myList[idx-1]+ myList[idx])

            rowList.append(1)
        return rowList
       