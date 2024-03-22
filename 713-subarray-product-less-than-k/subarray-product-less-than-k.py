from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        mult = 1
        l = 0
        r = 0
        total = 0

        while r < len(nums):
            if mult * nums[r] < k:
                mult *= nums[r] 
                total += r - l + 1
                r += 1
            else:
                if l == r:  # If the window size is 1
                    r += 1
                    l += 1
                else:
                    mult /= nums[l]
                    l += 1

        return total
