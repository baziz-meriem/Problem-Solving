import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_reversed = ""
        for i in str(x):#121
            x_reversed = i + x_reversed #121
        return str(x)==x_reversed