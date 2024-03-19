from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])

        current_sum = max_sum
        for start_p in range(len(nums) - k):
            current_sum = current_sum - nums[start_p] + nums[start_p + k]

            if current_sum > max_sum:
                max_sum = current_sum
                

        return max_sum / k
