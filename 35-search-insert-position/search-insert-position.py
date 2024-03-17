class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1]< target:
            return len(nums)
        for idx,val in enumerate(nums):
            
            if val == target:
                return idx
            elif val > target :
                return idx
        
