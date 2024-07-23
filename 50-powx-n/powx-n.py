class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        elif n==1:
            return x
        elif n<0:
            return 1/self.myPow(x,-n)
        if n%2==0:
            half_power = self.myPow(x,n//2)
            return half_power*half_power
        return x*self.myPow(x,n-1)