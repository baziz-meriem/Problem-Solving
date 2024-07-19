class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        sum=0
        if k >0:
            pickOnes = min(k,numOnes)
            sum += pickOnes
            k -= pickOnes
            if k >0:
                pickZeros = min(k,numZeros)
            
                k -= pickZeros
            if k >0:
                pickNeg = min(k,numNegOnes)
                sum -= pickNeg

        return sum