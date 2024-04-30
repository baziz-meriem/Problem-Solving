class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n==1:
            return True
        elif n <=0 or n % 4 != 0 :
            return False
        else:
            n=n//4
            return self.isPowerOfFour(n)