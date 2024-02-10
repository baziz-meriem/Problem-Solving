from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        violations = 0
        viol_idx = -1

        for idx in range(len(nums) - 1):
            if nums[idx] > nums[idx + 1]:
                violations += 1
                viol_idx = idx + 1
                if violations > 1:
                    return False

        if violations == 0:
            return True

        # Attempt to fix the violation
        if viol_idx == 1 or nums[viol_idx - 2] <= nums[viol_idx]:
            nums[viol_idx - 1] = nums[viol_idx]
        elif viol_idx == len(nums) - 1 or nums[viol_idx - 1] <= nums[viol_idx + 1]:
            nums[viol_idx] = nums[viol_idx - 1]
        else:
            return False

        # Check if the array is non-decreasing after modification
        for idx in range(len(nums) - 1):
            if nums[idx] > nums[idx + 1]:
                return False

        return True

        