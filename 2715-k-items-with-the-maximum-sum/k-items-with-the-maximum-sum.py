class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        a=2*numOnes+numZeros-k
        return min(k,numOnes,a)