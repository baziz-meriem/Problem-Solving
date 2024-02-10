from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        violations = 0
        viol_idx = -1

        for idx in range(len(nums) - 1):
            if nums[idx] > nums[idx + 1]:
                violations += 1
                viol_idx = idx
                if violations > 1:
                    return False

        if violations == 0:
            return True

        if violations == 1:
            if viol_idx==0 :
                # Attempt to fix the violation
                nums[viol_idx] = nums[viol_idx+1]
                
            else :
                if viol_idx+2<len(nums) and nums[viol_idx+2]< nums[viol_idx]:
                    nums[viol_idx] = nums[viol_idx+1]
                else:
                    nums[viol_idx+1] = nums[viol_idx]
                


        # Check if the array is non-decreasing after modification
        for idx in range(len(nums) - 1):
            if nums[idx] > nums[idx + 1]:
                return False

        return True

        