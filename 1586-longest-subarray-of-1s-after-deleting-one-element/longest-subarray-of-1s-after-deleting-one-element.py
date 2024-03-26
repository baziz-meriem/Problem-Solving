class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left =0
        right= 0
        count_zero = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right]==0:
                count_zero += 1
            while count_zero>1 and left<len(nums):
                if nums[left]==0:
                    count_zero -= 1
                left += 1

            max_len = max(max_len,right-left) 
        return max_len