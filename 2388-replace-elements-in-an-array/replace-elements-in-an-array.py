class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        nums_dict = {num: idx for idx, num in enumerate(nums)}
        for op0,op1 in operations:
            nums[nums_dict[op0]] = op1
            nums_dict[op1] = nums_dict[op0]
            del nums_dict[op0]
            
        return nums
            