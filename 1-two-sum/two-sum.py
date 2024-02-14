class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,num in enumerate(nums):
            for idx in range(i+1,len(nums)):
               
                if num + nums[idx] == target:
                    return [idx,i]
            


        