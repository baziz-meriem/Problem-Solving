class Solution:
    def mySqrt(self, x: int) -> int:
        
        res = 0
        for num in range(1,math.ceil(x/2) + 2):
       
            if num**2 == x:
                res = num

            elif num**2 > x:
                res = num-1
                break
        return res