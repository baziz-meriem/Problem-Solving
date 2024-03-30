class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur=curMax= nums[0]
        for num in nums[1:]:
            cur = max(num,cur+num)
            curMax = max(cur,curMax)
        return curMax
