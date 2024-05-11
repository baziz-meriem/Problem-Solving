# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #binary search
        min_val = 0
        max_val = n-1
        while min_val<=max_val:
            mid_point = (min_val + max_val)//2
            
            if isBadVersion(mid_point):
                max_val = mid_point - 1

            elif not isBadVersion(mid_point):
                min_val = mid_point + 1

        return min_val