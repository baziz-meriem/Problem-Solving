import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(sqrt(c))

        nums = [num for num in range(n+1)]
        idx_start = 0
        idx_end = len(nums)-1

        while idx_start<len(nums) and idx_end>=0:
            if nums[idx_start]**2 + nums[idx_end]**2 == c:
                return True
            elif nums[idx_start]**2 + nums[idx_end]**2< c:
                idx_start += 1
            else:
                idx_end -= 1
        return False
            
