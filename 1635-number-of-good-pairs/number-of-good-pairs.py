from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs  = 0
        for i,_ in enumerate(nums):
            for j,_ in enumerate(nums):
                if i<j and nums[i] == nums[j] :
                    pairs = pairs + 1
        return pairs



