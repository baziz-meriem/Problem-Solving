# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:


    def guessNumber(self, n: int) -> int:
        min_val = 1
        max_val = n
        while min_val <= max_val:
            mid_point = (max_val + min_val)//2
            out = guess(mid_point)
            if out == -1:
                max_val = mid_point - 1
            elif out == 1:
                min_val = mid_point + 1
            else:
                return mid_point