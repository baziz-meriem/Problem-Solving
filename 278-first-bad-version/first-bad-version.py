# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #binary search
        min_val = 0
        max_val = n-1
        while min_val<=max_val:
            mid_point = (min_val + max_val)//2
            out = isBadVersion(mid_point)
            
            if out==True:
                max_val = mid_point - 1

            elif out==False and isBadVersion(mid_point+1):
                return mid_point+1
            elif out==False:
                min_val = mid_point + 1
        