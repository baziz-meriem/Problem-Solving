class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0
        for idx in range(len(nums)):
            if left_sum == right_sum - nums[idx]:
                return idx
            right_sum -= nums[idx]#4
            left_sum += nums[idx]#12

        return -1