class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        curr_min_sum = 0
        prefix_sum = 0

        for num  in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - curr_min_sum)
            
            curr_min_sum = min(curr_min_sum,prefix_sum)

        return max_sum