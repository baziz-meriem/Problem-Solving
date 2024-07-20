class Solution:
    def canJump(self,nums):
        farthest = 0
        for idx in range(len(nums)):
            if idx>farthest:
                return False
            farthest = max(farthest,nums[idx]+idx)
            if farthest>= len(nums)-1:
                return True