class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        numMoves = 0
        totalNumber = 0
        newTarget = target
        while newTarget >1 and maxDoubles:
            newTarget //= 2
            if newTarget >=1:
                totalNumber += newTarget
                numMoves +=1
                maxDoubles -= 1

        numMoves += target - totalNumber - 1
        return numMoves