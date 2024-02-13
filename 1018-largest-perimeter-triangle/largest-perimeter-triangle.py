class Solution:
    def largestPerimeter(self, nums: List[int]) -> int: # nums = [3,6,2,3]
            # condition to create a triangle a < (b + c). where  a >= b >= c
            nums = sorted(nums, reverse=True) # nums after sorting = [6, 3, 3, 2]
            for i in range(len(nums)-2):
                if nums[i] < nums[i+1] +nums[i+2]: # When i =1 => 3 < 3+2 (True)
                    return nums[i]+nums[i+1] +nums[i+2] # 3 + 3 + 2 = 8
            return 0
        
        