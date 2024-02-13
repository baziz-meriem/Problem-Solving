class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        all_sides =[]
        max_sum = 0
        idx = 0
        nums = sorted(nums)
        while idx+2 < len(nums):
            all_sides = nums[idx:idx+3]
           
            if sum(all_sides[:-1]) > all_sides[-1] and sum(all_sides[-2:]) > all_sides[0] and all_sides[-1]+all_sides[0] > all_sides[1]:
                if sum(all_sides) > max_sum:
                    max_sum = sum(all_sides)
                
            idx += 1
        return max_sum
        
        