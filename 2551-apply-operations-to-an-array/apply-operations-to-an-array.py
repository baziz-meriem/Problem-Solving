class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        new_nums = []
        zeros = 0
        upper_range = len(nums)-1
  
        for idx in range(0,upper_range) :

            if nums[idx] != 0:

                if nums[idx] == nums[idx+1]:
                    nums[idx] = nums[idx+1] *2
                    nums[idx+1] = 0

                new_nums.append(nums[idx])
            else:
                zeros +=1
                
        new_nums.append(nums[idx+1])
                    

        new_nums.extend([0]*zeros)

        return new_nums


        