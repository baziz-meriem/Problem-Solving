class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        indices=[]
        for idx,num in enumerate(nums):
            if num==target:
                indices.append(idx)
        return indices
        