class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        sum_col = 0
        for idx,s in enumerate(strs):
            strs[idx] = list(s)
        rows = len(strs)
        cols = len(strs[0])
        previous = 60

        for col in range(cols):
            previous = 60
            for row in range(rows):
                if ord(strs[row][col]) < previous :   
                    sum_col += 1
                    break
                previous = ord(strs[row][col])
                
                
        return sum_col