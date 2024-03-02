from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors_count = Counter(nums)

        new_list=[]
        for idx in range(3):
            new_list.extend([idx]*colors_count[idx])
        for idx,num in enumerate(nums):
            nums[idx] = new_list[idx]
       
        