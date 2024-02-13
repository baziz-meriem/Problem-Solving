class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        max_sum =0
        idx = 0
        nums = sorted(nums,reverse=True)
        while idx+2 < len(nums):
           
            if sum(nums[idx:idx+3][-2:]) > nums[idx:idx+3][0] :
                max_sum = sum(nums[idx:idx+3])
                return max_sum
                
            idx += 1
        return max_sum
        
        