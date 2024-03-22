class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_length = len(nums)
        current_sum = 0
        l=0

        if sum(nums)< target:
            return 0
        for  r in range(len(nums)):
            current_sum += nums[r]#1
            if current_sum >= target:
                
                while l <= r and current_sum >= target :
                    min_length = r-l+1 if r-l+1 < min_length  else min_length
                    current_sum -= nums[l] 
                    l += 1
        return min_length
                    

        
        

        