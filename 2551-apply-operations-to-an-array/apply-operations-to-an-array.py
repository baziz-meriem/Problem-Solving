from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        new_nums = []
        zeros = 0
        
        for idx in range(len(nums) - 1):  # Iterate up to len(nums) - 1
            if nums[idx] != 0:
                if nums[idx] == nums[idx + 1]:
                    nums[idx] = nums[idx + 1] * 2
                    nums[idx + 1] = 0
                new_nums.append(nums[idx])
            else:
                zeros += 1
                
        # Handle the last element properly
        if nums[-1] != 0:
            new_nums.append(nums[-1])
        else:
            zeros += 1
            
        # Append zeros to new_nums
        new_nums.extend([0] * zeros)

        return new_nums
