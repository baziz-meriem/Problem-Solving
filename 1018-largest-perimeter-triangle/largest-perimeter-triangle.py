class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        max_sum =0
        idx = 0
        nums = sorted(nums,reverse=True)
        while idx+2 < len(nums):
           
            if sum(nums[idx+1:idx+3])> nums[idx]:
                max_sum = sum(nums[idx:idx+3])
                return max_sum
                
            idx += 1
        return max_sum
        
        