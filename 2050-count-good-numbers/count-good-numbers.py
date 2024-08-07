class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        if n % 2 == 0:
            half_n = n // 2
            return pow(20, half_n, MOD)
        else:
            half_n = n // 2
            return pow(5, half_n + 1, MOD) * pow(4, half_n, MOD) % MOD
