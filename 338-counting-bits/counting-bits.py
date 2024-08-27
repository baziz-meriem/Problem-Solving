class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for val in range(n+1):
            binary_representation = bin(val)
            ones = binary_representation.count('1')
            res.append(ones)
        return res