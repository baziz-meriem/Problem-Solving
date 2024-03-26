from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1  

        pref = [nums[0]]
        for idx in range(1, len(nums)):
            pref.append(pref[-1] + nums[idx])

        total_sum = pref[-1]

        for idx in range(len(nums)):

            if  pref[idx] - nums[idx] == total_sum - pref[idx]:
                return idx

        return -1
