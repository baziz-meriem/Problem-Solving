from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs  = 0
        for i,num_i in enumerate(nums):
            for j in range(i+1,len(nums)):
                if num_i== nums[j] :
                    pairs += 1
        return pairs



