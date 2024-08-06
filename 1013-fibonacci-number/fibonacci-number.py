class Solution:
    def fib(self, n: int, dic: dict = {}) -> int:

        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        if n in dic:
            return dic[n]
        
        prevFib = self.fib(n - 1, dic)
        prev2Fib = self.fib(n - 2, dic)
        
        # Update the memoization dictionary
        dic[n] = prevFib + prev2Fib
        
        return dic[n]