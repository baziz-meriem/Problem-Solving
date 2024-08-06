from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(index: int, memo: dict) -> int:
            if index in memo:
                return memo[index]
            if index < 0:
                return 0
            if index == 0:
                return nums[0]
            if index == 1:
                return max(nums[0], nums[1])
            
            rob_current = nums[index] + helper(index - 2, memo)
            skip_current = helper(index - 1, memo)

            memo[index] = max(rob_current, skip_current)
            return memo[index]
        
        return helper(len(nums) - 1, {})
